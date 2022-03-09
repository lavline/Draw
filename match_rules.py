import numpy as np
import matplotlib.pyplot as plt

f = open("C:/Users/vzt12/Desktop/match_cycle.txt")
lines = f.readlines()
length = len(lines)
data = np.zeros(length, dtype=float)
#check_rules = np.zeros(length, dtype=int)
index = 0
for line in lines:
    formline = line.split(' ')
    #print(formline[5])
    data[index] = formline[7]
    index += 1
#data_1_len = 1000000
#data_1 = data[0:data_1_len]

a1 = 0
a2 = 0
a3 = 0
a4 = 0
for d in data:
    if d <= 50:
        a1 += 1
    elif d <= 100:
        a2 += 1
    elif d <= 500:
        a3 += 1
    else:
        a4 += 1

print("0-50:\t%d(%.*f%%)" % (a1, 2, a1 / length * 100))
print("51-100:\t%d(%.*f%%)" % (a2, 2, a2 / length * 100))
print("101-500:\t%d(%.*f%%)" % (a3, 2, a3 / length * 100))
print(">500:\t%d(%.*f%%)" % (a4, 2, a4 / length * 100))
print("max:\t%d" % (np.max(data)))
print("min:\t%d" % (np.min(data)))
print("avg:\t%.*f" % (3, np.mean(data)))
print("std:\t%.*f" % (3, np.std(data)))


fig, ax = plt.subplots(constrained_layout=True)

x_index = np.arange(length)

ax.set_xlabel(f'{length} messages', size=15)
ax.set_ylabel('Check Rules', size=15)

ax.scatter(x_index, data, s=5, alpha=0.01)
#ax.plot(x_1, y_1, color='#FF3935')
#ax.set_xticklabels(x_index)
plt.xticks([])
#lt.yscale('log')
#plt.yticks([200, 400, 800, 1600], ['2', '4', '8', '16'])
plt.yticks(size=12)
plt.grid(axis='y', linestyle='--')
'''
plt.text(1060000, 500, "0-200: %.*f%%\n"
                                  "200-500: %.*f%%\n"
                                  ">500: %.*f%%\n"
                                  "max: %d\n"
                                  "min: %d\n"
                                  "average: %.*f\n"
                                  "std: %.*f" % (3, a1 / length * 100,
                                                 3, a2 / length * 100,
                                                 3, a3 / length * 100,
                                                 np.max(data),
                                                 np.min(data),
                                                 1, np.mean(data),
                                                 3, np.std(data)), size=18)
'''
test_name = "33x33x33x33x5-acl1"
plt.title(test_name, size=15)
fig.set_size_inches(5, 3)
plt.show()
fig.savefig('C:/Users/vzt12/Desktop/ACL_experiment/match_rules_'+test_name+'.png', dpi=300)