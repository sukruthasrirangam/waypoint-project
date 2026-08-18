from waypoint_core.distance import Distance

ALLOWED_DIFFICULTIES = ("easy", "moderate", "hard", "expert")

class Trail:
    default_unit = "km"

    def __init__(self, name, distance, elevation_gain_m, difficulty, id=None):
        self.id = id
        self.name = name
        self.distance = distance
        self.elevation_gain_m = elevation_gain_m
        self._difficulty = None
        self.set_difficulty(difficulty)

    def set_difficulty(self, difficulty):
        if difficulty not in ALLOWED_DIFFICULTIES:
            raise ValueError(f"Invalid difficulty: {difficulty}")
        self._difficulty = difficulty

    @property
    def difficulty(self):
        return self._difficulty

    @staticmethod
    def validate_elevation(elevation_gain_m):
        if elevation_gain_m < 0:
            raise ValueError("elevation_gain_m cannot be negative")
        return elevation_gain_m

    @classmethod
    def from_dict(cls, data):
        distance = Distance(data["distance_magnitude"], data.get("distance_unit", cls.default_unit))
        elevation = cls.validate_elevation(data["elevation_gain_m"])
        return cls(data["name"], distance, elevation, data["difficulty"], id=data.get("id"))

    def __eq__(self, other):
        if not isinstance(other, Trail):
            return NotImplemented
        return self.id == other.id