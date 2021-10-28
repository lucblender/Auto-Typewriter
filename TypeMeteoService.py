import requests
import json
import datetime
from PIL import Image
from io import BytesIO
from pyfiglet import Figlet
from AsciiGenerator import convertImageToAscii

from KeyDictionnary import test_string
from AutoTypewriter import AutoTypewriter

from A4Pages import A4Page

class DayPrevision():
    def __init__(self, datetime_day, temp_min, temp_max, weather_type, weather_type_id, ascii_img):
        self.datetime_day    = datetime_day 
        self.temp_min        = temp_min 
        self.temp_max        = temp_max 
        self.weather_type    = weather_type 
        self.weather_type_id = weather_type_id
        self.ascii_img       = ascii_img
        
day_previsions = [] 

def data_from_day(day):
    global day_previsions
    dt = day["dt"]
    datetime_day = datetime.datetime.fromtimestamp(dt)
    week_day = datetime_day.strftime('%A')
    temp_min = day["temp"]["min"]
    temp_max = day["temp"]["max"]
    weather_type = day["weather"][0]["main"]
    weather_type_id = day["weather"][0]["icon"]
    weather_type_icon_url = "http://openweathermap.org/img/wn/"+weather_type_id+"@4x.png"
    response = requests.get(weather_type_icon_url)
    img = Image.open(BytesIO(response.content))
    ascii_img = convertImageToAscii(img, 20, 0.43, False)
    day_prevision = DayPrevision(datetime_day, temp_min, temp_max, weather_type, weather_type_id,ascii_img) 
    day_previsions.append(day_prevision)

custom_fig = Figlet(font='basic')
page = A4Page()

URI = "https://api.openweathermap.org/data/2.5/onecall?lat=46.229352&lon=7.362049&units=metric&exclude=hourly,minutely&appid="
API_KEY = ""

r = requests.get(URI+API_KEY)

json_r = json.loads(r.text)

day = json_r["current"]
dt = day["dt"]
datetime_day = datetime.datetime.fromtimestamp(dt)
week_day = datetime_day.strftime('%A')
temp = day["temp"]
weather_type = day["weather"][0]["description"]
weather_type_id = day["weather"][0]["icon"]
weather_type_icon_url = "http://openweathermap.org/img/wn/"+weather_type_id+"@4x.png"
response = requests.get(weather_type_icon_url)
img = Image.open(BytesIO(response.content))
ascii_img = convertImageToAscii(img, 35, 0.43, False)
print(week_day, temp, weather_type, weather_type_id, weather_type_icon_url)
print(ascii_img)

for day in json_r["daily"]:
    data_from_day(day)

weather_txt = custom_fig.renderText('Weather')
report_txt = custom_fig.renderText('report')

page.insert_text(weather_txt, 0, 0)
page.insert_text(report_txt, 13, 7)
page.insert_line("=", 15)
page.insert_text(ascii_img, 0, 17)
page.insert_text("Today weather :", 3, 17)
page.insert_text(datetime_day.strftime("%A the %d %B %Y"), 30, 22)
page.insert_text("Weather type: "+ weather_type, 30, 24)
page.insert_text("Current temperature: "+ str(temp)+"°C", 30, 26)
page.insert_line("-", 30)
page.insert_text("Next 3 days prevision :", 3, 32)

for i in range(1,4):
    page.insert_text(day_previsions[i].ascii_img,3, 34+(i-1)*7)
    
for i in range(1,4):
    day_prevision = day_previsions[i]
    page.insert_text(day_prevision.ascii_img,3, 34+(i-1)*7)    
    page.insert_text(day_prevision.datetime_day.strftime("%A the %d %B %Y"), 30, 37+(i-1)*7)
    page.insert_text("Weather type: "+ day_prevision.weather_type, 30, 38+(i-1)*7)
    page.insert_text("Temperature range: "+ str(day_prevision.temp_min)+ "°C-" + str(day_prevision.temp_max)+"°C", 30, 39+(i-1)*7)
    page.insert_text("_"*34,30, 40+(i-1)*7)

page.insert_line("=", 59)

str_to_print = str(page)
str_to_print = str_to_print.replace('~', '-')
str_to_print = str_to_print.replace('`', "'")

print(str_to_print)

test_string(str_to_print)
auto_typewriter = AutoTypewriter()
auto_typewriter.press_string(str_to_print)