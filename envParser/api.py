import envParser

def get(lat, lon):
    e = envParser.EnvironmentParser(lat=lat, lon=lon)
    return e
