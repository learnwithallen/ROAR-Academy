import numpy as np
sample_list = [1,2,3,4,5,6,7,8,9,10,11,12]
def set_array(l,r,c):
    sample_array = np.array(l)
    shaped_array = sample_array.reshape(r,c)
    return(shaped_array)

x=set_array(sample_list,4,3)
y=set_array(sample_list,3,4)

z=x@y
print(z)