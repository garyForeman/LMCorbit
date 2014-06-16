#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last Modified: June 9, 2014
#Driver for the LMC SMC orbits calculation. Writes orbtis data to orbits.dat.
################################################################################

import numpy as np
from accelerate import accelLMC
from constants import *
from leapfrogKDK import leapfrogKDK

def writeData(filename, time, xLMC, xSMC, aLMC):
    """Writes data to filename. Filename should be opened for writing before 
    this function call."""
    xLMC_KPC = xLMC / CM_PER_KPC
    xSMC_KPC = xSMC / CM_PER_KPC
    filename.write(str(time / S_PER_YR) + " ") 
    for i in xrange(len(xLMC_KPC)): filename.write(str(xLMC_KPC[i]) + " ")
    for i in xrange(len(xSMC_KPC)): filename.write(str(xSMC_KPC[i]) + " ")
    for i in xrange(len(aLMC)): filename.write(str(aLMC[i]) + " ")
    filename.write("\n")

t = 0.0 #today
xLMC = CURRENT_POSITION_LMC
vLMC = CURRENT_VELOCITY_LMC
xSMC = CURRENT_POSITION_SMC
vSMC = CURRENT_VELOCITY_SMC
aLMC = accelLMC(xLMC, vLMC, xSMC)

year = 1 #used for run status io
outfile = open("orbits.dat", 'w')
writeData(outfile, t, xLMC, xSMC, aLMC)

while t > TOTAL_TIME:
    leapfrogKDK(xLMC, vLMC, xSMC, vSMC)
    aLMC = accelLMC(xLMC, vLMC, xSMC)
    t += DT
    writeData(outfile, t, xLMC, xSMC, aLMC)

    if int(np.ceil(-t / S_PER_YR / 1.E9)) % year == 0:
        print str(year - 1) + " Gyr"
        year += 1

outfile.close()
