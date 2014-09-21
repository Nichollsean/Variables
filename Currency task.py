#Sean Nicholls
#18/09/2014
#Currency Excercise

total= int(input("Please eter the amount you wish to convert"))

amount20= total//20
remainder20= total%20

amount10= remainder20//10
remainder10= amount20%10

amount5= remainder10//5
remainder5= amount10%5

amount2= remainder5//2
remainder2= amount5%2

amount1= remainder2//1
remainder1= amount2%1

print("minimum amount of change is {0} £20 notes, {1} £10 notes, {2} £5 notes, {3} £2 coins and {4} £1 coins" .format(amount20, amount10, amount5, amount2, amount1))
