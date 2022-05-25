import time
import random
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(u,x,k):
    return (u[1], - k*u[1] - k*u[0] + np.cos(2*x))

y0 = [0, 0]
t = np.linspace(0,10)
for j in range(5):
    start = time.time()
    for i in range(10000):
        k = random.randint(1,10000)
        us = odeint(model, y0, t, args=(k,))
        ys = us[:,0]
    stop = time.time()
    print(stop-start)