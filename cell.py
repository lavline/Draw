import numpy as np
import matplotlib.pyplot as plt
#this is a test
f = open("C:/Users/zzt55/Desktop/cell_size.txt")
lines = f.readlines()
length = len(lines)
data = np.zeros(length, dtype=int)
index = 0
for line in lines:
    formline = line.split(' ')
    data[index] = formline[3]
    index += 1
sum = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
for d in data:
    if d == 0:
        continue
    else:
        sum += 1
    if d <= 10:
        a1 += 1
    elif d <= 20:
        a2 += 1
    elif d <= 30:
        a3 += 1
    else:
        a4 += 1

print("0-10: %d %.*f%%" % (a1, 5, a1 / sum * 100))
print("10-20: %d %.*f%%" % (a2, 5, a2 / sum * 100))
print("20-30: %d %.*f%%" % (a3, 5, a3 / sum * 100))
print(">30: %d %.*f%%" % (a4, 5, a3 / sum * 100))
print("max: %d" % (np.max(data)))
print("std: %.*f" % (3, np.std(data)))
# data_1_len = 1000000
# data_1 = data[0:data_1_len]

fig, ax = plt.subplots(constrained_layout=True)

# 设置柱形的间隔
# width = 0.12  # 柱形的宽度
# x = np.arange(0, data_1_len*width, width)
x_index = np.arange(length)

# 设置左侧Y轴对应的figure
ax.set_xlabel(f'{length} cells', size=20)
ax.set_ylabel('Number', size=20)

# ax.bar(x, data_1, width)
ax.scatter(x_index, data, s=5, alpha=0.5)
# ax.set_xticklabels(x_index)
plt.xticks([])
plt.yscale('log')
plt.yticks([2, 4, 8, 10, 20, 30, 40, 50, 100, 200, 300],
           ['2', '4', '8', '10', '20', '30', '40', '50', '100', '200', '300'], size=20)
plt.grid(axis='y', linestyle='--')
plt.text(1500000, 50, "0-10: %.*f%%\n"
                                  "10-20: %.*f%%\n"
                                  "20-30: %.*f%%\n"
                                  ">30: %.*f%%\n"
                                  ">0: %d\n"
                                  "max: %d\n"
                                  "std: %.*f" % (5, a1 / sum * 100,
                                                 5, a2 / sum * 100,
                                                 5, a3 / sum * 100,
                                                 5, a4 / sum * 100,
                                                 sum,
                                                 np.max(data),
                                                 3, np.std(data)), size=18)
fig.set_size_inches(21, 9)
plt.show()

#fig.savefig('C:/Users/zzt55/Desktop/ACL_experiment/cell-33x257x65x4.png', dpi=300)
