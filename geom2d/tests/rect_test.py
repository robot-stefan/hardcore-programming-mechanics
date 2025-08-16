import unittest

from geom2d.point import Point
from geom2d.segment import Segment
from geom2d.rect import Rect
from geom2d.size import Size
from geom2d.polygon import Polygon


class TestRect(unittest.TestCase):
    origin = Point(0, 0)
    size = Size(3, 4)

    def test_left(self):
        Actual = Rect(self.origin, self.size).left
        Expected = 0
        self.assertEqual(Actual, Expected)

    def test_right(self):
        Actual = Rect(self.origin, self.size).right
        Expected = 3
        self.assertEqual(Actual, Expected)

    def test_bottom(self):
        Actual = Rect(self.origin, self.size).bottom
        Expected = 0
        self.assertEqual(Actual, Expected)

    def test_top(self):
        Actual = Rect(self.origin, self.size).top
        Expected = 4
        self.assertEqual(Actual, Expected)

    def test_area(self):
        expected = 12
        actual = Rect(self.origin, self.size).area
        self.assertEqual(actual, expected)

    def test_perimeter(self):
        expected = 14
        actual = Rect(self.origin, self.size).perimeter
        self.assertEqual(actual, expected)

    def test_contains_point(self):
        P = Point(1, 1)
        R = Rect(self.origin, self.size)
        self.assertTrue(R.contains_point(P))

    def test_does_not_contains_point_on_perimeter(self):
        P = Point(0, 0)
        R = Rect(self.origin, self.size)
        self.assertFalse(R.contains_point(P))

    def test_does_not_contains_point(self):
        P = Point(-5, -2)
        R = Rect(self.origin, self.size)
        self.assertFalse(R.contains_point(P))

    def test_to_polygon(self):
        Expected = Polygon( [
            self.origin,
            Point(3, 0),
            Point(3, 4),
            Point(0, 4),
        ])
        Actual = Rect(self.origin, self.size).to_polygon()
        self.assertEqual(Actual, Expected)

    def test_equal(self):
        A = Rect(self.origin, self.size)
        B = Rect(Point(0, 0), Size(3, 4))
        self.assertEqual(A, B)

    def test_not_equal(self):
        A = Rect(self.origin, self.size)
        B = Rect(Point(0, 0), Size(3, 5))
        self.assertNotEqual(A, B)

    def test_intersection_with(self):
        A = Rect(self.origin, self.size)
        B = Rect(Point(1, 1), Size(4, 5))
        Actual = A.intersection_with(B)
        Expected = Rect(Point(1, 1), Size(2, 3))
        self.assertEqual(Actual, Expected)

    def test_no_intersection_with(self):
        A = Rect(self.origin, self.size)
        B = Rect(Point(-10, -8), Size(4, 5))
        Actual = A.intersection_with(B)
        self.assertIsNone(Actual)

