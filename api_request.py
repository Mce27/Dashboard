from tokenize import String
import requests
import json

hourNumber = []
hourlyTemp = []
wind = ""
hourlyIcons= []
dailyForecast = ""
isDaytime = False

def hourly_api_req():
    response = requests.get("https://api.weather.gov/gridpoints/BUF/74,60/forecast/hourly")
    json = response.json()
    properties = json["properties"]["periods"]

    wind = properties[0]["windSpeed"]

    hourNumber.clear()
    hourlyTemp.clear()
    hourlyIcons.clear()

    for i in range(0,5):
        hour = properties[i]["number"]
        hourNumber.append(hour)
        hourlyTemp.append(properties[i]["temperature"])
        hourlyIcons.append(properties[i]["icon"])
        
def daily_api_req():
    response = requests.get("https://api.weather.gov/gridpoints/BUF/74,60/forecast/")
    json = response.json()
    properties = json["properties"]["periods"]

    dailyForecast = properties[0]["detailedForecast"]
    isDaytime = properties[0]["isDaytime"]


def test_api_pull(link:str):
    response = requests.get(link)
    print("\nStatus code = " +str(response.status_code))
    print("\n\nContent = "+ str(response.content))
    print("\n\nText = "+ str(response.text))
    print("\n\nJson = "+ str(response.json()))

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    

def main():
    print("Api output:\n")
    response = requests.get("https://api.weather.gov/gridpoints/BUF/74,60/forecast/hourly")
    json = response.json()
    properties = json["properties"]["periods"]
    hours = []
    
    for i in properties:
        hour = i["number"]
        hours.append(hour)
        

    #jprint(properties)
    print (hours)

main()
