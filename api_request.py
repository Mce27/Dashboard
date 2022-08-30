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
        hourTime.append(properties[i]["startTime"])
    
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
    
def cli():
    """
    A command line interface for the weather api
    Displays the daily forcast, 5 hours of weather and the current wind
    """
    hourNumber = []
    hourlyTemp = []
    hourTime=[]
    wind = "uhhh"
    hourlyIcons= []
    dailyForecast = "uhhh"
    isDaytime = False

    wind,hourNumber, hourlyTemp, hourlyIcons, hourTime = hourly_api_req(wind,hourNumber,hourlyTemp,hourlyIcons,hourTime)
    dailyForecast, isDaytime = daily_api_req(dailyForecast,isDaytime)
    print("Daily Forecast: \n"+ dailyForecast+ "\n")

    for n in hourNumber:
        print("Hour: "+ str(hourTime[n-1])+ "\n")
        print("Temp: "+ str(hourlyTemp[n-1])+ "\n")
    
    print("Wind: "+wind)
        
    input("Press enter to end")
    

def main():
    cli()

main()
