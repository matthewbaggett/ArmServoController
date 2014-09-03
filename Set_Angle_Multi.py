#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

import argparse

rangeMax = 16

parser = argparse.ArgumentParser(description='Set motor positions')
for i in range(rangeMax):
  parser.add_argument('-m' + str(i),'--motor-' + str(i), help='Percentage position Motor ' + str(i), required=False)
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

for i in range(rangeMax):
  param = 'motor_' + str(i)
  print "Checking for " + param + " ..."
  if param in args:
    if args[param] is not None:
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


