import requests

class Place:
    def __init__(self, latlong: tuple[float], name: str, fullName: str, countryCode: str, countryName: str):
        self.name = name
        self.countryCode = countryCode
        self.countryName = countryName
        self.latlong = latlong
        self.fullName = fullName

# query location data from a string like "London, UK"
def queryPlace(query: str) -> Place:
    headers = {'User-Agent': 'OpenWeather'}
    params = {
        'q': query,
        'addressdetails': 1,
        'accept-language': 'en',
        'limit': 10,
        'format': 'json'
    }
    data = requests.get("http://nominatim.openstreetmap.org/search", params=params, headers=headers, verify=False).json()[0]
    latlong = (float(data['lat']), float(data['lon']))
    name = data['name']
    countryName = data['address']['country']
    countryCode = data['address']['country_code']
    fullName = data['display_name']
    place = Place(latlong, name, fullName, countryCode, countryName)
    return place
