from __future__ import division

import sys
sys.path.insert(0, '../utils')

import utils as utils
import math as math
import derivative as derivative


def test_derivative():
  assert_equal(utils.is_in(derivative.derivative(utils.to_math('x^2'), 3, 1), 1, 6), True)
