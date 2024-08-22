# **Lid-driven cavity flow of an incompressible FENE-P fluid**

&emsp; This program solves the continuity, incompressible Cauchy momentum equations, and the log-conforation formulation of the FENE-P viscoelastic fluid model in 2D, given by

$$ \nabla \cdot  **u** = 0, $$

$$ \rho \left( \frac{\partial u}{\partial t} + u \cdot \nabla u \right) = \frac{\partial \tau_{xx}}{\partial x} + \frac{\partial \tau_{xy}}{\partial y} 
    + \beta \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right), $$

	
$$ Wi\frac{\partial \tau_{xx}}{\partial t} + \tau_{xx} = 2\frac{\partial u}{\partial x}, $$

$$  Wi\frac{\partial \tau_{xy}}{\partial t} + \tau_{xy} = \frac{\partial v}{\partial x} + \frac{\partial u}{\partial y}, $$

and

$$ Wi\frac{\partial \tau_{yy}}{\partial t} + \tau_{yy} = 2\frac{\partial v}{\partial y}. $$

where $u$ and $v$ are the components of the local fluid velocity in the $x$ and $y$ directions, $\tau_{xy}$ is the local "polymeric" shear stress, 
and $\tau_{xx}$ and $\tau_{yy}$ are local, polymeric normal stresses.




![Fene-P_vary_L2](https://github.com/user-attachments/assets/fc54c1de-52ff-4131-95e5-bf193920e8a6)
