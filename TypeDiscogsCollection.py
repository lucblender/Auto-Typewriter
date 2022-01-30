import csv
from A4Pages import A4Page
import math
from KeyDictionnary import *
import sys

from AutoTypewriter import AutoTypewriter

autoTypewriter = AutoTypewriter()

PATH = "/home/pi"
FILE = ""

PRINTING_ENABLE = True
FILE_PATH = PATH+"/"+FILE
ARTIST = 1
TITLE = 2 
FORMAT = 4
RELEASED_YEAR = 6
HALF_COLLUMN = 64
LINE_PER_PAGE = 45
#CATEGORY_KEY = "CDs"
#CATEGORY_KEY = "Vinyles"
CATEGORY_KEY = "New Vinyls"
TITLE_STR = "Vinyl addition 02.01.2022"
#CDs Collection
#Vinyls Record Collection

def truncate_text(text, max_len):
    return text[:max_len-3] + (text[max_len-3:], '...')[len(text) > max_len]

final_len = 0
vinyl_formated_lines = []
with open(FILE_PATH, newline='', encoding="utf-8") as csvfile:
    discogs_csv = csv.reader(csvfile, delimiter=',')
    i = 0
    vinyl_row = []
    for row in discogs_csv:
        if i == 0:
            print(row)
        else:
            if row[8] == CATEGORY_KEY:
                vinyl_row.append(row)     
        i+=1
    vinyl_row = sorted(vinyl_row, key=lambda x: (x[ARTIST][4:] if "The " in x[ARTIST][0:4] else x[ARTIST] ,x[RELEASED_YEAR]))
    first_letter = " "
    last_first_letter = " "
    for row in vinyl_row:
        first_letter = row[ARTIST][4:][0] if "The " in row[ARTIST][0:4] else row[ARTIST][0]
        if last_first_letter != first_letter:
            vinyl_formated_lines.append("@@"+first_letter+"@@")
            final_len+=1
        last_first_letter = first_letter
        RE_RM = ""
        if "RM" in row[FORMAT]:
            RE_RM = RE_RM+"RM-"
        if "RE" in row[FORMAT]:
            RE_RM = RE_RM+"RE-"
        YEAR = ""
        if row[RELEASED_YEAR] != "0":
            YEAR = row[RELEASED_YEAR]
        addon = RE_RM+YEAR
        if addon != "":
            addon = "(" + addon + ")"  
        ARTIST_TITLE_MAX_LEN = int((HALF_COLLUMN-2)/2)
        artist = truncate_text(row[ARTIST],ARTIST_TITLE_MAX_LEN).ljust(ARTIST_TITLE_MAX_LEN," ")
        title = truncate_text(row[TITLE],ARTIST_TITLE_MAX_LEN-len(addon)).ljust(ARTIST_TITLE_MAX_LEN-len(addon)," ")
        text = "{0} {1} {2}".format(artist, title, addon)
        vinyl_formated_lines.append(text)
        final_len+=1

page_number = math.ceil(len(vinyl_formated_lines)/LINE_PER_PAGE)

print(page_number)
pages = []
for i in range(0, page_number):
    pages.append(A4Page())
    
# create first page
pages[0].insert_delimiter_text_calign("@@{0}@@".format(TITLE_STR),3)

for page in pages:
    page.insert_line("-",0)
    page.insert_line("-",page.line-1)
    
page_index = 0
line_index = 0
for line in vinyl_formated_lines:
    
    line_index+=1
    if line_index > LINE_PER_PAGE:
        line_index = 0
        page_index+=1
    pages[page_index].insert_delimiter_text(line, 0, line_index+5)

#add page number
i = 1
for page in pages:
    to_add  = "page{0}/{1}".format(i, len(pages))
    i+=1
    page.insert_text_ralign(to_add, page.line-2)

answer = input("There is {0} page(s) to print, do you confirm this ? Y/n ".format(page_number))

if answer in " yY":
    print( "yes")
else:
    print("Ending program")
    sys.exit()
    
index = 1

for page in pages:    
    input("Printing page n° {0}. Load a new paper and press any key to continue.".format(index))
    if PRINTING_ENABLE:
        autoTypewriter.underline_delimiter_press_string(correct_string(str(page)))
    print(correct_string(str(page)))
    index += 1

        