import numpy as np
from numpy import array

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

print(a - mu)