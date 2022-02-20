import numpy as np
import matplotlib.pyplot as plt

class particle:
    def __init__(this, x, p):
        this.x = x
        this.p = p

particles = []

# Constants

alpha = 4
beta = 1

# Friction

gamma = 0.1

# sinusoidal outward force

A = 0
omega = 2

def force(x, p, t):
    return alpha * x - beta * x**3 - gamma * p - A * np.sin(omega * t)

width = 60

density = 0.5

for i in np.arange(-width, width, density):
    for j in np.arange(-width, width, density):
        particles.append(particle(i, j))

pos = []

dt = 0.01
t = 0

end_t = 100

final_pos = []

while t < end_t:
    for ob in particles:
        f = force(ob.x, ob.p, t)
        ob.p += f * dt
        ob.x += ob.p * dt
        # pos.append(ob.x)
    t += dt

for ob in particles:
    final_pos.append(ob.x)

plt.figure(figsize = (10, 10))
plt.imshow(np.array(final_pos).reshape(240, 240).transpose(), cmap = 'viridis')
plt.axis('off')
plt.show()
