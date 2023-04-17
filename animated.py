import numpy as np 
import matplotlib.pyplot as plt 

def on_close(event):
	global exit
	exit = True

t= np.linspace(0,4*np.pi,100)
y= np.sin(t)
y2=np.cos(t)
y3=np.sin(1/2*t)
y4=np.cos(1/2*t)

def inicio():
	plt.rcParams['figure.figsize'] = [5, 2]
	plt.connect('close_event', on_close)

def close():
	global exit
	exit = False

def grafica(a,b,b2):
	inicio()
	close()
	for i in range(len(t)):
		if exit:
			break
		plt.plot(a[i],b[i], color='blue', marker='+')
		plt.plot(a[i],b2[i], color='navy', marker='.')
		plt.grid(color='silver')
		plt.xlim((0,4*np.pi))
		plt.ylim((-2,2))
		plt.pause(0.05)
		plt.show(block=False)
	plt.close()

grafica(t,y,y2)
grafica(t,y3,y4)