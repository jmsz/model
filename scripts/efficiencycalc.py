# 10% efficiency at 50% solida angle coverage

import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

source_activity = 1000 # gammas per s
inner_radius = 1 # m

detector_x = 0.1 # m
detector_y = 0.1 # m
detector_area = detector_x * detector_y # m^2

solid_angle = detector_area / (4 * np.pi * inner_radius ** 2)

solid_angle= 0.5

number_of_layers = 1
thickness = 1 # cm

incidient_gamma_energy = 500 # keV
incident_gamma = source_activity * solid_angle

# at 500 keV
mu_rho = 8.212E-02 #at 500 keV
# mu_en_rho = 2.930E-02
density_ge = 5.323 # g/cm^3

for i in number_of_layers:
    outgoing_gamma = incident_gamma * np.exp(-mu_rho * density_ge * thickness)
    stopped_gamma =
    outgoing_gamma_avg_energy =
