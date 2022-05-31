import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


f1 = open("./data/match_cycle.txt")
f2 = open("./data/match_log.txt")
line1 = f1.readline()
line2 = f2.readline()
cycle = []
checks = []
field = []
innernodes = []
leafnodes = []
match_time = []
counter = 0


while line1:
    formline1 = line1.split(' ')
    formline2 = line2.split(' ')
    #if int(formline2[7]) < 50 and int(formline1[5]) > 1500:
        #print(int(formline1[1]), int(formline2[7]), int(formline1[5]))
        #counter += 1
    if int(formline1[5]) < 10000:
        cycle.append(int(formline1[5]))
        #match_time.append(float(formline1[7]))
        innernodes.append(int(formline2[5]))
        leafnodes.append(int(formline2[7]))
        checks.append(int(formline2[9]))
    #field.append(int(formline2[9]))
    line1 = f1.readline()
    line2 = f2.readline()

#print(counter)
length = len(cycle)
print(length)

cycle = np.array(cycle)
checks = np.array(checks)
innernodes = np.array(innernodes)
leafnodes = np.array(leafnodes)

#x = np.zeros(22)
#for nodes in leafnodes:
#    x[nodes] += 1
#for n in x:
#    print(n)

#field = np.array(field)

#X = np.unique(checks)
#Y = np.unique(field)
#X, Y = np.meshgrid(checks, field)
#ZZ, _Z = np.meshgrid(cycle, cycle)
#Z = (ZZ + _Z) / 2

fig, ax = plt.subplots(constrained_layout=True)
#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')


#data1 = np.array(data1)
#data2 = np.array(data2)
#x_index = np.arange(length)
#ax.set_xlabel('Check Fields', size=15)
ax.set_xlabel('Check innernodes', size=15)
ax.set_ylabel('Cycle', size=15)
#ax.set_ylabel('Check Fields', size=15)
#ax.set_ylabel('check leafnodes', size=15)
#ax.set_ylabel('Time(um)', size=15)

#ax.plot_surface(X, Y, Z, rstride=10, cstride=20, cmap='rainbow')

# x=np.arange(length)
# cycle.sort()
ax.scatter(cycle, checks, s=1)
#ax.scatter(innernodes, leafnodes, s=5, alpha=0.8)
#ax.scatter(field, cycle, s=5, alpha=0.8)
#ax.scatter(checks, field, s=5, alpha=0.1)
#ax.scatter3D(checks, field, cycle, s=5, alpha=0.8)
#ax.plot3D(checks, field, cycle)

#ax.plot(x_index, data1)
#ax.plot(x_index, data2)
#ax.set_xticklabels(x_index)
#plt.xticks([])
#plt.xticks([4,6,8,10,12,14,16,18,20])
#plt.yscale('log')

# xtick=[]
# xtick_str=[]
# for i in range(11):
#     xtick_str.append(i / 10)
#     xtick.append(length * i / 10)
#
# plt.xticks(xtick, xtick_str)

plt.grid(axis='x', linestyle='--')
plt.grid(axis='y', linestyle='--')

#test_name = "65x65x33x33-rules2"
#plt.title(test_name, size=15)
fig.set_size_inches(10, 6)


# transition = lambda x,N: (1+np.sin(-0.5*np.pi+2*np.pi*x / (1.0*N)))/2.0
# for i in range(40):
#     horiAngle = 45+50*transition(i, 40)
#     verAngle = 50+43*transition(i, 40)
#     ax.view_init(verAngle, horiAngle)
#     filename = 'animFram/' + str('%03d'%i) + '.png'
#     plt.savefig(filename, dpi=96)

#ax.view_init(elev=90, azim=0)
plt.show()
#fig.savefig('C:/Users/vzt12/Desktop/ACL_experiment/match_rules_'+test_name+'.png', dpi=300)