# prgram to check the value error
try:
    n = int(input("Enter the number"))
    print(n)
except ValueError as ex:
    print(ex)