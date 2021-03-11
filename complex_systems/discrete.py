from pylab import *

a = 1.1
b = 1

def initialize():
    global x, result, t, timesteps
    x = 1
    result = [x]
    t = 0
    timesteps = [t]

def observe():
    global x, result, t, timesteps
    result.append(x)
    timesteps.append(t)

def update():
    global x, result, t, timtesteps
    x = a * x + b
    t = t + 0.1


initialize()
while t < 10.:
    update()
    observe()

plot(timesteps, result)
show()