# imports
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import scipy as sci
from scipy.optimize import fsolve
from pyXSteam.XSteam import XSteam as xs

# variables of global importance
reactor_type = 1
save_plots = True
print_vals = True
mesh_elements = 1000

# given conditions
if 1 == reactor_type:
    ## geometry everything in m/K/Pa/kg/s
    height = 4
    d_rod = 0.95 / 100
    t_gap = 0.006 / 100
    d_fuel = 0.82 / 100
    pitch = 1.26 / 100

    ## material properties
    k_gap = 0.25
    k_fuel = 3.6
    k_clad = 21.5

    ## conditions
    mass_flux = 4000
    qp = 430 * 100
    p_z0 = 15e6
    tf_0 = 277 + 273

    ## fluid properties
    mu_l = 69.403e-6
    mu_v = 22.716e-6

if 2 == reactor_type:
    ## geometry everything in m/K/Pa/kg/s
    height = 4.1
    d_rod = 1.227 / 100
    t_gap = 0.010 / 100
    d_fuel = 1.04 / 100
    pitch = 1.62 / 100

    ## material properties
    k_gap = 0.25
    k_fuel = 3.6
    k_clad = 21.5

    ## conditions
    mass_flux = 2350
    qp = 605 * 100
    p_z0 = 7.5e6
    tf_0 = 272 + 273

    ## fluid properties
    mu_l = 89.451e-6
    mu_v = 11.656e-6


# enthalpy functions
st = xs(xs.UNIT_SYSTEM_BARE)  # m/kg/s/K/MPa/W

## empty enthalpy dicts
hg_poly = []
hf_poly = []
hfg_poly = []

## getting all enthalpies
beginning_pressures = np.linspace(0.001, 22.06, 1000)
for pressure in beginning_pressures:
    hg_poly.append(st.hV_p(pressure))
    hf_poly.append(st.hL_p(pressure))
    hfg_poly.append(hg_poly[-1] - hf_poly[-1])

## interpolating enthalpies as a function of pressure
poly_degree = 25
hg_poly = np.polynomial.Polynomial.fit(
    beginning_pressures, hg_poly, deg=poly_degree)
hf_poly = np.polynomial.Polynomial.fit(
    beginning_pressures, hf_poly, deg=poly_degree)
hfg_poly = np.polynomial.Polynomial.fit(
    beginning_pressures, hfg_poly, deg=poly_degree)

## taking the derivatives of the enthalpy as a function of pressure
dhg_dp_poly = hg_poly.deriv()
dhf_dp_poly = hf_poly.deriv()
dhfg_dp_poly = hfg_poly.deriv()

## making functions of enthalpy that take pressure in Pa
def hg_vs_p(p): return hg_poly(p * 1e-6)
def hf_vs_p(p): return hf_poly(p * 1e-6)
def hfg_vs_p(p): return hfg_poly(p * 1e-6)

def dhg_dp(p): return dhg_dp_poly(p * 1e-6)
def dhf_dp(p): return dhf_dp_poly(p * 1e-6)
def dhfg_dp(p): return dhfg_dp_poly(p * 1e-6)

def h_pt(p, t): return st.h_pt(p * 1e-6, t)

## plotting
def plot_enthalpies():
    hg = hg_vs_p(beginning_pressures * 1e6)
    hf = hg_vs_p(beginning_pressures * 1e6)
    hfg = hg_vs_p(beginning_pressures * 1e6)

    dhg = dhg_dp(beginning_pressures * 1e6)
    dhf = dhg_dp(beginning_pressures * 1e6)
    dhfg = dhg_dp(beginning_pressures * 1e6)

    enthalpies = [hg, dhg, hf, dhf, hfg, dhfg]
    titles = ['hg', 'dhg', 'hf', 'dhf', 'hfg', 'dhfg']

    for enthalpy, title in zip(enthalpies, titles):
        plt.plot(beginning_pressures, enthalpy)
        plt.xlabel("Pressure [MPa]")
        plt.ylabel(title)
        plt.grid("both")
        plt.savefig(f"plots/{title.replace('/', '_')}.png", dpi=600)
        plt.close()

if save_plots: plot_enthalpies()


# calculated parameters
## geometry
xi = np.pi * d_rod              # heated/wetted perimeter
a_fluid = pitch**2 - np.pi / 4 * d_rod**2   # fluid area
d_hydro = 4 * a_fluid / xi       # hydralic diameter

## fluid properties
rho_0 = st.rho_pt(p_z0 * 1e-6, tf_0)         # density of water

mu_f = st.my_pt(p_z0 * 1e-6, tf_0)     # dynamic viscosity
k_fluid = st.tc_pt(p_z0 * 1e-6, tf_0)  # thermal conductivity of water
cp = st.Cp_pt(p_z0 * 1e-6, tf_0) * 1e3 # specific heat capacity of water

mw = 18                         # atomic mass of water
pc = 22.06 * 1e6                # critial pressure

rho_f = st.rhoL_p(p_z0 * 1e-6)
rho_g = st.rhoV_p(p_z0 * 1e-6)
rho_fg = rho_f - rho_g

## flow propeties
re = mass_flux * d_hydro / mu_f # reynolds number
pr = cp * mu_f / k_fluid * 1e3  # prandtl number
nu = 0.023 * re**0.8 * pr**0.4  # nusselt number
if re > 10000: nu = 4.36

h_f0 = nu / d_hydro * k_fluid   # convective heat transfer coefficient
ff = 0.316 * re**(-1/4)         # friction factor

