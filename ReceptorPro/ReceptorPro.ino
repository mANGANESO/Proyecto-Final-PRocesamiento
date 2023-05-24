#include <SPI.h>
#include <RF24.h>
#include <RF24Network.h>

// Configuración del módulo NRF24L01
RF24 radio(9, 10); // Pins CE y CSN del módulo NRF24L01
RF24Network network(radio);

const uint16_t nodoActual = 01; // Dirección del nodo receptor
const uint8_t canal = 90; // Canal de comunicación (puede ser cualquier valor entre 0 y 127)

// Matriz para recibir los datos
char matriz[10][10];

void setup() {
  Serial.begin(9600);
  radio.begin();
  network.begin(canal, nodoActual);
  radio.setPALevel(RF24_PA_LOW);
}

void loop() {
  network.update();
  while (network.available()) {
    RF24NetworkHeader header;
    network.read(header, &matriz, sizeof(matriz));

//Serial.println("Matriz recibida:");
  for (char i = 0; i < 10; i++) {
    for (char j = 0; j < 10; j++) {
      char simbolo;
      if (matriz[i][j] == 48)
        simbolo = '0';
      else if (matriz[i][j] == 49)
        simbolo = '1';
      else if (matriz[i][j] == 50)
        simbolo = '2';
      else if (matriz[i][j] == 51)
        simbolo = '3';
      Serial.print(simbolo);
    }
  Serial.println();
  }
  Serial.println();
}
}