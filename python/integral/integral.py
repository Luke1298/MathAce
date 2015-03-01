from __future__ import division
import sys
sys.path.insert(0, '../utils')

import utils as utils
import math as math

def integral (function, lowerbound, upperbound, interval_power):
  _lowerbound = lowerbound
  _upperbound = upperbound
  interval_number = interval_power*1000*(abs(upperbound-lowerbound))

  if (interval_number == 0):
    return 0
  else:
    interval_space = abs(upperbound-lowerbound)/interval_number

  if (lowerbound > upperbound):
    flip_it = True
    upperbound = _lowerbound
    lowerbound = _upperbound
  else:
    flip_it = False

  a = lowerbound
  area = 0
  while (a<upperbound):
    b = a + interval_space
    x = (a+b)/2
    area += eval(function)*interval_space
    a+= interval_space

  if (flip_it):
    return (-1.0*area)

  else:
    return area