## printing
if print_vals:
    print(f"--- Geometry ---\nXi: {xi} m\nFluid Area: {a_fluid} m^2\nHydraulic Diameter: {d_hydro} m\nrho_0: {rho_0} kg/m^3\n\n--- Fluid Properties ---\nDynamic Viscosity: {mu_f} Pa*s\nLiquid Mu: {mu_l} Pa*s\nVapor Mu: {mu_v} Pa*s\nThermal Conductivity of Water: {k_fluid} W/m/K \nSpecific Heat: {cp} J/kg/K\nMolar Mass of Water: {mw} amu\nCritical Pressure: {pc} Pa\nLiquid Density: {rho_f} kg/m^3\nVapor Density: {rho_g} kg/m^3\n\n --- Flow Properties ---\nReynold's Number: {re}\nPrandtl Number: {pr}\nNusselt Number: {nu}\nConvective Heat Transfer Coefficient: {h_f0} W/m^2/K\nFriction Factor: {ff}\n")


# data lists
temp_fluid = [tf_0]
temp_sat = [st.tsat_p(p_z0 * 1e-6)]

pressures = [p_z0]
chi_es = [cp * (tf_0 - temp_sat[0]) / hfg_vs_p(pressures[0])]

# functions
def heat_flux(z): return qp / xi * np.sin(np.pi * z / height)
def qppp(z): return 4 * qp / np.pi / d_fuel**2 * np.sin(np.pi * z / height)

def vL_p(p): return st.vL_p(p * 1e-6)
def vV_p(p): return st.vV_p(p * 1e-6)

def hf(p): return st.hL_p(p * 1e-6)
def hg(p): return st.hV_p(p * 1e-6)
def hfg(p): return hg(p) - hf(p)

def tsat_p(p): return st.tsat_p(p * 1e-6)
def solve_fluid(ms):
    zs = np.linspace(0, height, ms)

    if print_vals:
        print("--- Fluid Vals ---")
        print(f"z: {0} \ttf: {temp_fluid[-1]} \tp: {pressures[-1]} \tchi_e: {chi_es[-1]} \tt_sat: {temp_sat[-1]}")

    for i in range(1, len(zs)):
        ## stepping vars
        z = zs[i]
        dz = z - zs[i - 1]

        chi_e0 = chi_es[i - 1]
        tf0 = temp_fluid[i - 1]
        p0 = pressures[i - 1]

        qpp = heat_flux(z)

        chi = chi_e0
        dchi = 0

        ## quality
        if chi <= 0:
            chi = 0
            dchi = 0
        if chi > 0 and chi < 1:
            chi_prev = chi_es[i - 1]
            if chi_prev < 0: chi_prev = 0
            dchi = chi - chi_prev

        ## densities
        nu_f = vL_p(p0)
        nu_g = vV_p(p0)
        nu_fg = nu_g - nu_f

        # nu_m = nu_f + chi * nu_fg
        rho_m = (1 / rho_f + 1 / (rho_g - rho_f) * chi)**(-1)

        hf0 = hf(p0)
        hg0 = hg(p0)
        hfg0 = hfg(p0)

        ## next pressure step
        if chi_e0 <= 0:
            dp = (mass_flux / nu_f + ff * mass_flux**2 * xi / 2 / a_fluid) * dz
            print(dp)
        if chi_e0 > 0:
            mu_m = 1 / (chi_e0 / mu_v) + (1 - chi_e0 / mu_l)
            f_val = 0.046 * Re**(-0.2) * (mu_l / mu_v)**(-0.2) 
            pc1 = xi * f_val * mass_flux**2 / 2 / a_fluid / rho_m # top P1
            pc2 = rho_m * 9.81 # top P2 
            pc3 = mass_flux * qpp * xi / rho_fg / a_fluid / hfg0
            pc4 = chi * dhg_dp(p0)
            pc5 = (1 - chi) * dhf_dp(p0)
            pc6 = mass_flux**2 / rho_fg / hfg0 * (pc4 + pc5)

            dp = ((pc1 + pc2 + pc3) / (1 - pc6)) * dz
        
        p1 = p0 + dp

        ## enthalpies
        hf1 = hf(p1)
        hg1 = hg(p1)
        hfg1 = hfg(p1)

        dhf = hf1 - hf0
        dhg = hg1 - hg0
        dhfg = hfg1 - hfg0

        ## next chi_e
        chi_c1 = qpp * xi / a_fluid / mass_flux / hfg0
        chi_c2 = chi * dhg_dp(p1) * dp/dz
        chi_c3 = (1 - chi) * dhf_dp(p1) * dp/dz
        chi_c4 = 1 / hfg0 * (chi_c2 + chi_c3)

        dchi_e = dz * (chi_c1 - chi_c4)
        chi_e1 = chi_e0 + dchi_e

        ## next fluid temp
        t_sat = tsat_p(p1)
        tf1 = hfg_vs_p(p1) * chi_e1 / cp + tsat_p(p1)

        ## output
        if i in np.linspace(1, ms, 10) or i == (ms -1) and print_vals:
            print(f"z: {round(z,5)} \ttf: {round(tf1,5)} \tp: {round(p1,5)} \tchi_e: {round(chi_e1,3)} \tt_sat: {round(t_sat,3)}")

        temp_fluid.append(tf1)
        pressures.append(p1)
        chi_es.append(chi_e1)
        temp_sat.append(t_sat)

    ## interpolating
    tf_z = np.polynomial.Polynomial.fit(zs, temp_fluid, poly_degree)
    p_z = np.polynomial.Polynomial.fit(zs, pressures, poly_degree)
    chi_z = np.polynomial.Polynomial.fit(zs, chi_es, poly_degree)
    tsat_z = np.polynomial.Polynomial.fit(zs, temp_fluid, poly_degree)

    return_dict = {
            "tf": tf_z,
            "p": p_z,
            "chie": chi_z,
            "tsat": tsat_z,
        }

    return return_dict

dict = solve_fluid(100)
