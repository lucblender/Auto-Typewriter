
from PIL import Image

from GCalendarEvents import getEvents

from datetime import datetime
from datetime import timedelta  

from columnar import columnar

from A4Pages import A4Page

from AsciiGenerator import convertImageToAscii
from KeyDictionnary import *
from AutoTypewriter import AutoTypewriter

page = A4Page()

events = getEvents()
headers  = []
today  =datetime.today()
monday = today - timedelta(days=today.weekday())
sunday = monday+ timedelta(days=6)
day = monday
for i in range(0,6):
    headers.append(day.strftime("%a\n%d"))
    day = day+ timedelta(days=1)

data = [[""]*7 for i in range(24)]

for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    start_datetime = datetime.fromisoformat(start)
    end = event['end'].get('dateTime', event['end'].get('date'))
    end_datetime = datetime.fromisoformat(start)    
    day_index = start_datetime.weekday()
    hour_index = start_datetime.hour 
    event_text = event['summary']
    event_time = start_datetime.strftime("%H:%M") #+"\n"+end_datetime.strftime("%H:%M")
    if data[hour_index][day_index] != "":
        data[hour_index][day_index]+= "========\n"
    data[hour_index][day_index]+=(event_time+"\n"+event_text+"\n")
    
while(data[0] == ['']*7):
    data.pop(0)
    
while(data[-1] == ['']*7):
    data.pop()


table = columnar(data, headers, min_column_width=9, max_column_width=9, terminal_width=65,column_sep="'")


img = Image.open("Calendar_icon.png")
ascii_img = convertImageToAscii(img, 30, 0.5, False)
page.insert_text(ascii_img, 30, 1)
page.insert_line("=", 0)
page.insert_line("_", 16)
page.insert_text("Calendar of week "+str(monday.isocalendar()[1]), 3, 4)
page.insert_text("From "+monday.strftime("%a, the %d %b %Y"), 3, 7)
page.insert_text("To   "+sunday.strftime("%a, the %d %b %Y"), 3, 8)
page.insert_text("_"*25, 3, 10)
page.insert_text(str(len(events))+ " event(s) this week", 3, 13)

page.insert_text(table, 2, 18)

split_table = table.splitlines()


page.insert_line("=", 18+len(split_table)+2)

print(str(page))
test_string(str(page))
auto_typewriter = AutoTypewriter()
auto_typewriter.press_string(str(page))


