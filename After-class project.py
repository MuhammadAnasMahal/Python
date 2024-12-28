class dog:
    speices = 'dog'
    def __init__ (self, name, age):
        
        self.name = name
        self.age = age

Husky = dog("Aarav", 3)

print("the speices of husky is", dog.speices)
print("the name of lory is", dog.name)
print("the age of lory is", dog.age)