struct StudentIn
    matrikelnummer::Int
    name:: String
    kommtzurübung::Bool
end

x = StudentIn(1234, "Julia", true)
println(x)
println(x.kommtzurübung)
print(typeof(x))

# StudentIn(1234, "Julia", true)
# true