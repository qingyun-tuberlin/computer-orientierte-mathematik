struct Point 
    x:: Real
    y:: Real
end

p1 = Point(2.0,0)
p2 = Point(2.0,0)
p3 = Point(2.0,0.0)
println("p1===p2: ",p1===p2 )
println("p1===p3: ",p1===p3 )

mutable struct Fruit
    height::Real
    weight::Real
end

f1 = Fruit(2.0,0)
f2 = Fruit(2.0,0)
f3 = f1
println("f1===f2: ",f1===f2 )
println("f1===f3: ",f1===f3 )


# Gleichheit bei struct-Datentypen
#     Bei unveränderlichen Datentypen
#     ist a === b genau dann wahr,
#     wenn alle gespeicherten Werte
#     identisch (=== ) sind.

#     Bei veränderlichen Datentypen ist
#     a === b genau dann wahr, wenn
#     beide auf dasselbe Objekt
#     verweisen (d. h. dieselbe
#     Speicheradresse enthalten).

#     Standardmäßig greifen== und
#     isequal auf=== zurück. Man
#     kann diese Operatoren aber
#     überschreiben.