sp=float(input ("Enter the selling price"))
cp=float(input ("Enter the cost price"))
if sp > cp:
    print("the profit is", sp-cp)
else:
    print("the loss is", cp-sp)
    