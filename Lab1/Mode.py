from statistics import mode
from fractions import Fraction as fr

data1 = (2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7)
data2 = (2.4, 1.3, 1.3, 1.3, 2.4, 4.6)
data3 = (fr(1, 2), fr(1, 2), fr(10, 3), fr(2, 3))
data4 = (-1, -2, -2, -2, -7, -7, -9)
data5 = ("red", "blue", "black", "blue", "black", "black", "brown")

print("Mode of data set 1 is % s" % (mode(data1)))
print("Mode of data set 2 is % s" % (mode(data2)))
print("Mode of data set 3 is % s" % (mode(data3)))
print("Mode of data set 4 is % s" % (mode(data4)))
print("Mode of data set 5 is % s" % (mode(data5)))
