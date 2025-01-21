import numpy as np
import numpy.linalg as la

# question 2
def q2():
    lams = np.radians(np.array([30,48,78]))
    phi = np.radians(65)

    sfs = np.cos(phi) * np.cos(lams)

    crrs = 2.5 * np.max(sfs)

    print("----- Q2 -----\n" +
          f"Schmidt Factors: {sfs}\n" +
          f"Critical Resolved Sheer Stress: {crrs}\n")

# question 3
def q3():
    s0 = 30
    ky = 100 / 8

    # b
    db = 3e3
    dhalf = db**(-1/2)
    syb = s0 + ky * dhalf

    # c
    d0 = 2 
    d1 = 3.4
    d2 = 4.7

    n = 2.1
    t1 = 250

    k = (d1**n - d0**n) / t1
    tf = (d2**n - d1**n) / k

    print("----- Q3 -----\n" +
          f"ky: {ky}\n" +
          f"d^1/2: {dhalf}\n" +
          f"sigma_y: {syb}\n" +
          "--- part c ---\n" +
          f"K: {k}\n" +
          f"Tf: {tf}\n")

# question 4
def q4():
    qrt = 140e3 / 8.314 / 473

    A = np.array([[1, np.log(55)],
                  [1, np.log(89)]])

    B = np.array([np.log(2.5e-3) + qrt,
                  np.log(2.4e-2) + qrt])
    
    logK2, n = la.solve(A, B)
    k2 = np.exp(logK2)

    edots = k2 * (48)**n * np.exp(-qrt)

    print("----- Q3 -----\n" +
          f"K2: {k2}\n" +
          f"n: {n}\n" +
          f"Strain rate: {edots * 1e3} * 1e3\n")

# question 5
def q5():
    ca = 70
    c0 = 65
    cl = 57

    wl = (ca - c0) / (ca - cl)
    wa = (c0 - cl) / (ca - cl)

    print("----- Q5 -----\n" +
          f"Liquid Weight Fraction: {wl}\n" +
          f"Alpha Weight Fraction: {wa}\n")

q2()
q3()
q4()
q5()
