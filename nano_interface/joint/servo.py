##  @filename: servo.py
#

class Servo:
    def __init__(self,pin,pwm_generator):
        self._curr_pos = 250
        self._curr_deg = 90
        self._pin = pin
        self._min = 250
        self._center = 250
        self._max = 250
        self._deg_max = 90
        self._deg_center = 90
        self._deg_min = 90
        self._pwm_board = pwm_generator
    def actuate_pwm(self, pwm_pos):
        self._curr_pos = pwm_pos
        self._pwm_board.set_pwm(self._pin,0,self._curr_pos)
    def actuate_deg(self, deg_pos):
        # Convert to pwm
        if (deg_pos == 90):
            self._curr_pos = self._center
        elif (deg_pos < 90):
            #interpolate between min and center
            self._curr_pos = ((self._center - self._min)/(self._deg_center - self._deg_min))
            self._curr_pos = self._curr_pos * (deg_pos - self._deg_min)
            self._curr_pos = seld._curr_pos + self._min
            self._curr_pos = int(self._curr_pos)
        else:
            #interpolate between center and max
            self._curr_pos = ((self._max - self._center)/(self._deg_max - self._deg_center))
            self._curr_pos = self._curr_pos * (deg_pos - self._deg_center)
            self._curr_pos = seld._curr_pos + self._center
            self._curr_pos = int(self._curr_pos)

        self._pwm_board.set_pwm(self._pin,0,self._curr_pos)
    def on(self):
        self._pwm_board.set_pwm(self._pin,0,self._curr_pos)
    def off(self):
        self._pwm_board.set_pwm(self._pin,0,0)
    def set_min(self, deg):
        self._min = deg
    def set_center(self, deg):
        self._center = deg
    def set_max(self, deg):
        self._max = deg
