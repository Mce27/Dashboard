from ast import Lambda
import queue
from tkinter import *
from tkinter import ttk
import tkinter
from api_request import *
from PIL import Image ,ImageTk
import asyncio
import time

hourNumber = []
hourlyTemp = []
hourTime=[]
wind = str("uhhh")
hourlyIcons= []
dailyForecast = str("uhhh")
isDaytime = False
hourlyImg = []
date=str("")
Mfont=["Comic sans MS", 20]

root = Tk()
frm = ttk.Frame(root, padding="20")
frm.grid()
hourfrm = ttk.Frame(root,padding="10")
hourfrm.grid()
gui_queue = queue.Queue()

#all labels to follow
dateVar =StringVar(frm)
dateLabel= ttk.Label(frm,textvariable=dateVar)
dateLabel.grid(column=0,row=0)

dailyForcastVar = StringVar(frm)
dailyForecastLabel=ttk.Label(frm,textvariable=dailyForcastVar)
dailyForecastLabel.grid(column=0, row=1)

hourlyImg0=ttk.Label(hourfrm).grid(column=0,row=2)
hourlyImg1=ttk.Label(hourfrm).grid(column=1,row=2)
hourlyImg2=ttk.Label(hourfrm).grid(column=2,row=2)
hourlyImg3=ttk.Label(hourfrm).grid(column=3,row=2)
hourlyImg4=ttk.Label(hourfrm).grid(column=4,row=2)
hourTimelist = []
for i in range(0,5):
    hourTimelist[i].append(StringVar(hourfrm,value=str(0)))
    
"""
hourTime0 =StringVar(hourfrm,value=str(0))
hourTime1 =StringVar(hourfrm,value=str(0))
hourTime2 =StringVar(hourfrm,value=str(0))
hourTime3 =StringVar(hourfrm,value=str(0))
hourTime4 =StringVar(hourfrm,value=str(0))
"""


async def updateWeather():
    while True:
        wind,hourNumber,hourlyTemp,hourlyIcons,hourTime,date = await hourly_api_req()
        hourlyImgPath = await photoDown(hourlyIcons)
        dailyForecast,isDaytime = await daily_api_req()
        print('weather obtained') 
        gui_queue.put(lambda: updateWeatherGui(wind,hourNumber,hourlyTemp,hourlyIcons,hourTime,
                                                date,hourlyImgPath,dailyForecast,isDaytime))
        await asyncio.sleep(30)
        
def updateWeatherGui(wind1:str,hourNumber1:list,hourlyTemp1:list,hourlyIcons1:list,hourTime1:list,date1:str,hourlyImgPath1,dailyForecast1,isDaytime1):
    
    
    
    
    print('weather GUI refreshed')


def infoUpdate():
    global hourNumber 
    global hourlyTemp
    global hourTime
    global wind 
    global hourlyIcons
    global hourlyImg
    global dailyForecast 
    global isDaytime
    global date
    #wind,hourNumber,hourlyTemp,hourlyIcons,hourTime
    wind,hourNumber,hourlyTemp,hourlyIcons,hourTime,date=hourly_api_req()
    hourlyImgPath = photoDown(hourlyIcons)
    for path in hourlyImgPath:
        #hourlyImg.append(tkinter.PhotoImage(file=path))
        hourlyImg.append(ImageTk.PhotoImage((Image.open(path)).resize(((56*3),(56*3)))))
    #dailyForecast,isDaytime
    dailyForecast,isDaytime= daily_api_req()
    

    

def gui():
    """
    A gui interface for the weather api
    Displays the daily forcast, 5 hours of weather and the current wind
    Updates every hour
    """
    
    #create the root of the gui
    
    infoUpdate()
    root.title("DashBoard")
    #frame = ttk.Frame(root)
    #frame.grid()
    #ttk.Label(frame,image=hourlyImg[0]).grid(column=0,row=0)
    
    dateLabel= ttk.Label(frm, text=date, font=Mfont)
    
    dailyForecastLabel=ttk.Label(frm, text=dailyForecast, font=Mfont)

    for hour in hourNumber:
        ttk.Label(hourfrm, image=hourlyImg[hour-1]).grid(column=hour-1,row=2)
        ttk.Label(hourfrm, textvariable=hourTime0, font=Mfont).grid(column=hour-1,row=1)
        ttk.Label(hourfrm, text=str(hourlyTemp[hour-1]) + " °F", font=Mfont).grid(column=hour-1,row=3)

    #ttk.Label(frm, text= "the weather").grid(column=0,row=0)
    #ttk.Button(frm, text="exit",command=root.destroy).grid(column=1,row=0)
    #root.after(3000,lambda:hourTime0.set("6") )
    #starts the gui
    root.mainloop()

def main():
    gui()

main()