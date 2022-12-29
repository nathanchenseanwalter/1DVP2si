import numpy as np
from tqdm import tqdm
from numba import njit
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

import integration, field, helper

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

f1 = helper.gen_func_1d(xx, vv, v_pm, v_std, x_k, x_max)

def animate(i, f, x, v, dx, dv, dt, v_th, n_0, a, k, renorm, render_skip):

    global f1

    # for loop within animate to speed up render time without losing precision
    for _ in range(render_skip):
        rho = field.get_density(f1, v_th, n_0)
        E = field.get_E_1d(rho, x_n, x_len)

        # f = centered_VP(f, v_mat, E, dx, dv, dt, x_n, v_n)
        f1 = integration.classic_semi(f1, v_mat, x, E, dx, dv, dt, x_n, v_n, x_len, n_0, v_th)

        if renorm:
            if np.amax(f1) > 1.01 or np.amin(f1) < 1.01:
                f1 = helper.renormalize(f1)
        else:
            if np.isnan(f1).any():
                print("encountered NaN")
                sys.exit(1)

    im.set_array(f1)
    ax.set_title(i * render_skip)
    ax.set_xlabel("position")
    ax.set_ylabel("velocity")

# anim param
fig, ax = plt.subplots()
im = ax.imshow(f, cmap=plt.get_cmap('plasma'),vmin=0,vmax=1,interpolation='bicubic')
plt.colorbar(im, ax=ax)
render_skip = 10

# run param
runs = int(t / dt)
x_len = max(x_arr) - min(x_arr)
x_n = len(x_arr)
v_n = len(v_arr)

v_mat = np.transpose(np.tile(v_arr,(x_n,1)))

ani = animation.FuncAnimation(fig, animate, fargs=(f, x_arr, v_mat, dx, dv, dt, v_th, n_0, pert_amp, pert_freq, True, render_skip), interval = 100, frames=tqdm(range(int(runs/render_skip)-1),file=sys.stdout))
ani.save("vp1d.mp4", writer="ffmpeg", fps=60)
fig.show()