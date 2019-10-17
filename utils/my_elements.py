from math import *
import random
import numpy as np 

def rotation_no_twiss(Qx_rot, Qy_rot, twiss , x, px, y, py):
    x1 = cos(Qx_rot)*x+sin(Qx_rot)*px
    px1 = -sin(Qx_rot)*x+cos(Qx_rot)*px
    y1 = cos(Qy_rot)*y+sin(Qy_rot)*py
    py1 = -sin(Qy_rot)*y+cos(Qy_rot)*py
    return x1, px1, y1, py1

def rotation(Qx_rot, Qy_rot, twiss, x, px, y, py):
    x1 = (cos(Qx_rot) + twiss.alpha_x*sin(Qx_rot))*x + twiss.beta_x*sin(Qx_rot)*px
    px1 = -twiss.gamma_x*sin(Qx_rot)*x+ (cos(Qx_rot)-twiss.alpha_x*sin(Qx_rot))*px
    y1 = (cos(Qy_rot) + twiss.alpha_y*sin(Qy_rot))*y + twiss.beta_y*sin(Qy_rot)*py
    py1 = -twiss.gamma_y*sin(Qy_rot)*y+ (cos(Qy_rot)- twiss.alpha_y*sin(Qy_rot))*py
    return x1, px1, y1, py1

def octupole_map(k3, x, px, y, py):
    k3_kick = k3/6.
    x1 = x
    px1 = px - k3_kick*(x**3-3*x*y**2)
    y1 = y
    py1 = py - k3_kick*(y**3-3*y*x**2)
    return x1, px1, y1, py1
    
def noise_map(Delta, x, px, y, py):
    z_px = random.gauss(0,1)    
    x1 = x
    px1 = px + Delta*z_px
    y1 = y
    py1 = py
    return x1, px1, y1, py1

def BB_4D_map(xi, sigmax, sigmapx, sigmay, sigmapy, x, px, y, py):    
    # Note: The formula of Lebedev for the BB kick is for normalised coordinates. 
    # As here physical coordinates are used, the BB parameters and the kick itself need 
    # to be normalised with the sigmax and sigmapx. 
    
    r_sq = x**2/(sigmax**2) # + y**2/(sigmay**2), uncomment when V motion is included

    x1 = x
    factor_x = ((8.*np.pi*xi*x1/sigmax)/r_sq)*sigmapx
    px1 = px + factor_x*(1.-np.exp(-r_sq/2.))
   
    y1 = y
    factor_y = 0. #((8.*np.pi*xi*y1/sigmay)/r_sq)*sigmapy, # uncomment when V motion is included
    py1 = py + factor_y*(1.-np.exp(-r_sq/2.))
   
    return x1, px1, y1, py1

def feedback_system_map(gain, sigmapx, x, px, y, py):
    px_average, py_average = np.nanmean(px/sigmapx), np.nanmean(py)
    
    x1 = x
    px1 = px - gain*px_average
    y1 = y
    py1 = py - gain*py_average
    return x1, px1, y1, py1
