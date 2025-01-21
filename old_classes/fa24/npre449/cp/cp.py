import numpy as np
import numpy.linalg as la
import scipy as sci
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from pyXSteam.XSteam import XSteam as xs

reactor = 1
save_plots = True
print_vals = True

# given conditions
if 1 == reactor:
    # geometry everything in m/K/Pa/kg/s
    height = 4
    d_rod = 0.95 / 100
    t_gap = 0.006 / 100
    d_fuel = 0.82 / 100
    pitch = 1.26 / 100

    # material properties
    k_gap = 0.25
    k_fuel = 3.6
    k_clad = 21.5

    # conditions
    g = 4000
    qp = 430 * 100
    p_z0 = 15
    tf_0 = 277 + 273.15

    # fluid properties
    mu = 97.575e-6
    mu_l = 69.403e-6
    mu_v = 22.716e-6

if 2 == reactor:
    # geometry everything in m/K/Pa/kg/s
    height = 4.1
    d_rod = 1.227 / 100
    t_gap = 0.010 / 100
    d_fuel = 1.04 / 100
    pitch = 1.62 / 100

    # material properties
    k_gap = 0.25
    k_fuel = 3.6
    k_clad = 21.5

    # conditions
    g = 2350
    qp = 605 * 100
    p_z0 = 7.5
    tf_0 = 272 + 273.15

    # fluid properties
    mu_l = 89.451e-6
    mu_v = 11.656e-6


# enthalpy functions
st = xs(xs.UNIT_SYSTEM_BARE)  # m/kg/s/K/MPa/W

# empty enthalpy list
hg_list = []
hf_list = []
hfg_list = []

# getting all enthalpies
przs = np.linspace(0.001, 22.06, 1000)
for pressure in przs:
    hg_list.append(st.hV_p(pressure))
    hf_list.append(st.hL_p(pressure))
    hfg_list.append(hg_list[-1] - hf_list[-1])

# interpolating enthalpies as a function of pressure
poly_deg = 25
hgp = np.polynomial.Polynomial.fit(
    przs, hg_list, deg=poly_deg) * 1e3
hfp = np.polynomial.Polynomial.fit(
    przs, hf_list, deg=poly_deg) * 1e3
hfgp = np.polynomial.Polynomial.fit(
    przs, hfg_list, deg=poly_deg) * 1e3

# taking the derivatives of the enthalpy as a function of pressure
dhgp = hgp.deriv() * 1e-6
dhfp = hfp.deriv() * 1e-6
def dhfgp(z): return (-7.7343e-16*(z)**2+1.65472e-8*(z)+1.4331e-1)



# geometry
a_fluid = pitch**2 - np.pi * d_rod**2 / 4
xi = np.pi * d_rod
d_h = 4 * a_fluid / xi


# heat gen
def heat_qp(z): return qp * np.sin(z * np.pi / height)
def heat_qpp(z): return qp(x) / xi


# fluid properties
# one phase
cp = st.Cp_pt(p_z0, tf_0) * 1e3
k = st.tc_pt(p_z0, tf_0)

re = g * d_h / mu
pr = cp * mu / k
if re > 1e4: nu = 0.023 * re**(0.8) * pr**(0.4)
if re < 2100: nu = 4.36

h = nu * k / d_h
f = 0.316 * re**(-1/4)

# two-phase
def pratio(p): return st.rhoV_p(p) / st.rhoL_p(p)
def alpha(chi_e, p): return 1 / (1 + (chi_e**(-1) - 1) * pratio(p))
def tsat(p): return st.tsat_p(p)

rho_l = st.rhoL_p(p_z0)
rho_f = st.rhoV_p(p_z0)
rho_fg = rho_l - rho_f


# solving fluid
def solve_fluid(ms):
    ps = [p_z0 * 1e6]
    chi_es = [cp * (tf_0 - tsat(p_z0)) / hfgp(p_z0)]
    chis = [0]
    tfs = [tf_0]
    tsats = [tsat(ps[-1])]

    zs = np.linspace(0, height, ms)

    for i in range(1, 3):#len(zs)):
        dz = zs[i] - zs[i - 1]

        p0 = ps[i - 1]
        chi_e0 = chi_es[i - 1]

        if chi_e0 <= 0:
            chi0 = 0
        if chi_e0 > 0:
            chi0 = chi_e0

        nu_l = st.vL_p(p_z0)
        nu_g = st.vV_p(p_z0)
        nu_fg = nu_g - nu_l
        rho_m = 1 / (nu_l + chi0 * nu_fg)

        # pressure
        if chi_e0 <= 0:
            dp = (9.81 / nu_l + f * g**2 * nu_l * xi / 2 / a_fluid)
        if chi_e0 > 0 and chi_e0 < 1:
            mu_m = 1 / (chi_e0 / mu_v + (1 - chi_e0) / mu_l)
            ff = 0.046 * Re**(-0.2) * (mu_l / mu_m)**(-0.2)

            tp1 = xi / a_fluid * ff * g**2 / 2 * (nu_l + chi_e0 * nu_fg)
            tp2 = rho_m * 9.81
            tp3 = g * qp(z[i]) * nu_fg / (a_fluid * hfgp(p0 * 1e-6))

            bp1 = dhfp(p0 * 1e-6) + chi_e0 * dhfgp(p0 * 1e-6)
            bp2 = 1 - g**2 * nu_fg / hfgp(p0 * 1e-6) * bp1

            dp = (tp1 + tp2 + tp3) / bp2

        p1 = p0 - dp * dz
        dpdz = (p1 - p0) / dz

        # eq quality
        chip1 = 1e6 * dhfp(p0 * 1e-6) * dpdz + chi_e0 * dhfgp(p0) * dpdz
        print(dhfp(p0 * 1e-6), dpdz, chi_e0, dhfgp(p0))
        chip2 = heat_qp(zs[i]) / (a_fluid * g * hfgp(p1 * 1e-6)) - 1 / hfgp(p1 * 1e-6) * chip1
        #print(chip1, chip2)
        chi_e1 = chi_e0 + chip2 * dz

        # quality
        if chi_e1 <= 0:
            chi1 = 0
        if chi_e1 > 0:
            chi1 = chi_e1


        # fluid temp
        if chi_e1 <= 0:
            tf1 = hfgp(p1 * 1e-6) / cp * chi_e1 + tsat(p1 * 1e-6)
        if chi_e1 > 0:
            tf1 = tsat(p1 * 1e-6)

        tsats.append(tsat(p1 * 1e-6))
        ps.append(p1)
        chi_es.append(chi_e1)
        chis.append(chi1)
        tfs.append(tf1)

    return tsats, ps, chi_es, chis, tfs

tsats, ps, chi_es, chis, tfs = solve_fluid(1000) 
