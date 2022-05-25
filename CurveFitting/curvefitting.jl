using CurveFit
using BenchmarkTools
using Plots; gr()

function PolyFit(x, y, degree, nx)
    coef = curve_fit(Polynomial, x, y, degree)
    y0b = coef.(nx)
    return y0b
end

xdata = [0.0, 1.0, 2.0, 2.5, 3.0]
ydata = [2.9, 3.7, 4.1, 4.4, 5.0]

nx = LinRange(minimum(xdata),maximum(xdata), 100)

@benchmark PolyFit($xdata, $ydata, $3, $nx)