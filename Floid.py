# right angled pattern
n= int(input("rnter the number of rwo"))
k = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k, end =  " ")
        k += 1
    print()
