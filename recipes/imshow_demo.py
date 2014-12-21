'''
Demo script for demonstrating the imshow() function
'''

import matplotlib.pyplot as plt
import matplotlib.cm as cm

x = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 1]]
plt.imshow(x, cmap=cm.Greys_r)
plt.show()
