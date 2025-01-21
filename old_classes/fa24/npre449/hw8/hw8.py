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
    Eloss = 0.05 * 1043 * (103 - 77)
    qpp = Eloss / (np.pi * 0.15 * 5)
    Ts = qpp / 6

    re = 4 * 0.05 / 2.068e-5 / np.pi / 0.15
    qpp = 77 / ((1/11.84) + (1/6))
    tw = qpp / 6

    print(f"----- Q3 -----\n" +
          f"Edot_loss: {Eloss} W\n" +
          f"Re: {re}\n" +
          f"q\" {qpp} w/m^2\n" +
          f"Tw {tw} K")

# question 4
def q4():
    h = 3.66 * 0.138 / 50e-3
    
    exp = h * np.pi * 50e-3 * 25 / 2131 / 0.5
    tl = 150-(150-20)*np.exp(-exp)
    q = 0.5 * 2131 * (tl - 20)

    print(f"----- Q4 -----\n" +
          f"h: {h} W/m^2*K\n" +
          f"T(L): {tl} *C\n" +
          f"q: {q} W")

# question 5
def q5():
    cp = 4182
    mdot = 2
    d = 40e-3
    h = 6918.15
    perm_h = d * np.pi
    mu = 8.9e-4
    
    A = d**2 / 4 * np.pi
    G = mdot / A

    f = 0.0174
    
    logger = np.log((25 - 100) / (75 - 100))
    L = cp * mdot / h / perm_h * logger

    re = 116415
    pr = mu * cp / 0.6

    dp = f * G**2 * L / 2 / 1000 / d
    
    print(f"----- Q5 -----\n" +
          f"L for 75*C: {L}\n" +
          f"Pr: {pr}\n" +
          f"dP: {dp}")

q5()
