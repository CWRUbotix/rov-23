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
#define SYRINGE_SUCK 9  // Set high to suck water into the syringe
#define SYRINGE_PUMP 10 // Set high to blow water out of the syringe

// Limit switch pins
#define LIMIT_FULL  11  // Low when syringe is full
#define LIMIT_EMPTY 12  // Low when syringe is empty

#define TEAM_NUM 42

// Change to 434.0 or other frequency, must match RX's freq!
#define RF69_FREQ 877.0

// All delays in ms
#define RELEASE_MAX   60000
#define SUCK_MAX      30000
#define DESCEND_TIME  30000
#define PUMP_MAX      30000
#define ASCEND_TIME   30000
#define TX_MAX        60000
#define ONE_HOUR      3600000

#define WAIT 0
#define SUCK 1
#define PUMP 2
#define STOP 3

unsigned long SCHEDULE[][] = {
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

  // Wait until serial console is open; remove if not tethered to computer
  // while (!Serial) { delay(1); }

  #ifndef ESP8266
    while (!Serial); // wait for serial port to connect. Needed for native USB
  #endif

  Serial.println("Float Transceiver");
  Serial.println();

  previous_time = millis();

  pinMode(LIMIT_EMPTY, INPUT_PULLUP);
  pinMode(LIMIT_FULL,  INPUT_PULLUP);

  pinMode(SYRINGE_SUCK, OUTPUT);
  pinMode(SYRINGE_PUMP, OUTPUT);

  digitalWrite(SYRINGE_SUCK, LOW);
  digitalWrite(SYRINGE_PUMP, LOW);

  initRTC();
  initRadio();
}


void loop() {
  sendTime();

  // Move to next stage if necessary
  if (
    millis() >= previous_time + SCHEDULE[stage][1]   ||
    (SCHEDULE[stage][0] == WAIT && signalReceived()) ||
    (SCHEDULE[stage][0] == SUCK && digitalRead(LIMIT_FULL)  == LOW) ||
    (SCHEDULE[stage][0] == PUMP && digitalRead(LIMIT_EMPTY) == LOW)
  ) {
    stage++;
    digitalWrite(SYRINGE_SUCK, LOW);
    digitalWrite(SYRINGE_PUMP, LOW);

    // If we signal a third profile
    if (stage >= SCHEDULE_LENGTH) {
      stage = 1;
    }

    if (SCHEDULE[stage][0] == SUCK) {
      digitalWrite(SYRINGE_SUCK, HIGH);
    }
    else if (SCHEDULE[stage][0] == PUMP) {
      digitalWrite(SYRINGE_PUMP, HIGH);
    }

    previous_time = millis();
  }
}

void sendTime() {
  DateTime now = rtc.now();

  if (now.second() != prevTime.second()) {
    char radiopacket[20] = "";

    char namepacket[10] = "Team ";
    itoa(TEAM_NUM, namepacket + 5, 10);

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

bool signalReceived() {
  if (rf69.available()) {
    uint8_t buf[RH_RF69_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    if (rf69.recv(buf, &len)) {
      if (!len) return;
      buf[len] = 0;
      Serial.print("Received [");
      Serial.print(len);
      Serial.print("]: '");
      Serial.print((char*) buf);
      Serial.println("'");
      Serial.print("RSSI: ");
      Serial.println(rf69.lastRssi(), DEC);

      if (strcmp((char*) buf, "su") == 0) {
        return true;
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
    Serial.println("RTC is NOT initialized, let's set the time!");

    Serial.println("Assume year is 2023");
    Serial.println("Enter month [number format]");
    while (Serial.available() == 0);
    int month = Serial.parseInt();
    Serial.println(month);
    Serial.println("Enter day");
    while (Serial.available() == 0);
    int day = Serial.parseInt();
    Serial.println(day);
    Serial.println("Enter hour");
    while (Serial.available() == 0);
    int hour = Serial.parseInt();
    Serial.println(hour);
    Serial.println("Enter minute [make sure you have enough time to enter seconds!]");
    while (Serial.available() == 0);
    int minute = Serial.parseInt();
    Serial.println(minute);
    Serial.println("Enter second");
    while (Serial.available() == 0);
    int second = Serial.parseInt();
    Serial.println(second);

    rtc.adjust(DateTime(2023, month, day, hour, minute, second));
    
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
