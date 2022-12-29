import numpy as np
from numba import njit

def gen_func_1d(x, v, v_pm, v_std, x_k, x_max):
    # generate 2 stream initial conditions

    f = np.exp(-(v+v_pm)**2 / 2 / v_std **2) + np.exp(-(v-v_pm)**2 / 2 / v_std **2)
    f *= 0.5 * np.cos(x/x_k*np.pi)**2+ 0.5
    # set v boundaries to 0
    f[0,:] = 0
    f[-1,:] = 0
    return f

@njit
def renormalize(f):
    # hacky way of renormalizing so that the program doesn't crash

    min = np.amin(f)
    size = np.amax(f) - min

    f -= min
    return f/size