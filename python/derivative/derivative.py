from __future__ import division
import sys
sys.path.insert(0, '../utils')

import utils as utils
import math as math

def derivative (function, point, interval_power):
  lower_x_coor = point - (1/(1000*interval_power))
  upper_x_coor = point + (1/(1000*interval_power))
  delta_x = (2/(1000*interval_power))
  x = upper_x_coor
  upper_y_coor = eval(function)
  x = lower_x_coor
  lower_y_coor = eval(function)
  delta_y = upper_y_coor - lower_y_coor

  return (delta_y / delta_x)

def nomial_derive(function, var):
  m = -1
  coefficient = ''
  power = ''
  c = 0
  for y in function:
    if y == var:
      m = c
    c += 1
  if (m >= 0):
    coefficient = function[:m]
    power = function[(m+1):]
    _coefficient = ''
    _power = ''

    for x in coefficient:
      if x != '*':
        _coefficient+=x
    coefficient = _coefficient

    if (coefficient == ''):
      coefficient = '1'

    for x in power:
      if x != '*':
        _power+=x
    power = _power

    if (power != ''):
      new_coefficient = eval(coefficient)*eval(power)
      new_power = eval(power)-1
      return utils.to_math(str(new_coefficient) + var + '^' + str(new_power))

    else:
      new_coefficient = eval(coefficient * 1)
      return str(new_coefficient)
  else:
    return '0'

def polynomial_derive(function, var):
  y = ''
  ind_poly = []
  poly_derive = []
  signs = []
  final = ''
  for x in function:
    if (x != '+') and (x!= '-'):
      y+=x
    else:
      ind_poly.append(y)
      signs.append(x)
      y = ''
  ind_poly.append(y)
  for x in ind_poly:
    poly_derive.append(nomial_derive(x,'x'))
  for x in range(0, len(signs)):
    final += poly_derive[x]
    final += signs[x]
  final += poly_derive[-1]
  return final


