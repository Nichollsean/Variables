#Sean Nicholls
#16/09/14
#Exercise 2.3

heightinch= int(input("How tall are you in inches: "))
weightstone= int(input("I you dont mind, how much do you weigh in stones: "))

heightcm= heightinch*2.54
weightkg= weightstone*6.364

print("Your height in centimeters is: {0:.0f}".format(heightcm))
print("Your weight in kilograms is: {0:.0f}".format(weightkg))
