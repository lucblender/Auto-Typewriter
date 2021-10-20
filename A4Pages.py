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
            
    def insert_line(self, char, y):
        for i in range(0, self.column):
            self.page[y][i] = char
            
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