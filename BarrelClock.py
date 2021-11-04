#HW 2
#Analog Clock
#Sawyer P, James S, Ilan Felberg

#install these (terminal) before running code
#sudo pip3 install adafruit-circuitpython-pca9685
#sudo pip3 install adafruit-circuitpython-servokit


import time
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit


class Clock():
    def __init__(self):
        # Set channels to the number of servo channels on your kit.
        # 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
        self.kit = ServoKit(channels=16)

        self.sec_servo = self.kit.servo[0]
        self.min_servo = self.kit.servo[1]
        self.hour_servo = self.kit.servo[2]
        self.servos = [self.sec_servo, self.min_servo, self.hour_servo]

        self.prev_sec = -1
        self.prev_min = -1
        self.prev_hour = -1

        ## SETUP CONSTANTS ##
        max_servo = 180. # this worked despite a true range of 150. 
        # Increments and dictionaries for seconds and minutes
        sixty_increment = max_servo / 60

        self.sec_to_degree = dict()
        self.min_to_degree = dict()
        idx = 0
        for i in range(60, -1,-1):
            self.sec_to_degree[idx] = sixty_increment * i
            idx += 1

        for i in range(60): # account for reverse mechanical position
            self.min_to_degree[i] = sixty_increment * i

        twelve_increment = max_servo / 12
        self.twelve_to_degree = dict()
        for i in range(11,-1,-1):
            self.twelve_to_degree[i] = twelve_increment * i
        ## END SETUP CONSTANTS ##

        self.t0 = time.time() # grab initial time to zero speed-mode

    def setup(self, starting_angle=180):
        raise NotImplementedError # It turned out not to be necessary to account for the difference between the servo's expected and true range.
        # go to initial 
        # for servo in self.servos:
        #     servo.actuation_range = 180
        
        # self.sec_servo.angle = starting_angle
        # self.hour_servo.angle = starting_angle
        # self.min_servo.angle = 0 if starting_angle == 180 else 180

    def set_time(self, sec, minute, hour):
        # Set servos to mapped values. Only send if the new time differs from the previous.
        if (self.prev_sec != sec):
            self.sec_servo.angle = self.sec_to_degree[int(sec)]
            self.prev_sec = sec
        if (self.prev_min != minute):
            self.min_servo.angle = self.min_to_degree[int(minute)]
            self.prev_min = minute
        if (self.prev_hour != hour):
            self.hour_servo.angle = self.twelve_to_degree[int(hour)]
            self.prev_hour = hour

    def run(self, time_multiplier=1):
        if (time_multiplier > 1):
            # Zero to run speed-mode from 00:00:00 
            t = (time.time() - self.t0) * time_multiplier
        else:
            t = time.time()

        localtime = time.localtime(t)
        hour = localtime.tm_hour
        if hour > 12: # account for military time
            hour = hour - 12
        minute = localtime.tm_min
        sec = localtime.tm_sec
        self.set_time(sec, minute, hour)

### MAIN ####
#makes time move faster! great for demoing our robot
#set to 10 or 100 for clean results
time_multiplier = 1.

clock = Clock()
#clock.setup()

#run this while loop in real time
while (True):
    clock.run(time_multiplier)
    time.sleep(0.1)

#this section is for unit testing
#s=59
#m=59
#h=11
#clock.set_time(s,m,h)
