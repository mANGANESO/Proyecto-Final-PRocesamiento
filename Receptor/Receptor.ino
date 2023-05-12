#include <SPI.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(1, 0xF0F0F0F0E1LL); // Dirección de lectura del transmisor
  radio.startListening();
}

void loop() {
  if (radio.available()) {
    int text = ""; // Almacenar el mensaje recibido
    
    radio.read(&text, sizeof(text));
    
    Serial.println("Mensaje recibido: ");
    Serial.println(text);
    delay(1000);
  }
}
