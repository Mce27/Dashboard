from api_request import *

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

    wind,hourNumber,hourlyTemp,hourlyIcons,hourTime,date = hourly_api_req(wind,hourNumber,hourlyTemp,hourlyIcons,hourTime)
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