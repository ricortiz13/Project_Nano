## @file: leg.py
#

from servo import Servo

class Leg:
    def __init__(self):
        self._j = []
    def j_0(self, deg):
        self._j[0].actuate_deg(deg)
    def j_1(self,deg):
        self._j[1].actuate_deg(deg)
    def j_2(self,deg):
        self._j[2].actuate_deg(deg)
    def extend(self):
        self.j_0(90)
        self.j_1(90)
        self.j_2(180)
    def fold(self):
        self.j_0(10)
        self.j_1(90)
        self.j_2(10)
    def add_joint(self, joint):
        self._j.append(joint)