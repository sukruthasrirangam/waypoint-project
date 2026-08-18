from waypoint_core.trail import Trail, DayHike, BackpackingRoute, TrailRun, RatedDayHike
from waypoint_core.distance import Distance
from waypoint_core.itinerary import Itinerary
from waypoint_core.trail import GuidedDayHike
from waypoint_core.trail import FakeTrail

t = DayHike("Ridge Loop", Distance(8, "km"), 400, "moderate")
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
t2 = DayHike.from_dict(data)
print(t2.name, t2.distance.magnitude, t2.distance.unit, t2.difficulty)

t3 = DayHike("Ridge A", Distance(8, "km"), 400, "moderate", id=1)
t4 = DayHike("Ridge A Renamed", Distance(9, "km"), 500, "hard", id=1)
t5 = DayHike("Different Trail", Distance(8, "km"), 400, "moderate", id=2)
print(t3 == t4)  # True — same id, different data
print(t3 == t5)  # False — different id

it1 = Itinerary()
it1.add_trail(t3)
it1.add_trail(t5)
print(it1.total_distance().magnitude)  # 8 + 8 = 16

it2 = Itinerary()
it2.add_trail(t4)
print(it1.total_distance().magnitude)  # still 16 — proves it1/it2 are independent

# Week 8 Testing
hike = DayHike("Forest Loop", Distance(10, "km"), 300, "easy", id=10)
route = BackpackingRoute("Summit Traverse", Distance(40, "km"), 2000, "hard", days=3, id=11)
run = TrailRun("Ridge Sprint", Distance(15, "km"), 500, "moderate", id=12)

print(hike.summary(), hike.estimated_time())
print(route.summary(), route.estimated_time())
print(run.summary(), run.estimated_time())

try:
    Trail("Bad", Distance(1, "km"), 10, "easy")
except TypeError as e:
    print("Correctly rejected abstract instantiation:", e)

d1 = Distance(3, "km")
d2 = Distance(2, "km")
print(d1 + d2)         # 5.00 km
print(d1 - d2)         # 1.00 km
print(d1 + Distance(1, "mi"))  # auto-converts mi to km
print(sorted([Distance(5, "km"), Distance(2, "km"), Distance(3, "km")]))
print(repr(d1))

guided = GuidedDayHike("Canyon Trail", Distance(12, "km"), 600, "moderate", guide_name="Alex", id=13)
print(guided.summary())
print(guided.estimated_time())  # inherited from DayHike, unchanged
print(isinstance(guided, DayHike))  # True — real inheritance
print(isinstance(guided, Trail))    # True — through the chain

rated = RatedDayHike("Lakeside Path", Distance(5, "km"), 100, "easy", id=14)
rated.add_rating(4)
rated.add_rating(5)
print(rated.grade_percent())
print(rated.average_rating())
print([c.__name__ for c in RatedDayHike.__mro__])

mixed_trails = [hike, route, run, guided, rated, FakeTrail("Test Trail")]
for trail_item in mixed_trails:
    print(f"{trail_item.summary()} -> {trail_item.estimated_time()} hours")