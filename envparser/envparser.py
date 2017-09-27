import requests
import sys
import json
import gmaps
import cwb
import epa
from xml.dom import minidom

class EnvironmentParser:
    def __init__(self, lat, lon):
        self.lat = lat
        self.long = lon
        self.location = {}
        self.LocDict = {}
        self.dict = {} 
        self.parseLocData()
        self.parseWeatherData()
        self.parseEnvironmentData()

    def parseLocData(self):
        # Get the address data through latitude and longitude
        self.location = gmaps.locationGenerator(lon=120.999645,lat=24.789071)
        self.location.getAddressComponent()
        self.LocDict = self.location.getDict()

    def parseWeatherData(self):    
        # Pass the address to get some weather data from CWB(Central Weather Bureau)
        env = cwb.Environment(self.location['l1'], self.location['l2'], self.location['l3'])
        self.dict['HUMD'] = env.HUMD
        self.dict['TEMP'] = env.TEMP

    def parseEnvironmentData(self):
        env2 = epa.Environment(self.location['l1'], self.location['l2'], self.location['l3'])
        env2.parseEPAData()
        self.dict['County'] = env2.County
        self.dict['SiteName'] =env2.SiteName
        self.dict['AQI'] = env2.AQI
        self.dict['Pollutant'] = env2.Pollutant
        self.dict['Status'] = env2.Status
        self.dict['SO2'] = env2.SO2 
        self.dict['CO'] = env2.CO
       	self.dict['CO_8hr'] = env2.CO_8hr
        self.dict['O3'] = env2.O3
        self.dict['O3_8hr'] = env2.O3_8hr
        self.dict['PM10'] = env2.PM10
        self.dict['PM2.5'] = env2.PM2_5
        self.dict['NO2'] = env2.NO2
        self.dict['NOx'] = env2.NOx
        self.dict['NO'] = env2.NO
        self.dict['WindSpeed'] = env2.WindSpeed
        self.dict['WindDirec'] = env2.WindSpeed
        self.dict['PublishTime'] = env2.PublishTime
        self.dict['PM10_AVG'] = env2.PM10_AVG
        self.dict['PM2.5_AVG'] = env2.PM2_5_AVG

    def __getitem__(self, name):
        return self.dict[name]

