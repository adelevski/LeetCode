from pylab import *


x0 = 0
x1 = 1
xresult = [x]
yresult = [y]

def observe(x, y):
    xresult.append(x)
    yresult.append(y)

def update(x, y):
    newX = x + y
    newY = b * x + y
    x, y = newX, newY
    return x, y

for t in range(30):
    x, y = update(x, y)
    observe(x, y)

fig1 = plot(xresult, 'b-')
fig1 = plot(yresult, 'g--')
show()

fig2 = plot(xresult, yresult)
show()