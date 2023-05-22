#include <SPI.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(0xF0F0F0F0E1LL); // Dirección de escritura del receptor
}

void loop() {
 
    
  for(int i = 1; i <= 1000; i++){
  int text = i; // Mensaje a enviar
  
  radio.write(&text, sizeof(text));
  Serial.println("Mensaje enviado: ");
  Serial.println(text);
  delay(1000):
  }
  
  delay(1000);
}