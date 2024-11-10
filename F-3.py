def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def Mult(a,b):
    return a * b
def Div(a,b):
    return a / b


choice = input(" 1. Addition \n 2. Substartion \n 3. Multiplication \n 4. division \n Enter Your Choice ")
if choice =="1":
    a = int(input("Enter the number"))
    b= int(input("Enter the Numbetr"))
    print( "the sum of two numbers", add (a,b))
elif choice =="2":
    a = int(input("Enter the number"))
    b= int(input("Enter the Numbetr"))
    print( "the sub of two numbers", sub (a,b))
elif choice =="3":
    a = int(input("Enter the number"))
    b= int(input("Enter the Numbetr"))
    print( "the Mult of two numbers", Mult (a,b))
elif choice =="1":
    a = int(input("Enter the number"))
    b= int(input("Enter the Numbetr"))
    print( "the Div of two numbers", Div (a,b))

