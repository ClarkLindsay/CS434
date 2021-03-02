#!/usr/bin/env python3

def mul(list1, list2):
	ans = [x*y for x, y in zip(list1, list2)]

	return ans

def mydot(v1, v2):
    return sum([x*y for x,y in zip(v1, v2)])

def matmulvec(M, v):
    return [mydot(r,v) for r in M]


def transpose(list):
	ans = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
	for i in range(len(list)):
		ans[i][0] = list[i]

	return ans

def average(list):
    avg = sum(list) / len(list)
    return avg

def function(x, w, b):
    return w*x + b

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]

xt = transpose(x)
print(xt)
xmul = matmulvec(xt, x)
print(xmul)

# w = (sum(mul(x,y)) - (sum(x)*sum(y))/len(x)) / (sum(mul(x,x)) - (sum(x)**2)/len(x))
# b = (sum(y) - w*sum(x))/len(x)
# 
# print(w)
# print(b)
#
# h = [None]*10
# for i in x:
#     h[i] = w*x[i] + b
#
#
# print(h)
#
# ans = function(3.3, w, b)
# print(ans)
