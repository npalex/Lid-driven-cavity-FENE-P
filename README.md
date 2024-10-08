# **Lid-driven cavity flow of an incompressible FENE-P fluid**

&emsp; OpenFoam with RheoTool<sup>1</sup> was used to solve the continuity equation, the Cauchy momentum equation, and the log-conformation<sup>2,3</sup> formulation 
of the FENE-P (Finitely-Extensible Nonlinear Elastic) viscoelastic fluid model in 2D, given by

$$ \nabla \cdot  **u** = 0, $$

$$ \rho \left( \frac{\partial u}{\partial t} + u \cdot \nabla u \right) = -\nabla p + \nabla \cdot \tau_p + \eta_s \nabla^2 u, $$

and 

$$ \frac{\partial **\Theta** }{\partial t} + u \cdot \nabla \Theta - \left( \Omega \cdot \Theta - \Theta \cdot \Omega \right) -2B 
			= \frac{1}{\lambda} \left( a e^{-\Theta} - fI \right). $$

Here, $u$ is the local fluid velocity, $\Theta$ is the natural logarithm of the conformation tensor $C$, given by $\Theta = ln(C)$, and $I$ is the identity tensor.
The velocity gradient tensor was decomposed according to: $\nabla u = \Omega + B + N \cdot C^{-1}$ where $\Omega$ and $N$ are antisymmetric tensors that describe pure rotational deformation (with the former similar to the vorticity tensor) 
and $B$ is symmetric, traceless, and describes volume-preserving deformation (similar to the shear rate tensor).<sup>2</sup>
The parameter $a$, the function $f$, and the polymeric stress tensor $\tau_p$ are defined acccording to:

$$ a = \frac{L^2}{L^2 - 3}, $$

$$ f = \frac{L^2}{L^2 - tr(e^{\Theta})},$$

and 

$$ \tau_p = \frac{\eta_p}{\lambda} \left( f e^{-\Theta} - aI \right) , $$

where $\rho$, $\eta_s$, $\eta_p$, and $\lambda$ are the fluid density, the solvent viscosity, and the polymer contribution to the mixture viscosity, 
the polymer relaxation time, respectively. The parameter $L$ is the finite extensibility parameter, defined as the ratio of the length of the fully extended polymer over the root mean
square of the end-to-end separation distance of the polymer chain in its equilibrium configuration.

&emsp; The kinetic (KE) and elastic potential (PE) energy densities were calculated via

$$ KE = \frac{\rho}{2 V} \int_V dV (u \cdot u) $$

and 

$$ PE = \frac{1}{2 V} \int_V dV tr(\tau_p) ,$$

where $V$ is the volume of the cavity.

## **Numerical Scheme:**
&emsp; The rheoFOAM solver implementing the SIMPLE algorithm was used to evaluate the fluid velocity, log-conformation tensor, and pressure fields at each time step on a uniform 51x51 cell grid.
In addition, the improved both sides diffusion technique<sup>4</sup> was used to improve the numerical stability of the solver. Gradient, divergence, and Laplacian terms were discretized using the Gauss linear scheme, 
convection terms were discretized using the CUBISTA scheme, and time discretization was performed using the Crank-Nicolson method. 

&emsp; In accordance with the SIMPLE algorithm, the velocity, pressure, and log-conformation tensor equations above were solved separately. The corresponding discretized linear systems of equations of the form $Ax = b$ for each variable $u$, $p$, and $\Theta$, were solved using iterative linear solvers.
The Generalized geometric-algebraic multi-grid (GAMG) solver was used for both the pressure and velocity fields with a Diagonal-based Incomplete Cholesky (DIC) preconditioner, 
which requires the matrix $A$ to be symmetric positive definite (SPD). Note, the convective term in the momentum equation has been neglected, since $Re = 0$, so that the matrix $A$ for the discretized momentum equation is SPD. The matrix $A$ for Laplace's equation governing the pressure is also SPD. For $\Theta$, the preconditioned (bi-)conjugate gradient (PBiCG) method was used. 
However, the matrix $A$ for the FENE-P model governing $\Theta$ is not SPD since the advective terms remain. Hence, Cholesky decomposition could not be used and the Diagonal-based Incomplete LU (DILU) preconditioner, which is relatively slow (Cholesky decomposition is approximately twice as efficient as LU decomposition), was used instead. 
Note, all calculations were performed using a single core.

### **Initial/boundary conditions:**
&emsp; The fluid velocity, log-conformation tensor, and pressure fields were set equal to zero at time $t = 0$, corresponding to a fluid at rest.
The lid velocity was defined according to the following ramp<sup>3</sup>

