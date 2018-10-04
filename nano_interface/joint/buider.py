## @file: buider.py
#
from servo import Servo
from json_manager import JSON_Manager

class Builder:
    def __init__(self):
        self._build = None
    def build(self):
        pass
    def get_build(self):
        return self._build

class Servo_Builder(Builder):
    def __init__(self, pin, pwm_generator):
        self._build = None
        self._pwm = pwm_generator
        self._pin = pin
    def build(self):
        cal_data = JSON_Manager().read()
        self._build = Servo(self._pin,self._pwm)
        
        self._build.set_pwm_center(cal_data[self._pin]["pwm_center"])
        self._build.set_pwm_max(cal_data[self._pin]["pwm_max"])
        self._build.set_pwm_min(cal_data[self._pin]["pwm_min"])
    def build_lean(self):
        self._build = Servo(self._pin,self._pwm)
