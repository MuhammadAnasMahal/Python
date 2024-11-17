# Check a given alphabet is preasent or not 
str1 = input("enter the string")
ch = input("enter the alphabet")
for i in str1:
    if i == ch:
        print(ch,"the alphabet is preasent is ", str1)
        break
else:
    print(ch, "The given alphabet is not preasent ", str1)
    