from __future__ import division

from nose.tools import *
import sys
sys.path.insert(0, '../utils')

import utils as utils
import integral as integral
import math as math

def is_in(value, percent, expected):
  percent_up = 1+(percent*.01)
  percent_down = 1-(percent*.01)
  fix_up = expected*percent_up
  fix_down = expected*percent_down
  if (value <= fix_up and value >= fix_down and value >= 0):
    return True
  elif (value >= fix_up and value <= fix_down and value <= 0):
    return True
  else:
    return False


def test_integral():
  assert_equal(is_in(integral.integral(utils.to_math('3x^3+x^2-1'), 3, 5, 10), 1, (1316/3) ), True)
  assert_equal(is_in(integral.integral(utils.to_math('3x^3+2^x-1'), 3, 5, 10), 1, (406+(24/math.log(2))) ), True)
  assert_equal(is_in(integral.integral(utils.to_math('3x^3+x^2-1'), 5, 3, 10), 1, (-1316/3) ), True)
  assert_equal(is_in(integral.integral(utils.to_math('3x^3+x^2-1'), 3, 3, 10), 1, (0) ), True)
