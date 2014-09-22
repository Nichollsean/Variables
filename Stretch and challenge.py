#Sean Nicholls
#22/09/14
#Stretch and challenge refresher excercise

sideA= int(input("What is the length of your garden in meters? "))
sideB= int(input("What is the width of your garden in meters? "))

area= (sideA*sideB)
border = (sideA*1)+(sideB*1)*2

area2= area-border

cost= area2*10

print("It will cost £{0} to turf your garden".format(cost))

