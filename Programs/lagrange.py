import numpy as np
from matplotlib.pyplot import *
from scipy import interpolate                   #Used for making smooth color maps
from scipy.optimize import newton
from numpy import array                         #Arrays are used in making the color map
from numpy import concatenate
import tkinter as tk
from tkinter import Tk
from tkinter import ttk

#function for first three lagrange points
def func(x, s0, s1, M1, M2):
    alpha = M2/(M1+M2)
    return x**5 + (3-alpha)*x**4 + (3-2*alpha)*x**3 + (1-s1-alpha*(1+s0-s1))*x*x - 2*s0*alpha*x - s0*alpha

#derivative of func
def func_deriv(x, s0, s1, M1, M2):
    alpha = M2/(M1+M2)
    return 5*x**4 + 4*(3-alpha)*x**3 + 3*(3-2*alpha)*x*x + 2*(1-s1-alpha*(1+s0-s1))*x - 2*s0*alpha

#Adds two tuples component by component
def add(t1, t2):
    return tuple(map(lambda x, y: x+y, t1, t2))

def plot(var):
    x = var[0]
    y = var[1]
    phi = var[2]
    r1 = var[3]
    r2 = var[4]
    L1 = var[5]
    L2 = var[6]
    L3 = var[7]
    L4 = var[8]
    L5 = var[9]
    phi1 = var[10]
    phi2 = var[11]
    phi3 = var[12]
    gca().clear()
    rcParams['contour.negative_linestyle'] = 'solid'
    contour(x,y,phi,levels=[phi1,phi2,phi3], colors='k')
    xlabel('x/a')
    ylabel('y/a')
    #Circles
    gca().add_artist(Circle((0,0),0.02,color='b')) #CM
    gca().add_artist(Circle((-r1,0),0.04,color='k')) #M1
    gca().add_artist(Circle((r2,0),0.04,color='k')) #M2
    gca().add_artist(Circle(L1,0.015,color='k')) #L1
    gca().add_artist(Circle(L2,0.015,color='k')) #L2
    gca().add_artist(Circle(L3,0.015,color='k')) #L3
    gca().add_artist(Circle(L4,0.015,color='k')) #L4
    gca().add_artist(Circle(L5,0.015,color='k')) #L5
    #Text Labels
    gca().text(0,-0.2,r'$CM$',size=13)
    gca().text(-r1-0.05,0.08,r'$M_1$',size=13)
    gca().text(r2-0.02,0.08,r'$M_2$',size=13)
    gca().text(add(L1,(-0.18,0))[0],add(L1,(-0.18,0))[1],r'$L_1$',size=13)
    gca().text(add(L2,(0.06,0))[0],add(L2,(0.06,0))[1],r'$L_2$',size=13)
    gca().text(add(L3,(-0.18,0))[0],add(L3,(-0.18,0))[1],r'$L_3$',size=13)
    gca().text(add(L4,(-0.02,0.04))[0],add(L4,(-0.02,0.04))[1],r'$L_4$',size=13)
    gca().text(add(L5,(-0.02,0.04))[0],add(L5,(-0.02,0.04))[1],r'$L_5$',size=13)

    gca().set_aspect(1) #Sets a 1:1 aspect ratio

def calc(M1,M2):
    G = 6.67E-11 #duh
    a = 5E8 #meters, separation
    MS = 1.989E30 #kg, Sun
    ME = 5.972E24
    M1 *= MS #kg, primary
    M2 *= MS #kg, secondary
    r1 = M2*a/(M1+M2) #meters, M1 distance from CM
    r2 = a - r1 #meters, M2 distance from CM
    w = np.sqrt(G*(M1+M2) / a**3) #rad/sec, orbital angular velocity

    dx = 0.01 #resolution
    x = np.arange(-2,2+dx,dx)*a
    y = -np.arange(-2,2+dx,dx)*a

    #define proper matrices
    x2 = np.asarray([x**2 for i in x])
    y2 = np.transpose(x2)

    #convert to polar coordinates
    r = np.sqrt(x2 + y2)
    t = [[np.arctan2(i,j) for j in x] for i in y]

    #distance from M1 and M2 to point (r,t)
    s1 = np.sqrt(r1**2 + r**2 + 2*r1*r*np.cos(t))
    s2 = np.sqrt(r2**2 + r**2 - 2*r2*r*np.cos(t))

    #effective gravitational potential
    phi = -G*(M1/s1 + M2/s2) - 0.5*w*w*r*r

    #convert everything to be in nice units
    x /= a
    y /= a
    r1 /= a
    r2 /= a
    phi /= G*(M1+M2)/a

    #calculate lagrange points and contour levels
    L1 = (r2+newton(func,1,fprime=func_deriv,args=(-1,1,M1,M2)),0)
    L2 = (r2+newton(func,1,fprime=func_deriv,args=(1,1,M1,M2)),0)
    L3 = (r2+newton(func,-1,fprime=func_deriv,args=(-1,-1,M1,M2),maxiter=10000),0)
    L4 = ((M1-M2)/(M1+M2)/2,np.sqrt(3)/2)
    L5 = ((M1-M2)/(M1+M2)/2,-np.sqrt(3)/2)
    phi1 = (-G*(M1/((r1+L1[0])*a) + M2/((r2-L1[0])*a)) - 0.5*w*w*L1[0]*L1[0]*a*a) / (G*(M1+M2)/a)
    phi2 = (-G*(M1/((r1+L2[0])*a) + M2/((L2[0]-r2)*a)) - 0.5*w*w*L2[0]*L2[0]*a*a) / (G*(M1+M2)/a)
    phi3 = (-G*(M1/((-L3[0]-r1)*a) + M2/((r2-L3[0])*a)) - 0.5*w*w*L3[0]*L3[0]*a*a) / (G*(M1+M2)/a)

    return (x,y,phi,r1,r2,L1,L2,L3,L4,L5,phi1,phi2,phi3)

figure(1)
ion()
plot(calc(0.85,0.17))
show(block=False)

gui = Tk()
ttk.Label(gui, text = 'M1').grid(row=0,column=0)
str1 = tk.StringVar(); str1.set('0.85')
tk.Entry(gui,textvariable=str1,width=10).grid(row=0,column=2)
ttk.Label(gui, text = 'M2').grid(row=1,column=0)
str2 = tk.StringVar(); str2.set('0.17')
ttk.Entry(gui,textvariable=str2,width=10).grid(row=1,column=2)
ttk.Button(gui, text = 'update', command = lambda: plot(calc(float(str1.get()),float(str2.get())))).grid(row=2,columnspan=3)



print('Done ...')
