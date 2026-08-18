KM_PER_MI = 1.60934

class Distance:
    def __init__(self, magnitude, unit="km"):
        if magnitude < 0:
            raise ValueError("Distance magnitude cannot be negative")
        if unit not in ("km", "mi"):
            raise ValueError(f"Unsupported unit: {unit}")
        self._magnitude = magnitude
        self._unit = unit

    @property
    def magnitude(self):
        return self._magnitude

    @property
    def unit(self):
        return self._unit

    def convert(self, to_unit):
        if to_unit == self._unit:
            return Distance(self._magnitude, self._unit)
        if to_unit == "mi":
            return Distance(self._magnitude / KM_PER_MI, "mi")
        if to_unit == "km":
            return Distance(self._magnitude * KM_PER_MI, "km")
        raise ValueError(f"Unsupported unit: {to_unit}")

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        other_in_self_unit = other.convert(self._unit)
        return Distance(self._magnitude + other_in_self_unit.magnitude, self._unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        other_in_self_unit = other.convert(self._unit)
        return Distance(self._magnitude - other_in_self_unit.magnitude, self._unit)

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return abs(self._magnitude - other.convert(self._unit).magnitude) < 1e-9

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self._magnitude < other.convert(self._unit).magnitude

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self._magnitude > other.convert(self._unit).magnitude

    def __str__(self):
        return f"{self._magnitude:.2f} {self._unit}"

    def __repr__(self):
        return f"Distance({self._magnitude!r}, {self._unit!r})"