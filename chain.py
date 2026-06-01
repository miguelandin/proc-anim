from pygame.math import Vector2
import pygame
from math import pi, cos, sin
from utils import constraint_angle, constraint_distance


class Chain:
    radius: int
    angles: list[float]
    max_angle: float

    def __init__(self, origin: Vector2, joint_count: int, radius: int, max_angle: float = 2*pi):
        self.radius: int = radius
        self.max_angle: float = max_angle
        self.joints: list[Vector2] = []
        self.joints.append(origin)
        self.angles: list[float] = []
        self.angles.append(0)

        space = Vector2(0, self.radius)
        for i in range(1, joint_count):
            self.joints.append(Vector2(self.joints[i-1] + space))
            self.angles.append(pi/2)

    def resolve(self, pos: Vector2):
        self.angles[0] = (pos-self.joints[0]).angle_rad
        self.joints[0] = pos

        for i in range(1, len(self.joints)):
            current_angle = (self.joints[i-1]-self.joints[i]).angle_rad
            self.angles[i] = constraint_angle(
                current_angle, self.angles[i-1], self.max_angle)

            self.joints[i] = self.joints[i-1] - \
                Vector2(cos(self.angles[i]), sin(self.angles[i])) * self.radius

    def fabrik_resolve(self, pos: Vector2, accuracy: float = 1.0, max_it: int = 10):
        anchor = self.joints[-1]

        self.joints[0] = pos
        for _ in range(max_it):
            for i in range(1, len(self.joints)):
                self.joints[i] = constraint_distance(
                    self.joints[i], self.joints[i-1], self.radius)

            self.joints[-1] = anchor
            for i in range(len(self.joints)-2, -1, -1):
                self.joints[i] = constraint_distance(
                    self.joints[i], self.joints[i+1], self.radius)

            if self.joints[0].distance_to(pos) <= accuracy:
                break

    def display_radius(self, surface: pygame.Surface, width: int = 1):
        for i in self.joints:
            pygame.draw.circle(surface, (255, 255, 255), i, self.radius, width)

    def display_points(self, surface: pygame.Surface, width: int = 1):
        for i in self.joints:
            pygame.draw.circle(surface, (255, 255, 255), i, width, 0)

    def display_lines(self, surface: pygame.Surface, width: int = 1):
        for i in range(1, len(self.joints)):
            pygame.draw.line(surface, (255, 255, 255),
                             self.joints[i-1], self.joints[i], width)

    def get_coords(self):
        return self.joints.copy()
