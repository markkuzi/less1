class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def full_mass(self, mass_1m2, depth):
        full_mass = self._length * self._width * mass_1m2 * depth
        self.road_mass = full_mass
        return self.road_mass


first_road = Road(20, 5000)
print(first_road.full_mass(25, 5))
