from abc import ABC, abstractmethod
from waypoint_core.distance import Distance

ALLOWED_DIFFICULTIES = ("easy", "moderate", "hard", "expert")

class ElevationMixin:
    def grade_percent(self):
        distance_m = self.distance.convert("km").magnitude * 1000
        if distance_m == 0:
            return 0
        return (self.elevation_gain_m / distance_m) * 100


class RatingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ratings = []

    def add_rating(self, stars):
        if not (1 <= stars <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self._ratings.append(stars)

    def average_rating(self):
        if not self._ratings:
            return None
        return sum(self._ratings) / len(self._ratings)

class Trail(ABC):
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

    @abstractmethod
    def estimated_time(self):
        """Return estimated completion time in hours."""
        ...

    @abstractmethod
    def summary(self):
        """Return a short human-readable summary string."""
        ...

class DayHike(Trail):
    def estimated_time(self):
        return self.distance.convert("km").magnitude / 4  # ~4 km/h pace

    def summary(self):
        return f"{self.name}: a {self.distance.magnitude}{self.distance.unit} day hike"


class BackpackingRoute(Trail):
    def __init__(self, name, distance, elevation_gain_m, difficulty, days, id=None):
        super().__init__(name, distance, elevation_gain_m, difficulty, id=id)
        self.days = days

    def estimated_time(self):
        return self.days * 6  # ~6 hours of hiking per day

    def summary(self):
        return f"{self.name}: a {self.days}-day backpacking route"


class TrailRun(Trail):
    def estimated_time(self):
        return self.distance.convert("km").magnitude / 10  # ~10 km/h running pace

    def summary(self):
        return f"{self.name}: a {self.distance.magnitude}{self.distance.unit} trail run"

class GuidedDayHike(DayHike):
    def __init__(self, name, distance, elevation_gain_m, difficulty, guide_name, id=None):
        super().__init__(name, distance, elevation_gain_m, difficulty, id=id)
        self.guide_name = guide_name

    def summary(self):
        base_summary = super().summary()
        return f"{base_summary}, guided by {self.guide_name}"

class RatedDayHike(ElevationMixin, RatingMixin, DayHike):
    pass

class FakeTrail:
    """Duck-typed trail — doesn't inherit from Trail at all, but has the same interface."""
    def __init__(self, name):
        self.name = name

    def estimated_time(self):
        return 1.0

    def summary(self):
        return f"{self.name}: a fake trail for testing"
