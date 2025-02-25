import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

i = np.arange(0,2.6,0.2)
bg = np.array([200,322,444,582,717,853,993,1124,1247,1382,1503,1630,1745])
bt = bg/10000
bts = np.power(bt,2)

w = np.array([94.2,94.312,94.418,94.576,94.807,95.110,95.454,95.819,96.214,96.707,97.216,97.753,98.184])
ow = 94.2

dw = (w-ow)
slopearr = np.gradient(dw*0.001,bts)
slope = np.mean(slopearr)
print(slope)


df = pd.DataFrame({'i':i,'bg':bg,'bt':bt,'bts':bts,'w':w,'dw':dw})
df.to_csv('weight2.csv', sep='\t', encoding='utf-8', index=False, header=True)
ms = ((2*9.8*4*np.pi*0.0000001)/0.000167)*slope
print(ms)
plt.plot(bts,dw)
plt.show()
