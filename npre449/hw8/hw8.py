import numpy as np
import matplotlib.pyplot as plt

# question 1
def q1():
    deltaT = 60
    cp = 4182
    qpp = 2000
    mdot = 0.01
    perm_h = np.pi * 6e-2

    l = deltaT * mdot * cp / perm_h / qpp
    h = 4.36 * 0.66 / 6e-2
    tw = qpp / h + 80
    

    print(f"----- Q1 -----\n" +
          f"length: {l} m\n" +
          f"h: {h}\n" +
          f"Wall Temp: {tw} *C")

# question 2
def q2():
    dT = 60 - 20
    mdot = 0.1
    cp = 4182
    perm_h = np.pi * 20e-3

    qpp = 1e6 * (np.pi/4 * ( (40e-3)**2 - (20e-3)**2)) / np.pi / 20e-3

    l = 40 * 0.1 * 4182 / 15000 / np.pi / 20e-3
    
    h = qpp / (70 - 60)

    print(f"----- Q2 -----\n" +
          f"q\'\': {qpp} W/m^2\n" + 
          f"l: {l} m\n" + 
          f"h: {h} W/m^2*K") 

# question 3
def q3():
    Eloss = 0.05 * 1e3 * (103 - 77)
    qpp = Eloss / (np.pi * 0.15 * 5)
    Ts = qpp / 6

    print(f"----- Q3 -----\n" +
          f"Edot_loss: {Eloss} W\n" +
          f"q\'\': {qpp} W/m^2\n" +
          f"Ts: {Ts} C")


q3()
