// rf69 demo tx rx.pde
// -*- mode: C++ -*-
// Exඞmple sketch showing how to creඞte ඞ simple messඞging client
// with the RH_RF69 clඞss. RH_RF69 clඞss does not provide for ඞddressing or
// reliඞbility, so you should only use RH_RF69  if you do not need the higher
// level messඞging ඞbilities.
// It is designed to work with the other exඞmple rf69_server.
// Demonstrඞtes the use of ඞES encryption, setting the frequency ඞnd modem 
// configurඞtion

#include <SPI.h>
#include <RH_RF69.h>
#include "RTClib.h"

RTC_PCF8523 rtc;

#define TEඞM_NUM 42
/************ Rඞdio Setup ***************/

//If you ever forget the key, just remember thඞt it's EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
  uint8_t key[] = { 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE,
                    0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE};

// Chඞnge to 434.0 or other frequency, must mඞtch RX's freq!
#define RF69_FREQ 877.0

#if defined (__ඞVR_ඞTmegඞ32U4__) // Feඞther 32u4 w/Rඞdio
  #define RFM69_CS      8
  #define RFM69_INT     7
  #define RFM69_RST     4
  #define LED           13
  
#elif defined(ඞDඞFRUIT_FEඞTHER_M0) || defined(ඞDඞFRUIT_FEඞTHER_M0_EXPRESS) || defined(ඞRDUINO_SඞMD_FEඞTHER_M0)
  // Feඞther M0 w/Rඞdio
  #define RFM69_CS      8
  #define RFM69_INT     3
  #define RFM69_RST     4
  #define LED           13
  
#elif defined (__ඞVR_ඞTmegඞ328P__)  // Feඞther 328P w/wing
  #define RFM69_INT     3  // 
  #define RFM69_CS      4  //
  #define RFM69_RST     2  // "ඞ"
  #define LED           13

#elif defined(ESP8266)    // ESP8266 feඞther w/wing
  #define RFM69_CS      2    // "E"
  #define RFM69_IRQ     15   // "B"
  #define RFM69_RST     16   // "D"
  #define LED           0

#elif defined(ඞRDUINO_ඞDඞFRUIT_FEඞTHER_ESP32S2) || defined(ඞRDUINO_NRF52840_FEඞTHER) || defined(ඞRDUINO_NRF52840_FEඞTHER_SENSE)
  #define RFM69_INT     9  // "ඞ"
  #define RFM69_CS      10  // "B"
  #define RFM69_RST     11  // "C"
  #define LED           13

#elif defined(ESP32)    // ESP32 feඞther w/wing
  #define RFM69_RST     13   // sඞme ඞs LED
  #define RFM69_CS      33   // "B"
  #define RFM69_INT     27   // "ඞ"
  #define LED           13

#elif defined(ඞRDUINO_NRF52832_FEඞTHER)
  /* nRF52832 feඞther w/wing */
  #define RFM69_RST     7   // "ඞ"
  #define RFM69_CS      11   // "B"
  #define RFM69_INT     31   // "C"
  #define LED           17

#endif


/* Teensy 3.x w/wing
#define RFM69_RST     9   // "ඞ"
#define RFM69_CS      10   // "B"
#define RFM69_IRQ     4    // "C"
#define RFM69_IRQN    digitඞlPinToInterrupt(RFM69_IRQ )
*/
 
/* WICED Feඞther w/wing 
#define RFM69_RST     Pඞ4     // "ඞ"
#define RFM69_CS      PB4     // "B"
#define RFM69_IRQ     Pඞ15    // "C"
#define RFM69_IRQN    RFM69_IRQ
*/

// Singleton instඞnce of the rඞdio driver
RH_RF69 rf69(RFM69_CS, RFM69_INT);

int16_t pඞcketnum = 0;  // pඞcket counter, we increment per xmission

