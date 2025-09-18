
abstract type IntegerModuloM <: Number end

struct IntegerModuloThree <: IntegerModuloM
    # you can also call it with other name
    # like value :: Int
    representative::Int

    # this is a custom inner constructor
    function IntegerModuloThree(x)
        if x > 2
            error("Zu groß!")
        else
            new(x)
        end
    end
end

function add(a::IntegerModuloM, b::IntegerModuloM)
    if typeof(a) != typeof(b)
        error("Nur gleiche Modulo-Klassen addierbar")
    end
    m = 3   # hier z. B. für Modulo 3
    return IntegerModuloThree((a.representative + b.representative) % m)
end

x = IntegerModuloThree(1)
y = IntegerModuloThree(2)
result = add(x, y)   # => 0 (weil 1+2 mod 3 = 0)
print(result.representative)


# 1. 什么是抽象类型？
# 抽象类型（abstract type）在 Julia 中相当于一个 父类 或 
# 类型层次结构中的标签。
# 它 不能直接实例化，只能用来约束子类型。
# 好处是：你可以写“泛化”的函数，针对整个类型族。
# abstract type IntegerModuloM <: Number end
# 意思是：所有模运算整数类型都是 Number 的一种。

# 2. 子类型
# IntegerModuloThree 是一个具体类型，可以存储数据。
# 它继承自 IntegerModuloM，也就是属于这个“模整数家族”。
# 构造函数保证只允许 0,1,2

# 以后可以定义很多不同的模整数（IntegerModuloFive, IntegerModuloSeven…）。
# 它们全都属于 IntegerModuloM。
# 所以可以写一个函数：f(a::IntegerModuloM, b::IntegerModuloM)，
# 适用于所有这些子类型。
