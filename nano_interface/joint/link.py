## @file: link.py
#

class Joint_V2:
    def __init__(self):
        self.__max = 180
        self.__min = 0
        self.__curr_pos = 90
    def __init__(self, j_range):
        self.__max = 90 + j_range
        self.__min = 90 - j_range
    def move(self, pos):


class Link:
    def __init__(self):
        self.__joint = None
        self.__child = None
    def add_joint(self, joint):
        self.__joint = joint
    def set_pos(self, pos):
        self.__joint.actuate_deg(pos)
    def get_pos(self):
        return self.__joint.get_pos()
    def add_child(self, child):
        self.__child = child
    def get_child(self):
        return self.__child

class Master_Link(Link):
    def __init__(self):
        self.__child = {}
    def set_joint_pos(self, pos, link):
        pass #@TODO set function
    def add_child(self, child_name, child):
        self.__child[child_name] = child
    def get_child(self, child_name):
        return self.__child[child_name]
