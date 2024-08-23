#*************************************************************************** 
#
# created by: Nathan Alexander (March 2024)
#
# The purpose of this program is to extract and then animate numerical data
#
#***************************************************************************
     
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML
from io import StringIO
import pandas as pd

#-- print parameters
file_name = '/home/npalex/OpenFOAM/npalex-9/run/cavity_Fene-P_Wi_2_Re_0_beta_0_5_L2_5/'

with open(file_name + 'constant/constitutiveProperties', 'r') as f:
    print(f.read())

#-- define parameters
steps = 250
t_final = 5.0
dt = t_final/steps
meqn = 6
mx = 51
my = mx
grid_tot = mx*mx - 1
t = np.arange(0, t_final + dt, dt)

#-- initialize arrays 
q = np.zeros((meqn,steps+1, mx, mx))                

#-- extract data from files at each time step
for i in range(1, steps+1):
    
    if (int(t[i]) - t[i] != 0):
        f = pd.read_csv(file_name + str(np.round(t[i], 10)) + "/p", 
                        skiprows=21, skipfooter = 21, dtype = float, names = None, header = None, sep = '\s+', engine='python')

        g = pd.read_csv(file_name + str(np.round(t[i], 10)) + "/U", 
                        skiprows=21, skipfooter = 21, names = None, header = None, sep = '\s+', engine='python', usecols=np.arange(0,2))

        h = pd.read_csv(file_name + str(np.round(t[i], 10)) + "/tau", 
                        skiprows=21, skipfooter = 21, names = None, header = None, sep = '\s+', engine='python', usecols=np.arange(0,4))

   
    else:
        f = pd.read_csv(file_name + str(int(t[i])) + "/p", 
                        skiprows=21, skipfooter = 21, dtype = float, names = None, header = None, sep = '\s+',engine='python')
        
        g = pd.read_csv(file_name + str(int(t[i])) + "/U", 
                        skiprows=21, skipfooter = 21, names = None, header = None, sep = '\s+',engine='python', usecols=np.arange(0,2))

        h = pd.read_csv(file_name + str(int(t[i])) + "/tau", 
                        skiprows=21, skipfooter = 21, names = None, header = None, sep = '\s+', engine='python', usecols=np.arange(0,4))

    f = f.values
    f = f.T

    g = g.values
    g = g.T

    h = h.values
    h = h.T

    #-- remove '(' from first column of array
    for k in range(0, mx*my):
            g[0, k] = np.char.strip(g[0,k], '(')
            h[0, k] = np.char.strip(h[0,k], '(')

    for j in range(0, mx):

        #--U
        q[0,i, j, :] = g[0,j*mx:(j+1)*mx]   # u
        q[1,i, j, :] = g[1,j*mx:(j+1)*mx]   # v

        #-- p
        q[2,i, j, :] = f[0,j*mx:(j+1)*mx]

        #-- tau
        q[3,i, j, :] = h[0,j*mx:(j+1)*mx]   # tau_xx
        q[4,i, j, :] = h[1,j*mx:(j+1)*mx]   # tau_xy
        q[5,i, j, :] = h[3,j*mx:(j+1)*mx]   # tau_yy
            
#------------------------------------------------
#-- plot results as an animation using matplotlib
#------------------------------------------------
q_step = 2                           # quiver plot spacing

#-- define array of cell centers
xlow = 0
ylow = 0
dx = 1/51
dy = dx
x = np.arange(xlow + dx/2, 1, dx)
y = np.arange(ylow + dy/2, 1, dy)
xgrid, ygrid = np.meshgrid(x, y)

#-- establish figure and axes objects
# fig = plt.figure(figsize = (7, 6), layout = "tight")
# ax = fig.gca()

# ax.axis('square')
# p = ax.pcolormesh(xgrid, ygrid, q[2,0,:,:], cmap = 'coolwarm',vmin = -10, vmax = 10)
# cbar = fig.colorbar(p, fraction = 0.045, pad = 0.05, ticks = np.arange(-10, 12, 2))
# cbar.set_label('$p/(\u03C1 U^2)$', size = 20)

#------------------------------------------------
#-- plot vector field and pressure distribution
#------------------------------------------------
#-- define function, which is an argument for the method animation.FuncAnimation() and is called for each frame
# def fplot(frame_number):
    
    # ax.clear()
    
    # #-- plot pressure distribution
    # ax.pcolormesh(xgrid, ygrid, q[2,frame_number,:,:], cmap = 'coolwarm',vmin =-10, vmax = 10) #--cmap = 'GnBu'
    
    # #-- plot velocity distribution
    # ax.quiver(x[::q_step], y[::q_step], q[0,frame_number,::q_step,::q_step], q[1,frame_number,::q_step,::q_step], scale_units = 'xy', scale = 1)

    # #-- set axes title
    # ax.set_title('t(U/L) = %.2f' %t[frame_number], fontsize = 20)
    
    # #-- set axes limits and tick marks
    # ax.set_xticks(np.arange(0, 1.2, .2))
    # ax.set_yticks(np.arange(0, 1.2, .2))
    # ax.set_xlim(left = 0, right = 1.)
    # ax.set_ylim(bottom = 0, top = 1.)
    
    # ax.set_ylabel('$y$', fontsize = 16)
    # ax.set_xlabel('$x$', fontsize = 16)
    
    # return()

