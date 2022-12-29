import numpy as np

import field

def centered_VP(f, v, E, dx, dv, dt, x_n, v_n):
    # simple fd solver

    # vdx term (cyclic)
    B = (np.roll(f,1,1)-np.roll(f,-1,1)) / 2 / dx
    BA = v * B

    # edv term (ignore boundaries)
    C = E * (np.roll(f,1,0)-np.roll(f,-1,0)) / 2 / dv
    C[-1:0,:] = 0

    return f - dt * (BA + C)

def classic_semi(f, v, x, E, dx, dv, dt, x_n, v_n, x_len, n_0, v_th):
    # conservative fd solver

    B = np.zeros_like(f)
    C = np.zeros_like(f)

    # f1
    C = E * (np.roll(f,1,0)-np.roll(f,-1,0)) / 2 / dv
    C[-1:0,:] = 0
    f1 = f - dt / 2 * C

    # f2
    B = (np.roll(f1,1,1)-np.roll(f1,-1,1)) / 2 / dx
    BA = v * B
    f2 = f1 - dt * BA

    # E1
    rho1 = field.get_density(f2, v_th, n_0)
    E1 = field.get_E_1d(rho1, x_n, x_len)

    # fnp1
    C = E * (np.roll(f2,1,0)-np.roll(f2,-1,0)) / 2 / dv
    C[-1:0,:] = 0
    fnp1 = f2 - dt / 2 * C

    return fnp1