import numpy as np
import matplotlib.pyplot as plt
#this is a test
f = open("C:/Users/vzt12/Desktop/cell_size.txt")
lines = f.readlines()
length = len(lines)
data = np.zeros(length, dtype=int)
index = 0
for line in lines:
    formline = line.split(' ')
    data[index] = formline[3]
    index += 1
sum = 0
sum1 = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
for d in data:
    if d == 0:
        continue
    else:
        sum += 1
        sum1 += d
    if d <= 10:
        a1 += 1
    elif d <= 100:
        a2 += 1
    elif d <= 1000:
        a3 += 1
    else:
        a4 += 1

print(">0:\t%d(%.*f%%)" % (sum, 3, sum / length * 100))
print("1-10:\t%d(%.*f%%)" % (a1, 3, a1 / sum * 100))
print("11-100:\t%d(%.*f%%)" % (a2, 3, a2 / sum * 100))
print("101-1K:\t%d(%.*f%%)" % (a3, 3, a3 / sum * 100))
print(">1K:\t%d(%.*f%%)" % (a4, 3, a4 / sum * 100))
print("max:\t%d" % (np.max(data)))
print("avg:\t%.*f" % (3, sum1 / sum))
print("std:\t%.*f" % (3, np.std(data)))
# data_1_len = 1000000
# data_1 = data[0:data_1_len]

fig, ax = plt.subplots(constrained_layout=True)

# 设置柱形的间隔
# width = 0.12  # 柱形的宽度
# x = np.arange(0, data_1_len*width, width)
x_index = np.arange(length)

# 设置左侧Y轴对应的figure
ax.set_xlabel(f'{length} cells', size=15)
ax.set_ylabel('Number', size=15)

# ax.bar(x, data_1, width)
ax.scatter(x_index, data, s=5, alpha=0.7)
# ax.set_xticklabels(x_index)
plt.xticks([])
plt.yscale('log')
plt.yticks([1, 10, 100, 1000],
          ['1', '10','100', '1K'], size=15)
plt.grid(axis='y', linestyle='--')
'''
plt.text(1500000, 350, "0-10: %.*f%%\n"
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
'''
test_name = "33x33x33x33x5-acl1"
plt.title(test_name, size=15)
fig.set_size_inches(5, 3)
plt.show()
fig.savefig('C:/Users/vzt12/Desktop/ACL_experiment/cell-'+test_name+'.png', dpi=300)
