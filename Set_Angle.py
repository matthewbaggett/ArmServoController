#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-m','--motor', help='Selected motor', required=True)
parser.add_argument('-p','--position', help='Position to set (between 0 and 100)', required=True)
args = vars(parser.parse_args())

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoRange = servoMax - servoMin

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
perPercentageDuty = float(float(servoRange) / float(100))
print "Duty Max: %d Duty Min: %d" % (servoMax, servoMin)
print "Per Percentage Duty: %d" % perPercentageDuty
servoPositionMultiplied = perPercentageDuty * int(args['position'])
print "Position Multiplied: %d" % servoPositionMultiplied
pwmOn = servoPositionMultiplied + servoMin
print "Servo %d Duty: %d" % (int(args['motor']), pwmOn)
pwm.setPWM(0, int(args['motor']), pwmOn)


