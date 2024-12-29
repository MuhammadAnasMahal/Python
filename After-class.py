class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print('the area is', 3.14*self.radius*self.radius)
ctr1 = circle(7)
ctr1.area()