from waypoint_core.distance import Distance


class Itinerary:
    def __init__(self):
        self._trails = []

    def add_trail(self, trail):
        self._trails.append(trail)

    def total_distance(self):
        total_km = sum(trail.distance.convert("km").magnitude for trail in self._trails)
        return Distance(total_km, "km")