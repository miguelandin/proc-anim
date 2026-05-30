from math import pi
from pygame import Vector2


# el ángulo no pasa de 2π
def simplify_angle(angle: float) -> float: return angle % (2*pi)


# calcula la ruta angular más corta entre dos ángulos
def calc_angle_diff(angle: float, anchor: float) -> float: return pi - \
    simplify_angle(angle+pi-anchor)


# la ruta angular no pasa del ángulo constraint
def constraint_angle(angle: float, anchor: float, constraint: float) -> float:
    angle_diff = calc_angle_diff(angle, anchor)
    if abs(angle_diff) <= constraint:
        return simplify_angle(angle)
    if angle_diff > constraint:
        return simplify_angle(anchor - constraint)
    return simplify_angle(anchor + constraint)


# el punto pos tendrá siempre el mismo radio sobre su anchor
def constraint_distance(pos: Vector2, anchor: Vector2, constraint: float) -> Vector2:
    displacement = pos - anchor
    if displacement.length() == 0:
        return anchor.copy()

    displacement.scale_to_length(constraint)
    return anchor + displacement
