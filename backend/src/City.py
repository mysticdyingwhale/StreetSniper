from __future__ import annotations
from typing import Any, List, Optional
import pandas as pd

# City class

class City:
	cityName: str
	cityStreets: List[Street]

	def __init__(self, cityNam: str,






#import googlemaps
#
## Replace 'YOUR_API_KEY' with your actual API key
#gmaps = googlemaps.Client(key='YOUR_API_KEY')
#
## Geocoding example (address to coordinates)
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#print(geocode_result)
#
## Reverse geocoding example (coordinates to address)
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
#print(reverse_geocode_result)
#
## Directions API example
#directions_result = gmaps.directions("Sydney Town Hall",
#                                 "Parramatta, NSW",
#                                 mode="transit",
#                                 departure_time=datetime.datetime.now())
#print(directions_result)