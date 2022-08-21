from planet_simulation import Planet
from planet_simulation import Force
import matplotlib.pyplot as plt
from matppasslotlib import animation
import random


fig = plt.figure()

point_1 = Planet('r', 1, (0, 1), (0.5, 0))
point_2 = Planet('b', 1, (0, -1), (-0.5, 0))


def get_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


class RunEnv:
    def __init__(self, number, xlim, ylim):
        self.planets = [Planet(get_color(), random.uniform(0, 2), (random.uniform(-xlim/10, xlim/10), random.uniform(-ylim/10, ylim/10)),
                         (random.uniform(0, 1), random.uniform(0, 1))) for _ in range(number)]
        self.xlim = xlim
        self.ylim = ylim

    def update(self):
        for p_self in self.planets:
            for p_other in self.planets:
                if p_self == p_other: continue
                p_self.gravity(p_other)

    def draw(self):
        for p in self.planets:
            x, y = p.position
            print(x, y)
            plt.scatter(x, y, s=p.mass * 10)

        plt.xlim(-self.xlim, self.xlim)
        plt.ylim(-self.ylim, self.ylim)
        plt.draw()

    def step(self, span=1):
        for _ in range(span):
            self.update()
        self.draw()


run_env = RunEnv(number=40, xlim=10000, ylim=10000)


def animate(i):

    run_env.step()


ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, interval=1)
plt.show()