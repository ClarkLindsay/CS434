#!/usr/bin/env python3

# Transpose of a row vector into a column vector
def transpose(list):
	ans = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
	for i in range(len(list)):
		ans[i][0] = list[i]
	return ans

# multiplication of two row vectors
def mul(list1, list2):
	ans = [x*y for x, y in zip(list1, list2)]
	return ans

# Scalar muliplication when the list is a row vector
def scalarmul(c, list):
	ans = [0]*len(list)
	for i in range(len(list)):
	    ans[i] = c*list[i]
	return ans

# Dot product when both lists are row vectors
def dot(list1, list2):
	ans = 0
	for i in range(len(list1)):
		ans = ans + list1[i]*list2[i]
	return ans

# Dot product when one list is a row vector and one is a column vector
def dott(list1, list2):
	ans = 0
	for i in range(len(list1)):
		ans = ans + list1[i]*list2[i][0]
	return ans

# To find y values given an x value
def function(x, w, b):
    return w*x + b

# x-values
x = [20, 16, 19.8, 18.4, 17.1, 15.5, 14.7, 17.1, 15.4, 16.2, 15, 17.2, 16, 17]
# y-values
y = [88.6, 71.6, 93.3, 84.3, 80.6, 75.2, 69.7, 82, 69.4, 83.3, 79.6, 82.6, 80.6, 83.5]

# Alternative method I tried to get the w and b value
# walt = (sum(mul(x,y)) - (sum(x)*sum(y))/len(x)) / (sum(mul(x,x)) - (sum(x)**2)/len(x))
# balt = (sum(y) - walt*sum(x))/len(x)
# print(walt)

# Take the transpose of x
xt = transpose(x)
# Take the inverse of the dot product of x and x transpose (in this case, because x*xt is a scalar, the inverse is just 1/input)
inv = 1/dott(x, xt)
# Multiply the inverse we just found by the transpose of x (scalar multiplication)
psuinv = []
for i in range(len(xt)):
    psuinv.append(inv*xt[i][0])

# I thought it needed to be multiplied out this way before I realized it was a dot product
# w = mul(y, psuinv)
# print(w)

# Dot product of y and the pseudo-inverse
w = dot(y, psuinv)
print("Optimal value of w: " + str(w))

# I made the same mistake with h here that I did with w before, thinking it needed this type of multiplication
# h = mul(w, x)
# print(h)

# Multiply the w value found in the training section by the starting x values
h = scalarmul(w, x)
print("h(x): " + str(h))

x1 = 14.8
x2 = 18
y1 = w*x1
y2 = w*x2
print("y1 = " + str(y1))
print("y2 = " + str(y2))

# Using the alternative method I discussed above
# y1alt = function(x1, walt, balt)
# y2alt = function(x2, walt, balt)
# print(y1alt)
# print(y2alt)
