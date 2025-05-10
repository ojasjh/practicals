import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


i = np.arange(0.0,1.6,0.1)
b = np.array([66,147,363,620,874,1126,1393,1652,1896,2160,2430,2670,2920,3150,3400,3610])
b0 = b-b[0]
slopeb = np.polyfit(i,b0,1)[0]

i = np.arange(0.0,1.6,0.1)
v1 = np.array([180.2,181.008,181.978,183.270,184.886,186.502,188.280,189.896,191.835,193.128,195.229,197.491,199.430,201.208,202.985,204.924])
v10 = v1-v1[0]
slope1 = np.polyfit(i,v10,1)[0]
print(slope1)
r1 = (slope1)*(1/slopeb)*(0.063/1.94)*np.power(10,8)
print(r1)

i = np.arange(0.0,1.6,0.1)
v2 = np.array([506.000,506.950,508.089,509.608,511.508,513.407,515.496,517.395,519.674,521.193,523.662,526.321,528.600,530.689,532.778,535.057])
v20 = v2-v2[0]
slope2 = np.polyfit(i,v20,1)[0]
r2 = (slope2)*(1/slopeb)*(0.063/2.28)*np.power(10,8)
print(r2)

i = np.arange(0.0,1.6,0.1)
v3 = np.array([377,380,383,385,389,393,395,399,403,406,411,414,418,422,426,429])
v30 = v3-v3[0]
slope3 = np.polyfit(i,v30,1)[0]
r3 = (slope3)*(1/slopeb)*(0.063/4)*np.power(10,8)
print(r3)

i = np.arange(0.0,1.6,0.1)
v4 = np.array([301.000,302.500,307.000,308.499,309.999,312.998,315.998,317.497,320.497,323.497,324.996,329.496,330.995,333.995,338.494,341.494])
v40 = v4-v4[0]
slope4 = np.polyfit(i,v40,1)[0]
r4 = (slope4)*(1/slopeb)*(0.063/3)*np.power(10,8)
print(r4)

plt.show()
plt.plot(i,v10)
plt.show()
plt.plot(i,v20)
plt.show()
plt.plot(i,v30)
plt.show()
plt.plot(i,v40)
plt.show()
plt.show()
