// FLOAT TRANSCEIVER sketch originally built from:
//  rf69 demo tx rx.pde
//  -*- mode: C++ -*-
//  Example sketch showing how to create a simple messageing client
//  with the RH_RF69 class. RH_RF69 class does not provide for addressing or
//  reliability, so you should only use RH_RF69  if you do not need the higher
//  level messaging abilities.
//  It is designed to work with the other example rf69_server.
//  Demonstrates the use of AES encryption, setting the frequency and modem
//  configuration

#include <SPI.h>
#include <RH_RF69.h>
#include "RTClib.h"

#if defined (__AVR_ATmega32U4__) // Feather 32u4 w/Radio
#define RFM69_CS      8
#define RFM69_INT     7
#define RFM69_RST     4
#define LED           13

#elif defined(ADAFRUIT_FEATHER_M0) || defined(ADAFRUIT_FEATHER_M0_EXPRESS) || defined(ARDUINO_SAMD_FEATHER_M0)
// Feather M0 w/Radio
#define RFM69_CS      8
#define RFM69_INT     3
#define RFM69_RST     4
#define LED           13

#elif defined (__AVR_ATmega328P__)  // Feather 328P w/wing
#define RFM69_INT     3  // 
#define RFM69_CS      4  //
#define RFM69_RST     2  // "A"
#define LED           13

#elif defined(ESP8266)    // ESP8266 feather w/wing
#define RFM69_CS      2    // "E"
#define RFM69_IRQ     15   // "B"
#define RFM69_RST     16   // "D"
#define LED           0

#elif defined(ARDUINO_ADAFRUIT_FEATHER_ESP32S2) || defined(ARDUINO_NRF52840_FEATHER) || defined(ARDUINO_NRF52840_FEATHER_SENSE)
#define RFM69_INT     9  // "A"
#define RFM69_CS      10  // "B"
#define RFM69_RST     11  // "C"
#define LED           13

#elif defined(ESP32)    // ESP32 feather w/wing
#define RFM69_RST     13   // same as LED
#define RFM69_CS      33   // "B"
#define RFM69_INT     27   // "A"
#define LED           13

#elif defined(ARDUINO_NRF52832_FEATHER)
/* nRF52832 feather w/wing */
#define RFM69_RST     7   // "A"
#define RFM69_CS      11   // "B"
#define RFM69_INT     31   // "C"
#define LED           17

#endif


/* Teensy 3.x w/wing
  #define RFM69_RST     9   // "A"
  #define RFM69_CS      10   // "B"
  #define RFM69_IRQ     4    // "C"
  #define RFM69_IRQN    digitalPinToInterrupt(RFM69_IRQ )
*/

/* WICED Feather w/wing
  #define RFM69_RST     PA4     // "A"
  #define RFM69_CS      PB4     // "B"
  #define RFM69_IRQ     PA15    // "C"
  #define RFM69_IRQN    RFM69_IRQ
*/

// H-bridge direction control pins
#define MOTOR_PWM 9   // Leave 100% cycle for top speed
#define MOTOR_DIR 10  // Set high for pump (CW when facing down), low for suck (CCW when facing down)


// Limit switch pins
#define LIMIT_FULL  6  // Low when syringe is full
#define LIMIT_EMPTY 5  // Low when syringe is empty

#define TEAM_NUM 11

// Change to 434.0 or other frequency, must match RX's freq!
#define RF69_FREQ 877.0

#define SECOND 1000

// All delays in ms
#define RELEASE_MAX   1200000
#define SUCK_MAX      45000
#define DESCEND_TIME  5000
#define PUMP_MAX      45000
#define ASCEND_TIME   5000
#define TX_MAX        60000
#define ONE_HOUR      360000

#define WAIT 0
#define SUCK 1
#define PUMP 2
#define STOP 3

unsigned long SCHEDULE[][2] = {
  // Wait for max <time> or until surface signal
  {WAIT, RELEASE_MAX },

  // Profile 1
  {SUCK, SUCK_MAX    },
  {WAIT, DESCEND_TIME},
  {PUMP, PUMP_MAX    },
  {WAIT, ASCEND_TIME },

  {WAIT, TX_MAX      },

  // Profile 2
  {SUCK, SUCK_MAX    },
  {WAIT, DESCEND_TIME},
  {PUMP, PUMP_MAX    },
  {WAIT, ASCEND_TIME },

  {WAIT, ONE_HOUR    },
};

