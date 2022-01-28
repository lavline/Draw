import numpy as np
import matplotlib.pyplot as plt

f = open("C:/Users/zzt55/Desktop/match_cycle.txt")
lines = f.readlines()
length = len(lines)
data = np.zeros(length, dtype=int)
check_rules = np.zeros(length, dtype=int)
index = 0
for line in lines:
    formline = line.split(' ')
    #print(formline[5])
    data[index] = formline[5]
    index += 1
#data_1_len = 1000000
#data_1 = data[0:data_1_len]

a1 = 0
a2 = 0
a3 = 0
for d in data:
    if d <= 1000:
        a1 += 1
    elif d<=2000:
        a2 += 1
    else:
        a3 += 1

print("0-1k: %d %.*f%%" % (a1, 5, a1 / length * 100))
print("1k-2k: %d %.*f%%" % (a2, 5, a2 / length * 100))
print(">2k: %d %.*f%%" % (a3, 5, a3 / length * 100))
print("max: %d" % (np.max(data)))
print("min: %d" % (np.min(data)))
print("average: %.*f" % (3, np.mean(data)))
print("std: %.*f" % (3, np.std(data)))


fig, ax = plt.subplots(constrained_layout=True)

x_index = np.arange(length)

# 设置左侧Y轴对应的figure
ax.set_xlabel(f'{length} messages', size=20)
ax.set_ylabel('Cycle', size=20)

ax.scatter(x_index, data, s=5, alpha=0.05)
#ax.plot(x_1, y_1, color='#FF3935')
#ax.set_xticklabels(x_index)
plt.xticks([])
plt.yscale('log')
plt.yticks([200, 300, 500, 1000, 2000, 3000, 10000, 50000], ['200', '300', '500', '1K', '2K', '3K', '10K', '50K'], size=20)
plt.grid(axis='y', linestyle='--')
plt.text(1000000, 10000, "0-1k: %.*f%%\n"
                                  "1k-2k: %.*f%%\n"
                                  ">2k: %.*f%%\n"
                                  "max: %d\n"
                                  "min: %d\n"
                                  "average: %.*f\n"
                                  "std: %.*f" % (5, a1 / length * 100,
                                                 5, a2 / length * 100,
                                                 5, a3 / length * 100,
                                                 np.max(data),
                                                 np.min(data),
                                                 3, np.mean(data),
                                                 3, np.std(data)), size=18)
test_name = "33x257x65x4-(5)"
plt.title(test_name, size=20)
fig.set_size_inches(21, 9)
plt.show()
#fig.savefig('C:/Users/zzt55/Desktop/ACL_experiment/match_cycle_'+test_name+'.png', dpi=300)

