#!python3
"""
    Python app for regular, strictly convex polygons
"""

import math

class Polygon:
    """
    Polygon class for regular, strictly convex polygons
    """

    def __init__(self, n, R):
        if n < 3:
            raise ValueError("Polygon must have at least three sides/vertices")
        self._n = n
        self._R = R

        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def count_edges(self):
        return self._n

    @property
    def count_vertices(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        """
            Calculate the interior angle
            lazy property
        """
        if self._interior_angle is None:
            self._interior_angle = (self._n - 2) * 180 / self._n

        return self._interior_angle

    @property
    def edge_length(self):
        """
            Calculate the edge length
            lazy property
        """
        if self._edge_length is None:
            self._edge_length = 2 * self._R * math.sin(math.pi / self._n)

        return self._edge_length

    @property
    def apothem(self):
        """
            Calculate the apothem
            lazy property
        """
        if self._apothem is None:
            self._apothem = self._R * math.cos(math.pi / self._n)

        return self._apothem

    @property
    def area(self):
        """
            Calculate the area of the polygon
            lazy property
        """
        if self._area is None:
            self._area = self._n / 2 * self.edge_length * self.apothem

        return self._area

    @property
    def perimeter(self):
        """
            Calculate the perimeter of the polygon
            lazy property
        """
        if self._perimeter is None:
            self._perimeter = self._n * self.edge_length

        return self._perimeter

    # functionality
    def __repr__(self):
        return f"Polygon(edges={self._n}, circumradius={self._R})"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            return (self.count_edges == other.count_edges
                    and self.circumradius == other.circumradius)

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            return self.count_vertices > other.count_vertices


class PolygonsIterator:
    """
        Class to iterate of a sequence of polygons
    """
    def __init__(self, m, R):
        if m < 3:
            raise ValueError("m must be greater than 3")
        self._m = m
        self._R = R
        self._i = 3

    def __iter__(self):
        return self

    def __next__(self):
        if self._i > self._m:
            return StopIteration
        else:
            result = Polygon(self._i, self._R)
            self._i += 1
            return result

class Polygons:
    """
    Polygons class for a sequence of polygons
    """
    def __init__(self, m, R):
        if m < 3:
            raise ValueError("m must be greater than 3")
        self._m = m
        self._R = R
        self._max_efficiency_polygon = None

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f"Polygons(m={self._m}, R={self._R})"

    def __iter__(self):
        return PolygonsIterator(self._m, self._R)

    @property
    def max_efficiency_polygon(self):
        if self._max_efficiency_polygon is None:
            sorted_polygons = sorted(
                PolygonsIterator(self._m, self._R),
                key = lambda p: p.area / p.perimeter,
                reverse=True
            )
            self._max_efficiency_polygon = sorted_polygons[0]

        return self._max_efficiency_polygon
