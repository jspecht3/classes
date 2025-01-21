import numpy as np
import matplotlib.pyplot as plt

# Question 2
## parameters
h = 1000
k = 28
D = 0.5
Tw = 300
q = 526.048 * 3600
mu = 7.4676

## constants
C2 = (-2*h - D*h**2/k)**(-1) * ((1 + np.exp(-mu*D) + D*h/k) * (-q/mu - q*h/k/mu**2) - Tw*h*(2 + h*D/k))
C1 = h*C2/k - h*Tw/k - h*q/k**2/mu**2 - q/k/mu

## temperature function
def temp2(x):
    return -q/k/mu**2*np.exp(-mu*x) + C1*x + C2

def plot2():
    x = np.linspace(0, 0.5, 1000)
    t = temp2(x)

    plt.plot(x, t)
    plt.show()

def q2_out():
    print(f"C1: {C1} *F/ft\nC2: {C2} *F")
    
    T0 = temp2(0)
    Td = temp2(0.5)
    print(f"T(r=0): {T0} *F\nT(r=D): {Td} *F")
    
    x = np.linspace(0, 0.5, 10000)
    t = temp2(x)
    Tmax = np.max(t)
    print(f"T max: {Tmax} *F")

#q2_out()

# question 3
Rfgc = 12.52e-3 / 2
Rfg = Rfgc - 0.86e-3
Rf = Rfg - 230e-6

kf = 2.7 #(1 - 0.88) / (1 + (1.5 - 1)*0.88) * 2.7
kc = 17
h = 4300

To = 295
q = 44e3 / np.pi / Rf**2

def q3_params():
    print(f"R_fgc: {Rfgc} m\nRfg: {Rfg} m\nRf: {Rf} m")
    print(f"kf: {kf}\nkc: {kc}\nh: {h}")
    print(f"q: {q * 1e-8}e8")

#q3_params()

C3 = q * Rf * Rfg / 2 / kc
C4 = To - C3 * np.log(Rfgc) 
C2 = q*Rf/2/h + q*Rf**2/2/kf + To

def t_fuel(r): return -q*r**2/4/kf + C1*np.log(r) + C2
def t_clad(r): return C3*np.log(r) + C4

#print(t_fuel(Rf), t_clad(Rfg))

# question 4
## parameters
r = 1/12
rho = 490
cp = 0.122
V = 4/3 * np.pi * r**3
A = 4 * np.pi * r**2
h = 2

tau = rho * cp * V / h / A

## temps
To = 850
Tinf = 200
Tf = 300

t = tau * np.log((To - Tinf) / (Tf - Tinf))

def q4_out():
    print(f"tau: {tau} hr = {tau * 3600} s\nt: {t} hr = {t *3600} s")

#q4_out()

# question 5
## parameters
r = 1/2 / 12
V = 4/3 * np.pi * r**3
A = 4 * np.pi * r**2

cp = 0.04
rho = 700
h = 200

To = 100
Tinf = 500
Tf = 499

tau = rho * cp * V / h / A
t = tau * np.log((To - Tinf) / (Tf - Tinf))

def q4_out():
    print(f"tau: {tau} hr = {tau * 3600} s\nt: {t} hr = {t *3600} s")

q4_out()
