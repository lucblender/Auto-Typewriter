from unicodedata import normalize

left_1 = 5
left_2 = 6
left_3 = 13
left_4 = 19
left_5 = 26
left_6 = 16
left_7 = 20
left_8 = 21

right_1 = 4
right_2 = 17 
right_3 = 18 
right_4 = 27 
right_5 = 22 
right_6 = 24 
right_7 = 23 
right_8 = 25 

keys_dict = {
"1"         :(left_1,	right_1, False, False),
"2"         :(left_1,	right_2, False, False),
"q"         :(left_1,	right_3, False, False),
"w"         :(left_1,	right_4, False, False),
"a"         :(left_1,	right_5, False, False),
"s"         :(left_1,	right_6, False, False),
"y"         :(left_1,	right_7, False, False),
"x"         :(left_1,	right_8, False, False),
"3"         :(left_2,	right_1, False, False),
"4"         :(left_2,	right_2, False, False),
"e"         :(left_2,	right_3, False, False),
"r"         :(left_2,	right_4, False, False),
"d"         :(left_2,	right_5, False, False),
"f"         :(left_2,	right_6, False, False),
"c"         :(left_2,	right_7, False, False),
"v"         :(left_2,	right_8, False, False),
"5"         :(left_3,	right_1, False, False),
"6"         :(left_3,	right_2, False, False),
"t"         :(left_3,	right_3, False, False),
"z"         :(left_3,	right_4, False, False),
"g"         :(left_3,	right_5, False, False),
"h"         :(left_3,	right_6, False, False),
"b"         :(left_3,	right_7, False, False),
"n"         :(left_3,	right_8, False, False),
"7"         :(left_4,	right_1, False, False),
"8"         :(left_4,	right_2, False, False),
"u"         :(left_4,	right_3, False, False),
"i"         :(left_4,	right_4, False, False),
"j"         :(left_4,	right_5, False, False),
"k"         :(left_4,	right_6, False, False),
"m"         :(left_4,	right_7, False, False),
","         :(left_4,	right_8, False, False),
"9"         :(left_5,	right_1, False, False),
"0"         :(left_5,	right_2, False, False),
"o"         :(left_5,	right_3, False, False),
"p"         :(left_5,	right_4, False, False),
"l"         :(left_5,	right_5, False, False),
"ö"         :(left_5,	right_6, False, False),
"."         :(left_5,	right_7, False, False),
"-"         :(left_5,	right_8, False, False),
"'"         :(left_6,	right_1, False, False),
"^"         :(left_6,	right_2, False, False),
"ü"         :(left_6,	right_3, False, False),
"¨"         :(left_6,	right_4, False, False),
"ä"         :(left_6,	right_5, False, False),
"$"         :(left_6,	right_6, False, False),
"§"         :(left_6,	right_7, False, False),
"¨withspace":(left_6,	right_8, False, False),
"unknown_1" :(left_7,	right_1, False, False),
"unknown_2" :(left_7,	right_2, False, False),
"unknown_3" :(left_7,	right_3, False, False),
"goend"     :(left_7,	right_4, False, False),
"changepitch" :(left_7,	right_5, False, False),
"unknown_5" :(left_7,	right_6, False, False),
"shiftlock" :(left_7,	right_7, False, False),
"unknown_6" :(left_7,	right_8, False, False),
"return"    :(left_8,	right_1, False, False),
"unknown_7" :(left_8,	right_2, False, False),
"unknown_8" :(left_8,	right_3, False, False),
"\n"        :(left_8,	right_4, False, False),
"shift"     :(left_8,	right_5, False, False),
"correct"   :(left_8,	right_6, False, False),
" "         :(left_8,	right_7, False, False),
"tab"       :(left_8,	right_8, False, False),
"+"         :(left_1,	right_1, True, False),
"\""         :(left_1,	right_2, True, False),
"Q"         :(left_1,	right_3, True, False),
"W"         :(left_1,	right_4, True, False),
"A"         :(left_1,	right_5, True, False),
"S"         :(left_1,	right_6, True, False),
"Y"         :(left_1,	right_7, True, False),
"X"         :(left_1,	right_8, True, False),
"*"         :(left_2,	right_1, True, False),
"ç"         :(left_2,	right_2, True, False),
"E"         :(left_2,	right_3, True, False),
"R"         :(left_2,	right_4, True, False),
"D"         :(left_2,	right_5, True, False),
"F"         :(left_2,	right_6, True, False),
"C"         :(left_2,	right_7, True, False),
"V"         :(left_2,	right_8, True, False),
"%"         :(left_3,	right_1, True, False),
"&"         :(left_3,	right_2, True, False),
"T"         :(left_3,	right_3, True, False),
"Z"         :(left_3,	right_4, True, False),
"G"         :(left_3,	right_5, True, False),
"H"         :(left_3,	right_6, True, False),
"B"         :(left_3,	right_7, True, False),
"N"         :(left_3,	right_8, True, False),
"/"         :(left_4,	right_1, True, False),
"("         :(left_4,	right_2, True, False),
"U"         :(left_4,	right_3, True, False),
"I"         :(left_4,	right_4, True, False),
"J"         :(left_4,	right_5, True, False),
"K"         :(left_4,	right_6, True, False),
"M"         :(left_4,	right_7, True, False),
";"         :(left_4,	right_8, True, False),
")"         :(left_5,	right_1, True, False),
"="         :(left_5,	right_2, True, False),
"O"         :(left_5,	right_3, True, False),
"P"         :(left_5,	right_4, True, False),
"L"         :(left_5,	right_5, True, False),
"é"         :(left_5,	right_6, True, False),
":"         :(left_5,	right_7, True, False),
"_"         :(left_5,	right_8, True, False),
"?"         :(left_6,	right_1, True, False),
"`"         :(left_6,	right_2, True, False),
"è"         :(left_6,	right_3, True, False),
"´"         :(left_6,	right_4, True, False),
"à"         :(left_6,	right_5, True, False),
"£"         :(left_6,	right_6, True, False),
"fi"        :(left_6,	right_7, True, False),
"°"         :(left_2,	right_8, False, True),
"["         :(left_1,	right_4, False, True),
"]"         :(left_4,	right_3, False, True)
}

        
def test_string(string):
    for char in string:
        try:
            keys_dict[char]
        except:
            print("error, key not in dict: ", char)

        
def correct_string(string, contain_delimiter = True):
    to_return = ""
    for char in string:
        if contain_delimiter and char == "@":
            to_return+=char
        else:
            try:
                keys_dict[char]
                to_return+=char
            except:
                try:
                    new_char = normalize('NFD', char).encode('ascii', 'ignore').decode("utf-8")
                    keys_dict[new_char]
                    to_return+=new_char
                except:
                    to_return+="?"
    return to_return