# #-- generate animation
# anim = animation.FuncAnimation(fig = fig, func = fplot, frames=int(steps+1), interval=40, repeat=False)
# plt.close()                        #-- removes residual plot at final time
# #HTML(anim.to_jshtml())             #-- print animation in jupyter notebook

# #-- save animation as an html file
# with open("Vector_field_Re_0_1_Wi_2.html", "w") as f:
    # print(anim.to_html5_video(embed_limit=None), file=f)
    
#------------------------------------------------
#-- plot streamlines and pressure field
#------------------------------------------------
fig = plt.figure(figsize = (7.5, 6), layout = "tight")
ax = plt.axes(xlim=(-0.02, 1.02), ylim=(-0.02, 1.1))            # creates axes at specifed limits, (gca() not required)
q_step = 1                           # quiver plot spacing

#-- generate colorbar
ax.axis('square')
p = ax.pcolormesh(xgrid, ygrid, q[5,0,:,:], cmap = 'coolwarm',vmin =-10, vmax = 10)
cbar = fig.colorbar(p, fraction = 0.045, pad = 0.05, ticks = np.arange(-10, 12, 2))
cbar.set_label('$p/(\u03C1 U^2)$', size = 20)

#-- define function, which is an argument for the method animation.FuncAnimation() and is called for each frame
def fplot(frame_number):
    
    ax.clear()
    
    #-- plot pressure distribution
    ax.pcolormesh(xgrid, ygrid, q[2,frame_number,:,:], cmap = 'coolwarm',vmin =-10, vmax = 10)
    
    #-- plot velocity distribution
    ax.streamplot(xgrid, ygrid, q[0,frame_number,::q_step,::q_step], q[1,frame_number,::q_step,::q_step], color = "black", linewidth = .3, density=.7, broken_streamlines=False)  

    #-- set axes title
    ax.set_title('t(U/L) = %.2f' %t[frame_number], fontsize = 20)
    
    #-- set axex limits and tick marks
    ax.set_xticks(np.arange(0, 1.2, .2))
    ax.set_yticks(np.arange(0, 1.2, .2))
    ax.set_xlim(left = 0, right = 1.)
    ax.set_ylim(bottom = 0, top = 1.)
    
    ax.set_ylabel('$y$', fontsize = 16)
    ax.set_xlabel('$x$', fontsize = 16)
    
    return()

#-- generate animation
anim = animation.FuncAnimation(fig = fig, func = fplot, frames=int(steps+1), interval=40, repeat=False)
plt.close()                        #-- removes residual plot at final time
#HTML(anim.to_jshtml())             #-- print animation in jupyter notebook

#-- save animation as an html file
with open("Streamlines_Re_0_1_Wi_2.html", "w") as f:
    print(anim.to_html5_video(embed_limit=None), file=f)
    
    
#------------------------------------------------
#-- plot streamlines and normal stress tau_xx field
#------------------------------------------------
# fig = plt.figure(figsize = (7.5, 6), layout = "tight")
# ax = plt.axes(xlim=(-0.02, 1.02), ylim=(-0.02, 1.1))            # creates axes at specifed limits, (gca() not required)
# q_step = 1                           # quiver plot spacing

# #-- generate colorbar
# ax.axis('square')
# p = ax.pcolormesh(xgrid, ygrid, q[2,0,:,:], cmap = 'coolwarm',vmin =-0.5, vmax = 0.5)
# cbar = fig.colorbar(p, fraction = 0.045, pad = 0.05, ticks = np.arange(-0.5, 0.6, .1))
# cbar.set_label('$\u03C4_{xx}/(\u03B7 U/L)$', size = 20) 

# #-- define function, which is an argument for the method animation.FuncAnimation() and is called for each frame
# def fplot(frame_number):
    
    # ax.clear()
    
    # #-- plot tau_xx distribution
    # ax.pcolormesh(xgrid, ygrid, q[3,frame_number,:,:], cmap = 'coolwarm',vmin =-.5, vmax = .5)
    
    # #-- plot velocity distribution
    # ax.streamplot(xgrid, ygrid, q[0,frame_number,::q_step,::q_step], q[1,frame_number,::q_step,::q_step], color = "black", linewidth = .3, density=.7, broken_streamlines=False)  

    # #-- set axes title
    # ax.set_title('t(U/L) = %.2f' %t[frame_number], fontsize = 20)
    
    # #-- set axex limits and tick marks
    # ax.set_xticks(np.arange(0, 1.2, .2))
    # ax.set_yticks(np.arange(0, 1.2, .2))
    # ax.set_xlim(left = 0, right = 1.)
    # ax.set_ylim(bottom = 0, top = 1.)
    
    # ax.set_ylabel('$y$', fontsize = 16)
    # ax.set_xlabel('$x$', fontsize = 16)
    
    # return()

# #-- generate animation
# anim = animation.FuncAnimation(fig = fig, func = fplot, frames=int(steps+1), interval=40, repeat=False)
# plt.close()                        #-- removes residual plot at final time
# #HTML(anim.to_jshtml())             #-- print animation in jupyter notebook

# #-- save animation as an html file
# with open("Streamlines_tau_xx_Re_0_1_Wi_2.html", "w") as f:
    # print(anim.to_html5_video(embed_limit=None), file=f)