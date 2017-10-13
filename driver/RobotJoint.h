//==============================================================================
/**
 * @file    RobotJoint.h
 * Date:    10/8/2017
 * Authors: Amanda Justiniano
 *          Ricardo Ortiz
 *
 * RobotJoint.h will be utilized to control all low level
 * actions to be performed by the robots joint.
 */
//==============================================================================

#ifndef _ROBOTJOINT_H_
#define _ROBOTJOINT_H_
#include <Servo.h>
#include <math.h>
#include <Arduino.h>

/**
 * @class RobotJoint
 *
 * Basic implementation of a robot joint via servo control.
 */

class RobotJoint
{
public:
  /// Arduino servo object
  Servo _joint;

  /// Current joint angle.
  uint8_t _jointCurrDeg;

  /// Maximum joint degree value that can be commanded to joint.
  uint8_t _jointMaxDeg;

  /// Minimum joint degree value that can be commanded to joint.
  uint8_t _jointMinDeg;

  /// Maximum potentiometer value that is seen at max joint degree.
  uint16_t _jointCurrPot;

  /// Maximum potentiometer value that is seen at max joint degree.
  uint16_t _jointMaxPot;

  /// Minimum potentiometer value that is seen at min joint degree.
  uint16_t _jointMinPot;

  /// Maximum joint degree value that the joint can mechanically achieve.
  uint8_t _jointMechMaxDeg;

  /// Minimum joint degree value that the joint can mechanically achieve.
  uint8_t _jointMechMinDeg;

  /// Pin location for servo.
  uint8_t _servoPin;

  /// Pin location for potentiometer.
  uint8_t _potPin;

  /// Default constructor.
  RobotJoint (void);

  /**
   * Initializing constructor.
   *
   * @param[in]      servoPin        Servo pin location
   * @param[in]      potPin          Potentiometer pin location
   */
  RobotJoint (uint8_t servoPin, uint8_t potPin);

  /**
   * Copy constructor
   *
   * @param[in]     joint         The source robot joint.
   */
  RobotJoint (const RobotJoint & joint);

  /// Destructor.
  ~RobotJoint (void);

  /**
   * Calibrates the servo pertaining to the joint
   *
   * A full pan ranging from the max and min possible displacement of the joint
   * is performed and once the potentiomer indicates end points, it pans in the
   * opposite direction
   *
   */
  void manualCalibrate(void);

  /**
   * Auto calibrates the servo pertaining to the joint
   *
   * A full pan ranging from the max and min possible displacement of the joint
   * is performed and once the potentiomer indicates end points, it pans in the
   * opposite direction
   *
   */
  void autoCalibrate(void);

  /**
   * Ensures the servo is detached(off) after
   * use is complete.
   *
   */
  void off(void);

  /**
   * Will appropriately move joint to desired angle
   *
   */
  uint8_t setAngle(uint8_t desiredAngle);

  /**
   * Will utilize the pot to read current angle
   *
   */
  int getAngle(void);

};

//#include "RobotJoint.cpp"
#endif   // !defined _ROBOTJOINT_H_
