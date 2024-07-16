import numpy as np

def swap_Rows(M,a,b):
    if a >= M.shape[0] or b >= M.shape[0] or a<0 or b<0:
        raise IndexError("Row Indicies are out of bounds")
    temp = M[a].copy()
    M[[a,b],:]=M[[b,a],:]


    return M
def swap_Columns(M,a,b):
    if a >= M.shape[1] or b >= M.shape[1] or a<0 or b<0:
        raise IndexError("Row Indicies are out of bounds")
    temp = M[:,a].copy()
    M[:,a]=M[:,b]
    M[:,b] = temp
    M[:,[a,b]]=M[:,[b,a]]
    return M

v = np.array([[0,1,2],[3,4,5]])
-