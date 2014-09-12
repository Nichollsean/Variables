#Sean Nicholls
#variable improvement exercise
#12-09-12

import math

radius = int (input("please enter the radius of the circle: "))
circumfrence = 2 * math.pi * radius
circumfrenceANS = round(circumfrence,2)
area = int (math.pi * radius**2)
answer = round(area,2)
print("The circumference of this circle is {0}.".format(circumfrenceANS))
print("The area of this circle is {0}.".format(answer))
