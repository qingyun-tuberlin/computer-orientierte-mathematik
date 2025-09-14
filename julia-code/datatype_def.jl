# Content:
# 1) define your own data structure
# 2) define your own function
# 3）primitive data type

# type annotation by using ::
fruit :: String = "apple"
println(fruit)


# define your own data structure
# struct is not mutable
struct Point
    x::Int
    y::Int
end

p::Point = Point(1,2)
println(p.x)


println("mutable makes struct mutable\n")
mutable struct Car
    height::Int
    length::Int
end
c::Car = Car(10,3)
println(c.height)
c.height = 50
println(c.height)


print("define your own function\n")
# return is optional
# Das Ergenis des letzten Ausdrucks wird automatisch zurückgegeben.
function f(x,y)
    return x+y
end
println(f(2,3))


# common data type
# 整数 (Integers)
# 有符号 (Signed)
# Int8 （-128 … 127）
# Int16
# Int32
# Int64 （通常就是 Int，依赖系统位数）
# Int128

# 无符号 (Unsigned)
# UInt8 （0 … 255，常用于字节）
# UInt16
# UInt32
# UInt64 （通常就是 UInt）
# UInt128

# 浮点数 (Floating-point)
# Float16
# Float32
# Float64 （默认浮点类型）
# 大数 (Arbitrary precision)
# BigInt （任意精度整数）
# BigFloat （任意精度浮点）

# 🔹 布尔与字符
# Bool （只有 true 和 false）
# Char （单个 Unicode 字符，比如 'a', '中'）

# 🔹 字符串与符号
# String （UTF-8 字符串，常用 "hello"）
# SubString （从 String 派生的切片）
# Symbol （符号，像 :name，用于元编程、字典键）

# 🔹 特殊类型
# Nothing （只有一个值 nothing，类似 Python None）
# Missing （缺失值，用于统计/数据分析）
# Nothing 和 Missing 都是单例类型。

# 🔹 复数与有理数
# Complex{T} （复数，如 1 + 2im）
# Rational{T} （有理数，如 3//4）

# 🔹 集合相关
# 虽然不是“原始类型”，但也算基础容器：
# Tuple （不可变序列，类型固定，比如 (1,"a")）
# NamedTuple （带名字的元组，像 (x=1, y=2)）
# Array{T} （多维数组，最常用的数据结构）
# Dict{K,V} （字典/哈希映射）