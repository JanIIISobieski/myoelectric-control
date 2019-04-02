#include<Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

int SP1 = 0;
int SP2 = 0;
int SP3 = 0;
int SP4 = 0;
int SP5 = 0;

int whichAction = 10;

void getData(){
  if(Serial.available() > 0){
    whichAction = Serial.read() - '0';
  }
}

void openHand() {
    servo1.write(0);
    servo2.write(0);
    servo3.write(0);
    servo4.write(0);
    servo5.write(0);
}

void closeHand() {
    servo1.write(180);
    servo2.write(180);
    servo3.write(180);
    servo4.write(180);
    servo5.write(180); 
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo1.attach(4);
  servo2.attach(7);
  servo3.attach(8);
  servo4.attach(12);
  servo5.attach(2);

}

void loop() {
    if (whichAction != 10) {
        if (whichAction == 1) {
            openHand();
            delay(1000);
            Serial.println(0);
        }
        else if (whichAction == 2) {
            closeHand();
            delay(1000);
            Serial.println(0);
        }
    else {

    }
    whichAction = 10;
    }
    else {
        getData();     
    }
}
