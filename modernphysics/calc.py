import numpy as np
from decimal import Decimal

a = 16*0.052
b = 3*np.power(np.pi,3)*np.power(300,2)
c = 1.76*(10^11)

slope = (0.0595-0.0545)/(793.86-706.6)

em = (a/b)*(1/slope)*np.power(10,14)
print("{:.2E}".format(Decimal(em)))


