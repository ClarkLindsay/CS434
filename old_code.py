#!/usr/bin/env python3
# import numpy as np
# import matplotlib.pyplot as plt

def average(list):
    avg = sum(list) / len(list)
    return avg

def listmul(list1, list2):
	ans = [x*y for x, y in zip(list1, list2)]

	return ans

def function(x, w, b):
    return w*x + b

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]
# number of observations/points
n = len(x)

# mean of x and y vector
avgx = average(x);
avgy = average(y);

# calculating cross-deviation and deviation about x
xy = sum(listmul(x, y)) - n*avgy*avgx
xx = sum(listmul(x, x)) - n*avgx*avgx
# calculating regression coefficients
w = xy / xx
b = avgy - w*avgx
print(b)
print(w)
ans = function(3.3, w, b)
print(ans)
