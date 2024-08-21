# Lid-driven-cavity-FENE-P

&emsp; This program solves the continuity, incompressible Cauchy momentum equations, and the Oldroyd-B viscoelastic fluid model in 2D, 
using the log-conformation method, given by

$$ \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0, $$

$$ Re\left( \frac{\partial u}{\partial t} + \frac{\partial u^2}{\partial x} + \frac{\partial (u v)}{\partial y} 
	+ \frac{\partial p}{\partial x}\right) = \frac{\partial \tau_{xx}}{\partial x} + \frac{\partial \tau_{xy}}{\partial y} 
    + \beta \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right), $$

$$ Re\left( \frac{\partial v}{\partial t} + \frac{\partial (u v)}{\partial x} + \frac{\partial v^2}{\partial y} 
	+ \frac{\partial p}{\partial y}\right) = \frac{\partial \tau_{xy}}{\partial x} + \frac{\partial \tau_{yy}}{\partial y} 
    + \beta \left( \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} \right), $$
	
$$ Wi\frac{\partial \tau_{xx}}{\partial t} + \tau_{xx} = 2\frac{\partial u}{\partial x}, $$

$$  Wi\frac{\partial \tau_{xy}}{\partial t} + \tau_{xy} = \frac{\partial v}{\partial x} + \frac{\partial u}{\partial y}, $$

and

$$ Wi\frac{\partial \tau_{yy}}{\partial t} + \tau_{yy} = 2\frac{\partial v}{\partial y}. $$

where $u$ and $v$ are the components of the local fluid velocity in the $x$ and $y$ directions, $\tau_{xy}$ is the local "polymeric" shear stress, 
and $\tau_{xx}$ and $\tau_{yy}$ are local, polymeric normal stresses.




![Fene-P_vary_L2](https://github.com/user-attachments/assets/fc54c1de-52ff-4131-95e5-bf193920e8a6)
