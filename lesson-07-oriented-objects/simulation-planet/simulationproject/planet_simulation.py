import math


class Vec:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __iadd__(self, other):
        self.x = self.x + other.x
        self.y = self.x + other.y

        return self


class Force(Vec):
    def __truediv__(self, mass):
        return Acc(self.x / mass, self.y / mass)


class Acc(Force):
    pass


class Planet:
    Number = 0

    def __init__(self, color, mass, position, v_init):
        Planet.Number += 1
        self.color = color
        self.mass = mass
        self.__x, self.__y = position
        self.__vx, self.__vy = v_init
        self.eps = 1
        self.current_force = Force()

    def gravity(self, other_planet):
        distance = math.sqrt((self.x - other_planet.x) ** 2 + (self.y - other_planet.y) ** 2)
        f = self.mass * other_planet.mass / (distance ** 2)

        self.current_force += Force(
            (other_planet.x - self.x) / distance * f,
            (other_planet.y - self.y) / distance * f
        )

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def v(self):
        acc = self.current_force / self.mass
        self.__vx += acc.x
        self.__vy += acc.y

        return self.__vx, self.__vy

    @property
    def position(self):
        vx, vy = self.v
        self.__x += vx
        self.__y += vy
        return self.__x, self.__y