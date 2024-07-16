import numpy as np
a3 = np.array([list(range(i * 10,i * 10+6)) for i in range(6)])
print(a3)
a = a3[:,1]
b=a3[1, 2:4]
c=a3[2:4, 4:]
d=a3[2::2, ::2]
print(a,b,c,d)
