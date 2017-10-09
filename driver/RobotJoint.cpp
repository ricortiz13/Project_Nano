#include "RobotJoint.h"

//
// RobotJoint Default Constructor
//
RobotJoint::RobotJoint (void):
//_joint(),
_jointMaxDeg(159),
_jointMinDeg(0),
_jointMaxPot(520),
_jointMinPot(25),
_servoPin(0),
_potPin(0)
{}

//
// RobotJoint (uint8_t,uint8_t) - Initializing Constructor
//
RobotJoint::RobotJoint (uint8_t servoPin, uint8_t potPin):
_jointMaxDeg(180),
_jointMinDeg(0),
_jointMaxPot(520),
_jointMinPot(25),
_servoPin(servoPin),
_potPin(potPin)
{
  //_joint.attach(servoPin);
  Serial.begin(9600);
}

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
}

void RobotJoint::autoCalibrate (void)
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
  int actualAngle = map(desiredAngle,90,180,48,160);
  this->_joint.attach(this->_servoPin);
  this->_joint.write(actualAngle);
  delay(10);
}

int RobotJoint::getAngle(void)
{
  this->_jointCurrPot = analogRead(this->_potPin);
  this->_jointCurrDeg = map(this->_jointCurrPot,this->_jointMinPot,this->_jointMaxPot,this->_jointMinDeg,this->_jointMaxDeg);
  //this->_jointCurrDeg = map(this->_jointCurrPot,23,533,this->_jointMinDeg,this->_jointMaxDeg);
  return this->_jointCurrDeg;
}
