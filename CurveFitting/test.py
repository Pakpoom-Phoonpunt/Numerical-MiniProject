import numpy as np
import time


x = np.array([0.0, 1.0, 2.0, 2.5, 3.0])
y = np.array([2.9, 3.7, 4.1, 4.4, 5.0])
nx = np.linspace(min(x), max(x), 100)

run_time = []

def test(x, y, degree):
    answer = np.polyfit(x, y, degree)
    return answer

sample = 10000
for i in range(sample):
    start = time.time()
    coef = test(x, y , 3)
    ny = np.polyval(coef, nx)
    end = time.time()
    run_time.append(end-start)

print("Average Time: ",sum(run_time)/len(run_time))