#Das heißt: MyInt belegt 8 Bits (1 Byte), gehört zu Signed.
primitive type MyInt <: Signed 8 end
println(isprimitivetype(MyInt)) # true
x = reinterpret(MyInt, UInt8(5));
y = reinterpret(UInt8, x)
print(y)