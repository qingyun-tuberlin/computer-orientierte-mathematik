
# Innerhalb der struct-Deklaration 
# steht der Standardkonstruktor als Funktion zur Verfügung.
struct Teacher
    matrikelnummer::Int
    name::String
    kommtzurübung::Bool

    # This is an inner constructor
    Teacher(m::Int, n::AbstractString, k::Bool) =
        new(m, uppercase(String(n)), k)
end

Base.show(io::IO, t::Teacher) =
    print(io, "Teacher($(t.matrikelnummer), \"$(t.name)\", $(t.kommtzurübung))")

y = Teacher(1234, "Julia", true)
println(y)
println(y.kommtzurübung)

# Teacher(1234, "JULIA", true)
# true



# inner constructor
# also take abstracut_type.jl into consideration
# Normally, you’d call Teacher(...) 
# and Julia would automatically build the struct for you.
# Inside an inner constructor, you must explicitly call new(...).
# new is special: it creates an instance of 
# the current type (IntegerModuloThree here).
# Without new, if you wrote IntegerModuloThree(x) inside, 
# you’d just call the constructor again → infinite recursion.