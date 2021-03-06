import matplotlib.pyplot as plt
import numpy             as np
import csv
from numpy import genfromtxt

<<<<<<< HEAD
# set the prefix to the sample you want to evaluate
prefix = '../loggings-1819/jesenwang-26-10-2018/stint-03/'

#traj_data         = genfromtxt(prefix + '/path.csv',         delimiter=',')
#path_data         = genfromtxt(prefix + '/t3_tp.log',        delimiter=',')
data   = genfromtxt(prefix + '/t3_tp.log',   delimiter=',')
=======
data = genfromtxt('../example-data/wemding-2018-08-05/trackdrive-v04/t3_tp.log', delimiter=',')
>>>>>>> 0a54cf1e1fff4bb2869432a3b24ef48aee652c93
# data_darknet = genfromtxt('../example-data/wemding-2018-08-02/trackdrive-v16/t3_darknet.log', delimiter=',')

fig, ax = plt.subplots(figsize=(16,16))

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_title("X/Y Map")

acc_data = []
acc_data_2 = []
#acc_data_3 = []
#acc_data_4 = []

counter = 0
for frame in data:
    dim      = frame[2]
    dim_2    = frame[3]
    #if counter % 10:
    acc_data = np.append(acc_data, dim)
    acc_data_2 = np.append(acc_data_2, dim_2)
    #acc_data_3 = np.append(acc_data_3, dim_3)
    #acc_data_4 = np.append(acc_data_4, dim_4)
    #counter += 1

#acc_data_dark = []
#
#for frame_dark in data_darknet:
#    dim      = frame_dark[14]
#    #if counter % 10:
#    acc_data_dark = np.append(acc_data_dark, dim)


plt.ylim(-3,3,0.5)

# ax.scatter(acc_data, acc_data_2, s = 2.5)
plt.plot(acc_data, label = 'distance')
plt.plot(acc_data_2, label = 'angle')
#plt.plot(acc_data_3, label = 'yaw_rate should')
#plt.plot(acc_data_4, label = 'vx')
#plt.plot(acc_data_dark, label = 'yaw_rate is')
plt.grid()
plt.legend()
plt.show()