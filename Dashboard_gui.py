from ast import Lambda
from asyncio.windows_events import NULL
from email.mime import image
import queue
from tkinter import *
from tkinter import ttk
import tkinter
from api_request import *
from PIL import Image ,ImageTk
import asyncio
import time

data={}
dailyForecast = str("uhhh")
isDaytime = False
Mfont=["Comic sans MS", 20]

root = Tk()
root.grid()
frm = ttk.Frame(root, padding="20")
frm.grid(column=0,row=0)
hourfrm = ttk.Frame(root,padding="10")
hourfrm.grid(column=0,row=1)
gui_queue = queue.Queue()
#all labels to follow
dateVar =StringVar(frm)
ttk.Label(frm,textvariable=dateVar,font=Mfont).grid(column=0,row=0)


dailyForcastVar = StringVar(frm)
ttk.Label(frm,textvariable=dailyForcastVar,font=Mfont).grid(column=0, row=1)


hourTimelist = []
hourlyImgList = []
for i in range(0,HOURNUM):
    hourlyImgList.append(ttk.Label(hourfrm,image=tkinter.PhotoImage("./icons/cry.png")))
    
    hourTimelist.append(StringVar(hourfrm,value=str(0)))

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
"""

def infoUpdate():
    global dailyForecast 
    global isDaytime
    global data
    global hourlyImgList
    data = hourly_api_req()
    hourlyImages = []
    for i in data.values():
        hourlyImages.append(i[2])
    hourlyImgPath = photoDown(hourlyImages)
    for i in range(0,len(hourlyImgList)):
        #hourlyImg.append(tkinter.PhotoImage(file=path))
        img = (ImageTk.PhotoImage((Image.open(hourlyImgPath[i])).resize(((56*3),(56*3)))))  # type: ignore
        hourlyImgList[i].configure(image=img)
    #dailyForecast,isDaytime
    dailyForecast,isDaytime= daily_api_req()
    

    

def gui():
    """
    A gui interface for the weather api
    Displays the daily forcast, 5 hours of weather and the current wind
    Updates every hour
    """ 
    infoUpdate()
    root.title("DashBoard")
    dateVar.set(data[1][4])
    dailyForcastVar.set(dailyForecast)
    for i in range(0,len(hourTimelist)):
        hourTimelist[i].set(data[i+1][3])
        ttk.Label(hourfrm,textvariable= hourTimelist[i],font=Mfont).grid(column=i,row=1)
        hourlyImgList[i].grid(column=i,row=2)
        print(hourlyImgList[i].cget('image'))

        
    
    

    #root.after(3000,lambda:hourTime0.set("6") )
    #starts the gui
    root.mainloop()

def main():
    gui()

main()