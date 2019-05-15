## @file buider.py
#

#  Inclusions required by Servo_Builder class
from .servo import Servo
from .json_manager import JSON_Manager

#  Inclusions required by Leg_Builder class
from .link import Link

#  Inclusions required by Robot_Builder class
from .robot import Robot

from .drivers.PCA9685 import PCA9685

## @class Builder
#  Abstract class used to define all subsequent builders
#
class Builder(object):

    # Constructor
    def __init__(self):
        self._build = None

    # The build method shall be called by the director class
    # to create the desired object
    def build(self):
        pass

    # @return returns the desired builder object at its current state
    def get_build(self):
        return self._build

## @class Servo_Builder
#  Used by the director class, produces a servo object
class Servo_Builder(Builder):

    # Constructor
    # @param pwm_generator API to board generating pwm control signal
    # @param pin position of pin for this servo
    def __init__(self, pwm_generator, pin=0):
        self._build = None
        self._pwm = pwm_generator
        self._pin = pin
        self.cal_data = JSON_Manager().read()

    # This build method is responsible for creating each servo
    # on this robot. When this method is called sequentially it
    # may produce all of the servos on this robot without
    # additional inputs. If there is a need to build a servo to
    # a specific pin, a new servo builder object needs to be created.
    def build(self):
        self._build = Servo(self._pin,self._pwm)
        self._build.set_pwm_center(self.cal_data[str(self._pin)]["pwm_center"])
        self._build.set_pwm_max(self.cal_data[str(self._pin)]["pwm_max"])
        self._build.set_pwm_min(self.cal_data[str(self._pin)]["pwm_min"])
        # @TODO servos of opposite polarity are hard coded, consider including
        #       this information in json file
        if (self._pin in set([0,4,5,6,10,11])):
            self.change_polarity()
        self._pin+=1

    # The build lean method is the most basic build
    # possible by this object. This method is meant to
    # allow the client to build a custom servo on the
    # fly by sequentially calling the different options
    # or settings desired for the servo before requesting
    # the completed product.
    def build_lean(self):
        self._build = Servo(self._pin,self._pwm)
        if (self._pin in set([0,4,5,6,10,11])):
            self.change_polarity()
        self._pin+=1
    
    # Adds the pwm generator to this servo
    # @param pwm_generator API to board generating pwm control signal
    def add_pwm(self, pwm):
        self._pwm = pwm

    # The hip joint (the joint that moves the leg left or right) 
    # has a narrower mobility band due to hardware limits as 
    # compared to the other two joints in a leg (0 to 180 deg). 
    # By default all servos are allowed to travel their full range; 
    # this joint is the exception and the limits need to be modified
    # approprietely. 
    def hip_joint(self):
        self._build.set_deg_min(60)
        self._build.set_deg_max(120)

    # For this robot it is useful to change the polarity
    # in order to treat all joints equally.
    # e.g When the knee is commanded to 45 deg, the leg should bend to an internal 
    # 45 deg angle in all cases
    # A servo that may be mounted differently on the robot could require
    # a command of 135 deg to achieve the same behaviour. 
    # When we change the polarity we compensate for motors mounted in different
    # directions to achieve the same behaviour with less complexity.
    def change_polarity(self):
        self._build.change_polarity()

## @class Leg_Builder
#  Class used to build all legs of the robot leveraging the servo builder
class Leg_Builder(Builder):
    
    # Constructor
    # @param pwm_generator API to board generating pwm control signal
    def __init__(self,pwm):
        self.servo_builder = Servo_Builder(pwm)
        self._build = None
        self._joints = []

    # @param servo
    def add_joint(self, servo):
        self._build.add_joint(servo)

    # The add child method allows to define a hirearchical relationship
    # between the independent components that form this build.
    # For this example, servos will have a parent to child relationship
    # in the link object that is being constructed.
    # This hirearchical relationship will allow for easier control
    # of the full leg.
    def add_child(self, child=None):
        self._build.add_child(child)

    # This method will create three joints and add them to a list.
    # The list will act as a source of servos when building the leg.
    def get_joints(self):
        self._joints = []
        self.servo_builder.build()
        self._joints.append(self.servo_builder.get_build())

        self.servo_builder.build()
        self.servo_builder.hip_joint()
        self._joints.append(self.servo_builder.get_build())

        self.servo_builder.build()
        self._joints.append(self.servo_builder.get_build())

    # build femur, tibia and hip are built using a hardcoded order for
    # physically wiring each motor. The pattern is:
    # hip on 0th pos
    # femur on 1st pos
    # tibia on 2nd pos
    # This pattern is consistent with all 12 motors of the robot
    def build_femur(self,child_link=None):
        self._build = Link()
        self._build.add_joint(self._joints[1])
        self._build.add_child(child_link)

    def build_tibia(self,child_link=None):
        self._build = Link()
        self._build.add_joint(self._joints[2])

    def build_hip(self,child_link=None):
        self._build = Link()
        self._build.add_joint(self._joints[0])
        self._build.add_child(child_link)

    # Each segment of the leg is built in a hierarchical order:
    # From Top (root) to bottom (leaf): hip -> femur -> tibia -> None
    def build(self):
        self.get_joints()
        self.build_tibia()
        curr_tibia = self.get_build()
        self.build_femur(curr_tibia)
        curr_femur = self.get_build()
        self.build_hip(curr_femur)
        
# @class Robot_Builder
# Robot builder is currently the higher level builder and
# it is the desired builder to exist within the robot class
# constructor. See robot_test.py for an example use case.
class Robot_Builder(Builder):

    # Constructor
    def __init__(self):
        self._build = None
        self._pwm = PCA9685()
        self._leg_builder = Leg_Builder(self._pwm)

    # Leverage the Leg_Builder class to build each of
    # the robots 4 legs
    # Legend:
    # fr = front right leg
    # fl = front left leg
    # bl = back left leg
    # br = back right leg
    def build(self):
        leg_dict = {}
        self._build = Robot()
        self._leg_builder.build()
        leg_dict['fr'] = self._leg_builder.get_build()

        self._leg_builder.build()
        leg_dict['fl'] = self._leg_builder.get_build()

        self._leg_builder.build()
        leg_dict['bl'] = self._leg_builder.get_build()

        self._leg_builder.build()
        leg_dict['br'] = self._leg_builder.get_build()
        
        self._build.add_legs(leg_dict)

# Functionality testing
if __name__ == "__main__":
    pwm = PCA9685()
    builder = Leg_Builder(pwm)
    builder.build()
    print(builder.get_build())
    print(builder.get_build().get_child())
    print(builder.get_build().get_child().get_child())
