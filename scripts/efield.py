import os
import sys
import matplotlib.pyplot as plt
import numpy as np

def calc_field_1d(x):
    efield = []
    v = []
    L = 5
    d = L
    V1 = 2000 #Volts
    V2 = 0 #Volts
    V = V2 - V1
    for x_value in x:
        efield.append(V/d * x_value)
    potential = - np.gradient(efield)
    print(x)
    print(efield)
    print(potential)
    plt.plot(x, efield, '-')
    plt.plot(x, potential, '-')
    plt.show()

def calc_weighting_field_1d(x):
    efield = []
    v = []
    L = 5
    d = L
    V1 = 2000 #Volts
    V2 = 0 #Volts
    V = V2 - V1

    psi_1 = []
    psi_0 = []
    for x_value in x:
        efield.append(V/d * x_value)
        psi_1.append(x_value/L) #weighting field
        psi_0.append(1- x_value/L)
    potential = - np.gradient(efield)
    print(x)
    print(efield)
    print(potential)
    plt.plot(x, psi_1, 'b-')
    plt.plot(x, psi_0, 'r-')
    #plt.plot(x,, 'g-')
    plt.show()

x = np.linspace(0, 5, 100)
calc_field_1d(x)
calc_weighting_field_1d(x)

    # check efield TODO

    # weighting field... in 1d
