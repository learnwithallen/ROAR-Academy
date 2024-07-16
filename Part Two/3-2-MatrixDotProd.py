import numpy as np

p1 = np.array([[6,-9,1],[4,24,8]])
p1result = p1*2

mi = np.eye(2)
m2result = mi@p1

p2 = np.array([[4,3],[3,2]])
p3 = np.array([[-2,3],[3,-4]])

rop3p2 = p2@p3
print(rop3p2)