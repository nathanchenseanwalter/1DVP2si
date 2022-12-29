#! For animations, run the animate.py file instead this one will only generate final

import numpy as np
from tqdm import tqdm
from numba import njit
import matplotlib.pyplot as plt
import sys

import integration, field, helper, main

# initialize parameters

# time
t_in = 30
dt_in = 0.0001

# length
x_max_in = 10
v_max_in = 10

# grid points
x_points = 128
v_points = 128

# perturbuation strength
pert_amp = 1
pert_freq = 1

# initial distribution
v_pm_in = 2
v_std_in = .75
x_k_in = 5

# constants

e = 1
n_0 = 1
m_e = 1

# normalization

v_th = v_max_in / 2   # thermal velocity
w_pe = np.sqrt(e**2 * n_0 / m_e)    # plasma frequency
l_d = v_th / w_pe                   # debye length

t = t_in * w_pe
dt = dt_in * w_pe
x_max = x_max_in / l_d
v_max = v_max_in / v_th

dx = x_max * 2 / x_points
dv = v_max_in * 2 / v_points

v_pm = v_pm_in / v_th
v_std = v_std_in / v_th
x_k = x_k_in / l_d

# generate lattice

x_arr = np.linspace(-x_max, x_max, x_points)
v_arr = np.linspace(-v_max, v_max, v_points)
xx, vv = np.meshgrid(x_arr, v_arr)

f = helper.gen_func_1d(xx, vv, v_pm, v_std, x_k, x_max)

f1 = main.main_loop_1d(f, x_arr, v_arr, dx, dv, dt, v_th, n_0, pert_amp, pert_freq, renorm=True)
plt.pcolormesh(xx,vv,f1) # run with plotting
plt.colorbar()
plt.show()