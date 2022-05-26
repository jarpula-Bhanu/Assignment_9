import matplotlib.pyplot as plt
import numpy as np 

x= np.linspace(-10,10,100)
y = x**2

plt.axhline(y = 0, color = 'r', linestyle = '-')
plt.axvline(x = 0, color = 'r', linestyle = '-')
plt.plot(0,50,'ko')
plt.plot(7,50,'ko')
plt.plot(-7,50,'ko')
plt.plot(7,0,'ko')
plt.plot(-7,0,'ko')
plt.annotate('$y$',(0.5,50),size=12,color='red')
plt.annotate('$x^2$',(9.5,80),size=12,color='red')
plt.annotate('$0$',(0,0),size=12,color='red')
plt.annotate('$-\sqrt{y}$',(-7,0),size=12,color='red')
plt.annotate('$\sqrt{y}$',(7,0),size=12,color='red')

plt.plot(x,y)
plt.show()