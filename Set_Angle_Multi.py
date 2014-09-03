#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-m0','--motor-zero', help='Selected motor', required=False)
parser.add_argument('-m1','--motor-one', help='Selected motor', required=False)
parser.add_argument('-m2','--motor-two', help='Selected motor', required=False)
parser.add_argument('-m3','--motor-three', help='Selected motor', required=False)
parser.add_argument('-m4','--motor-four', help='Selected motor', required=False)
parser.add_argument('-m5','--motor-five', help='Selected motor', required=False)
parser.add_argument('-m6','--motor-six', help='Selected motor', required=False)
parser.add_argument('-m7','--motor-seven', help='Selected motor', required=False)
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

for i in range(8):
  if 'm' + i in args:
    perPercentageDuty = float(float(servoRange) / float(100))
    print "Duty Max: %d Duty Min: %d" % (servoMax, servoMin)
    print "Per Percentage Duty: %d" % perPercentageDuty
    servoPositionMultiplied = perPercentageDuty * int(args['m' + i]])
    print "Position Multiplied: %d" % servoPositionMultiplied
    pwmOn = servoPositionMultiplied + servoMin
    pwmOff = 4096 - pwmOn
    intMotor = int(args['m' + i])
    print "Servo %d Duty: %d" % (i, pwmOn)
    intPwmOn = int(pwmOn)
    intPwmOff = int(pwmOff)
    pwm.setPWM(intMotor, 0, intPwmOn)


