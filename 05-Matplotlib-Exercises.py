# Follow the instructions to recreate the plots using this data:
#
# ## Data

import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2

# ** Import matplotlib.pyplot as plt and set %matplotlib inline if you are using the jupyter notebook. What command do you use if you aren't using the jupyter notebook?**

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# ## Exercise 1
# ** Follow along with these steps: **
# * ** Create a figure object called fig using plt.figure() **
# * ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
# * ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Title')

# ## Exercise 2
# ** Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**

fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,.5,.2,.2])

ax1.plot(x,y,color='red')
ax2.plot(x,y,color='red')

# ** Now plot (x,y) on both axes. And call your figure object to show it.**

# ## Exercise 3
# ** Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**

fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([.2,.5,.4,.4])

ax1.plot(x,z)
ax1.set_xlabel('X')
ax1.set_ylabel('Z')

ax2.plot(x,y)
ax2.set_title('zoom')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])

# ** Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:**

# ## Exercise 4
#
# ** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**

fig,axes = plt.subplots(1,2,figsize=(12,2))

axes[0].plot(x,y,color='blue',lw=3, ls='-')
axes[1].plot(x,z,color='red',lw=3, ls='--')


# ** Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style**
