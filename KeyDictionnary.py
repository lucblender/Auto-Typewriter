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
"1"         :(left_1,	right_1, False),
"2"         :(left_1,	right_2, False),
"q"         :(left_1,	right_3, False),
"w"         :(left_1,	right_4, False),
"a"         :(left_1,	right_5, False),
"s"         :(left_1,	right_6, False),
"y"         :(left_1,	right_7, False),
"x"         :(left_1,	right_8, False),
"3"         :(left_2,	right_1, False),
"4"         :(left_2,	right_2, False),
"e"         :(left_2,	right_3, False),
"r"         :(left_2,	right_4, False),
"d"         :(left_2,	right_5, False),
"f"         :(left_2,	right_6, False),
"c"         :(left_2,	right_7, False),
"v"         :(left_2,	right_8, False),
"5"         :(left_3,	right_1, False),
"6"         :(left_3,	right_2, False),
"t"         :(left_3,	right_3, False),
"z"         :(left_3,	right_4, False),
"g"         :(left_3,	right_5, False),
"h"         :(left_3,	right_6, False),
"b"         :(left_3,	right_7, False),
"n"         :(left_3,	right_8, False),
"7"         :(left_4,	right_1, False),
"8"         :(left_4,	right_2, False),
"u"         :(left_4,	right_3, False),
"i"         :(left_4,	right_4, False),
"j"         :(left_4,	right_5, False),
"k"         :(left_4,	right_6, False),
"m"         :(left_4,	right_7, False),
","         :(left_4,	right_8, False),
"9"         :(left_5,	right_1, False),
"0"         :(left_5,	right_2, False),
"o"         :(left_5,	right_3, False),
"p"         :(left_5,	right_4, False),
"l"         :(left_5,	right_5, False),
"é"         :(left_5,	right_6, False),
"."         :(left_5,	right_7, False),
"-"         :(left_5,	right_8, False),
"'"         :(left_6,	right_1, False),
"^"         :(left_6,	right_2, False),
"è"         :(left_6,	right_3, False),
"¨"         :(left_6,	right_4, False),
"à"         :(left_6,	right_5, False),
"$"         :(left_6,	right_6, False),
"§"         :(left_6,	right_7, False),
"¨withspace":(left_6,	right_8, False),
"unknown_1" :(left_7,	right_1, False),
"unknown_2" :(left_7,	right_2, False),
"unknown_3" :(left_7,	right_3, False),
"goend"     :(left_7,	right_4, False),
"changepitch" :(left_7,	right_5, False),
"unknown_5" :(left_7,	right_6, False),
"shiftlock" :(left_7,	right_7, False),
"unknown_6" :(left_7,	right_8, False),
"return"    :(left_8,	right_1, False),
"unknown_7" :(left_8,	right_2, False),
"unknown_8" :(left_8,	right_3, False),
"\n"        :(left_8,	right_4, False),
"shift"     :(left_8,	right_5, False),
"correct"   :(left_8,	right_6, False),
" "         :(left_8,	right_7, False),
"tab"       :(left_8,	right_8, False),
"+"         :(left_1,	right_1, True),
"\""         :(left_1,	right_2, True),
"Q"         :(left_1,	right_3, True),
"W"         :(left_1,	right_4, True),
"A"         :(left_1,	right_5, True),
"S"         :(left_1,	right_6, True),
"Y"         :(left_1,	right_7, True),
"X"         :(left_1,	right_8, True),
"*"         :(left_2,	right_1, True),
"ç"         :(left_2,	right_2, True),
"E"         :(left_2,	right_3, True),
"R"         :(left_2,	right_4, True),
"D"         :(left_2,	right_5, True),
"F"         :(left_2,	right_6, True),
"C"         :(left_2,	right_7, True),
"V"         :(left_2,	right_8, True),
"%"         :(left_3,	right_1, True),
"&"         :(left_3,	right_2, True),
"T"         :(left_3,	right_3, True),
"Z"         :(left_3,	right_4, True),
"G"         :(left_3,	right_5, True),
"H"         :(left_3,	right_6, True),
"B"         :(left_3,	right_7, True),
"N"         :(left_3,	right_8, True),
"/"         :(left_4,	right_1, True),
"("         :(left_4,	right_2, True),
"U"         :(left_4,	right_3, True),
"I"         :(left_4,	right_4, True),
"J"         :(left_4,	right_5, True),
"K"         :(left_4,	right_6, True),
"M"         :(left_4,	right_7, True),
";"         :(left_4,	right_8, True),
")"         :(left_5,	right_1, True),
"="         :(left_5,	right_2, True),
"O"         :(left_5,	right_3, True),
"P"         :(left_5,	right_4, True),
"L"         :(left_5,	right_5, True),
"ö"         :(left_5,	right_6, True),
":"         :(left_5,	right_7, True),
"_"         :(left_5,	right_8, True),
"?"         :(left_6,	right_1, True),
"`"         :(left_6,	right_2, True),
"ü"         :(left_6,	right_3, True),
"´"         :(left_6,	right_4, True),
"ä"         :(left_6,	right_5, True),
"£"         :(left_6,	right_6, True),
"fi"         :(left_6,	right_7, True)
}

        
def test_string(string):
    for char in string:
        try:
            keys_dict[char]
        except:
            print("error, key not in dict: ", char)
