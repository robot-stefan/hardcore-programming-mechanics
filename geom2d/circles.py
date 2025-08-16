from geom2d.point import Point
from geom2d.circle import Circle
from geom2d.segment import Segment
from geom2d.line import Line
import math


def make_circle_from_points(a: Point, b: Point, c: Point):
    chord_one_bisec = Segment(a, b).bisector
    chord_two_bisec = Segment(b, c).bisector
    center = chord_one_bisec.intersection_with(chord_two_bisec)
    radius = center.distance_to(a)
    return Circle(center, radius)

def make_circle_from_diameter(center: Point, diameter: float):
    radius = diameter/2
    return Circle(center, radius)

def make_circle_from_segments(a: Segment, b: Segment, c: Segment):
    return make_circle_from_lines(Line(a.point_at(0), a.direction_vector),
                                  Line(b.point_at(0), b.direction_vector),
                                  Line(c.point_at(0), c.direction_vector))

def make_circle_from_lines(a: Line, b: Line, c: Line):
    PointA = a.intersection_with(b)
    PointB = b.intersection_with(c)
    PointC = c.intersection_with(a)
    SegmentDirectionA = Segment(PointB, PointA).direction_vector
    SegmentDirectionB = Segment(PointB, PointC).direction_vector
    SegmentDirectionB2 = Segment(PointC, PointB).direction_vector
    SegmentDirectionC = Segment(PointC, PointA).direction_vector
    SegDirBHalf = SegmentDirectionB.rotated_radians(SegmentDirectionA.angle_to(SegmentDirectionB) * .5 * -1)
    ThetaB2toC = SegmentDirectionB2.angle_to(SegmentDirectionC) * .5
    SegDirCHalf = SegmentDirectionB2.rotated_radians(ThetaB2toC)
    center = Line(PointC, SegDirCHalf).intersection_with(Line(PointB, SegDirBHalf))
    radius = Segment(center, PointC).length * math.sin(ThetaB2toC)
    return Circle(center, radius)

