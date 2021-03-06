import numpy as np
from numpy import array
from numpy import tensordot

T = array([
  [[1,2,3],    [4,5,6],    [7,8,9]],
  [[11,12,13], [14,15,16], [17,18,19]],
  [[21,22,23], [24,25,26], [27,28,29]],
  [[30,32,23], [44,25,26], [27,28,29]],
  ])

# help(T.shape)
print(T.shape)
print(T.shape[0])
# ######################################################################


A = array([
  [[1,2,3],    [4,5,6],    [7,8,9]],
  [[11,12,13], [14,15,16], [17,18,19]],
  [[21,22,23], [24,25,26], [27,28,29]],
  ])
B = array([
  [[1,2,3],    [4,5,6],    [7,8,9]],
  [[11,12,13], [14,15,16], [17,18,19]],
  [[21,22,23], [24,25,26], [27,28,29]],
  ])
# C = A + B
# print(C)
#######################################################################
D = tensordot(A, B)
print(D)

####################################################

a = np.arange(60)

print(a)