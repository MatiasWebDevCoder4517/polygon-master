<<<<<<< HEAD
POLYGON MASTER SIMPLE PROJECT
=======
### Project Solution: Goal 1

We need to create a Polygon class with the following properties:

- number of vertices `n` -> passed to the initializer
- circumradius `R` -> passed to the initializer
- number of edges
- number of sides
- interior angle (in degrees)
- side length
- apothem
- surface area
- perimeter
- supports equality based on number of vertices and circumradius
- supports `>` based on number of vertices

-> Apart from number of edges / vertices (`n`) and circumradius (`R`), all the other properties are computed properties.
-> We will make our Polygon immutable (by basically making `n` and `R` "private" variables - by convention using the `_` prefix).

####

To do that we are going to use the fact that we have pre-calculated what some results should evaluate to, and we'll make sure they match.

For example:

- the side length of a square whose circumradius is `1`, should be `sqrt(2)`
- the area of a square whose circumradius is `1`, should be `2`

####

As you should already be aware, comparing floats for equality is not something we should do.

Instead, we are going to use the math module's `is_close` function with relative and absolute tolerances set to `0.001`. (I cover this in Part 1 of this series, but you can also see the documentation here:

- https://docs.python.org/3/library/math.html
- https://www.python.org/dev/peps/pep-0485/

####

-> We need to add support for equality and ordering based on number of vertices.
-> We'll do that by implementing the `__eq__` and `__gt__` methods.

####

By the way, did you notice that we spent at the same, if not more, amount of time **testing** our code as we did it **writing** it?
In practice, that is often how that goes - you should always test your code - you obviously cannot test every case, but you shoudl always try to test everything at least once, and then also cover edge cases if there are any.
You should also try to ensure, within reason, that all the code you wrote is tested (i.e. executed, or _exercised_) during your tests - this is called **test coverage**, or sometimes **code coverage**.

### Project Solution: Goal 2

Now we need to create a sequence type that will return these Polygons, starting with 3 vertices, up to (and including) a polygon of `m` sides.

Our sequence type will need to implement:

- a `__len__` method
- a `__getitem__` method
- a method that identifies the polygon with largest area to perimeter ratio: let's call it `max_efficiency_polygon` - note that the Polygon class does not have an `efficiency` method, so we'll have to calculate it outside of the Polygon class.

### Project Solution: Goal 3



>>>>>>> 30c79ab (Implementing bases and basics)
