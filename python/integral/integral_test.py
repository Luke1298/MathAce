from __future__ import division

from nose.tools import *
import sys
sys.path.insert(0, '../utils')

import utils as utils
import integral as integral
import math as math

def test_integral():
  assert_equal(utils.is_in(integral.integral(utils.to_math('3x^3+x^2-1'), 3, 5, 1), 1, (1316/3) ), True)
  assert_equal(utils.is_in(integral.integral(utils.to_math('3x^3+2^x-1'), 3, 5, 1), 1, (406+(24/math.log(2))) ), True)
  assert_equal(utils.is_in(integral.integral(utils.to_math('3x^3+x^2-1'), 5, 3, 1), 1, (-1316/3) ), True)
  assert_equal(utils.is_in(integral.integral(utils.to_math('3x^3+x^2-1'), 3, 3, 1), 1, (0) ), True)
