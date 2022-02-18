GlowScript 3.1 VPython

grep = graph(fast = True)
f1 = gcurve(color = color.red)
f2 = gdots(color = color.blue, radius = 1)

# 0.01
d_scale = 0.01
v_scale = 0    # Range of velocities to be given to the particles initially
n_particles = 5000

# yax = cylinder(radius = 0.02, length = 5, axis = vec(0, 1, 0), pos = vec(0, -2.5, 0))

bodies = []
for i in range(n_particles):
  if i < 2:
    body = simple_sphere(pos = vec(d_scale * (1 * random() - 0.5), 0, 0), radius = 0.02, emissive = True, make_trail = False)
  else:
    body = simple_sphere(pos = vec(d_scale * (1 * random() - 0.5), 0, 0), radius = 0.02, emissive = True)
  bodies.append(body)


# body.px = vec(10, 0, 0)
# body.mass = 1
# x_dot = 0000000000

for i in range(len(bodies)):
  bodies[i].vel = vec(v_scale * (random() - 0.5), 0, 0)
  if bodies[i].pos.x > 0:
    bodies[i].color = vec(0, 1, 0)
  else:
    bodies[i].color = vec(1, 0, 0)

x_ddot = 0

t = 0
dt = 0.02
# 0.1
alpha = 0.1
# 4
beta = 4
# 1
gamma = 1
# 2
omega = 2
# 1
delta = 1

# print(scene.camera.pos)
scene.camera.pos = vec(0, 0, 1.3)
scene.camera.autoscale = False

def duffing(x, x_dot, t):
  return beta * x - gamma * x**3 - alpha * x_dot - delta * sin(omega * t)
  
def potential(x):
  return -beta * x**2 * 0.5 + gamma * 0.25 * x**4

count = 0

while True:
  rate(300)
  for body in bodies:
    f = duffing(body.pos.x, body.vel.x, t)
    body.vel.x += f * dt
    body.pos.x += body.vel.x * dt
    # body.pos.y = potential(body.pos.x) - (body.vel.x) * 0.2  
    body.pos.y = body.vel.x * 0.3
    # body.pos.z = -body.vel.x * body.pos.x * 0.1
  # f2.plot(t, bodies[10].pos.x)
  # if count % 10 == 0:
    # f2.plot(bodies[4].pos.x, bodies[4].vel.x)
    # body.color = vec(abs(body.pos.x) * 0.2, body.pos.y * 0.2, (abs(body.pos.x) + body.pos.y) * 0.1)
  t += dt
  count += 1
  if count < 1500:
    dt = 0
  else:
    dt = 0.02
  # if count % 500 == 0:
  #   print(t)
