import numpy as np
import matplotlib.pyplot as plt
import math


def q2():
    a = 5


    def pn(n):
        return a**n / math.factorial(n) * np.exp(-a) * 100


    print("----- Question 2 -----")
    print(f"a) {pn(0)}")
    print(f"b) {pn(10)}")

    ns = np.arange(0, 15 + 1)
    ps = []

    for n in ns:
        ps.append(pn(n))

    plt.plot(ns, ps)
    plt.xlabel("n value [counts]")
    plt.ylabel("Probability")
    plt.grid("both")
    plt.savefig("hw01-q3.png", dpi=600)
    plt.close()



