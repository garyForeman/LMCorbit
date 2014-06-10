#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last Modified: June 9, 2014
#Plots the data in orbits.dat
################################################################################

import numpy as np
import matplotlib.pylab as plt

infile = open("orbits.dat", "r")
lines = infile.readlines()
infile.close()

#posxLMC, posyLMC, poszLMC = [], [], []
#posxSMC, posySMC, poszSMC = [], [], []
rLMC = []
rSMC = []
sepLS = []
time = []
count = 0

for line in lines:
    line = [float(elmnt) for elmnt in line[:-2].split(" ")]
    xLMC = np.array(line[1:4])
    xSMC = np.array(line[4:7])
    rLMC.append(np.linalg.norm(xLMC))
    rSMC.append(np.linalg.norm(xSMC))
    sepLS.append(np.linalg.norm(xLMC - xSMC))
    time.append(line[0] / 1.0E9)

plt.plot(time, sepLS, "k-", lw = 2.0, label = "LMC-SMC")
plt.plot(time, rLMC, "k-", label = "LMC-Galaxy")
plt.plot(time, rSMC, "k--", label = "SMC-Galaxy")
plt.title(r"Bekki & Chiba model A, $\Lambda_{LS} = 0.56$")
plt.legend()
plt.xlabel("Time (Gyr)")
plt.ylabel("Distance (kpc)")
plt.ylim(ymax = 250)
plt.xlim(xmin = -8.8, xmax = 0)
#plt.xticks(range(-8,1,2), ["-8", "-6", "-4", "-2", "0"])
#plt.yticks(np.arange(5) * 50, \
#           ["0", "50", "100", "150", "200"])
plt.savefig("modelA0.56.png")
#plt.show()
