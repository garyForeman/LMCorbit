#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last Modified: June 7, 2014
#functions to calculate acceleration based on galaxies' position and velocity
################################################################################

import numpy as np
from constants import *

def accelLMC(xLMC, vLMC, xSMC):
    """Returns the sum of the acceleration components acting on the LMC. These 
    components are the gravitational field of the Milky Way, dynamical friction 
    of the Milky Way, and the graviational field of the SMC. Returns a numpy 
    array of len(xLMC)."""
    distMW = np.linalg.norm(xLMC)
    velTot = np.linalg.norm(vLMC)
    distSMC = np.linalg.norm(xLMC - xSMC)

    aMWGrav = -V0**2 * xLMC / distMW**2
    aMWFric = -FRIC_CONST * LAMBDA_MW * G * MASS_LMC / distMW**2 * vLMC / velTot
    aSMCGrav = -G * MASS_SMC / (distSMC**2 + SCALE_RADIUS**2)**1.5 * \
               (xLMC - xSMC)

    return aMWGrav + aMWFric + aSMCGrav

def accelSMC(xSMC, vSMC, xLMC, vLMC):
    """Returns the sum of the acceleration components acting on the LMC. These 
    components are the gravitational field of the Milky Way, dynamical friction 
    of the Milky Way, the gravitational field of the LMC, and if close enough, 
    dynamical friction of the LMC. Returns a numpy array of len(xSMC)."""
    distMW = np.linalg.norm(xSMC)
    velTot = np.linalg.norm(vSMC)
    distLMC = np.linalg.norm(xSMC - xLMC)

    aMWGrav = -V0**2 * xSMC / distMW**2
    aMWFric = -FRIC_CONST * LAMBDA_MW * G * MASS_SMC / distMW**2 * vSMC / velTot
    aLMCGrav = -G * MASS_LMC / (distLMC**2 + SCALE_RADIUS**2)**1.5 * \
               (xSMC - xLMC)

    if distLMC <= R_MIN_FRIC: 
        vLS = vSMC - vLMC
        velTotLS = np.linalg.norm(vLS)
        aLMCFric = -FRIC_CONST * LAMBDA_LS * G * MASS_SMC / distLMC**2 * vLS / \
                   velTotLS
    else:
        aLMCFric = np.zeros(3)

    return aMWGrav + aMWFric + aLMCGrav + aLMCFric
