import numpy as np
import matplotlib.pyplot as plt

dow = np.loadtxt('dow.csv', delimiter=',')
print(dow)
print(dow.shape, dow.size)

a = np.array(dow)
print(a)

b = a[a > 5.5e9]
print(a > 5.5e9)
print(b)
print(b.sum())

# plt.plot()
plt.plot(b)
plt.title('Dow', fontsize=26)
plt.savefig('image_dow.png')
plt.show()