w = float(input("enter the weight in kgs"))
h = float(input("enter the height in m"))
bmi = w/(h*h)
if bmi > 18.5:
    print(bmi,"underweght")
elif bmi < 25:
    print(bmi,"it is healthy ")
elif bmi < 30:
    print(bmi,"it is overweight ")
else:
    print(bmi,"it is obese")