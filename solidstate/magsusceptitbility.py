import numpy as np
import matplotlib.pyplot as plt

i = np.arange(0,2.6,0.2)
bg = np.array([200,322,444,582,717,853,993,1124,1247,1382,1503,1630,1745])
bt = bg/10000
bts = np.power(bt,2)
w = np.array([90.9555, 91.0236, 91.1366, 91.3109, 91.4795, 
                  91.8070, 92.1346, 92.5082, 92.9095, 93.3568, 
                  93.8730, 94.3567, 94.7964])

ow = 90.9

dw = (w-ow)*(0.001)
slo = np.gradient(dw,bts)
slope = np.mean(slo)
print(slope)
ms =((2*9.8*4*np.pi*0.0000001)/(0.000158))*slope
print(ms)
plt.plot(bts,dw)
plt.show()
