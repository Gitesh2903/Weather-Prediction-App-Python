from tkinter import *
import tkinter as tk
import folium
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from datetime import *
import requests
import pytz
import math
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj= TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    city_name=city

    #city_name=city
    api_key="af7484715ffb62f9849957a59620c753"
    #exclude = 'minutely,hourly,main,weather'

    def get_weather(api_key,city_name):
        #url=f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
#http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}
        forecast_url = 'http://api.openweathermap.org/data/2.5/forecast'
        forecast_params = {
            'q': city,
            'appid': 'af7484715ffb62f9849957a59620c753',
            'units': 'metric'
        }

        # Set the API endpoint URL and parameters for today's weather
        today_url = 'http://api.openweathermap.org/data/2.5/weather'
        today_params = {
            'q': city,
            'appid': '4d4025e09c70c93385293bf58af15cbf',

            'units': 'metric'
        }
        today_response = requests.get(today_url, params=today_params)

        today_data = today_response.json()

        response = requests.get(forecast_url, params=forecast_params)
        json_data = response.json()
        temperature_data = {}

        # Extract and store date-wise day and night temperatures
        today = datetime.now()

        for forecast in json_data["list"]:
            forecast_datetime = datetime.fromtimestamp(forecast["dt"])
            forecast_date = forecast_datetime.date()



        for forecast in json_data['list']:
            date = forecast['dt_txt'][:10]
            temperature = forecast['main']['temp']
            time = forecast['dt_txt'][-8:-3]

            if date not in temperature_data:
                temperature_data[date] = {'Day Temperature': None, 'Night Temperature': None}

            if time == '12:00':
                temperature_data[date]['Day Temperature'] = temperature
            elif time == '00:00':
                temperature_data[date]['Night Temperature'] = temperature

        #json_data=requests.get(url).json()
        #current_date = datetime.now().strftime('%Y-%m-%d')
        print(json_data)

        temp=today_data['main']['temp']
        humidity=today_data['main']['humidity']
        pressure=today_data['main']['pressure']
        wind_speed=today_data['wind']['speed']
        description=today_data['weather'][0]['description']

        #temp=math.floor(temp-273.5)


        t.config(text=(temp,"°C"))
        h.config(text=(humidity,"%"))
        p.config(text=(pressure,"hPa"))
        w.config(text=(wind_speed,"m/s"))
        d.config(text=description)


        #frist cell


        firstdayimage=json_data['list'][0]['weather'][0]['icon']
        photo1=ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
        firstimage.config(image=photo1)
        firstimage.image=photo1
        date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

        # Check if the date exists in the temperature_data dictionary
        if date in temperature_data:
            temperature_info = temperature_data[date]
            day_temperature1 = temperature_info['Day Temperature']
            night_temperature1 = temperature_info['Night Temperature']
            day1temp.config(text=f"Day:{day_temperature1}\n Night:{night_temperature1}")

        # tempday1 = json_data['list'][0]['main']['temp_max']
        # tempnight1 = json_data['list'][0]['main']['temp_min']
        #
        # day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")

        # second cell



        seconddayimage = json_data['list'][1]['weather'][0]['icon']

        img=(Image.open(f"icon/{seconddayimage}@2x.png"))
        resized_image=img.resize((50,50))
        photo2=ImageTk.PhotoImage(resized_image)
        secondimage.config(image=photo2)
        secondimage.image=photo2

        date = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')

        # Check if the date exists in the temperature_data dictionary
        if date in temperature_data:
            temperature_info = temperature_data[date]
            day_temperature2 = temperature_info['Day Temperature']
            night_temperature2 = temperature_info['Night Temperature']
            day2temp.config(text=f"Day:{day_temperature2}\n Night:{night_temperature2}")

        # tempday2 = json_data['list'][1]['main']['temp_max']
        # tempnight2 = json_data['list'][1]['main']['temp_min']
        #
        # day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")



        # third cell

        thirddayimage = json_data['list'][2]['weather'][0]['icon']
        img = (Image.open(f"icon/{thirddayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo3 = ImageTk.PhotoImage(resized_image)
        thirdimage.config(image=photo3)
        thirdimage.image = photo3

        date = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')

        # Check if the date exists in the temperature_data dictionary
        if date in temperature_data:
            temperature_info = temperature_data[date]
            day_temperature3 = temperature_info['Day Temperature']
            night_temperature3 = temperature_info['Night Temperature']
            day3temp.config(text=f"Day:{day_temperature3}\n Night:{night_temperature3}")

        # tempday3 = json_data['list'][2]['main']['temp_max']
        # tempnight3 = json_data['list'][2]['main']['temp_min']
        #
        # day3temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")





        #fourth cell
        fourthdayimage = json_data['list'][3]['weather'][0]['icon']
        img = (Image.open(f"icon/{fourthdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo4 = ImageTk.PhotoImage(resized_image)
        fourthimage.config(image=photo4)
        fourthimage.image = photo4

        date = (datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d')

        # Check if the date exists in the temperature_data dictionary
        if date in temperature_data:
            temperature_info = temperature_data[date]
            day_temperature4 = temperature_info['Day Temperature']
            night_temperature4 = temperature_info['Night Temperature']
            day4temp.config(text=f"Day:{day_temperature4}\n Night:{night_temperature4}")

        # tempday4 = json_data['list'][3]['main']['temp_max']
        # tempnight4 = json_data['list'][3]['main']['temp_min']
        #
        # day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")



        #fifth cell
        fifthdayimage = json_data['list'][4]['weather'][0]['icon']
        img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo5 = ImageTk.PhotoImage(resized_image)
        fifthimage.config(image=photo5)
        fifthimage.image = photo5

        date = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')

        # Check if the date exists in the temperature_data dictionary
        if date in temperature_data:
            temperature_info = temperature_data[date]
            day_temperature5 = temperature_info['Day Temperature']
            night_temperature5 = temperature_info['Night Temperature']
            day5temp.config(text=f"Day:{day_temperature5}\n Night:{night_temperature5}")

        # tempday5 = json_data['list'][4]['main']['temp_max']
        # tempnight5 = json_data['list'][4]['main']['temp_min']
        #
        # day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")




        #sixth cell
        sixthdayimage = json_data['list'][5]['weather'][0]['icon']
        img = (Image.open(f"icon/{sixthdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo6 = ImageTk.PhotoImage(resized_image)
        sixthimage.config(image=photo6)
        sixthimage.image = photo6

        date = (datetime.now() + timedelta(days=6)).strftime('%Y-%m-%d')

        # Check if the date exists in the temperature_data dictionary
        if date in temperature_data:
            temperature_info = temperature_data[date]
            day_temperature6 = temperature_info['Day Temperature']
            night_temperature6 = temperature_info['Night Temperature']
            day6temp.config(text=f"Day:{day_temperature6}\n Night:{night_temperature6}")

        # tempday6 = json_data['list'][5]['main']['temp_max']
        # tempnight6 = json_data['list'][5]['main']['temp_min']
        #
        # day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")






        #days

        first = datetime.now()
        day1.config(text=first.strftime("%A"))

        second = first+timedelta(days=1)
        day2.config(text=second.strftime("%A"))

        third = first + timedelta(days=2)
        day3.config(text=third.strftime("%A"))

        fourth = first + timedelta(days=3)
        day4.config(text=fourth.strftime("%A"))

        fifth = first + timedelta(days=4)
        day5.config(text=fifth.strftime("%A"))

        sixth = first + timedelta(days=5)
        day6.config(text=sixth.strftime("%A"))




    get_weather(city_name,api_key)





    #weather
    #api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly,daily&appid=ae55d878ebb9d72f105380828e646b2f"
    #json_data=requests.get(api).json()

    #current
   ## temp=json_data['current']['temp']
   # humidity=json_data['current']['humidity']
    #pressure=json_data['current']['pressure']
    #wind=json_data['current']['wind_speed']
    #description=json_data['current']['weather'][0]['description']
    #print(temp)
    #print(humidity)
    #print(pressure)
    #print(wind)
    #print(description)

##icon
image_icon = PhotoImage(file="Images\logo.png")
root.iconphoto(False, image_icon)


Round_box=PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root,image=Round_box,bg="#57adff").place(x=45,y=110)

#label
label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=50,y=180)

label5=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=50,y=200)

##search box
Search_image=PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="Images/Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)

textfield.focus()

Search_icon=PhotoImage(file="Images/Layer 6.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)


#button

button_icon=PhotoImage(file="Images/button.jpg")
button=Button(image=button_icon ,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
button.place(x=800,y=20)

##Bottom box

frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox=PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=20)
#Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)

#clock
clock=Label(root,font=("helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)





#timezone
timezone=Label(root,font=("helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat=Label(root,font=("helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)

#thpwd
t=Label(root,font=("Hevletica",11),fg="white",bg="#203243")
t.place(x=150,y=120)
h=Label(root,font=("Hevletica",11),fg="white",bg="#203243")
h.place(x=150,y=140)
p=Label(root,font=("Hevletica",11),fg="white",bg="#203243")
p.place(x=150,y=160)
w=Label(root,font=("Hevletica",11),fg="white",bg="#203243")
w.place(x=150,y=180)
d=Label(root,font=("Hevletica",11),fg="white",bg="#203243")
d.place(x=150,y=200)


#first cell
firstframe=Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=315)

day1=Label(firstframe,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=100,y=5)

firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

day1temp=Label(firstframe,bg="#282829",fg="#57adff",font="arial 15 bold")
day1temp.place(x=100,y=50)


#second cell
secondframe=Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=305,y=325)

day2=Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=7,y=5)

secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=7,y=25)

day2temp=Label(secondframe,bg="#282829",fg="#fff")
day2temp.place(x=2,y=70)


#third cell
thirdframe=Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=405,y=325)

day3=Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=7,y=5)

thirdimage=Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=25)

day3temp=Label(thirdframe,bg="#282829",fg="#fff")
day3temp.place(x=2,y=70)

#fourth cell
fourthframe=Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=505,y=325)

day4=Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=7,y=5)

fourthimage=Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=25)

day4temp=Label(fourthframe,bg="#282829",fg="#fff")
day4temp.place(x=2,y=70)

#fifth cell
fifthframe=Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=605,y=325)

day5=Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=7,y=5)

fifthimage=Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=25)

day5temp=Label(fifthframe,bg="#282829",fg="#fff")
day5temp.place(x=2,y=70)

#sixth cell
sixthframe=Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=705,y=325)

day6=Label(sixthframe,bg="#282829",fg="#fff")
day6.place(x=7,y=5)

sixthimage=Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=25)

day6temp=Label(sixthframe,bg="#282829",fg="#fff")
day6temp.place(x=2,y=70)

#seventh cell
#seventhframe=Frame(root,width=70,height=115,bg="#282829")
# seventhframe.place(x=805,y=325)
#
# day7=Label(seventhframe,bg="#282829",fg="#fff")
# day7.place(x=10,y=5)
#
# seventhimage=Label(seventhframe,bg="#282829")
# seventhimage.place(x=7,y=25)





















root.mainloop()
