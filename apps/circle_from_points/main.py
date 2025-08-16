from apps.circle_from_points.input import parse_points, read_config
from geom2d import make_circle_from_points
from apps.circle_from_points.output import draw_to_svg

if __name__ == '__main__':
    (a, b, c) = parse_points()
    circle = make_circle_from_points(a, b, c)
    draw_to_svg((a, b, c), circle, read_config())



