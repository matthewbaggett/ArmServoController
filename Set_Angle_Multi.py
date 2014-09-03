#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-m0','--motor-0', help='Selected motor', required=False)
parser.add_argument('-m1','--motor-1', help='Selected motor', required=False)
parser.add_argument('-m2','--motor-2', help='Selected motor', required=False)
parser.add_argument('-m3','--motor-3', help='Selected motor', required=False)
parser.add_argument('-m4','--motor-4', help='Selected motor', required=False)
parser.add_argument('-m5','--motor-5', help='Selected motor', required=False)
parser.add_argument('-m6','--motor-6', help='Selected motor', required=False)
parser.add_argument('-m7','--motor-7', help='Selected motor', required=False)
args = vars(parser.parse_args())

servoMin = 100  # Min pulse length out of 4096
servoMax = 700  # Max pulse length out of 4096
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

print args

for i in range(8):
  param = 'motor_' + str(i)
  print "Checking for " + param + " ..."
  if param in args:
    perPercentageDuty = float(float(servoRange) / float(100))
    print "Duty Max: %d Duty Min: %d" % (servoMax, servoMin)
    print "Per Percentage Duty: %d" % perPercentageDuty
    servoPositionMultiplied = perPercentageDuty * int(args[param])
    print "Position Multiplied: %d" % servoPositionMultiplied
    pwmOn = servoPositionMultiplied + servoMin
    pwmOff = 4096 - pwmOn
    print "Servo %d Duty: %d" % (i, pwmOn)
    intPwmOn = int(pwmOn)
    intPwmOff = int(pwmOff)
    pwm.setPWM(i, 0, intPwmOn)


