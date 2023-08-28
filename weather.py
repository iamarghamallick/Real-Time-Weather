# pip install geopy
# pip install timezonefinder
# pip install requests
# pip install pytz

API_KEY = "c4910bb187874a6893f170604232603"

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Real Time Weather Update")
root.iconbitmap('favicon.ico')
root.geometry("900x500+300+200")
root.resizable(False, False)

def get_weather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()

        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")

        # fetch api
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
        weather = requests.get(url).json()
        print(weather)

        time_zone = weather['location']['tz_id']
        condition = weather['current']['condition']['text']
        temp = weather['current']['temp_c']
        real_feel = weather['current']['feelslike_c']
        pressure = weather['current']['pressure_mb']
        humidity = weather['current']['humidity']
        wind = weather['current']['wind_kph']
        cloud = weather['current']['cloud']

        clock.config(text=f"Current Weather | {current_time}")
        tz.config(text=f"Time Zone - {time_zone}")
        t.config(text=(temp, "°C"))
        c.config(text=f"{condition} | FEELS LIKE {real_feel} °C")
        w.config(text=(wind, "kph"))
        h.config(text=(humidity))
        cld.config(text=f"{cloud}%")
        p.config(text=(pressure, "mb"))

    except Exception as e:
        messagebox.showerror("Weather App", "Some Error Occured!")
        print(e)

# search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0,cursor="hand2", bg="#404040", command=get_weather)
myimage_icon.place(x=400, y=34)

# logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
clock = Label(root, font=("Helvetica", 20), text="Get weather on Real Time")
clock.place(x=500, y=40)

# label
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'),fg="white",bg="#1ab5ef")
label2.place(x=300, y=400)

label3 = Label(root, text="CLOUDS", font=("Helvetica", 15, 'bold'),fg="white",bg="#1ab5ef")
label3.place(x=500, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'),fg="white",bg="#1ab5ef")
label4.place(x=680, y=400)

# time zone
tz = Label(root, font=("arial", 15, "bold"))
tz.place(x=420, y=140)

t=Label(font=("arial",70,"bold"),fg="#ee666d", text="Search")
t.place(x=410,y=170)

c=Label(font=("arial",15, "bold"), text="Your Location")
c.place(x=420,y=270)

w=Label(text= "..............",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=90, y=430)

h=Label(text= "....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=330, y=430)

cld=Label(text= ".......",font=("arial",20,"bold"),bg="#1ab5ef")
cld.place(x=515, y=430)

p=Label(text= "................",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
