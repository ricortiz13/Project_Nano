##  @filename: servo.py
#

class Servo:
    def __init__(self,pin):
        self._pos = 250
        self._pin = pin
        self._deg0 = None
        self._deg90 = None
        self._deg180 = None
        self._upper_limit = None
        self._lower_limit = None
    def actuate(self, pwm_generator, position):
        self._pos = position
        pwm_generator.set_pwm(self._pin,0,self._pos)
    def on(self, pwm_generator):
        pwm_generator.set_pwm(self._pin,0,self._pos)
    def off(self, pwm_generator):
        pwm_generator.set_pwm(self._pin,0,0)
    def set_lower_limit(self, lower_limit):
        self._lower_limit = lower_limit
    def set_upper_limit(self, upper_limit):
        self._upper_limit = upper_limit
    def set_deg0(self, deg):
        self._deg0 = deg
    def set_deg90(self, deg):
        self._deg90 = deg
    def set_deg180(self, deg):
        self._deg180 = deg
