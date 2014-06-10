#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last Modified: May 14, 2014
#Constants necessary for performing the KDK leapfrog orbits calculation of the
#LMC and SMC around the Milky Way
################################################################################

import numpy as np

#Physical Constants and Unit Conversions
CM_PER_KPC = 3.08568025E21 #centimeters per kiloparsec
CM_PER_KM = 1.E5 #centimeters per kilometer
G_PER_M_SUN = 1.98892E33 #grams per solar mass
S_PER_YR = 31556926.
G = 6.67300E-8 #cm^3 / s^2 / g, gravitational constant

#constant parameters used for this calculation
V0 = 220.0 * CM_PER_KM #cm / s, Milky Way rotational velocity used for 
                       #isothermal sphere potential
MASS_LMC = 1.0E10 * G_PER_M_SUN #g, mass of the Large Magellanic Cloud
MASS_SMC = 3.0E9 * G_PER_M_SUN #g, mass of the Small Magellanic Cloud
SCALE_RADIUS = 3.0 * CM_PER_KPC #cm, scale radius for the Plummer sphere
LAMBDA_MW = 3.0 #Coulomb logarithm for dynamical friction within the Milky Way
LAMBDA_LS = 0.56 #Coulomb logarithm for dynamical friction on the SMC in the LMC
R_MIN_FRIC = 13.0 * CM_PER_KPC #cm minimum distance between LMC and SMC for
                               #dynamical friction to be applied to the SMC
FRIC_CONST = 0.428 #constant in front of the dynamical friction equation

TOTAL_TIME = -10.0E9 * S_PER_YR #s, total integration time
DT = -1.4E6 * S_PER_YR #s, timestep, this quantity is negative because we start
                       #the orbits calculation using present values and use
                       #KDK leapfrog to compute the position of the galaxies in
                       #the past

#current positions of the LMC and SMC in Milky Way centered coordinate system
CURRENT_POSITION_LMC = np.array([-1.0, -40.8, -26.8]) * CM_PER_KPC
CURRENT_POSITION_SMC = np.array([13.6, -34.3, -39.8]) * CM_PER_KPC
#current velocities of the LMC and SMC in Milky Way centered coordinate system
CURRENT_VELOCITY_LMC = np.array([-5.0, -225.0, 194.0]) * CM_PER_KM
CURRENT_VELOCITY_SMC = np.array([40.0, -185.0, 171.0]) * CM_PER_KM
