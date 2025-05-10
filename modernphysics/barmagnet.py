import numpy as np
import matplotlib.pyplot as plt
import math as mt

i = np.array([0.2,0.2,0.2,0.2,0.2])
v = np.arange(6,36,6)

f1 = np.array([0.52, 1.22, 1.82, 2.65, 3.45])
t1 = np.array([78.5, 81.8, 83.2, 84.7, 85.2])

f2 = np.array([0.78, 1.58, 2.25, 2.85, 3.42])
t2 = np.array([84.8, 88.6, 90.3, 91.2, 91.3])

y1 = i+f1


y2 = f2-i


y = ((y1+y2)/2)*(mt.pow(10,(-2)))
t = (t1+t2)/2
vy = v*y
print(vy)
tangent = np.tan(np.deg2rad(t))
tangentsquare = np.power(tangent,2)
print(tangentsquare)


slope,c = np.polyfit(vy,tangentsquare,1)


em = (1/(0.025*0.14*np.power(0.32,2)*mt.pow(10,-3)*0.0002))*slope
print(em)


