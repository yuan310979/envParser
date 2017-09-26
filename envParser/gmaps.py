import requests

class locationGenerator:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.sen = "false"
        self.lan = "zh-TW"
        key = "AIzaSyAG8-U3vwtcENcIH-KnyCy0MQQcaOk3cU8"
        base = "https://maps.googleapis.com/maps/api/geocode/json"
        params = "latlng=" + str(self.lat) + "," + str(self.lon) + "&sensor=" + str(self.sen) + "&language=" + str(self.lan) + "&key=" + key
        url = base + "?" + params
        gmaps_res = requests.get(url)
        self.gmaps_json = gmaps_res.json()
        self.location = {'l1':'', 'l2':'', 'l3':''}

    def getFormattedAddress(self):
        return self.gmaps_json['results'][0]['formatted_address']

    def getAddressComponent(self):
        for comp in self.gmaps_json['results'][0]['address_components']:
            if comp['types'][0] == 'administrative_area_level_3':
                self.location['l3'] = comp['short_name']
            elif comp['types'][0] == 'administrative_area_level_2':
                self.location['l2'] = comp['short_name']
            elif comp['types'][0] == 'administrative_area_level_1':
                self.location['l1'] = comp['short_name']        

    def __getitem__(self, name):
        return self.location[name]

    def getDict(self):
        keys = ('l1', 'l2', 'l3')
        val = (self.location['l1'], self.location['l2'], self.location['l3'])
        return dict.fromkeys(keys,val)
