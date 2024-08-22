# **Lid-driven cavity flow of an incompressible FENE-P fluid**

&emsp; OpenFoam with RheoTool<sup>1</sup> is used here to solve the continuity equation, the incompressible Cauchy momentum equation, and the log-conformation formulation of the FENE-P viscoelastic fluid model in 2D, given by

$$ \nabla \cdot  **u** = 0, $$

$$ \rho \left( \frac{\partial u}{\partial t} + u \cdot \nabla u \right) = -\nabla p + \nabla \cdot \tau_p + \eta_s \nabla^2 u, $$

and 

$$ \frac{\partial **\Theta** }{\partial t} + u \cdot \nabla \Theta - \left( \Omega \cdot \Theta - \Theta \cdot \Omega \right) -2B 
			= \frac{1}{\lambda} \left( a e^{-\Theta} - fI \right). $$

Here, $u$ is the local fluid velocity, $\Theta$ is the natural logarithm of the conformation tensor $C$, given by $\Theta = ln(C)$, $I$ is the identity tensor,
$\Omega$ is a part of the velocity gradient tensor that describes pure rotation (similar to the vorticity tensor) and $B$ is symmetric and traceless (similar to the shear rate tensor).
The parameter $a$, the function $f$, and the polymeric stress tensor $\tau_p$ are defined acccording to:

$$ a = \frac{L^2}{L^2 - 3}, $$

$$ f = \frac{L^2}{L^2 - tr(e^{\Theta})},$$

and 

$$ \tau_p = \frac{\eta_p}{\lambda} \left( f e^{-\Theta} - aI \right) , $$

where $\rho$, $\eta_s$, $\eta_p$, $\lambda$, and $L$ are, respectively, the fluid density, the solvent viscosity, the polymer contribution to the mixture viscosity, 
the viscoelastic relaxation time, and the fully extended polymer length.

## **Numerical Scheme:**
The cavity was discretized on a 51x51 cell grid.

### Initial and boundary conditions:
The fluid velocity, stress tensor, conformation tensor, and pressure fields were set equal to zero at time $t = 0$, corresponding to a fluid at rest.
The Lid velocity was defined according to the following ramp<sup>2</sup>

$$u(t,x,y=1) = 8\left[1 + tanh\left(8\left(t-\frac{1}{2}\right)\right)\right]x^2(1-x^2), $$

which drives smooth start-up flow and causes the velocity gradient $\nabla u$ to vanish at the corners of the cavity. In addition, Nuemann boundary conditions were defined 
at the cavity walls for the pressure, stress tensor, and the conformation tensor. 

## **Results**:
All calculations were performed with a Reynolds number $Re = \frac{\rho U D}{\eta_s}$, Wiessenberg number $Wi = \frac{U_{max} \lambda}{L}$, 
and viscosity ratio $\beta = \frac{\eta_s}{\eta_s + \eta_p}$ set equal to $Re = 0$, $Wi = 2$, $\beta = 0.5$, respectively, where $U_max$ is the maximum lid speed and $D$ is the length of the cavity wall.

### **Velocity and pressure fields for $L = \infty$ (Oldroyd-B) over the time interval $[0, 20]$**

![Fene-P_vary_L2](https://github.com/user-attachments/assets/fc54c1de-52ff-4131-95e5-bf193920e8a6)
