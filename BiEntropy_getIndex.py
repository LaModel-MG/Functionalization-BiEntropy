#!/usr/bin/python3

import sys

from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np


def Read_Two_Column_File(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(float(p[0]))
            y.append(float(p[1]))

    return x, y


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def get_closest(array, values):
    # make sure array is a numpy array
    array = np.array(array)

    # get insert positions
    idxs = np.searchsorted(array, values, side="left")
    
    # find indexes where previous index is closer
    prev_idx_is_less = ((idxs == len(array))|(np.fabs(values - array[np.maximum(idxs-1, 0)]) < np.fabs(values - array[np.minimum(idxs, len(array)-1)])))
    idxs[prev_idx_is_less] -= 1
    
    return array[idxs]
    
# Histogram from: https://stackoverflow.com/questions/7805552/fitting-a-histogram-with-python
# Extracting nearest value from: https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
# Extracting index from: https://stackoverflow.com/questions/176918/how-to-find-the-index-for-a-given-item-in-a-list

file_name = sys.argv[1]

filen=file_name+".dat"

# Read data from a text file. Two number per line
x, y = Read_Two_Column_File(filen)
datos = y

# best fit of data
(mu, sigma) = norm.fit(datos)

# the histogram of the data
n, bins, patches = plt.hist(datos, 50, facecolor='green', alpha=0.75)
#print(n.max())


# add a 'best fit' line
y = n.max() * norm.pdf(bins, mu, sigma) / norm.pdf(bins, mu, sigma).max()
#print("y norm.pdf max", norm.pdf(bins, mu, sigma).max())

l = plt.plot(bins, y, 'r--', linewidth=2)



val = []
val = [mu]
#print(r'mu=%.8f' %mu)
#print("get_closest value:", get_closest(datos, val))
#print("get_closest index:", datos.index(get_closest(datos, val)))
#print("get_closest delta:", mu - get_closest(datos, val))
#print("find_nearest value", find_nearest(datos, val))
print(datos.index(find_nearest(datos, val)))
#print("find_nearest delta:", mu - find_nearest(datos, val))

#plot

ax = plt.gca()
plt.xlabel('BiEntropy ({})'.format(file_name[10:]))
plt.ylabel('Frequency')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
#plt.text(0, 0, '{}'.format(datos.index(find_nearest(datos, val))), horizontalalignment='left',
#         verticalalignment='center', transform = ax.transAxes,
#         fontsize=12, color='blue')
plt.savefig(file_name+".pdf", format="pdf", bbox_inches="tight")
plt.grid(True)

#plt.show()
