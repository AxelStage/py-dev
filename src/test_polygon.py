"""
    testing app module
"""
import pytest
import math
from polygon import Polygon

class TestPropertiesPolygon:
    """
        Test the properties of the Polygon class.
    """
    rel_tol = 0.001
    abs_tol = 0.001

    n = 3
    R = 1
    polygon = Polygon(n, R)
    p2 = Polygon(6,2)

    def test_count_edges(self):
        test = TestPropertiesPolygon.polygon.count_edges
        expect = TestPropertiesPolygon.n
        assert test == expect

    def test_count_vertices(self):
        test = TestPropertiesPolygon.polygon.count_vertices
        expect = TestPropertiesPolygon.n
        assert test == expect

    def test_circumradius(self):
        test = TestPropertiesPolygon.polygon.circumradius
        expect = TestPropertiesPolygon.R
        assert test == expect

    def test_interior_angle(self):
        test = TestPropertiesPolygon.polygon.interior_angle
        expect = 60
        assert math.isclose(
            test,
            expect,
            rel_tol = TestPropertiesPolygon.rel_tol,
            abs_tol = TestPropertiesPolygon.abs_tol
        )

    def test_edge_length(self):
        test = TestPropertiesPolygon.polygon.edge_length
        expect = 1.732
        assert math.isclose(
            test,
            expect,
            rel_tol = TestPropertiesPolygon.rel_tol,
            abs_tol = TestPropertiesPolygon.abs_tol
        )

    def test_apothem(self):
        test = TestPropertiesPolygon.polygon.apothem
        expect = 0.5
        assert math.isclose(
            test,
            expect,
            rel_tol = TestPropertiesPolygon.rel_tol,
            abs_tol = TestPropertiesPolygon.abs_tol
        )

    def test_area(self):
        test = TestPropertiesPolygon.polygon.area
        expect = 1.299
        assert math.isclose(
            test,
            expect,
            rel_tol = TestPropertiesPolygon.rel_tol,
            abs_tol = TestPropertiesPolygon.abs_tol
        )

    def test_perimeter(self):
        test = TestPropertiesPolygon.polygon.perimeter
        expect = 5.196
        assert math.isclose(
            test,
            expect,
            rel_tol = TestPropertiesPolygon.rel_tol,
            abs_tol = TestPropertiesPolygon.abs_tol
        )


class TestFunctionalityPolygon:
    """
        Test the functionality: equal, less then, ... of the Polygon class.
    """
    p1 = Polygon(3, 1)
    p2 = Polygon(6, 2)

    def test_representation(self):
        test = str(TestFunctionalityPolygon.p1)
        expect = f"Polygon(edges={TestFunctionalityPolygon.p1.count_edges}, circumradius={TestFunctionalityPolygon.p1.circumradius})"
        assert test == expect

    def test_equal(self):
        test = TestFunctionalityPolygon.p1
        expect = TestFunctionalityPolygon.p1
        assert test == expect

    def test_not_equal(self):
        test = TestFunctionalityPolygon.p1
        expect = TestFunctionalityPolygon.p2
        assert test != expect

    def test_greaterthen(self):
        test = TestFunctionalityPolygon.p1
        expect = TestFunctionalityPolygon.p2
        assert expect > test

    def test_lessthen(self):
        test = TestFunctionalityPolygon.p1
        expect = TestFunctionalityPolygon.p2
        assert test < expect

class TestExceptionsPolygon:
    """
        Test the exceptions of the Polygon class.
    """
    def test_edges_below_3(self):
        try:
            p = Polygon(2,1)
            assert False, ("Exception expected, created Polygon with 2 sides")
        except ValueError:
            pass