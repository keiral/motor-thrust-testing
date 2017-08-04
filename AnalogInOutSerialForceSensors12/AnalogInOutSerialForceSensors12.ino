/*
Reads forces from dyno, communicates them through usb. 
 */

//defining pins 
const int analogInF1Pin1 = A0;  // Analog input pin that the first force sensor is connect to
const int analogInF1Pin2 = A1; 
const int analogInF2 = A2;
const int analogInF3 = A3;
const int analogInF4Pin1 = A4;
const int analogInF4Pin2 = A5;

int F1sensorValue1 = 0;        // value read from A0
int F1outputValue1 = 0;        
int F1sensorValue2 = 0;       // value read from A1
int F1outputValue2 = 0; 

int F2sensorValue1 = 0;        // value read from A2
int F2outputValue1 = 0;        

int F3sensorValue1 = 0;       //value read from A3
int F3outputValue1 = 0; 

int F4sensorValue1 = 0;        // value read from A4
int F4outputValue1 = 0;        
int F4sensorValue2 = 0;       // value read from A5
int F4outputValue2 = 0; 

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(256000);
}

void loop() {
  // read the analog in value:
  F1sensorValue1 = analogRead(analogInF1Pin1);
  // map it to the range of the analog out:
  F1outputValue1 = map(F1sensorValue1, 0, 1023, 0, 255);
  // change the analog out value:

  
  // print the results to the serial monitor:
  //Serial.print("\n F1 signa1 = ");
  //Serial.print(F1sensorValue1);
  
  //delay(2); 

  F1sensorValue2 = analogRead(analogInF1Pin2);
  // map it to the range of the analog out:
  F1outputValue2 = map(F1sensorValue2, 0, 1023, 0, 255);
  // change the analog out value:

  //Serial.print("F1 signal2 = ");
  //Serial.print(F1sensorValue2);

  //delay(2); 

  F2sensorValue1 = analogRead(analogInF2);
  // map it to the range of the analog out:
  F2outputValue1 = map(F2sensorValue1, 0, 1023, 0, 255);
  // change the analog out value:

  //Serial.print("F2 signa1 = ");
  //Serial.print(F2sensorValue1);


  //delay(2); 

  F3sensorValue1 = analogRead(analogInF3);
  // map it to the range of the analog out:
  F3outputValue1 = map(F3sensorValue1, 0, 1023, 0, 255);
  // change the analog out value:

  //Serial.print("F3 signal = ");
  //Serial.print(F3sensorValue1);

  // wait 2 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  //delay(2);

  // read the analog in value:
  F4sensorValue1 = analogRead(analogInF4Pin1);
  // map it to the range of the analog out:
  F4outputValue1 = map(F4sensorValue1, 0, 1023, 0, 255);
  // change the analog out value:

  
  // print the results to the serial monitor:
  //Serial.print("\n F4 signal 1 = ");
  //Serial.print(F4sensorValue1);

  
  //delay(2); 

  F4sensorValue2 = analogRead(analogInF4Pin2);
  // map it to the range of the analog out:
  F4outputValue2 = map(F4sensorValue2, 0, 1023, 0, 255);
  // change the analog out value:


  //Serial.println("C");
  
 delay(5);
//F2outputValue1= F2outputValue1 - F2Cal;
//F3outputValue1= F3outputValue1 - F3Cal;
Serial.print(char(F2outputValue1)); //element 0
Serial.print(":");
Serial.print(char(F3outputValue1)); //element 2
Serial.print(":");
Serial.print(char(F1outputValue1));
Serial.print(":");
Serial.print(char(F1outputValue2));
Serial.print(":");
Serial.print(char(F4outputValue1));
Serial.print(":");
Serial.println(char(F4outputValue2));
/*  if(Serial.available() > 0 ){
    while(Serial.available() > 0){
      if(Serial.read() == 'R'){
        
      }
    }
  }*/
}
