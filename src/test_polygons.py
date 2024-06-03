"""
    testing Polygons module
"""
import pytest
import math
from polygon import Polygons

class TestPropertiesPolygons:
    """
        Test the properties of the Polygon class.
    """
    rel_tol = 0.001
    abs_tol = 0.001

    m = 500
    R = 1
    polygons = Polygons(m, R)

    def test_max_efficiency(self):
        test = TestPropertiesPolygons.polygons.max_efficiency_polygon.area
        # the with more edges, polygon approximate to a circle
        expect = math.pi
        assert math.isclose(
            test,
            expect,
            rel_tol = TestPropertiesPolygons.rel_tol,
            abs_tol = TestPropertiesPolygons.abs_tol
        )

class TestFunctionalityPolygons:
    """
        Test the functionality: slice of the Polygons class.
    """
    m = 8
    R = 1
    polygons = Polygons(m, R)

    def test_representation(self):
        test = str(TestFunctionalityPolygons.polygons[-1:])
        expect = f"[Polygon(edges={TestFunctionalityPolygons.m}, circumradius={TestFunctionalityPolygons.R})]"
        assert test == expect

    def test_len(self):
        test = len(TestFunctionalityPolygons.polygons)
        expect = TestFunctionalityPolygons.m - 2
        assert test == expect

    def test_slice(self):
        test = f"{TestFunctionalityPolygons.polygons[3:4]}"
        expect = "[Polygon(edges=6, circumradius=1)]"
        assert test == expect
