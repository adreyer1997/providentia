import matplotlib.pyplot as plt
import numpy as np
import csv
import config

ANALYSIS = ""

if config.KERN == 1:
    ANALYSIS = "kate"
elif config.KERN == 2:
    ANALYSIS = "reviews"
elif config.KERN == 3:
    ANALYSIS = "city"

t_avg = np.array([])
t_dev = np.array([])
p_avg = np.array([])
p_dev = np.array([])
j_avg = np.array([])
j_dev = np.array([])
x_perc = []
x_size = []

import matplotlib.pyplot as plt

all_val = np.array([])

with open('./%s_results/setup%d_results/setup%d_%s.csv' % (config.DS, config.SETUP, config.SETUP, ANALYSIS)) as csvfile:
    reader =  csv.reader(csvfile, delimiter=",")
    for row in reader:
        avg = float(row[0])
        dev = float(row[1])
        perc = float(row[2])
        g = row[3]
        size = float(row[4])

        if g == "JanusGraph":
            j_avg = np.append(j_avg, avg)
            j_dev = np.append(j_dev, dev)
            x_perc.append(perc)
            x_size.append(size)
        elif g == "TigerGraph":
            t_avg = np.append(t_avg, avg)
            t_dev = np.append(t_dev, dev)
        elif g == "PostgreSQL":
            p_avg = np.append(p_avg, avg)
            p_dev = np.append(p_dev, dev)

        all_val = np.concatenate((all_val, [avg]))

print(j_dev)
print(j_avg)
print(x_perc)
print(x_size)
plt.errorbar(x_size, j_avg, yerr=j_dev, label="JanusGraph", ecolor='purple', color="green")
plt.errorbar(x_size, t_avg, yerr=t_dev, label="TigerGraph", ecolor='red', color="orange")
plt.errorbar(x_size, p_avg, yerr=p_dev, label="PostgreSQL", ecolor='black', color="blue")

plt.title("Setup %d | Kernel %d: Database Response Times Over Data Loaded" % (config.SETUP, config.KERN))
plt.xlabel("Data loaded (MB)")
plt.ylabel("Response time (ms)")
plt.legend()
plt.savefig('./%s_graphs/%sPlotSetup%s.pdf' % (config.DB, ANALYSIS, config.SETUP))
