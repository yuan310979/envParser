import requests
from xml.dom import minidom

class Environment:
    def __init__(self, CITY1 ,CITY2, TOWN):
        if CITY1 == "":
            self.gmaps_CITY = CITY2
        else:
            self.gmaps_CITY = CITY1
        self.gmaps_TOWN = TOWN
        self.HUMD = ""
        self.TEMP = ""
        self.parseWeatherData()

    def parseWeatherData(self):
        payload = {'dataid': 'O-A0001-001', 'authorizationkey': 'CWB-73FDB36B-3738-46A6-AFDB-FA7A789C321A'}
        response = requests.get("http://opendata.cwb.gov.tw/opendataapi", params=payload)
        f1 = open('data1', 'wb')
        f1.write(response.text.encode('utf-8'))
        f1.close()
        xmldom = minidom.parse("data1")
        locs = xmldom.getElementsByTagName("location")
        CITY = ""
        TOWN = ""
        for loc in locs:
            name = loc.getElementsByTagName("locationName")[0].firstChild.data 
            for param in loc.getElementsByTagName("parameter"):
                if param.getElementsByTagName("parameterName")[0].firstChild.data == "CITY":
                    CITY = param.getElementsByTagName("parameterValue")[0].firstChild.data
                elif param.getElementsByTagName("parameterName")[0].firstChild.data == "TOWN":
                    TOWN = param.getElementsByTagName("parameterValue")[0].firstChild.data
            if CITY == self.gmaps_CITY and TOWN == self.gmaps_TOWN:
                elements = loc.getElementsByTagName("weatherElement")
                self.TEMP = elements[3].getElementsByTagName("elementValue")[0].getElementsByTagName("value")[0].firstChild.data
                self.HUMD = elements[4].getElementsByTagName("elementValue")[0].getElementsByTagName("value")[0].firstChild.data 
        keys = ('HUMD', 'TEMP')
        val = (self.HUMD, self.TEMP) 
        return dict.fromkeys(keys, val) 

    def __str__(self):
        return "HUMD:" + self.HUMD +" TEMP:" + self.TEMP
 
