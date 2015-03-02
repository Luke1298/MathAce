from __future__ import division

from nose.tools import *
import sys
sys.path.insert(0, '../utils')

import utils as utils
import math as math
import matrices as matrices

def matrices_multi_test():
  assert_equal(matrices.matrices_multi('[[1,1],[1,1]]','[[1],[1]]'), '[[2],[2]]')
  assert_equal(matrices.matrices_multi('[[1,1,1],[1,1,1],[1,1,1]]','[[1],[1],[1]]'), '[[3],[3],[3]]')
  assert_equal(matrices.matrices_multi('[[1],[2],[3]]', '[[1],[1]]'), 'Input ERROR')
  assert_equal(matrices.matrices_multi('[[1,1][1,1]]', '[[1,1],[1,1]]'), '[[2,2],[2,2]]')
