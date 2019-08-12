import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-2,2,50)
y1=2*x+1
y2=x**2
plt.figure()
plt.plot(x,y1,linewidth='5.0')
plt.plot(x,y2,color='red',linewidth=5.0,linestyle='--')
plt.xlabel('Xxx')
plt.ylabel('Yyy')
plt.show()