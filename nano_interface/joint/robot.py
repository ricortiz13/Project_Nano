## @file: robot.py
#
from link import Link
from drivers.PCA9685 import PCA9685



class Robot:
    def __init__(self):
        self._legs = {}

    def set_2D_45(self,leg):
        femur = self._legs[leg]
        hip = femur.get_child()
        tibia = hip.get_child()

        femur.set_pos(30) #controlling hip
        hip.set_pos(90)#controlling femur
        tibia.set_pos(30)#tibia
    def fold(self,leg):
        femur = self._legs[leg]
        hip = femur.get_child()
        tibia = hip.get_child()

        femur.set_pos(20)
        hip.set_pos(90)
        tibia.set_pos(20)
    def extend(self, leg):
        femur = self._legs[leg]
        hip = femur.get_child()
        tibia = hip.get_child()

        femur.set_pos(90)
        hip.set_pos(90)
        tibia.set_pos(160)

    def reach(self, leg): #reach, compress, push, retract
        femur = self._legs[leg]
        hip = femur.get_child()
        tibia = hip.get_child()

        femur.set_pos(130)
        hip.set_pos(90)
        tibia.set_pos(160)

    def compress(self, leg): #reach, compress, push, retract
        femur = self._legs[leg]
        hip = femur.get_child()
        tibia = hip.get_child()

        femur.set_pos(30)
        hip.set_pos(90)
        tibia.set_pos(90)

    def push(self, leg): #reach, compress, push, retract
        femur = self._legs[leg]
        hip = femur.get_child()
        tibia = hip.get_child()

        femur.set_pos(45)
        hip.set_pos(90)
        tibia.set_pos(160)

    def retract(self, leg): #reach, compress, push, retract
        femur = self._legs[leg]
        hip = femur.get_child()
        tibia = hip.get_child()

        femur.set_pos(30)
        hip.set_pos(90)
        tibia.set_pos(10)
        
    def add_legs(self, leg_dict):
        self._legs = leg_dict
