import numpy
import matplotlib.pyplot as plt
from drawnow import *

def makeFig(): #Create a function that makes our desired plot
    plt.ylim(80,90)                                 #Set y min and max values
    plt.title('Respuesta al Escalon')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Voltaje')                           #Set ylabels
    plt.plot(tempF, 'ro-', label='Degrees F')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    #plt2=plt.twinx()                                #Create a second y axis
    plt.ylim(93450,93525)                           #Set limits of second y axis- adjust to readings you are getting
    plt2.plot(pressure, 'b^-', label='Pressure (Pa)') #plot pressure data
    plt2.set_ylabel('Pressrue (Pa)')                    #label second y axis
    plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                  #plot the legend







##import numpy as np
##import matplotlib.pyplot as plt
##import matplotlib.animation as animation
##
##fig, ax = plt.subplots()
##
##x = np.arange(0, 2*np.pi, 0.01)        # x-array
##line, = ax.plot(x, np.sin(x))
##
##def animate(i):
##    line.set_ydata(np.sin(x+i/10.0))  # update the data
##    return line,
##
###Init only required for blitting to give a clean slate.
##def init():
##    line.set_ydata(np.ma.array(x, mask=True))
##    return line,
##
##ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
##    interval=25, blit=True)
##plt.show()
