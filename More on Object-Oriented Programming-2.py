class employ:
    def __init__(self, name):
        print("object Iniated")
        self.name = name
    def intro(self):
        print("I am", self.name)
    def __del__(self):
        print("object deleted")
em1 = employ("Anas")
em1.intro()
del em1