uint8_t SCHEDULE_LENGTH = 11;

uint8_t stage = 0;

unsigned long previous_time;


/************ Radio Setup ***************/

// If you ever forget the key, just remember that it's EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
uint8_t key[] = {
                  0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE,
                  0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE
                };

RTC_PCF8523 rtc;

// Singleton instance of the radio driver
RH_RF69 rf69(RFM69_CS, RFM69_INT);

DateTime prevTime((uint32_t) 0);


void setup() {
  Serial.begin(115200);
  
  Serial.println("Float Transceiver");
  Serial.println();

  previous_time = millis();

  pinMode(LED_BUILTIN, OUTPUT);

  pinMode(LIMIT_EMPTY, INPUT_PULLUP);
  pinMode(LIMIT_FULL,  INPUT_PULLUP);

  pinMode(MOTOR_PWM, OUTPUT);
  pinMode(MOTOR_DIR, OUTPUT);

  digitalWrite(MOTOR_PWM, LOW);
  digitalWrite(MOTOR_DIR, LOW);

  initRTC();
  initRadio();
}


void loop() {
  sendTime();

  // Move to next stage if necessary
  bool signal = signalReceived();

  if (
    millis() >= previous_time + SCHEDULE[stage][1]   ||
    (SCHEDULE[stage][0] == WAIT && signal) ||
    (SCHEDULE[stage][0] == SUCK && !digitalRead(LIMIT_FULL)) ||
    (SCHEDULE[stage][0] == PUMP && !digitalRead(LIMIT_EMPTY))
  ) {
    Serial.print(stage);
    Serial.print(" ");
    Serial.print(SCHEDULE[stage][0]);
    Serial.print(" ");
    Serial.print(previous_time);
    Serial.print(" ");
    Serial.print(SCHEDULE[stage][1]);
    Serial.print(" ");
    Serial.print(millis());
    Serial.print(" ");
    Serial.print(millis() >= previous_time + SCHEDULE[stage][1]);
    Serial.println();

    previous_time = millis();
    stage++;
    digitalWrite(MOTOR_PWM, LOW);
    digitalWrite(MOTOR_DIR, LOW);

    // If we signal a third profile
    if (stage >= SCHEDULE_LENGTH) {
      stage = 1;
    }

    if (SCHEDULE[stage][0] == SUCK) {
      digitalWrite(MOTOR_PWM, HIGH);
      digitalWrite(MOTOR_DIR, HIGH);
    }
    else if (SCHEDULE[stage][0] == PUMP) {
      digitalWrite(MOTOR_PWM, HIGH);
      digitalWrite(MOTOR_DIR, LOW);
    }

    Serial.println(stage);

    
  }
}

void sendTime() {
  DateTime now = rtc.now();

  if (now.second() != prevTime.second()) {
    char radiopacket[22] = "";

    char namepacket[12] = "Team EX";
    itoa(TEAM_NUM, namepacket + 7, 10);

    strcpy(radiopacket, namepacket);
    strcat(radiopacket, "  Time: ");

    char timepacket[10] = "";

    sprintf(timepacket, "%u:%u:%u", now.hour(), now.minute(), now.second());
    strcat(radiopacket, timepacket);

    Serial.print("Sending: ");
    Serial.println(radiopacket);

    // Send a message!
    rf69.send((uint8_t *) radiopacket, strlen(radiopacket));
    rf69.waitPacketSent();

    prevTime = now;
  }
}

uint8_t hours = 1;
uint8_t minutes = 1;
uint8_t seconds = 1;

