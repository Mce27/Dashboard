from api_request import *

def cli():
    """
    A command line interface for the weather api
    Displays the daily forcast, 5 hours of weather and the current wind
    """
    data = hourly_api_req()
    dailyForecast, isDaytime = daily_api_req()
    print("Daily Forecast: \n"+ dailyForecast+ "\n")

    for n in data:
        print("Hour: "+ str(data[n][3])+ "\n")
        print("Temp: "+ str(data[n][1])+ "\n")
        print("Wind: "+str(data[n][0])+"\n\n")
    
    
        
    input("Press enter to end")

def main():
    cli()

main()