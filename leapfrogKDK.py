#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last Modified: June 9, 2014
#Kick-drift-kick leapfrog integration algorithm
################################################################################

import numpy as np
from scipy.optimize import fsolve
from accelerate import *
from constants import DT

def vUpdateLMC(vLMC, xLMC, xSMC, vLMC_half):
    return vLMC_half + 0.5 * DT * accelLMC(xLMC, vLMC, xSMC) - vLMC

def vUpdateSMC(vSMC, xSMC, xLMC, vLMC, vSMC_half):
    return vSMC_half + 0.5 * DT * accelSMC(xSMC, vSMC, xLMC, vLMC) - vSMC

def leapfrogKDK(xLMC, vLMC, xSMC, vSMC):
    """Advances the positions and velocities of the LMC and SMC by one timestep based on the kick-drift-kick leapfrog algorithm. Note: because the dynamical friction components of the accelerations depend on the galaxies' velocities, the velocity updates are implicit!"""
    vLMC_half = vLMC + 0.5 * DT * accelLMC(xLMC, vLMC, xSMC)
    vSMC_half = vSMC + 0.5 * DT * accelSMC(xSMC, vSMC, xLMC, vLMC)

    xLMC += DT * vLMC_half
    xSMC += DT * vSMC_half 

    vLMC[:] = fsolve(vUpdateLMC, vLMC, args=(xLMC, xSMC, vLMC_half))
    vSMC[:] = fsolve(vUpdateSMC, vSMC, args=(xSMC, xLMC, vLMC, vSMC_half))
