## @file: buider.py
#

## @class: Servo_Builder
#
from servo import Servo
from json_manager import JSON_Manager

## @class: Leg_Builder
#
from link import Link

## @class: Robot_Builder
#
from robot import Robot

from drivers.PCA9685 import PCA9685

class Builder:
    def __init__(self):
        self._build = None
    def build(self):
        pass
    def get_build(self):
        return self._build

class Servo_Builder(Builder):
    def __init__(self, pwm_generator, pin=0):
        self._build = None
        self._pwm = pwm_generator
        self._pin = pin
        self.cal_data = JSON_Manager().read()
    def build(self):
        self._build = Servo(self._pin,self._pwm)
        self._build.set_pwm_center(self.cal_data[str(self._pin)]["pwm_center"])
        self._build.set_pwm_max(self.cal_data[str(self._pin)]["pwm_max"])
        self._build.set_pwm_min(self.cal_data[str(self._pin)]["pwm_min"])
        if (self._pin in set([0,4,5,6,10,11])):
            self.change_polarity()
        self._pin+=1
    def build_lean(self):
        self._build = Servo(self._pin,self._pwm)
        if (self._pin in set([0,4,5,6,10,11])):
            self.change_polarity()
        self._pin+=1
    def add_pwm(self, pwm):
        self._pwm = pwm
    def hip_joint(self):
        self._build.set_deg_min(60)
        self._build.set_deg_max(120)
    def change_polarity(self):
        self._build.change_polarity()

class Leg_Builder(Builder):
    def __init__(self,pwm):
        self.servo_builder = Servo_Builder(pwm)
        self._build = None
        self._joints = []

    def add_joint(self, servo):
        self._build.add_joint(servo)

    def add_child(self, child=None):
        self._build.add_child(child)

    def get_joints(self):
        self._joints = []
        self.servo_builder.build()
        self._joints.append(self.servo_builder.get_build())#0

        self.servo_builder.build()
        self.servo_builder.hip_joint()
        self._joints.append(self.servo_builder.get_build())

        self.servo_builder.build()
        self._joints.append(self.servo_builder.get_build())

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

    def build(self):
        self.get_joints()
        self.build_tibia()
        curr_tibia = self.get_build()
        self.build_femur(curr_tibia)
        curr_femur = self.get_build()
        self.build_hip(curr_femur)
        
class Robot_Builder(Builder):
    def __init__(self):
        self._build = None
        self._pwm = PCA9685()
        self._leg_builder = Leg_Builder(self._pwm)

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


if __name__ == "__main__":
    pwm = PCA9685()
    builder = Leg_Builder(pwm)
    builder.build()
    print(builder.get_build())
    print(builder.get_build().get_child())
    print(builder.get_build().get_child().get_child())
