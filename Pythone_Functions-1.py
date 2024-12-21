# add two lists

l1 = [12,23,34,45,]
l2 = [56,67,78,89,90]
result = map(lambda x, y : x + y, l1, l2)

print("Addition of two list")
print(list(result))
print("the square")
num = [35,23,36.98]

squares = map(lambda x:x*x, num)
print(list(squares))