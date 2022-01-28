import numpy as np
import matplotlib.pyplot as plt

f = open("C:/Users/zzt55/Desktop/cell_size.txt")
lines = f.readlines()
length = len(lines)
data = np.zeros(length, dtype=int)
index = 0
for line in lines:
    formline = line.split(' ')
    data[index] = formline[3]
    index += 1


