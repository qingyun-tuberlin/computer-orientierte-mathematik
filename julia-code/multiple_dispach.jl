# Das zentrale Paradigma von Julia ist 
# die mehrfache Verteilung (Multiple Dispatch).
# Das bedeutet, dass eine Funktion mehrere Methoden haben kann, 
# die anahnd der Typen ihrer Argumente unterschieden werden.
# Julia 的核心范式是 多重分派（Multiple Dispatch）。
# 这意味着：一个函数可以有多个方法，Julia 会根据参数的类型来决定调用哪一个方法。
# Julia 不像 Python 只有单一函数体，而是允许给同一个函数名字定义多个版本（方法）。
# Julia 的运行时会根据参数类型，自动选择最匹配的方法执行，这就是 Multiple Dispatch。

function foo(x::Int)
    println("Int")
end

function foo(x::Float64)
    println("Float64")
end

foo(1)       # 输出 Int
foo(1.0)     # 输出 Float64
# foo("Hallo") # 报错: 没有 foo(::String) 方法