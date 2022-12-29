import numpy as np
from tqdm import tqdm
from numba import njit
import sys

import integration, field, helper

def static_main_1d(f, x, v, dx, dv, dt, v_th, n_0, a, k, renorm):
    # main function for outputting a final array

    runs = int(t / dt)
    x_len = max(x) - min(x)
    x_n = len(x)
    v_n = len(v)
    
    v_mat = np.transpose(np.tile(v,(x_n,1)))

    for i in tqdm(range(runs)):

        rho = field.get_density(f, v_th, n_0)
        E = field.get_E_1d(rho, x_n, x_len)

        # f = integration.centered_VP(f, v_mat, E, dx, dv, dt, x_n, v_n)
        f = integration.classic_semi(f, v_mat, x, E, dx, dv, dt, x_n, v_n, x_len, n_0, v_th)

        if renorm:
            if np.amax(f) > 1.01 or np.amin(f) < 1.01:
                f = helper.renormalize(f)
        else:
            if np.isnan(f).any():
                print("encountered NaN")
                sys.exit(1)

    return f
