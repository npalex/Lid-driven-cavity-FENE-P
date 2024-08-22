# **Lid-driven cavity flow of an incompressible FENE-P fluid**

&emsp; This program solves the continuity equation, the incompressible Cauchy momentum equation, and the log-conformation formulation of the FENE-P viscoelastic fluid model in 2D, given by

$$ \nabla \cdot  **u** = 0, $$

$$ \rho \left( \frac{\partial u}{\partial t} + u \cdot \nabla u \right) = -\nabla p + \nabla \cdot \tau_p + \eta_s \nabla^2 u, $$

and 

$$ \frac{\partial **\Theta** }{\partial t} + u \cdot \nabla \Theta - \left( \Omega \cdot \Theta - \Theta \cdot \Omega \right) -2B 
			= \frac{1}{\lambda} \left( a e^{-\Theta} - fI \right). $$

Here, $u$ is the local fluid velocity, $\Omega$ is a tensor that describes pure rotation (similar to the vorticity tensor) and $B$ is symmetric and tracless (similar to the shera rate tensor.
The parameter $a$, the function $f$, and the polymeric stress tensor $\tau_p$ are defined acccording to:

$$ a = \frac{L^2}{L^2 - 3}, $$

$$ f = \frac{L^2}{L^2 - tr(e^{\Theta})},$$

and 

$$ \tau_p = \frac{\eta_p}{\lambda} \left( f e^{-\Theta} - aI \right) , $$

where $\eta_s$, $\eta_p$, $\lambda$, and $L$ are the solvent viscosity, the polymer contribution the mixture viscosity, 
the viscoelastic relaxation time, and the fully extended polymer legth, respectively. 


![Fene-P_vary_L2](https://github.com/user-attachments/assets/fc54c1de-52ff-4131-95e5-bf193920e8a6)
