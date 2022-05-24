import random
import timeit
from scipy import optimize
def anotherVal(f,a,b):
    step = 1
    while(f(a)*f(b) >= 0):
        if(f(a)*f(b+step) < 0):
            return (b+step)
        elif(f(a)*f(b-step) < 0):
            return (b-step)
        step+=1
    return (b)
start = timeit.default_timer()
for i in range(3000):
    a0 = round(random.uniform(-1000.0, 1000.0), 2) ; a1 = round(random.uniform(-1000.0, 1000.0), 2)
    a2 = round(random.uniform(-1000.0, 1000.0), 2) ; a3 = round(random.uniform(-1000.0, 1000.0), 2)
    a4 = round(random.uniform(-1000.0, 1000.0), 2) ; a5 = round(random.uniform(-1000.0, 1000.0), 2)
    a6 = round(random.uniform(-1000.0, 1000.0), 2) ; a7 = round(random.uniform(-1000.0, 1000.0), 2)
    a8 = round(random.uniform(-1000.0, 1000.0), 2) ; a9 = round(random.uniform(-1000.0, 1000.0), 2)
    gx = lambda x: a9*(x**9) + a8*(x**8) + a7*(x**7) + a6*(x**6) + a5*(x**5) + a4*(x**4) + a3*(x**3) + a2*(x**2) + a1*(x**1) + a0*(x**0)
    fval = 1.0
    sval = anotherVal(gx,fval,-1.0)
    ans = optimize.root_scalar(gx,x0=fval,x1=sval,maxiter=1000  , method='secant')
    #print(gx(ans.root))
stop = timeit.default_timer()
print('Time: ', stop - start)  
