from __future__ import division

from nose.tools import *
import sys
sys.path.insert(0, '../utils')

import utils as utils
import math as math
import derivative as derivative


def test_derivative():
 #assert_equal(utils.is_in(derivative.derivative(utils.to_math(function), point, power), pecent_margin, expected_out), True/Flase)
  assert_equal(utils.is_in(derivative.derivative(utils.to_math('x^2'), 3, 1), 1, 6), True)
  assert_equal(utils.is_in(derivative.derivative(utils.to_math('x^2'), 3, 1), 1, 7), False)
  assert_equal(utils.is_in(derivative.derivative(utils.to_math('x^3'), 3, 1), 1, 27), True)
  assert_equal(utils.is_in(derivative.derivative(utils.to_math('pix^2'), 7, 1), 1, (math.pi)*14), True)
  assert_equal(utils.is_in(derivative.derivative(utils.to_math('x^3+2x+7'), 5, 1), 1, 77), True)

def test_nomial_derivative():
  assert_equal(derivative.nomial_derive(utils.to_math('x^2'), 'x'), utils.to_math('2x^1'))
  assert_equal(derivative.nomial_derive(utils.to_math('4x^3'), 'x') , utils.to_math('12x^2'))
  assert_equal(derivative.nomial_derive(utils.to_math('1/2x^2'), 'x') , utils.to_math('1.0x^1'))
  assert_equal(derivative.nomial_derive(utils.to_math('6x^4'), 'x') , utils.to_math('24x^3'))
  assert_equal(derivative.nomial_derive(utils.to_math('6^4'), 'x') , '0')
  assert_equal(derivative.nomial_derive(utils.to_math('6x'), 'x') , '6')

def test_polynomial_derivative():
  assert_equal(derivative.polynomial_derive(utils.to_math('x^2'), 'x'), utils.to_math('2x^1'))
  assert_equal(derivative.polynomial_derive(utils.to_math('x^3 + 3 x^2 + 4 x + 2'), 'x') , utils.to_math('3x^2 + 6 x^1 + 4 + 0'))
  assert_equal(derivative.polynomial_derive(utils.to_math('x^3 - 3 x^2 + 4 x - 2'), 'x') , utils.to_math('3x^2 - 6 x^1 + 4 - 0'))

