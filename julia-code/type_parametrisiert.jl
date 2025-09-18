struct Point{T}
    x::T
    y::T
end

# Bool is subtype of Integer
q = Point{Integer}(1, true)

print(Point{Float64} <: Point{Real}) 
# false, Konkrete Typen haben niemals Subtypen.


# Meta type（元类型） 指的是“类型对象的类型”。
# 在 Julia 里，所有具体类型（Int, Float64, Point{Int} …）本身都是 DataType 的实例。
# 所以 DataType 就是这些类型的 元类型。