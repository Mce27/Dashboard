from tkinter import *
from tkinter import ttk
import tkinter
from api_request import *

hourNumber = []
hourlyTemp = []
hourTime=[]
wind = "uhhh"
hourlyIcons= []
dailyForecast = "uhhh"
isDaytime = False
hourlyImg = []

def infoUpdate():
    global hourNumber 
    global hourlyTemp
    global hourTime
    global wind 
    global hourlyIcons
    global hourlyImg
    global dailyForecast 
    global isDaytime
    wind,hourNumber,hourlyTemp,hourlyIcons,hourTime=hourly_api_req(wind,hourNumber,hourlyTemp,hourlyIcons,hourTime)
    hourlyImgPath = photoDown(hourlyIcons)
    for path in hourlyImgPath:
        hourlyImg.append(tkinter.PhotoImage(file=path))
    dailyForecast,isDaytime= daily_api_req(dailyForecast,isDaytime)
    

    

def gui():
    """
    A gui interface for the weather api
    Displays the daily forcast, 5 hours of weather and the current wind
    Updates every hour
    """
    
    
    #create the root of the gui
    root = Tk()
    infoUpdate()
    root.title("DashBoard")
    frame = ttk.Frame(root)
    frame.grid()
    #ttk.Label(frame,image=hourlyImg[0]).grid(column=0,row=0)

   
    frm = ttk.Frame(root, padding="20")
    frm.grid()
    hourfrm = ttk.Frame(root,padding="10")
    hourfrm.grid()
    ttk.Label(frm,text=dailyForecast).grid(column=0, row=0)
    for hour in hourNumber:
        ttk.Label(hourfrm,image=hourlyImg[hour-1]).grid(column=hour-1,row=2)
        ttk.Label(hourfrm,text=hourTime[hour-1]).grid(column=hour-1,row=1)
        ttk.Label(hourfrm,text=str(hourlyTemp[hour-1]) + "F").grid(column=hour-1,row=3)
    

    #ttk.Label(frm, text= "the weather").grid(column=0,row=0)
    #ttk.Button(frm, text="exit",command=root.destroy).grid(column=1,row=0)

    #starts the gui
    root.mainloop()

def main():
    gui()

main()