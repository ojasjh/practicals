import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal

v = np.arange(700,820,20)
a = 16*0.052
b = 3*np.power(np.pi,3)*np.power(300,2)


i1 = np.array([1.1,1.1,1.1,1.1,1.1,1.1])
i2 = np.array([1.2,1.2,1.2,1.2,1.2,1.2])
i3 = np.array([1.3,1.3,1.3,1.3,1.3,1.3])
p1 = np.array([9.5,9.6,9.8,10.1,10.3,10.5])
q1 = np.array([14.2,14.3,14.5,14.6,15.1,15.3])

f1 = ((p1*q1)/(p1+q1))*(0.01)
if1 = np.power(1.1,2)*f1
slope1 = np.mean(np.gradient(if1,v))
em1 = (a/b)*(1/slope1)*np.power(10,14)
print("{:.2E}".format(Decimal(em1)))
plt.plot(v,if1)
plt.show()

p2 = np.array([5.5,5.6,5.8,5.9,6.1,6.3])
q2 = np.array([16,16.1,16.4,16.5,16.7,16.8])
f2 = ((p2*q2)/(p2+q2))*(0.01)
if2 = np.power(1.2,2)*f2
slope2 = np.mean(np.gradient(if2,v))
em2 = (a/b)*(1/slope2)*np.power(10,14)
print("{:.2E}".format(Decimal(em2)))
plt.plot(v,if2)
plt.show()

p3 = np.array([4.0,4.2,4.3,4.3,4.4,4.5])
q3 = np.array([16.1,15.5,16.1,16.3,16.6,16.0])
f3 = ((p3*q3)/(p3+q3))*(0.01)
if3 = np.power(1.3,2)*f3
slope3 = np.mean(np.gradient(if3,v))
em3 = (a/b)*(1/slope3)*np.power(10,14)
print("{:.2E}".format(Decimal(em3)))
plt.plot(v,if3)
plt.show()


df1 = pd.DataFrame({'i1':i1,'p1':p1,'q1':q1,'f1(cm)':f1,'if1':if1})
df2 = pd.DataFrame({'i2':i2,'p2':p2,'q2':q2,'f2(cm)':f2,'if1':if2})
df3 = pd.DataFrame({'i3':i3,'p3':p3,'q3':q3,'f3(cm)':f3,'if1':if3})

print(df1)
print(df2)
print(df3)
