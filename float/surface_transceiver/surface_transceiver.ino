// rf69 demo tx rx.pde
// -*- mode: C++ -*-
// Example sketch showing how to create a simple messageing client
// with the RH_RF69 class. RH_RF69 class does not provide for addressing or
// reliability, so you should only use RH_RF69  if you do not need the higher
// level messaging abilities.
// It is designed to work with the other example rf69_server.
// Demonstrates the use of AES encryption, setting the frequency and modem
// configuration

#include <SPI.h>
#include <RH_RF69.h>

/************ Radio Setup ***************/

//yes, the key is EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE. best key ever.
uint8_t key[] = { 
                  0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE,
                  0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE
                };

// Change to 434.0 or other frequency, must match float's freq!
#define RF69_FREQ 877.0

#if defined (__AVR_ATmega32U4__) // Feather 32u4 w/Radio
#define RFM69_CS      8
#define RFM69_INT     7
#define RFM69_RST     4
#define LED           13
#endif

#if defined(ADAFRUIT_FEATHER_M0) || defined(ADAFRUIT_FEATHER_M0_EXPRESS) || defined(ARDUINO_SAMD_FEATHER_M0)
// Feather M0 w/Radio
#define RFM69_CS      8
#define RFM69_INT     3
#define RFM69_RST     4
#define LED           13
#endif

#if defined (__AVR_ATmega328P__)  // Feather 328P w/wing
#define RFM69_INT     3  // 
#define RFM69_CS      4  //
#define RFM69_RST     2  // "A"
#define LED           13
#endif

#if defined(ESP8266)    // ESP8266 feather w/wing
#define RFM69_CS      2    // "E"
#define RFM69_IRQ     15   // "B"
#define RFM69_RST     16   // "D"
#define LED           0
#endif

#if defined(ARDUINO_ADAFRUIT_FEATHER_ESP32S2) || defined(ARDUINO_NRF52840_FEATHER) || defined(ARDUINO_NRF52840_FEATHER_SENSE)
#define RFM69_INT     9  // "A"
#define RFM69_CS      10  // "B"
#define RFM69_RST     11  // "C"
#define LED           13

#elif defined(ESP32)    // ESP32 feather w/wing
#define RFM69_RST     13   // same as LED
#define RFM69_CS      33   // "B"
#define RFM69_INT     27   // "A"
#define LED           13
#endif

#if defined(ARDUINO_NRF52832_FEATHER)
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

// Singleton instance of the radio driver
RH_RF69 rf69(RFM69_CS, RFM69_INT);

void setup() {
  Serial.begin(115200);
  // Wait until serial console is open; remove if not tethered to computer
  // while (!Serial) { delay(1); }

  Serial.println("Surface Transceiver");
  pinMode(RFM69_RST, OUTPUT);
  digitalWrite(RFM69_RST, LOW);

  Serial.println("Feather RFM69 RX Test!");
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

  // The encryption key has to be the same as the one on the float
  rf69.setEncryptionKey(key);

  Serial.print("RFM69 radio @");
  Serial.print((int) RF69_FREQ);
  Serial.println(" MHz");
}


void loop() {
  receiveData();

  if (Serial.available() == 1) {
    String command;
    command = Serial.readString();
    if (command == "submerge") {
      sendControlSignal("submerge");
    }
    else if (command == "extend") {
      sendControlSignal("extend");
    }
    else if (command == "retract") {
      sendControlSignal("retract");
    }
    else {
      Serial.println("Invalid command");
    }
  }
}

void receiveData() {
  if (rf69.available()) {
    uint8_t buf[RH_RF69_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    if (rf69.recv(buf, &len)) {
      if (!len) return;
      buf[len] = 0;
      Serial.print("Received [");
      Serial.print(len);
      Serial.print("]: ");
      Serial.println((char*) buf);
      // Serial.print("RSSI: ");
      // Serial.println(rf69.lastRssi(), DEC);
    }
    else {
      Serial.println("Receive failed");
    }
  }
}

void sendControlSignal(char* message) {
  rf69.send(message, sizeof(message));
  rf69.waitPacketSent();
  Serial.print(message);
  Serial.println(" signal sent!");
}
