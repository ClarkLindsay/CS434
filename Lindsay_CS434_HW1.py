#!/usr/bin/env python3

def transpose(list):
	ans = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
	for i in range(len(list)):
		ans[i][0] = list[i]

	return ans

def mulrc(list1, list2):
	ans = 10*[0]
	for i in range(len(list1)):
		ans[i] = list1[i]*list2[i][0]

	return ans

def mulrr(list1, list2):
	ans = [x*y for x, y in zip(list1, list2)]

	return ans

def dotp(list1, list2):
	ans = 0
	for i in range(len(list1)):
		ans = ans + list1[i]*list2[i][0]

	return ans

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]
xt = transpose(x)
dot = dotp(x, xt)
print(dot)
# inv = reversed(dot)
w = dot(dot, y)
print(w)
