amt = int(input("Enter the Amount"))
amt500 = amt//500
rem500 = amt%500
amt100 = rem500//100
rem100=rem500%100
amt10 = rem100//10
print("Number of 500 rupee note", amt500)
print("Number of 100 rupee note", amt100)
print("Number of 10 rupee note", amt10)