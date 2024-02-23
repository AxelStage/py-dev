#!python3
"""
    Python module for regular, strictly convex polygons
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
            Calculate the interior angle in rad
        """
        return (self._n - 2) * 180 / self._n

    @property
    def edge_length(self):
        """
            Calculate the edge length
        """
        return 2 * self._R * math.sin(math.pi / self._n)

    @property
    def apothem(self):
        """
            Calculate the apothem
        """
        return self._R * math.cos(math.pi / self._n)

    @property
    def area(self):
        """
            Calculate the area of the polygon
        """
        return self._n / 2 * self.edge_length * self.apothem

    @property
    def perimeter(self):
        """
            Calculate the perimeter
        """
        return self._n * self.edge_length

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


class Polygons:
    """
    Polygons class for a sequence of polygons
    """
    def __init__(self, m, R):
        if m < 3:
            raise ValueError("m must be greater than 3")
        self._m = m
        self._R = R
        self._polygons = [Polygon(i,R) for i in range(3, m + 1)]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(
            self._polygons,
            key = lambda p: p.area / p.perimeter,
            reverse=True
        )
        return sorted_polygons[0]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f"Polygons(m={self._m}, R={self._R})"

    def __getitem__(self, index):
        return self._polygons[index]


if __name__ == "__main__":
    polygons = Polygons(500,1)
    print(polygons.max_efficiency_polygon)