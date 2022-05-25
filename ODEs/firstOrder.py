import time
import random
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(u,x,k):
    return k * np.exp(-x)

y0 = 0
t = np.linspace(0,10)
for j in range(5):
    start = time.time()
    for i in range(10000):
        k = random.randint(1,10000)
        u = odeint(model, y0, t, args=(k,))
    stop = time.time()
    print(stop-start)