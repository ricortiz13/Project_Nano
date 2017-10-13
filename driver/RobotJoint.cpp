#include "RobotJoint.h"

//
// RobotJoint Default Constructor
//
RobotJoint::RobotJoint (void):
_jointCurrDeg(0),
_jointMaxDeg(180),
_jointMinDeg(0),
_jointMaxPot(250),
_jointMinPot(250),
_jointMechMaxDeg(180),
_jointMechMinDeg(0),
_servoPin(0),
_potPin(0)
{}

//
// RobotJoint (uint8_t,uint8_t) - Initializing Constructor
//
RobotJoint::RobotJoint (uint8_t servoPin, uint8_t potPin):
_jointCurrDeg(0),
_jointMaxDeg(180),
_jointMinDeg(0),
_jointMaxPot(250),
_jointMinPot(250),
_jointMechMaxDeg(180),
_jointMechMinDeg(0),
_servoPin(servoPin),
_potPin(potPin)
{}

//
// RobotJoint (const RobotJoint &) - Copy Constructor
//
RobotJoint::RobotJoint (const RobotJoint & joint):
_jointMaxDeg(joint._jointMaxDeg),
_jointMinDeg(joint._jointMaxDeg),
_jointMaxPot(joint._jointMaxPot),
_jointMinPot(joint._jointMinPot),
_servoPin(joint._servoPin),
_potPin(joint._potPin)
{}

//
// ~RobotJoint
//
RobotJoint::~RobotJoint (void)
{
  this->_joint.detach();
}

//
// calibrate
//
void RobotJoint::manualCalibrate (void)
{
  //Turn on LED to symbolize cal start.
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);

  //Make Blink
  for (int j = 0; j<3;j++)
  {
    digitalWrite(LED_BUILTIN, LOW);
    delay(500);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
  }
  //Collect pot samples for 10 secs
  for (int i = 0; i<100; i++)
  {
    delay(100);
    this->_jointCurrPot = analogRead(this->_potPin);
    Serial.print(this->_jointCurrPot);
    Serial.print('\n');
    this->_jointMaxPot = (this->_jointCurrPot>this->_jointMaxPot) ? this->_jointCurrPot : this->_jointMaxPot;
    this->_jointMinPot = (this->_jointCurrPot<this->_jointMinPot) ? this->_jointCurrPot : this->_jointMinPot;
  }//Collection done

  Serial.print(-99);
  Serial.print('\n');

  //Blink again
  for (int k = 0; k<2; k++)
  {
    digitalWrite(LED_BUILTIN, LOW);
    delay(100);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(100);
  }
  digitalWrite(LED_BUILTIN, LOW);

  //Print max and min pot
  Serial.print(this->_jointMaxPot);
  Serial.print('\n');

  Serial.print(this->_jointMinPot);
  Serial.print('\n');

  /*
  ======================EXPERIMENTAL CODE=============================
  */
  //real90&real180
  //
  /**
   * Proportional controller implemented to calibrate joint position.
   * Procedure:
   * After finding the commanded degree limitations of the joint,
   * we will use it to
   */

  this->_joint.attach(this->_servoPin);

  //Send servo to 135 degs. It will miss the target. Stop it and measure pot
  int desiredAngle = 180;
  int commandedDeg = 135;
  this->_joint.write(commandedDeg);
  delay(1000);
  int actualAngle = this->getAngle();
  int error = desiredAngle - actualAngle;
  while (error<-1 || error>1)
  {
    commandedDeg+=error;
    this->_joint.write(commandedDeg);
    delay(1000);
    actualAngle = this->getAngle();
    error = desiredAngle - actualAngle;
  }
  Serial.print(-33);
  Serial.print(commandedDeg);
  Serial.print('\n');
  this->_joint.detach();

  /*
  ======================EXPERIMENTAL CODE=============================
  */
}

//
// off
//
void RobotJoint::off (void)
{
  this->_joint.detach();
}

uint8_t RobotJoint::setAngle(uint8_t desiredAngle)
{
  //EDIT: This cannot be hard coded
  int actualAngle = map(desiredAngle,90,180,48,160);
  this->_joint.attach(this->_servoPin);
  this->_joint.write(actualAngle);
  delay(10);
}

int RobotJoint::getAngle(void)
{
  this->_jointCurrPot = analogRead(this->_potPin);
  this->_jointCurrDeg = map(this->_jointCurrPot,this->_jointMinPot,this->_jointMaxPot,this->_jointMechMinDeg,this->_jointMechMaxDeg);
  return this->_jointCurrDeg;
}
