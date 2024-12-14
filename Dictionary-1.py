# dictionary 
std = {"id1": 
    {"name" : "Anas",
    "age" : 12}, 
      "id1": 
    {"name" : "Dhruv",
    "age" : 12},
    "id1": 
    {"name" : "Anas",
    "age" : 12},
    "id3": 
    {"name" :"Apratim",
    "age" : 12}}
result =  {}
for key , value in std.items():
    if value not in result.values():
      result [key] = value 
print(result)