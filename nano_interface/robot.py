## @file: robot.py
#
import math
from .link import Link
from .drivers.PCA9685 import PCA9685




class Robot:
    def __init__(self):
        self._legs = {}

    def leg_ik(self,y):
        l1 = 70.6 #mm
        l2 = 73.0 #mm
        theta1 = (l1**2 - l2**2 + y**2)/(2*l1*y)
        theta1 = math.asin(theta1)
        
        angle = math.acos((l1/l2)*math.cos(theta1))
        theta2 = math.pi - theta1 - angle

        theta1 = math.degrees(theta1)
        theta2 = math.degrees(theta2)

        theta1 = int(theta1)
        theta2 = int(theta2)
        theta2 = 180 - theta2

        # switch = theta1
        # theta1 = theta2
        # theta2 = switch

        return theta1, theta2


    def controller(self, y, leg='fr'):
        femur = self._legs[leg]
        hip = femur.get_child()
        tibia = hip.get_child()


        l1 = 70.6 #mm
        l2 = 73 #mm
        if (y*(-1)>=(l1+l2)):
            y = (l1+l2) - (l1+l2)*0.10
        
        theta1, theta2 = self.leg_ik(y)

        print("Theta1: " + str(theta1))
        print("Theta2: " + str(theta2))

        femur.set_pos(theta1) #controlling hip
        hip.set_pos(90)#set straight
        tibia.set_pos(theta2)#tibia
        

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
