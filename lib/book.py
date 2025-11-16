#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title = None
        self.page_count = None

    def page_count(self):
        try:
            self.page_count = int(self.page_count)
        except ValueError:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    pass
    
        