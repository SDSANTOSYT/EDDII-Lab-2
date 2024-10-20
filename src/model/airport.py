import math

class Airport:
    
    def __init__(self, code, name, city, country, latitude, longitude) -> None:
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
    
    def haversine(self, airport) -> float:
        lat1 = float(self.latitude)
        lat2 = float(airport.latitude)
        long1 = float(self.longitude)
        long2 = float(airport.longitude)
        radius = 6371
        dlat = math.radians(lat2 - lat1)
        dlong = math.radians(long2 - long1)
        a = (math.sin(dlat/2) * math.sin(dlat/2)) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * (math.sin(dlong/2) * math.sin(dlong/2))
        c = 2 * math.asin(math.sqrt(a))
        return round(abs(radius * c),2)
    
    def __repr__(self) -> str:
        string = f'codigo: {self.code}, nombre: {self.name}, ciudad: {self.city}, pais: {self.country}, latitud: {self.latitude}, longitud: {self.longitude}'
        return string