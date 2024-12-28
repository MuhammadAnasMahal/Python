class parrot:
    speices = 'bird'
    def __init__ (self, name, age):
        
        self.name = name
        self.age = age


maccaw = parrot("Anas", 2)
lory = parrot("Aarav", 3)

print("the speices of maccaw is", maccaw.speices)
print("the name of maccaw is", maccaw.name)
print("the age of maccaw is", maccaw.age)

print("the speices of lory is", lory.speices)
print("the name of lory is", lory.name)
print("the age of lory is", lory.age)
