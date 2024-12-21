l1 = [1,2,3,5]
l2 = [100,200, 300, 500]
l3 = zip(l1,l2)
print(list(l2))

l2 = zip(l1,l2[::-1])
print(list(l2))

stock = ['Accelize', 'HCL', 'Alpha-Neumero']
price = [1243,1734,2343,3212]
dic1 = {stock:price for stock,price in zip(stock,price)}
print(dic1)