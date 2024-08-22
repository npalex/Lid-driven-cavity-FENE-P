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

where $\eta_s$, $\eta_p$, $\lambda$, and $L$ are, respectively, the solvent viscosity, the polymer contribution to the mixture viscosity, 
the viscoelastic relaxation time, and the fully extended polymer legth.

## **Numerical Scheme:**

## **Results**:

### **Velocity and pressure distribution for $Re = 0$, $Wi = 2$, $\beta = 0.5$, and $L = \inf$ (Oldroyd-B) over the time interval $[0, 20]$**

![Fene-P_vary_L2](https://github.com/user-attachments/assets/fc54c1de-52ff-4131-95e5-bf193920e8a6)
