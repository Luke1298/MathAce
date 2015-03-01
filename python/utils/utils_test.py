from nose.tools import *
import utils as utils

def test_find_pi():
  assert_equal(utils.find_pi('pipipipi'), '(math.pi)(math.pi)(math.pi)(math.pi)')
  assert_equal(utils.find_pi('3pi4pipii'), '3(math.pi)4(math.pi)(math.pi)i')
  assert_equal(utils.find_pi('pihere'), '(math.pi)here')
  assert_equal(utils.find_pi('piepiepie'), '(math.pi)e(math.pi)e(math.pi)e')
  assert_equal(utils.find_pi('ppipipp'), 'p(math.pi)(math.pi)pp')
  assert_equal(utils.find_pi('xpixpipix'), 'x(math.pi)x(math.pi)(math.pi)x')

def test_find_e():
  assert_equal(utils.find_e('eee'), '(math.e)(math.e)(math.e)')
  assert_equal(utils.find_e('eeemememe'), '(math.e)(math.e)(math.e)m(math.e)m(math.e)m(math.e)')
  assert_equal(utils.find_e('Lukee'), 'Luk(math.e)(math.e)')
  assert_equal(utils.find_e('knee'), 'kn(math.e)(math.e)')
  assert_equal(utils.find_e('meee'), 'm(math.e)(math.e)(math.e)')
  assert_equal(utils.find_e('3e4e5e'), '3(math.e)4(math.e)5(math.e)')

def test_paren_nxt_number():
  assert_equal(utils.paren_nxt_number('()3()'), '()*3*()')
  assert_equal(utils.paren_nxt_number('4(53)2'), '4*(53)*2')
  assert_equal(utils.paren_nxt_number('6(4(...'), '6*(4*(...')
  assert_equal(utils.paren_nxt_number('12(12)12(12)...12()'), '12*(12)*12*(12)...12*()')
  assert_equal(utils.paren_nxt_number('(((()()()()())))'), '(((()()()()())))')

def test_paren_next_paren():
  assert_equal(utils.paren_nxt_paren('()()'), '()*()')
  assert_equal(utils.paren_nxt_paren(')()()()((()('), ')*()*()*()*((()*(')
  assert_equal(utils.paren_nxt_paren('(((('), '((((')
  assert_equal(utils.paren_nxt_paren('()3'), '()3')
  assert_equal(utils.paren_nxt_paren('())'), '())')

def test_paren_nxt_var():
  assert_equal(utils.paren_nxt_var(')x', 'x'), ')*x')
  assert_equal(utils.paren_nxt_var('x(', 'x'), 'x*(')
  assert_equal(utils.paren_nxt_var('x(x)x', 'x'), 'x*(x)*x')
  assert_equal(utils.paren_nxt_var('y(y)y', 'x'), 'y(y)y')

def test_to_math():
  assert_equal(utils.to_math('x^2'),'x**2')
  assert_equal(utils.to_math('3x'), '3*x')
  assert_equal(utils.to_math('3x^2'), '3*x**2')
  assert_equal(utils.to_math('13x^2'), '13*x**2')
  assert_equal(utils.to_math('13x^4'), '13*x**4')
  assert_equal(utils.to_math('3*x**2'), '3*x**2')
  assert_equal(utils.to_math('3ex'), '3*(math.e)*x')
  assert_equal(utils.to_math('pix'), '(math.pi)*x')
  assert_equal(utils.to_math('epiex'), '(math.e)*(math.pi)*(math.e)*x')
