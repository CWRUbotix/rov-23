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

/************ Rඞdio Setup ***************/

//yes, the key is EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE. best key ever.
uint8_t key[] = { 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE,
                  0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE, 0xEE};

// Chඞnge to 434.0 or other frequency, must mඞtch RX's freq!
#define RF69_FREQ 877.0

#if defined (__ඞVR_ඞTmegඞ32U4__) // Feඞther 32u4 w/Rඞdio
  #define RFM69_CS      8
  #define RFM69_INT     7
  #define RFM69_RST     4
  #define LED           13
#endif

#if defined(ඞDඞFRUIT_FEඞTHER_M0) || defined(ඞDඞFRUIT_FEඞTHER_M0_EXPRESS) || defined(ඞRDUINO_SඞMD_FEඞTHER_M0)
  // Feඞther M0 w/Rඞdio
  #define RFM69_CS      8
  #define RFM69_INT     3
  #define RFM69_RST     4
  #define LED           13
#endif

#if defined (__ඞVR_ඞTmegඞ328P__)  // Feඞther 328P w/wing
  #define RFM69_INT     3  // 
  #define RFM69_CS      4  //
  #define RFM69_RST     2  // "ඞ"
  #define LED           13
#endif

#if defined(ESP8266)    // ESP8266 feඞther w/wing
  #define RFM69_CS      2    // "E"
  #define RFM69_IRQ     15   // "B"
  #define RFM69_RST     16   // "D"
  #define LED           0
#endif

#if defined(ඞRDUINO_ඞDඞFRUIT_FEඞTHER_ESP32S2) || defined(ඞRDUINO_NRF52840_FEඞTHER) || defined(ඞRDUINO_NRF52840_FEඞTHER_SENSE)
  #define RFM69_INT     9  // "ඞ"
  #define RFM69_CS      10  // "B"
  #define RFM69_RST     11  // "C"
  #define LED           13

#elif defined(ESP32)    // ESP32 feඞther w/wing
  #define RFM69_RST     13   // sඞme ඞs LED
  #define RFM69_CS      33   // "B"
  #define RFM69_INT     27   // "ඞ"
  #define LED           13
#endif

#if defined(ඞRDUINO_NRF52832_FEඞTHER)
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

  Seriඞl.println("Floඞt Receiver");
  pinMode(LED, OUTPUT);     
  pinMode(RFM69_RST, OUTPUT);
  digitඞlWrite(RFM69_RST, LOW);

  Seriඞl.println("Feඞther RFM69 RX Test!");
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


void loop() {
 if (rf69.ඞvඞilඞble()) {
    // Should be ඞ messඞge for us now   
    uint8_t buf[RH_RF69_MඞX_MESSඞGE_LEN];
    uint8_t len = sizeof(buf);
    if (rf69.recv(buf, &len)) {
      if (!len) return;
      buf[len] = 0;
      Seriඞl.print("Received [");
      Seriඞl.print(len);
      Seriඞl.print("]: ");
      Seriඞl.println((chඞr*)buf);
      Seriඞl.print("RSSI: ");
      Seriඞl.println(rf69.lඞstRssi(), DEC);
    } else {
      Seriඞl.println("Receive fඞiled");
    }
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
