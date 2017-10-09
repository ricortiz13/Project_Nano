/**
 * driver.ino
 * Date:    10/8/2017
 * Authors: Amanda Justiniano
 *          Ricardo Ortiz
 *          
 * driver.ino will be utilized as a test bed driver file 
 * for all .cpp & .h files developed for Project Nano.
 */

/**
 * Include prototype files below...
 */
#include "RobotJoint.h"
//#include <Servo.h>


void setup() {
  RobotJoint shoulderPitch(3,0);  
  shoulderPitch.manualCalibrate();
  shoulderPitch.setAngle(180);
  delay(1000);
  Serial.print(shoulderPitch.getAngle());
  shoulderPitch.off();
  
  /*
  Servo joint;
  joint.attach(3);
  joint.write(159);
  delay(3000);
  joint.detach();
  */
  
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
