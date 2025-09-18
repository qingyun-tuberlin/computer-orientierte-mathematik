# Union{T1, T2} ist Supertyp von T1
# und T2. Dieser liegt außerhalb der
# Arboreszenz der deklarierten Typen.
# 𝐴 isa𝐵 ∶⟺ typeof(𝐴) <∶ 𝐵

IntOrComplex = Union{Integer, Complex}
subtypes(IntOrComplex)
println(Complex <: IntOrComplex)
println(2 isa IntOrComplex)
println(IntOrComplex <: Number)
println(2.0 isa IntOrComplex)

# Häufig genutzt wird Union{T, Nothing} für einen beliebigen Typ T.
# Der Typ Union{} hat keine Instanzen und ist Subtyp jedes Typs.