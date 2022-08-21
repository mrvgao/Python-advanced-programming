from unittest import TestCase
from planet_simulation import Planet
import unittest


class TestPlanet(TestCase):
    def setUp(self) -> None:
        self.planet_a = Planet(
            color='red',
            mass=100,
            position=(100, 200),
            v_init=(100, 200),
        )

        self.another_planet = Planet(
            color='green',
            mass=10,
            position=(10, 20),
            v_init=(10, 20),
        )

    def test_init(self):

        self.assertEqual(self.planet_a.x, 100)
        self.assertEqual(self.planet_a.y, 200)
        self.assertEqual(self.planet_a.v, (100, 200))

    def test_gravity(self):
        self.planet_a.gravity(self.another_planet)

        self.assertIsNot(self.planet_a.current_force.x, 0)
        self.assertIsNot(self.planet_a.current_force.y, 0)

    def tearDown(self) -> None:
        pass

