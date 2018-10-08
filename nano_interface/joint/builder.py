## @file: buider.py
#

## @class: Servo_Builder
#
from servo import Servo
from json_manager import JSON_Manager

## @class: Leg_Builder
#
from link import Link

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
        self._pin+=1
    def build_lean(self):
        self._build = Servo(self._pin,self._pwm)
        self._pin+=1
    def add_pwm(self, pwm):
        self._pwm = pwm
    def hip_joint(self):
        self._build.set_deg_min(60):
        self._build.set_deg_max(120)
    def change_polarity(self):
        self._build.change_polarity()

class Leg_Builder(Builder):
    def __init__(self,pwm):
        self.servo_builder = Servo_Builder(pwm)
        self._build = None
    def add_joint(self, servo):
        self._build.add_joint(servo)
    def add_child(self, child=None):
        self._build.add_child(child)
    def build_femur(self,child_link=None):
        self._build = Link()
        self.servo_builder.build()
        servo = self.servo_builder.get_build()
        self._build.add_joint(servo)
        self._build.add_child(link)

    def build_tibia(self,child_link=None):
        self._build = Link()
        self.servo_builder.build()
        servo = self.servo_builder.get_build()
        self._build.add_joint(servo)

    def build_hip(self,child_link=None):
        self._build = Link()
        self.servo_builder.build()
        self.servo_builder.hip_joint()
        servo = self.servo_builder.get_build()
        self._build.add_joint(servo)
        self._build.add_child(link)

    def build(self):
        self.build_tibia()
        curr_tibia = self.get_build()
        self.build_femur(curr_tibia)
        curr_femur = self.get_build()
        self.build_hip(curr_femur)
        
class Robot_Builder(Builder):
    def add_pwm(self, pwm_board):
        pass
    def add_master_link(self, master_link):
        pass
    def add_leg(self, leg_name, leg):
        pass
    def build(self):
        #Build Robot from 0 to Robot

