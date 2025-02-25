import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

i = np.arange(0,2.6,0.2)
bg = np.array([200,322,444,582,717,853,993,1124,1247,1382,1503,1630,1745])
bt = bg/10000
bts = np.power(bt,2)
w = np.array([90.9567,91.0263,91.1418,91.3200,91.4923,91.8270,92.1618,92.5437,92.9538,93.4110,93.9386,94.4329,94.8823])

ow = 90.9

dw = (w-ow)*(0.001)
slo = np.gradient(dw,bts)
slope = np.mean(slo)
df = pd.DataFrame({'i':i,'bg':bg,'bt':bt,'bts':bts,'w':w,'dw':dw})
df.to_csv('weight1.csv', sep='\t', encoding='utf-8', index=False, header=True)
print(slope)
ms =((2*9.8*4*np.pi*0.0000001)/(0.000158))*slope
print(ms)
plt.plot(bts,dw)
plt.show()
