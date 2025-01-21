import numpy as np


def q1():
    theta = np.radians(44.77)
    E = 1e6
    E2f = 10e3

    a = 1
    b = 2 - 2*E/E2f * (1 - np.cos(theta))
    c = 1

    m1 = -b + (b**2 - 4 * a * c)**(1/2) / 2 / a
    m2 = -b - (b**2 - 4 * a * c)**(1/2) / 2 / a
    print(m1, m2)

    e2f1 = 2 * m1 / (1 + m1)**2 * E * (1 - np.cos(theta))
    e2f2 = 2 * m2 / (1 + m2)**2 * E * (1 - np.cos(theta))
    print(e2f1, e2f2)

    lam1 = 4 * m1 / (1 + m1)**2
    lam2 = 4 * m2 / (1 + m2)**2
    print(lam1, lam2)

    t1 = lam1 / 2 * E * (1 - np.cos(theta))
    t2 = lam2 / 2 * E * (1 - np.cos(theta))
    print(t1, t2)

    return


def q2():
    e = 200e3
    m1 = 4
    m2 = 48
    theta = np.radians(45)
    ed = 17

    lam = 4 * m1 * m2 / (m1 + m2)**(2)
