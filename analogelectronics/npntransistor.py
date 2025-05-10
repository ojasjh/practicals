import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


vb = np.arange(0.45,0.95,0.05)
v0 = np.array([0.5,1.4,7.6,67,231.1,492,786,1109,1478,1872])
v1 = np.array([0,0.1,1.4,9.4,138,461,762,1061,1435,1821])
v2 = np.array([0,0.1,1.5,9.3,100,411,755,1055,1426,1817])
v3 = np.array([0,0.1,1.4,9.2,96.3,401.5,698,1043,1396,1802])

vc0 = np.arange(0,0.2,0.05)
vc1 = np.arange(0.2,1.2,0.1)
vc = np.append(vc0,vc1)

i20 = np.array([0.37,0.78,2.46,2.92,3.10,3.48,3.49,3.51,3.52,3.53,3.54,3.55,3.56,3.56])
i30 = np.array([0.50,1,3.57,4.81,5.03,5.28,5.29,5.30,5.31,5.32,5.33,5.34,5.34,5.34])
i10 = np.array([0.20,0.23,1.02,1.56,1.59,1.6,1.63,1.65,1.66,1.67,1.68,1.69,1.72,1.72])
plt.plot(vc,i20)
plt.plot(vc,i30)
plt.plot(vc,i10)
df = pd.DataFrame({'vc':vc,'i10':i10,'i20':i20,'i30':i30})
print(df)
plt.show()
plt.plot(vb,v0)
plt.plot(vb,v1)
plt.plot(vb,v2)
plt.plot(vb,v3)
plt.show()
