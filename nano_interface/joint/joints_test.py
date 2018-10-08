## @file: joints_test.py
#

from director import Director
from builder import Servo_Builder
from drivers.PCA9685 import PCA9685
from iterator import List_Iterator
import time

class Robot:
    def __init__(self):
        self.joints = []
        self._pwm =  PCA9685()
        director = Director(Servo_Builder(self._pwm))
        for pin in range(0,12):
            director.build()
            self.joints.append(director.get_build())
            if (pin in set([1,4,7,10])):
                self.joints[pin].set_deg_max(120)
                self.joints[pin].set_deg_min(60)
        self._pwm.set_pwm_freq(60)

    def actuate_all(self, deg):
        lit = List_Iterator(self.joints)
        while(not(lit.isDone())):
            lit.get_current().actuate_deg(deg)
            lit.next()
            time.sleep(1)

ro = Robot()
ro.actuate_all(90)