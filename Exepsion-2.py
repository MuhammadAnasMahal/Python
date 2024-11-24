try:
    a, b = eval(input("enter the number separated by commas"))
    ans = a/b
    print("Teh result is", ans)
except ZeroDivisionError:
    print("the number cannot divide by zero")
except SyntaxError:
    print("You missed comma")
except :
    print("An error occurred ")
else:
    print("no exeption")
finally:
    print("however this will statement is excecuted")