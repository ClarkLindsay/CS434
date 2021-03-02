#!/usr/bin/env python3

import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
# xtran = np.transpose(x)
# mulx = x*xtran
# print(mulx)
# inv = np.linalg.inv(mulx)
# mulxx = inv*xtran
# print(inv)
#
# w = mulxx*y
# print(w)
pinv = np.linalg.pinv(x)
w = np.dot(pinv, y)
print(w)
