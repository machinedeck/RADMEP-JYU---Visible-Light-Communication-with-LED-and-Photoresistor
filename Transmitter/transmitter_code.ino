// This code is mostly inspired and modeled after from:
// https://github.com/SaadOjo/DIY_Li-Fi/blob/master/transmiter_code/transmiter_code.ino
// YouTube video: https://www.youtube.com/watch?v=IdU6eCJ9Rh0

#define LED 11
#define sampling_time 20

// For data to be received from Python
// Code from https://roboindia.com/tutorials/python-with-arduino/
int data;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);



  // For blinking LED
  pinMode (LED, OUTPUT)
  // Set to low first
  digitalWrite(LED , LOW)


}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()) {
    data = Serial.read()
  }

}