bool signalReceived() {
  if (rf69.available()) {
    uint8_t buf[RH_RF69_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    Serial.println(len);
    if (rf69.recv(buf, &len)) {
      if (!len) return false;
      buf[len] = 0;
      Serial.print("Received [");
      Serial.print(len);
      Serial.print("]: '");
      Serial.print((char*) buf);
      Serial.println("'");
      Serial.print("RSSI: ");
      Serial.println(rf69.lastRssi(), DEC);

      Serial.print(buf[0]);
      Serial.print(", ");
      Serial.println(buf[1]);

      if (strcmp((char*) buf, "su") == 0) {
        uint8_t test_packet[] = {50, 60};
        rf69.send(test_packet, strlen(test_packet));
        rf69.waitPacketSent();

        // Jiggle motor
        // digitalWrite(MOTOR_PWM, HIGH);
        // digitalWrite(MOTOR_DIR, HIGH);
        // delay(2000);
        // delay(100);
        // digitalWrite(MOTOR_PWM, LOW);
        // delay(500);
        return true;
      } else if (buf[0] == 104) { // hours
        Serial.println("Setting hours");
        hours = buf[1] - 50;
        rtc.adjust(DateTime(2023, 6, 23, hours, minutes, seconds));
        return false;
      } else if (buf[0] == 109) { // minutes
        Serial.println("Setting minutes");
        minutes = buf[1] - 50;
        rtc.adjust(DateTime(2023, 6, 23, hours, minutes, seconds));
        return false;
      } else if (buf[0] == 115) { // seconds
        Serial.println("Setting seconds");
        seconds = buf[1] - 50;
        rtc.adjust(DateTime(2023, 6, 23, hours, minutes, seconds));
        return false;
      }
      else {
        Serial.println("Invalid command");
      }
    }
    else {
      Serial.println("Receive failed");
    }
  }

  return false;
}


/******* Setup Methods (down here cause they're lorge) *******/

void initRTC() {
  if (!rtc.begin()) {
    Serial.println("Couldn't find RTC");
    Serial.flush();
    while (1) delay(10);
  }

  // Set rtc if power lost
  if (!rtc.initialized() || rtc.lostPower()) {
    Serial.println("Warning: RTC is NOT initialized");

    // Serial.println("Assume year is 2023");
    // Serial.println("Enter month [number format]");
    // while (Serial.available() == 0);
    // int month = Serial.parseInt();
    // Serial.println(month);
    // Serial.println("Enter day");
    // while (Serial.available() == 0);
    // int day = Serial.parseInt();
    // Serial.println(day);
    // Serial.println("Enter hour");
    // while (Serial.available() == 0);
    // int hour = Serial.parseInt();
    // Serial.println(hour);
    // Serial.println("Enter minute [make sure you have enough time to enter seconds!]");
    // while (Serial.available() == 0);
    // int minute = Serial.parseInt();
    // Serial.println(minute);
    // Serial.println("Enter second");
    // while (Serial.available() == 0);
    // int second = Serial.parseInt();
    // Serial.println(second);

    // rtc.adjust(DateTime(2023, month, day, hour, minute, second));
    
    // rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
    // This line sets the RTC with an explicit date & time, for example to set
    // January 21, 2014 at 3am you would call:
    // rtc.adjust(DateTime(2014, 1, 21, 3, 0, 0));
    //
    // Note: allow 2 seconds after inserting battery or applying external power
    // without battery before calling adjust(). This gives the PCF8523's
    // crystal oscillator time to stabilize. If you call adjust() very quickly
    // after the RTC is powered, lostPower() may still return true.
  }

  rtc.start();
}

void initRadio() {
  pinMode(RFM69_RST, OUTPUT);
  digitalWrite(RFM69_RST, LOW);

  Serial.println("Feather RFM69 TX Test!");
  Serial.println();

  // Manually reset radio module
  digitalWrite(RFM69_RST, HIGH);
  delay(10);
  digitalWrite(RFM69_RST, LOW);
  delay(10);

  if (!rf69.init()) {
    Serial.println("RFM69 radio init failed");
    while (1);
  }
  Serial.println("RFM69 radio init OK!");

  // Defaults after init are: 434.0MHz, modulation GFSK_Rb250Fd250
  // +13dbM (for low power module), no encryption
  // But we override frequency
  if (!rf69.setFrequency(RF69_FREQ)) {
    Serial.println("setFrequency failed");
  }

  // If you are using a high power RF69 eg RFM69HW, you *must* set a Tx power
  // with the ishighpowermodule flag set like this:
  rf69.setTxPower(20, true);  // range from 14-20 for power, 2nd arg must be true for 69HCW

  // The encryption key has to be the same as the one in the server
  rf69.setEncryptionKey(key);

  Serial.print("RFM69 radio @");  
  Serial.print((int) RF69_FREQ);  
  Serial.println(" MHz");
}
