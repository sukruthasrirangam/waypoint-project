from waypoint_core.trail import Trail
from waypoint_core.distance import Distance
from waypoint_core.itinerary import Itinerary

t = Trail("Ridge Loop", Distance(8, "km"), 400, "moderate")
print(t.name, t.difficulty)

try:
    t.set_difficulty("extreme")
except ValueError as e:
    print("Correctly rejected:", e)

data = {
    "name": "Sunset Trail",
    "distance_magnitude": 6,
    "elevation_gain_m": 150,
    "difficulty": "easy",
}
t2 = Trail.from_dict(data)
print(t2.name, t2.distance.magnitude, t2.distance.unit, t2.difficulty)

t3 = Trail("Ridge A", Distance(8, "km"), 400, "moderate", id=1)
t4 = Trail("Ridge A Renamed", Distance(9, "km"), 500, "hard", id=1)
t5 = Trail("Different Trail", Distance(8, "km"), 400, "moderate", id=2)
print(t3 == t4)  # True — same id, different data
print(t3 == t5)  # False — different id

it1 = Itinerary()
it1.add_trail(t3)
it1.add_trail(t5)
print(it1.total_distance().magnitude)  # 8 + 8 = 16

it2 = Itinerary()
it2.add_trail(t4)
print(it1.total_distance().magnitude)  # still 16 — proves it1/it2 are independent