/*humidité */

#include "DHT.h"
#define DHTTYPE DHT22
#define DHTPIN 7 
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600); //vitesse - commune avec processing
}

void loop() {
        // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
    delay(3000);
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);
      //Serial.print("DHT22, \t");
     // uint32_t start = micros();
    //  int chk = DHT.read22(DHT22_PIN);
      //uint32_t stop = micros();
      //int chk = DHT.read22(DHT22_PIN);
      //float h = dht.readHumidit
      //float t = dht.readTemperature();

      Serial.print(h, 1);
      Serial.print(",");
      //Serial.print(", % d'humidité,");
      Serial.println(t, 1);
      //Serial.println("°C,");
      delay(2000);
    

}
