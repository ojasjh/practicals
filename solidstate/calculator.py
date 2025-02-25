import numpy as np


a = (3.65-0.50)*0.001
b = (0.026-0.0035)
slope = a/b
s = (4*np.pi*0.0000001*2*9.8*slope)/(1.63*0.0001)
print(s)
