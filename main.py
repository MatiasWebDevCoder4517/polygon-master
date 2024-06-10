## Goal 1

from math import cos, isclose, sin, pi, sqrt

STRAIGHT_DEGREE = 180
INTERIOR_ANGLE = 60
RECT_ANGLE = 90


class Polygon:
    def __init__(self, n, radious):
        if n < 3:
            raise ValueError("Polygon must have at least 3 vertices.")
        self._n = n
        self._radious = radious

    def __repr__(self):
        return f"Polygon(n={self._n}, radious={self._radious})"

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circum_radious(self):
        return self._radious

    @property
    def interior_angle(self):
        return (self._n - 2) * STRAIGHT_DEGREE / self._n

    @property
    def side_length(self):
        return 2 * self._radious * sin(pi / self._n)

    @property
    def apothem(self):
        return self._radious * cos(pi / self._n)

    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem

    @property
    def perimeter(self):
        return self._n * self.side_length

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                self.count_edges == other.count_edges
                and self.circum_radious == other.circum_radious
            )
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented


## Testing with asserts

##def test_polygon():
##    n = 3
##    radious = 2
##    p = Polygon(n, radious)
##    assert str(p) == f"Polygon(n={n}, radious={radious}), actual: {str(p)}"
##    assert p.count_vertices == n, f"actual: {p.count_vertices}, expected: {n}"
##    assert p.count_edges == n
##    assert p.circum_radious == radious
##    assert p.INTERIOR_ANGLE == INTERIOR_ANGLE


##def test_polygon():
##    abs_tol = 0.001
##    rel_tol = 0.001
##
##    n = 3
##    radious = 1
##    p = Polygon(n, radious)
##    assert str(p) == "Polygon(n=3, radious=1)", f"actual: {str(p)}"
##    assert p.count_vertices == n, f"actual: {p.count_vertices}," f" expected: {n}"
##    assert p.count_edges == n, f"actual: {p.count_edges}, expected: {n}"
##    assert p.circum_radious == radious, f"actual: {p.circum_radious}, expected: {n}"
##    assert p.INTERIOR_ANGLE == INTERIOR_ANGLE, (
##        f"actual: {p.INTERIOR_ANGLE}," " expected: 60"
##    )
##
##    n = 4
##    radious = 1
##    p = Polygon(n, radious)
##    assert p.INTERIOR_ANGLE == RECT_ANGLE, (
##        f"actual: {p.INTERIOR_ANGLE}, " " expected: RECT_ANGLE"
##    )
##    assert isclose(p.area, 2, rel_tol=rel_tol, abs_tol=abs_tol), (
##        f"actual: {p.area}," " expected: 2.0"
##    )


def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    try:
        p = Polygon(2, 10)
        assert False, (
            "Creating a Polygon with 2 sides: " " Exception expected, not received"
        )
    except ValueError:
        pass

    n = 3
    radious = 1
    p = Polygon(n, radious)
    assert str(p) == "Polygon(n=3, radious=1)", f"actual: {str(p)}"
    assert p.count_vertices == n, f"actual: {p.count_vertices}," f" expected: {n}"
    assert p.count_edges == n, f"actual: {p.count_edges}, expected: {n}"
    assert p.circum_radious == radious, f"actual: {p.circum_radious}, expected: {n}"
    assert p.interior_angle == INTERIOR_ANGLE, (
        f"actual: {p.interior_angle}," " expected: 60"
    )
    n = 4
    radious = 1
    p = Polygon(n, radious)
    assert p.interior_angle == RECT_ANGLE, (
        f"actual: {p.interior_angle}, " " expected: 90"
    )
    assert isclose(p.area, 2, rel_tol=abs_tol, abs_tol=abs_tol), (
        f"actual: {p.area}," " expected: 2.0"
    )

    assert isclose(p.side_length, sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol), (
        f"actual: {p.side_length}," f" expected: {sqrt(2)}"
    )

    assert isclose(p.perimeter, 4 * sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol), (
        f"actual: {p.perimeter}," f" expected: {4 * sqrt(2)}"
    )

    assert isclose(p.apothem, 0.707, rel_tol=rel_tol, abs_tol=abs_tol), (
        f"actual: {p.perimeter}," " expected: 0.707"
    )
    p = Polygon(6, 2)
    assert isclose(p.side_length, 2, rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.apothem, 1.73205, rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.area, 10.3923, rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.perimeter, 12, rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.interior_angle, 120, rel_tol=rel_tol, abs_tol=abs_tol)

    p = Polygon(12, 3)
    assert isclose(p.side_length, 1.55291, rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.apothem, 2.89778, rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.area, 27, rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.perimeter, 18.635, rel_tol=rel_tol, abs_tol=abs_tol)
    assert isclose(p.interior_angle, 150, rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

##################################################################

## Goal 2
class Polygons2:
    def __init__(self, m, radious):
        if m < 3:
            raise ValueError("m must be greater than 3")

        self._m = m
        self._radious = radious

        self._polygons = [Polygon(i, radious) for i in range(3, m + 1)]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f"Polygons(m={self._m}, radious={self._radious})"

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(
            self._polygons, key=lambda p: p.area / p.perimeter, reverse=True
        )
        return sorted_polygons[0]


##################################################################

## Goal 3