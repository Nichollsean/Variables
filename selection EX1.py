#Sean Nicholls
#24/9/14
#IF statement work

age= int(input("How old are you? "))

if age >=18:
    print("Yes you able to vote")
else:
    print("I'm affraid you are to young to vote")

retire=(65-age)
if retire <=0:
    print("You are also able to retire at your age")
else:
    print("You have {0} years until you can retire".format(retire))

