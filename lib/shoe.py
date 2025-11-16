#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size
        self.condition = "Used"
    
    def requires_int_size(self):
        if not isinstance(self.size, int):
            print("size must be an integer")
        else:
            self.size = self.size
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
        return self.condition
    
    pass