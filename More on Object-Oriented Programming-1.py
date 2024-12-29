class IOSstring:
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("enter the string")
    def print_string(self):
        print("the uppercase is", self.str1.upper())
    
obj1 = IOSstring()
obj1.get_string()
obj1.print_string()