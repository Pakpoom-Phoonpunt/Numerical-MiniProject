import random
import timeit

def secant(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            # print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

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
    a0 = round(random.uniform(-1000.0, 1000.0), 5) ; a1 = round(random.uniform(-1000.0, 1000.0), 5)
    a2 = round(random.uniform(-1000.0, 1000.0), 5) ; a3 = round(random.uniform(-1000.0, 1000.0), 5)
    a4 = round(random.uniform(-1000.0, 1000.0), 5) ; a5 = round(random.uniform(-1000.0, 1000.0), 5)
    a6 = round(random.uniform(-1000.0, 1000.0), 5) ; a7 = round(random.uniform(-1000.0, 1000.0), 5)
    a8 = round(random.uniform(-1000.0, 1000.0), 5) ; a9 = round(random.uniform(-1000.0, 1000.0), 5)
    # gx = lambda x: -a10*(x**10) + a9*(x**9) + a8*(x**8) + a7*(x**7) + a6*(x**6) + a5*(x**5) + a4*(x**4) + a3*(x**3) + a2*(x**2) + a1*(x**1) + a0*(x**0)
    gx = lambda x: a9*(x**9) + a8*(x**8) + a7*(x**7) + a6*(x**6) + a5*(x**5) + a4*(x**4) + a3*(x**3) + a2*(x**2) + a1*(x**1) + a0*(x**0)
    fval = 1
    sval = anotherVal(gx,fval,-1)
    ans = secant(gx,fval,sval,1000)
stop = timeit.default_timer()
print('Time: ', stop - start)  
