# singleton-type ist nicht veränderlich.
# Alle Objekte eines Singleton-Typs sind identisch, 
# d. h. ein Singleton-Typ hat nur eine Instanz.
# Ein wichtiger Singleton-Typ ist Nothing, 
# dessen einzige Instanz nothingist.

# 一个重要的单例类型是 Nothing：
# Nothing 是一个单例类型。
# 它的唯一实例就是 nothing。
# 常用来表示“没有值”或者“空占位符”。

struct NoFields end
NoFields() === NoFields()   # true
x = NoFields()
y = NoFields()
x === y 


struct MyOption end

function do_something(x::Int, opt::MyOption)
    println("Doing something with MyOption")
end

do_something(42, MyOption())  # benutzt das spezielle Verhalten

struct UseGPU end
struct UseCPU end

function run(model, ::UseGPU)
    println("Running on GPU")
end

function run(model, ::UseCPU)
    println("Running on CPU")
end

run("MyModel", UseGPU())   # Running on GPU
run("MyModel", UseCPU())   # Running on CPU

struct Fast end
struct Safe end

function compute(x::Int, ::Fast)
    println("Compute fast (ohne Sicherheit)")
end

function compute(x::Int, ::Safe)
    println("Compute safe (mit Sicherheit)")
end

compute(10, Fast())   # Compute fast
compute(10, Safe())   # Compute safe

# 3. Vergleich mit Nothing
# Nothing ist auch ein Singleton-Typ, seine Instanz ist nothing.
# Unterschied: Nothing ist allgemein als „kein Wert“ gedacht,
# während NoFields oder UseGPU/UseCPU etc. benutzerdefiniert 
# sind und besondere Semantik haben können.