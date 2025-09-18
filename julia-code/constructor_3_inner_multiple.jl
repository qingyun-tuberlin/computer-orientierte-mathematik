struct Point
    x::Int
    y::Int
    function Point(x::Int, y::Int)
        if x < 0 || y < 0
            error("Coordinates must be nonnegative")
        end
        new(x, y)
    end
    # Another inner constructor: default y = 0
    Point(x::Int) = new(x, 0)
end

p1 = Point(3, 4)   # explicit
p2 = Point(5)      # uses default y=0
