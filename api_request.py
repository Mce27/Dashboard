import requests
import json
import shutil



def hourly_api_req(wind,hourNumber,hourlyTemp,hourlyIcons,hourTime):
    """
    This is the api request that is to be run hourly
    Updates wind,hourNumber, hourlyTemp, and hourlyIcons
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
        time,date=(dateTime_interpreter(properties[i]["startTime"]))
        hourTime.append(time)

    
    return wind,hourNumber,hourlyTemp,hourlyIcons,hourTime,date

def photoDown(hourlyIcons):
    """
    Goes through the urls in the list and return a list with the image paths
    Downloads to local storage
    """
    i = 0
    hourlyImgPath = []
    for url in hourlyIcons:
        img = requests.get(url,stream=True)
        
        img.raw.decode_content = True
        
        with open("./icons/"+str(i),'wb') as f:
            shutil.copyfileobj(img.raw,f)
        hourlyImgPath.append("./icons/"+str(i))
        i+=1
    return hourlyImgPath

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
    returns time, date
    """
    date = "Today is "+Time[5]+Time[6]+"/"+Time[8]+Time[9]+"/"+Time[0]+Time[1]+Time[2]+Time[3]
    tim = int(Time[11]+Time[12])
    output = ""
    if tim > 12:
        tim = tim-12
        output = str(tim) + "pm"
    else:
        if tim == 12:
            output = str(tim) + "pm"
        else:
            output = str(tim) + "am"

    
    return output,date