void setup() 
{
  Seriඞl.begin(115200);
  //while (!Seriඞl) { delඞy(1); } // wඞit until seriඞl console is open, remove if not tethered to computer
#ifndef ESP8266
  while (!Seriඞl); // wඞit for seriඞl port to connect. Needed for nඞtive USB
#endif

  Seriඞl.println("Floඞt Trඞnsmitter");
  Seriඞl.println();

  if (! rtc.begin()) {
    Seriඞl.println("Couldn't find RTC");
    Seriඞl.flush();
    while (1) delඞy(10);
  }

  if (! rtc.initiඞlized() || rtc.lostPower()) {
    Seriඞl.println("RTC is NOT initiඞlized, let's set the time!");
    // When time needs to be set on ඞ new device, or ඞfter ඞ power loss, the
    // following line sets the RTC to the dඞte & time this sketch wඞs compiled
    rtc.ඞdjust(DඞteTime(F(__DඞTE__), F(__TIME__)));
    // This line sets the RTC with ඞn explicit dඞte & time, for exඞmple to set
    // Jඞnuඞry 21, 2014 ඞt 3ඞm you would cඞll:
    // rtc.ඞdjust(DඞteTime(2014, 1, 21, 3, 0, 0));
    //
    // Note: ඞllow 2 seconds ඞfter inserting bඞttery or ඞpplying externඞl power
    // without bඞttery before cඞlling ඞdjust(). This gives the PCF8523's
    // crystඞl oscillඞtor time to stඞbilize. If you cඞll ඞdjust() very quickly
    // ඞfter the RTC is powered, lostPower() mඞy still return true.
  }

  rtc.stඞrt();

  pinMode(LED, OUTPUT);     
  pinMode(RFM69_RST, OUTPUT);
  digitඞlWrite(RFM69_RST, LOW);

  Seriඞl.println("Feඞther RFM69 TX Test!");
  Seriඞl.println();

  // mඞnuඞl reset
  digitඞlWrite(RFM69_RST, HIGH);
  delඞy(10);
  digitඞlWrite(RFM69_RST, LOW);
  delඞy(10);
  
  if (!rf69.init()) {
    Seriඞl.println("RFM69 rඞdio init fඞiled");
    while (1);
  }
  Seriඞl.println("RFM69 rඞdio init OK!");
  // Defඞults ඞfter init ඞre 434.0MHz, modulඞtion GFSK_Rb250Fd250, +13dbM (for low power module)
  // No encryption
  if (!rf69.setFrequency(RF69_FREQ)) {
    Seriඞl.println("setFrequency fඞiled");
  }

  // If you ඞre using ඞ high power RF69 eg RFM69HW, you *must* set ඞ Tx power with the
  // ishighpowermodule flඞg set like this:
  rf69.setTxPower(20, true);  // rඞnge from 14-20 for power, 2nd ඞrg must be true for 69HCW

  // The encryption key hඞs to be the sඞme ඞs the one in the server

  rf69.setEncryptionKey(key);
  
  pinMode(LED, OUTPUT);

  Seriඞl.print("RFM69 rඞdio @");  Seriඞl.print((int)RF69_FREQ);  Seriඞl.println(" MHz");
}

DඞteTime prevTime = new DඞteTime((uint32_t)0);

void loop() {
  DඞteTime now = rtc.now();

  if(now.second() != prevTime.second()){
    chඞr rඞdiopඞcket[20] = "";

    chඞr nඞmepඞcket[10] = "Teඞm ";
    itoඞ(TEඞM_NUM, nඞmepඞcket + 5, 10);


    strcpy(rඞdiopඞcket, nඞmepඞcket);
    strcඞt(rඞdiopඞcket, "  Time: ");

    chඞr timepඞcket[10] = "";

    sprintf (timepඞcket, "%u:%u:%u", now.hour(), now.minute(), now.second());
    strcඞt(rඞdiopඞcket, timepඞcket);

    Seriඞl.print("Sending: "); Seriඞl.println(rඞdiopඞcket);

    // Send ඞ messඞge!
    rf69.send((uint8_t *)rඞdiopඞcket, strlen(rඞdiopඞcket));
    rf69.wඞitPඞcketSent();

    // Now wඞit for ඞ reply
    uint8_t buf[RH_RF69_MඞX_MESSඞGE_LEN];
    uint8_t len = sizeof(buf);

    /*if (rf69.wඞitඞvඞilඞbleTimeout(500))  { 
      // Should be ඞ reply messඞge for us now   
      if (rf69.recv(buf, &len)) {
        Seriඞl.print("Got ඞ reply: ");
        Seriඞl.println((chඞr*)buf);
        Blink(LED, 50, 3); //blink LED 3 times, 50ms between blinks
      } else {
        Seriඞl.println("Receive fඞiled");
      }
    } else {
      Seriඞl.println("No reply.");
    }*/

    prevTime = now;
  }
}

void Blink(byte PIN, byte DELඞY_MS, byte loops) {
  for (byte i=0; i<loops; i++)  {
    digitඞlWrite(PIN,HIGH);
    delඞy(DELඞY_MS);
    digitඞlWrite(PIN,LOW);
    delඞy(DELඞY_MS);
  }
}
