from ast import Lambda
from asyncio.windows_events import NULL
from email.mime import image
import queue
import threading
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
hourImgList = []
hourTempList = []
hourWindList = [] 
for i in range(0,HOURNUM):
    hourImgList.append(ttk.Label(hourfrm,image=tkinter.PhotoImage("./icons/cry.png")))
    hourTempList.append(StringVar(hourfrm,value=str(0)))
    hourTimelist.append(StringVar(hourfrm,value=str(0)))
    hourWindList.append(StringVar(hourfrm,value=str(0)))

async def updateWeather():
    while True:
        await asyncio.sleep(120)

        global dailyForecast 
        global isDaytime
        global data
        global hourImgList
        data = hourly_api_req()
        hourlyImages = []
        for i in data.values():
            hourlyImages.append(i[2])
        hourlyImgPath = photoDown(hourlyImages)
        for i in range(0,len(hourImgList)):
            #hourlyImg.append(tkinter.PhotoImage(file=path))
            img = (ImageTk.PhotoImage((Image.open(hourlyImgPath[i])).resize(((56*3),(56*3)))))  # type: ignore
            hourImgList[i].configure(image=img)
            hourImgList[i].image = img  #VERY NEEDED
        #dailyForecast,isDaytime
        dailyForecast,isDaytime= daily_api_req()
        #hourlyImgPath = await photoDown(hour[])
        #dailyForecast,isDaytime = await daily_api_req()
        print('weather obtained') 
        #gui_queue.put(lambda: 
        updateWeatherGui(data,hourImgList,dailyForecast,isDaytime)



def updateWeatherGui(hour_data:dict,hourImgList1:list,dailyForcast1:str,isDaytme:bool):
    """
    updates the hourTimeList, hourTempList, hourWindList, dateVar, dailyForcastVar 
    should update gui
    """  
    dateVar.set(hour_data[1][4])
    dailyForcastVar.set(dailyForcast1)
    for i in range(0,len(hourTimelist)):
        hourTimelist[i].set(hour_data[i+1][3])
        hourTempList[i].set((str(hour_data[i+1][1]))+"°F")
        hourWindList[i].set(str(hour_data[i+1][0]))
    
    
    print('weather GUI refreshed')


def infoUpdate():
    global dailyForecast 
    global isDaytime
    global data
    global hourImgList
    data = hourly_api_req()
    hourlyImages = []
    for i in data.values():
        hourlyImages.append(i[2])
    hourlyImgPath = photoDown(hourlyImages)
    for i in range(0,len(hourImgList)):
        #hourlyImg.append(tkinter.PhotoImage(file=path))
        img = (ImageTk.PhotoImage((Image.open(hourlyImgPath[i])).resize(((56*3),(56*3)))))  # type: ignore
        hourImgList[i].configure(image=img)
        hourImgList[i].image = img  #VERY NEEDED
    #dailyForecast,isDaytime
    dailyForecast,isDaytime= daily_api_req()
    
async def test():
    """
    a test to figure out async
    #TODO remove when finished
    """
    await asyncio.sleep(5)
    global hourTimelist
    global hourImgList
    global dateVar
    global dailyForcastVar

    img = (ImageTk.PhotoImage((Image.open("./icons/cry.png")).resize(((56*3),(56*3)))))# type: ignore
    for i in range(0,len(hourTimelist)):
        hourTimelist[i].set(5)
        hourImgList[i].configure(image=img)
        hourImgList[i].image=img
    
    dateVar.set("today")
    dailyForcastVar.set("wimdy")


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
        hourTempList[i].set((str(data[i+1][1]))+"°F")
        hourWindList[i].set(str(data[i+1][0]))
        ttk.Label(hourfrm,textvariable= hourTimelist[i],font=Mfont).grid(column=i,row=1)
        ttk.Label(hourfrm,textvariable= hourTempList[i],font=Mfont).grid(column=i,row=3)
        ttk.Label(hourfrm,textvariable= hourWindList[i],font=Mfont).grid(column=i,row=4)
        hourImgList[i].grid(column=i,row=2)
        #print(hourImgList[i].cget('image'))

        
    
    def start_loop():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.create_task(updateWeather())
        loop.run_forever()
    threading.Thread(target=start_loop).start()

    #starts the gui
    root.mainloop()

def main():
    gui()

main()