import numpy as np
from numpy import array

# One dim list to array
a = [11, 22,33, 44, 55]
print(type(a))
a = array(a)
print(type(a))
print(a.ndim)

# Two dim array
a = np.arange(11,77, 11).reshape(3,2)
print(a)

# One dim indexing
print(a[0])

# Two dim indexing
a = np.arange(11, 77, 11).reshape(3,2)
print('\n',a)
print('\n', a[0,0])
print('\n', a[1,1])

a = np.arange(1, 61).reshape(6, 10)
print('\n',a)
print('\n',a[2:4, 3:6])
##############################################################
a = np.random.randint(10, size=(3,4,5))
print(a)
print(a.size)

###################################
a = np.zeros(10, dtype=int)
print(a)

#############################
a = np.arange(1,10).reshape(3,3)
print(a)