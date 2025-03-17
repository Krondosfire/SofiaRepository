import turtle01

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.integrate as integrate

g = 9.81
l = 1.0
k = 1.0
m = 1.0

def diffeq(state, t):
    phi1, w1, phi2, w2 = state
    deriv = np.zeros_like(state)

    deriv[0] = w1

    deriv[1] = -(g/l)*np.sin(phi1) - (k/m)*(phi1-phi2)

    deriv[2] = w2

    deriv[3] = -(g/l)*np.sin(phi2) + (k/m)*(phi1-phi2)

    return deriv

init_state = np.radians([45.0, 0.0, 10.0, 0.0]) # phi1, w1, phi2, w2
dt = 0.01
t = np.arange(0, 20, dt)
y = integrate.odeint(diffeq, init_state, t)

x1 = -2 + l*np.sin(y[:,0])
y1 = -np.cos(y[:,0])
x2 = 2 + l*np.sin(y[:,2])
y2 = -np.cos(y[:,2])

fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-2, 2)
ax.axis('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw = 2)

def animate(i):
    x = [-2, x1[i], x2[i], 2]
    y = [0, y1[i], y2[i], 0]
    line.set_data(x, y)
    return line

ani = animation.FuncAnimation(fig, animate, interval = 10)

for i in range(10):
    turtle01.forward(15)
    turtle01.penup()
    turtle01.forward(5)
    turtle01.pendown()

plt.show()