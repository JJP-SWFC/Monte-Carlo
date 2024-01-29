# Tested and working in Python 3.11

import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import warnings

# Update the number of points

def update(val):
    newx = []
    newy = []
    newcx = []
    newcy = []
    for _ in range(val):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 <=1:
            newcx.append(x)
            newcy.append(y)
        else:
            newx.append(x)
            newy.append(y)
    svals[0].set_xdata(newx)
    svals[0].set_ydata(newy)
    cvals[0].set_xdata(newcx)
    cvals[0].set_ydata(newcy)
    cv = (4*len(newcx)/(len(newcx)+len(newx)))
    ax.title.set_text(f"Estimated value of pi: {cv}")

# Update the size of the points

def updatemarker(val):
    svals[0].set_markersize(val)
    cvals[0].set_markersize(val)
    plt.draw()
    
warnings.filterwarnings("ignore")

pointlimit = 1000

# Initialize the values

xvals = []
yvals = []
xcvals = []
ycvals = []
interval = 10

# Create the starting points, assign them to the "cvals" if they're less than 1

for _ in range(interval**2):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <=1:
        xcvals.append(x)
        ycvals.append(y)
    else:
        xvals.append(x)
        yvals.append(y)

# Draw the figures
circ = plt.Circle((0,0),1,fill=False)
fig = plt.figure()
ax = fig.gca()
ax.set_aspect(1)
ax.add_artist(circ)

# Draw the points

svals = ax.plot(xvals,yvals,"ro",marker="o",markersize=1,color="green")
cvals = ax.plot(xcvals,ycvals,"ro",marker="o",markersize=1,color="blue")
axdots = fig.add_axes([0.25, 0.05, 0.65, 0.03])
axmar = fig.add_axes([0.25,0.01,0.65,0.03])
ax.set_xticks([])
ax.set_yticks([])

# Add the sliders

freq_slider = Slider(
    ax=axdots,
    label='Dots',
    valmin=10,
    valmax=1000,
    valinit=10,
    valstep=1
)
mark_slider = Slider(
    ax=axmar,
    label = "Marker Size",
    valmin = 1,
    valmax = 10,
    valinit = 1,
    valstep = 0.01
)

# Calculate the value approximated    
cv = 4*len(xcvals)/(len(xcvals)+len(xvals))
ax.title.set_text(f"Estimated value of pi: {cv}")


freq_slider.on_changed(update)
mark_slider.on_changed(updatemarker)

plt.show()
