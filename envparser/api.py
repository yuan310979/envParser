import envparser

def get(lat, lon):
    e = envparser.EnvironmentParser(lat=lat, lon=lon)
    return e
