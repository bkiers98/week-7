import unittest
from loader import *


class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        '''Tests that fetch_location_data works for valid locations.'''
        geolocator = get_geolocator()
        locations = [{
            'location': 'Museum of Modern Art',
            'latitude': '40.7618552',
            'longitude': '-73.9782438',
            'type': 'museum'},
            {'location': 'USS Alabama Battleship Memorial Park',
             'latitude': '30.684373',
             'longitude': '-88.015316',
             'type': 'park'}
            ]
        for location in locations:            
            result = fetch_location_data(geolocator, location['location'])
            for key, value in result.items():
                with self.subTest(key=key):
                    self.assertIsNotNone(value,
                        f'Value for {key} in {location['location']} is None')

    def test_invalid_location(self):
        '''Tests that fetch_location_data works for invalid locations.'''
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        for key, value in result.items():
            if key != 'location':
                with self.subTest(key=key):
                    self.assertIsNone(value,
                        'A nonexistent location should have an empty result.')


if __name__ == "__main__":
    unittest.main()
