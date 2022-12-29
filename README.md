# 1DVP2si (1D Vlasov Poisson, No External B, 2 Stream Instability)

### Vlasov-Poisson Equation

Assuming no B-field, the Vlasov-Poisson equation becomes

$\frac{\partial f}{\partial t} + v \frac{\partial f}{\partial x} - \frac{e}{m} E \frac{\partial f}{\partial v} = 0$

$\rho(x,t) = \int f(x,v,t)\,dv$ and $\nabla \cdot \vec{E} = \rho$

### Electron Kinetic 1-D Vlasov-Poisson

In 1-D with electron, this simplifies to

$\frac{\partial f}{\partial t} + v \frac{\partial f}{\partial x} - \frac{e}{m} E \frac{\partial f}{\partial v} = 0$

$\frac{dE}{dx} = e(n_0 - n_e) = en_0 - e\int f(x,v,t)\,dv$

### Normalization

This can be normalized with

$\omega_{pe} = \sqrt{\frac{e^2n_0}{m}} \qquad \lambda_D = v_{th}/\omega_{pe}$

$t' = t\omega_{pe} \qquad x'=x/\lambda_D \qquad v' = v/v_{th}$

Normalized, the Vlasov equation becomes

$\frac{\partial f}{\partial t'} + v' \frac{\partial f}{\partial x'} + E' \frac{\partial f}{\partial v'} = 0 \qquad E' = -\frac{e}{m\lambda_D\omega_{pe}^2}E$


And the density becomes

$\frac{dE'}{dx'} = \frac{v_{th}}{n_0}\int f\,dv' - 1$

### E Field Calculation

The field component can be solved using pseudo-spectral methods (with DFT). As shown above, this method is relatively accurate at reproducing the cyclical patterns.

Since $\nabla \cdot E =\rho$, then we can represent 1D $\rho$ with $\rho = \sum a_k e^{ikx}$

and therefore $E = \int \rho \,dx = \frac{1}{ik}\rho$

### Code Usage

View final distribution by running run.py (faster)

Get animation by running animate.py

### Output Interpretation

Plot shows the density function in both the x and v domain. The classic 2 stream instability test is used and shows the evolution of a 1-D plasma.

The plasma rapidly diffuses due to the simple scheme used. However, it is conservative.

### Resources
https://pnavaro.github.io/python-fortran/04.vlasov-poisson.html</br>
http://faculty.washington.edu/rjl/classes/am590a2013/_static/Fourier-Spectral.pdf</br>
https://www-m16.ma.tum.de/foswiki/pub/M16/Allgemeines/NumMethVlasov/Num-Meth-Vlasov-Notes.pdf</br>
https://doi.org/10.1016/S0010-4655(97)00119-7</br>
https://link.springer.com/article/10.1007/s00211-016-0816-z
