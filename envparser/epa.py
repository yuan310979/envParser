import requests
import json

class Environment:
    def __init__(self, CITY1, CITY2, TOWN):
        self.County = ""
        self.SiteName = ""
        self.AQI = ""
        self.Pollutant = ""
        self.Status = ""
        self.SO2 = ""
        self.CO = ""
        self.CO_8hr = ""
        self.O3 = ""
        self.O3_8hr = ""
        self.PM10 = ""
        self.PM2_5 = ""
        self.NO2 = ""
        self.NOx = ""
        self.NO = ""
        self.WindSpeed = ""
        self.WindDirec = ""
        self.PublishTime = ""
        self.PM10_AVG = ""
        self.PM2_5_AVG = ""
        if CITY1 == "":
            self.gmaps_CITY = CITY2
        else:
            self.gmaps_CITY = CITY1
        self.gmaps_TOWN = TOWN[:2]
        base = "https://opendata.epa.gov.tw/webapi/api/rest/datastore/"
        dataID = "355000000I-000259"
        form = "json"
        key = "BEnERA7gP0Kn/ftIYFsZ4A" 
        params = "format=" + form + "&token=" + key
        url = base + dataID + "?" + params
        response = requests.get(url, verify=False)
        self.r = json.loads(response.text)['result']

    def parseEPAData(self):
        candidate = {}
        for data in self.r['records']:
            if data['SiteName'] == self.gmaps_TOWN and data['County'] == self.gmaps_CITY:
                candidate = data
                break
            if data['County'] == self.gmaps_CITY:
                candidate = data
        self.County = candidate['County']
        self.SiteName = candidate['SiteName']
        self.AQI = candidate['AQI']
        self.Pollutant = candidate['Pollutant']
        self.Status = candidate['Status']
        self.SO2 = candidate['SO2']    
        self.CO = candidate['CO']
        self.CO_8hr = candidate['CO_8hr']
        self.O3 = candidate['O3']
        self.O3_8hr = candidate['O3_8hr']
        self.PM10 = candidate['PM10']
        self.PM2_5 = candidate['PM2.5']
        self.NO2 = candidate['NO2']
        self.NOx = candidate['NOx']
        self.NO = candidate['NO']
        self.WindSpeed = candidate['WindSpeed']
        self.WindDirec = candidate['WindSpeed']
        self.PublishTime = candidate['PublishTime']
        self.PM10_AVG = candidate['PM10_AVG']
        self.PM2_5_AVG = candidate['PM2.5_AVG']

    def __str__(self):
        return (self.County + self.SiteName + 
                "\nAQI: " + self.AQI +
                "\nPollutant: " + self.Pollutant +
                "\nStatus: " + self.Status +
                "\nSO2: " + self.SO2 +
                "\nCo: " + self.CO +
                "\nCO_8hr" + self.CO_8hr + 
                "\nO3: " + self.O3 +
                "\nO3_8hr: " + self.O3_8hr +
                "\nPM10: " + self.PM10 + 
                "\nPM2.5: " + self.PM2_5 +
                "\nNO2: " + self.NO2 +
                "\nNOx: " + self.NOx +
                "\nNO: " + self.NO +
                "\nWindSpeed: " + self.WindSpeed + 
                "\nWindDirec: " + self.WindDirec +
                "\nPublishTime: " + self.PublishTime +
                "\nPM2.5_AVG: " + self.PM2_5_AVG +
                "\nPM10_AVG:" + self.PM10_AVG).encode('utf-8')
