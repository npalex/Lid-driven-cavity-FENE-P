# **Lid-driven cavity flow of an incompressible FENE-P fluid**

&emsp; OpenFoam with RheoTool<sup>1</sup> is used here to solve the continuity equation, the incompressible Cauchy momentum equation, and the log-conformation formulation<sup>2,3</sup> of the FENE-P viscoelastic fluid model in 2D, given by

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

The kinetic (KE) and elastic potential (PE) energy densities were calculated via

$$ KE = \frac{\rho}{2 V} \int_V dV (u \cdot u) $$

and 

$$ PE = \frac{1}{2 V} \int_V dV tr(\tau_p)$$

## **Numerical Scheme:**
The cavity was discretized on a 51x51 cell grid.

### **Initial/boundary conditions:**
The fluid velocity, stress tensor, log-conformation tensor, and pressure fields were set equal to zero at time $t = 0$, corresponding to a fluid at rest.
The lid velocity was defined according to the following ramp<sup>3</sup>

$$u(t,x,y=1) = 8\left[1 + tanh8\left(t-\frac{1}{2}\right)\right]x^2(1-x^2), $$

which drives smooth start-up flow and causes the velocity gradient $\nabla u$ to vanish at the corners of the cavity. In addition, homogeneous Nuemann boundary conditions were defined 
at the cavity walls for the pressure, stress tensor, and the log-conformation tensor. 

## **Results**:
All calculations were performed with a Reynolds number $Re = \frac{\rho U_{max} D}{\eta_s}$, Wiessenberg number $Wi = \frac{U_{max} \lambda}{D}$, 
and viscosity ratio $\beta = \frac{\eta_s}{\eta_s + \eta_p}$ set equal to $Re = 0$, $Wi = 2$, $\beta = 0.5$, respectively, where $U_{max}$ is the maximum lid speed and $D$ is the length of the cavity wall.

### **Velocity and pressure fields for $L = \infty$ (Oldroyd-B) over the time interval $[0, 20]$**

### **Total kinetic and elastic potential energy as a function of time for $L^2 = 5, 25,$ and $\infty$**

![Fene-P_vary_L2](https://github.com/user-attachments/assets/fc54c1de-52ff-4131-95e5-bf193920e8a6)

These KE and PE transienst above indicate that the simulation reached steady-state for $L^2 = 5$ and $25$.

## **References**:

1.	F. Pimenta and M.A. Alves, 2016. RheoTool version 6.0, https://github.com/fppimenta/rheoTool.

2.	R. Fattala and R. Kupferman, 2004. Constitutive laws for the matrix-logarithm of the conformation tensor.
		J. Non-Newtonian Fluid Mech., 123, 281–285.

3.	R. Fattala and R. Kupferman, 2005. Time-dependent simulation of viscoelastic flows at high Weissenberg
		number using the log-conformation representation. J. Non-Newtonian Fluid Mech., 126, 23–37.

4.	