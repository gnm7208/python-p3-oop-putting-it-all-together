#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title = title
        self.page_count = page_count

    def page_count(self):
        if not isinstance(self.page_count, int):
            print("page count must be an integer")
        else:
            self.page_count = self.page_count
    

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    pass
    
        