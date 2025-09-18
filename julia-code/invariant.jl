struct Point{T}
    x::T
    y::T
end

println(Float16 <: Real) # true
println(Point{Float64} <: Point{Real}) # false

# Point{Real} ist ein konkreter Typ.
# Erinnere: Konkrete Typen haben niemals Subtypen.
# Man sagt, Typparameter zusammengesetzter Typen sind invariant


println(Point{Float64} <: Point{<:Real}) #所有 T <: Real