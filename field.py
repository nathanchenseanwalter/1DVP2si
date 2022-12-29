import numpy as np
from numba import njit

@njit
def get_density(f, v_th, n_0):
    # 0th moment for vp

    return v_th/n_0*np.sum(f,0) - 1

def get_E_1d(rho, x_elem, x_len):
    # E field integration

    ak = np.fft.fft(rho)

    ks = np.fft.fftfreq(len(rho)) * x_elem * x_len
    ak2 = np.divide(ak,ks,out=np.zeros_like(ak), where=ks!=0)
    
    return np.imag(np.fft.ifft(ak2))