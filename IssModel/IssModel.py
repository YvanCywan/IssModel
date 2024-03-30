class IssModel:
    mass: float = 1000
    radius: float = 1000
    height: float = 1000

    def get_mass(self) -> float:
        return self.mass

    def set_mass(self, mass: float):
        self.mass = mass

    def get_radius(self) -> float:
        return self.radius

    def set_radius(self, radius: float):
        self.radius = radius

    def get_height(self) -> float:
        return self.height

    def set_height(self, height: float):
        self.height = height
