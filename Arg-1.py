# program to caluculate the tip for the waiter
def totalamt(amt):
    total =amt + (amt*10)/100
    return total

amt =  float(input("Enter your tip"))
print("THe total amt is",totalamt(amt))