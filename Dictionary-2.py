dic1 = {
    'boeing 747' : 3,
    'A380' : 5,
    'b2 spirit' : 7, 
    'Air India' : 7
}
count = 0 
k = 7
for key, value in dic1.items():
    if value == k:
        count+= 1 
print("the items which have frekwency are", k, 'is', count)
