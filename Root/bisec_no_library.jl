using Roots
import Dates
using Distributions

function bisection(f , x1, x2 , N)
    if(f(x1)*f(x2)>=0)
        return Nothing # Bisection method fails.
    end
    a_n = x1 ; b_n = x2
    for j in 1:N
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0
            a_n = a_n; b_n = m_n
        elseif  f(b_n)*f_m_n < 0
            a_n = m_n; b_n = b_n
        elseif f_m_n == 0
            # println("Found exact solution.")
            return m_n
        else 
            return None
        end
    end
    return (a_n + b_n)/2
end

function anotherVal(f,a,b) 
    step = 1
    while ((f(a)*f(b)) >= 0)
        if ((f(a)*f(b+step)) < 0)
            return (b+step)
        elseif ((f(a)*f(b-step)) < 0)
            return (b-step)
        end
        step = step +1
    end
    return (b)
end

start = Dates.now()
for i in 1:10000
    a0 = round(rand(Uniform(-1000.0,1000.0)) ,digits = 2) ; a1 = round(rand(Uniform(-1000.0,1000.0)) ,digits = 2)
    a2 = round(rand(Uniform(-1000.0,1000.0)) ,digits = 2) ; a3 = round(rand(Uniform(-1000.0,1000.0)) ,digits = 2) 
    a4 = round(rand(Uniform(-1000.0,1000.0)) ,digits = 2) ; a5 = round(rand(Uniform(-1000.0,1000.0)) ,digits = 2)
    a6 = round(rand(Uniform(-1000.0,1000.0)) ,digits = 2) ; a7 = round(rand(Uniform(-1000.0,1000.0)) ,digits = 2)
    a8 = round(rand(Uniform(-1000.0,1000.0)) ,digits = 2) ; a9 = round(rand(Uniform(-1000.0,1000.0)) ,digits = 2)
    g(x) =  a9*(x^9) + a8*(x^8) + a7*(x^7) + a6*(x^6) + a5*(x^5) + a4*(x^4) + a3*(x^3) + a2*(x^2) + a1*(x^1) + a0*(x^0)
    firstval = 1
    secval = anotherVal(g,firstval,-1)
    ans = bisection(g , firstval , secval , 1000)
end
stop = Dates.now()
println("Time :" , stop-start)
