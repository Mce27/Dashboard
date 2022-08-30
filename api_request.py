from tokenize import String
import requests
import json

hourNumber = []
hourlyTemp = []
wind = ""
shortForecast = ""
hourlyIcons= []
dailyForecast = ""
isDaytime = False



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
