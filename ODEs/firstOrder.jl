import Dates
using DifferentialEquations
f(u, p, t) = p * exp(-t)
t_span = (0.0, 10.0)
for j in 1:5
    local start = Dates.now()
    for i in 1:10000
        local localprob = ODEProblem(f, 0, t_span, rand(1:10000))
        local num_sol = solve(prob)
    end
    local stop = Dates.now()
    println(stop - start)
end