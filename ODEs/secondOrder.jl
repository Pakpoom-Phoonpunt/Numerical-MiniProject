import Dates
using DifferentialEquations

function ode_func(du, u, p, t)
    - p * du - p * u + cos(2.0*t)
end
global t_span = (0.0, 10.0)
start = Dates.now()
# for i in 1:10000
prob = SecondOrderODEProblem(ode_func, 0, 0, t_span, rand(1:10000))
num_sol = solve(prob)
# end
stop = Dates.now()
print(stop - start)