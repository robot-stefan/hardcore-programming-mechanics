import unittest

from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.segment import Segment
from geom2d.circle import Circle
from geom2d.nums import are_close_enough
from geom2d.circles import make_circle_from_segments, make_circle_from_diameter, make_circle_from_points

class TestCircle(unittest.TestCase):
    center = Point(0, 0)
    radius = 5

    x = Segment(Point(1.75, -7.058808), Point(-6.771963, -1.6))
    y = Segment(Point(-8, 1.5), Point(0.725664, 6))
    z = Segment(Point(7.5, 3.1), Point(1.75, -7.058808))

    def test_contains_point(self):
        point = Point(0, -1)
        self.assertTrue(Circle.contains_point(self, point))

    def test_contains_point_on_circumfrence(self):
        point = Point(5, 0)
        self.assertTrue(Circle.contains_point(self, point))

    def test_doesnt_contain_point(self):
        point = Point(0, 10)
        self.assertFalse(Circle.contains_point(self, point))

    def test_make_circle_from_points(self):
        a = Point(0,5)
        b = Point(5,0)
        c = Point(0,-5)
        self.assertEqual(Circle(self.center, self.radius), make_circle_from_points(a, b, c))

    def test_make_circle_from_diameter(self):
        self.assertEqual(Circle(self.center, self.radius), make_circle_from_diameter(self.center, self.radius*2))

    def test_make_circle_from_segments(self):
        x = Segment(Point(1.75, -7.058808), Point(-6.771963, -1.6))
        y = Segment(Point(-8, 1.5), Point(0.725664, 6))
        z = Segment(Point(7.5, 3.1), Point(1.75, -7.058808))
        circle = make_circle_from_segments(x, y, z)
        self.assertTrue(are_close_enough(self.center.x, circle.center.x, .00001))
        self.assertTrue(are_close_enough(self.center.y, circle.center.y, .00001))
        self.assertTrue(are_close_enough(self.radius, circle.radius, .00001))


