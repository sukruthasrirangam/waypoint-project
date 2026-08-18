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