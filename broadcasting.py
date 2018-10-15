import numpy as np
from numpy import array

# Rules of Broadcasting

# Rule 1:
# If the two arrays differ in their number of dimensions,
# the shape of the one with fewer dimensions is padded with ones
# on its leading (left) side.

a = np.ones((2,3))
print(a)
b = np.arange(3) # -> b.shape(1,3)
print(b)

# Rule 2:
# If the shape of the two arrays does not match in any
# dimension, the array with shape equal to 1 in that dimension i
# s stretched to match the other shape.

b = np.arange(3)  # b.shape(2,3)

print(a + b)

# Rule 3:
# If in any dimension the sizes disagree and neither is
# equal to 1, an error is raised.

###############################################
a = array([1, 2, 3])
print(a)
b = 5
print(b)

c = a + b
print(c)
#########################################

# 2 dim array
a = np.arange(6).reshape(2, 3)
b = 5

print('\n',a)

c = a + b
print('\n',c)

# 2 dim and 1 dim array

a = np.random.normal(loc=[2., 20.], scale=[1., 3.5], size=(3, 2))
print(a)

mu = a.min(axis=1)[:, None]
print('\n', mu)

