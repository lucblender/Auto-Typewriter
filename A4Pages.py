import copy
class A4Page:

    column = 65
    line = 60

    def __init__(self):
        self.page = [[" "]*self.column for i in range(self.line)]

    def reset_page(self):
        self.page = [[" "]*self.column for i in range(self.line)]

    def insert_text(self, text, x, y):
        line_text  = text.splitlines()
        index_y = 0
        for line in line_text:
            index_x  = 0
            for char in line:
                self.page[index_y+y][index_x+x] = char
                index_x += 1
            index_y += 1
            
    def insert_text_ralign(self, text, y):
        self.insert_text(text, self.column-1-len(text), y)
            
    def insert_delimiter_text_ralign(self, text, y):
        self.insert_delimiter_text(text, self.column-1-len(text), y)
            
    def insert_text_calign(self, text, y):
        self.insert_text(text, int((self.column-len(text))/2), y)
            
    def insert_delimiter_text_calign(self, text, y):
        self.insert_delimiter_text(text, int((self.column-len(text))/2), y)

    def insert_delimiter_text(self, text, x, y):
        line_text  = text.splitlines()
        index_y = 0
        for line in line_text:
            index_x  = 0
            str_index  = 0
            while str_index < len(line):
                if line[str_index] == "@" and str_index+1 < len(line) and line[str_index+1] == "@":
                    self.page[index_y+y][index_x+x] = line[str_index]+line[str_index+1]
                    try:
                        self.page[index_y+y][index_x+x] += line[str_index+2]
                    except:
                        pass
                    str_index+=2
                else:
                    self.page[index_y+y][index_x+x] = line[str_index]
                index_x+=1
                str_index+=1
            index_y += 1

    def insert_line(self, char, y):
        for i in range(0, self.column):
            self.page[y][i] = char
            
    def beautiful_print(self):
        unformated_str = str(self)
        formated_str = ""
        even = True
        str_index  = 0
        while str_index < len(unformated_str):
            if unformated_str[str_index] == "@" and str_index+1 < len(unformated_str) and unformated_str[str_index+1] == "@":
                if even:
                    formated_str+="\033[4m"
                else:
                    formated_str+="\033[0m"
                even = not(even)
                str_index+=1
            else:
                formated_str+=unformated_str[str_index]
            
            str_index+=1
                
        
        
        return formated_str

    def __repr__(self):
        temp_page = copy.deepcopy(self.page)

        while(temp_page[-1] == [" "]*self.column):
            temp_page.pop()

        to_return = ""
        for char_line in temp_page:
            line = ""
            for char in char_line:
                line += char
            to_return += (line.rstrip()+"\n")
        return to_return