import requests
import json



def hourly_api_req(wind,hourNumber,hourlyTemp,hourlyIcons,hourTime):
    """
    This is the api request that is to be run hourly
    Updates hourNumber, hourlyTemp, and hourlyIcons
    """
    response = requests.get("https://api.weather.gov/gridpoints/BUF/74,60/forecast/hourly")
    json = response.json()
    properties = json["properties"]["periods"]

    wind = properties[0]["windSpeed"]

    hourNumber.clear()
    hourlyTemp.clear()
    hourlyIcons.clear()
    hourTime.clear()

    for i in range(0,5):
        hour = properties[i]["number"]
        hourNumber.append(hour)
        hourlyTemp.append(properties[i]["temperature"])
        hourlyIcons.append(properties[i]["icon"])
        hourTime.append((dateTime_interpreter(properties[i]["startTime"])))
    
    return wind,hourNumber,hourlyTemp,hourlyIcons,hourTime
        
def daily_api_req(dailyForecast,isDaytime):
    """
    This is the api request that is to be run (semi)daily
    Updates dailyForecast and isDaytime 
    """
    response = requests.get("https://api.weather.gov/gridpoints/BUF/74,60/forecast/")
    json = response.json()
    properties = json["properties"]["periods"]

    dailyForecast = properties[0]["detailedForecast"]
    isDaytime = properties[0]["isDaytime"]
    return dailyForecast,isDaytime

def test_api_pull(link:str):
    """
    Used to test if a api request is successful
    """
    response = requests.get(link)
    print("\nStatus code = " +str(response.status_code))
    print("\n\nContent = "+ str(response.content))
    print("\n\nText = "+ str(response.text))
    print("\n\nJson = "+ str(response.json()))

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def dateTime_interpreter(Time:str):
    """
    Takes a date and time in YYYY-MM-DDTHH:MM:SS-HH:MM and converts it to a more readable date and time
    """
    output = 0
    output += int(Time[11]+Time[12])
    
    if output > 12:
        output = output-12
    
    return output
