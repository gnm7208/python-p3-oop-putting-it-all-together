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
        if self.condition != "New":
            self.condition = "New"
            print("Your shoe is as good as new!")
        else:
            print("Your shoe is already new!")

    def __str__(self):
        return f"This is a {self.brand} shoe of size {self.size} and condition {self.condition}"
    pass