from django.test import TestCase
from django.urls import reverse
from .models import Trail, Park
from waypoint_core.distance import Distance


class TrailQueryTests(TestCase):
    def setUp(self):
        self.park = Park.objects.create(name="Test Park", region="Test Region")
        self.open_trail = Trail.objects.create(
            name="Open Trail", distance_km=5.0, elevation_gain=200,
            difficulty="easy", is_open=True, park=self.park
        )
        self.closed_trail = Trail.objects.create(
            name="Closed Trail", distance_km=3.0, elevation_gain=100,
            difficulty="moderate", is_open=False, park=self.park
        )

    def test_open_trails_query_excludes_closed(self):
        open_trails = Trail.objects.filter(is_open=True)
        self.assertIn(self.open_trail, open_trails)
        self.assertNotIn(self.closed_trail, open_trails)

    def test_trail_detail_404_for_missing_trail(self):
        response = self.client.get(reverse('trail_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_trail_detail_200_for_existing_trail(self):
        response = self.client.get(reverse('trail_detail', args=[self.open_trail.id]))
        self.assertEqual(response.status_code, 200)


class DistanceRuleTests(TestCase):
    def test_negative_distance_raises_value_error(self):
        with self.assertRaises(ValueError):
            Distance(-5, "km")