$$u(t,x,y=1) = 8\left[1 + tanh8\left(t-\frac{1}{2}\right)\right]x^2(1-x^2), $$

which drives smooth start-up flow and causes $\nabla u$ to vanish at the corners of the cavity. The fluid velocity was set equal to zero at the remaining walls. 
In addition, homogeneous Neumann boundary conditions were defined at the cavity walls for the pressure and the log-conformation tensor.

## **Results**:
&emsp; All calculations were performed with a Reynolds number $Re = \frac{\rho U_{max} D}{\eta_s}$, Wiessenberg number $Wi = \frac{U_{max} \lambda}{D}$, 
and viscosity ratio $\beta = \frac{\eta_s}{\eta_s + \eta_p}$ set equal to $Re = 0$, $Wi = 2$, $\beta = 0.5$, respectively, where $U_{max}$ is the maximum lid speed and $D$ is the length of the cavity wall.

### **Velocity and pressure fields for $L = \infty$ (Oldroyd-B) over the time interval $[0, 10]$**

https://github.com/user-attachments/assets/af22151e-9a1c-48f7-a741-729721fc70dc

### **Velocity and pressure fields for $L^2 = 25$ over the time interval $[0, 10]$**

https://github.com/user-attachments/assets/de4676a0-70c1-47bf-8194-d53354d0617a

### **Velocity and pressure fields for $L^2 = 5$ over the time interval $[0, 5]$**

https://github.com/user-attachments/assets/c8b9129f-c9bb-4a4d-8866-f42a561588d4

### **Total kinetic and elastic potential energy densities as a function of time for $L^2 = 5, 25,$ and $\infty$**

![Fene-P_vary_L2](https://github.com/user-attachments/assets/fc54c1de-52ff-4131-95e5-bf193920e8a6)

The KE and PE transients above indicate that the simulation reached steady-state for $L^2 = 5$ and $25$.

## **Discussion**:
&emsp; The videos above indicate a Newtonian response at early times, with a centrally located primary vortex, followed by viscoelastic relaxation that drives the primary vortex to migrate upstream toward the upper left corner of the cavity.
Finite extensibility under the conditions presented here, appears to reduce this effect as well as the effective viscoelastic relaxation time. This behavior can be understood by reformulating the FENE-P model in terms of the polymeric stress tensor $\tau_p$:

$$ \tau_p + \lambda_{eff} \tau_{p_{(1)}}
			= \eta_{p,eff} \left(\nabla u + \nabla u^T \right). $$ 
			
where $\tau_{p_{(1)}}$ denotes the upper convected derivative of $\tau_p$. Here, the effective viscoelastic relaxation time is given by

$$ \lambda_{eff} = \frac{\lambda}{f_2} ,$$

the effective polymeric viscosity is

$$ \eta_{p,eff} = \frac{a \eta_p}{f_2} ,$$
 
and the function $f_2$ is defined according to
 
$$ f_2 = \frac{L^2 + \frac{\lambda}{a \eta_p} tr(\tau_p)}{L^2-3} .$$

$\lambda_{eff}$ decreases with decreasing $L$ indicating that finite extensibility reduces the effective viscoelastic relaxation time of the fluid, which is consistent with the video simulations and the energy density curves above. 

&emsp; Furthermore, shear-thinning occurs when $\eta_{p,eff}$ decreases with an increase in the local elastic potential energy density $tr(\tau_p)$ 
as the polymers are stretched under flow, an effect that is more pronounced as $L$ decreases. Note, however, that all calculations were performed with $Wi = 2$, which may be insufficient to observe significant shear-thinning behavior induced by finite extensibility, 
as indicated by the steady shear curves presented in Yamani and McKinley.<sup>5</sup>

## **References**:

1.	F. Pimenta and M.A. Alves, 2016. RheoTool version 6.0, https://github.com/fppimenta/rheoTool.

2.	R. Fattala and R. Kupferman, 2004. Constitutive laws for the matrix-logarithm of the conformation tensor.
		J. Non-Newtonian Fluid Mech., 123, 281–285.

3.	R. Fattala and R. Kupferman, 2005. Time-dependent simulation of viscoelastic flows at high Weissenberg
		number using the log-conformation representation. J. Non-Newtonian Fluid Mech., 126, 23–37.

4.	C. Fernandes, M.S.B. Araujo, L.L. Ferrás, J. Miguel Nóbrega, 2017, 
		Improved both sides diffusion (iBSD): A new and straightforward stabilization approach for viscoelastic fluid flows
		J. Non-Newtonian Fluid Mech., 249, 63-78.

5.	S. Yamani, G. H. McKinley, 2023. Master Curves for FENE-P Fluids in Steady Shear Flow. J. Non-Newtonian Fluid Mech., 313, 104944.
