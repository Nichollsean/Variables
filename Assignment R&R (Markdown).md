#Reading and Research - Assignment Statements

These tasks are designed to introduce you to the programming topic we will be studying in class next lesson. You **must** complete these activities prior to the lesson.

##Simple Calculations

A simple task that we can perform in a programming language is returning the answer of basic calculations. We can use all of the standard mathematical **operators** in Python plus a few than look a little different.

###Task 1
Use the Python shell to investigate the expressions given below, describe what each symbol represents and given the answer provided by the shell.

![The Python Shell](images/shell.jpg)

|Expression|Symbol description|Answer|
|:--------:|------------------|------|
|`3 + 4`|*addition*|*7*|
|`2 - 1`|*subtraction* | *1*|
|`5 * 3`|*multiplication* | *15*|
|`2**3`|*exponentiation* |*8*|
|`27/7`| *division*|*3.86* |
|`27//7`| *integer division*| *3*|
|`27%7`|*modulus* |*6* |

Most of Task One should have been very straightforward but you may have struggled to find a description for the last two expressions in the table.

###Task 2
Use the Internet to discover the name of each of the symbols listed below and then explain in your own words 
the purpose of each symbol.

|Symbol|Name|Purpose|
|:----:|----|-------|
|`//`| *integer division*| *a division operation that returns an integer by discarding the remainder*|
|`%`|*modulus* | *finds the modulus of two integers*|

You will use all of the above symbols frequently whilst learning to program in Python so it is important to remember then. Often then are used together to calculate the result of more complex expressions.

##More Complex Calculations
Often more than one term will be evaluated in a single expression. In Mathematics there is a rule to deal with such situations.

Investigate the expressions below. Evaluate them by hand first before testing your answer in the Python shell.

###Task 3

|Expression|Expected Result (Manual Calculation)|Actual Result from Python Shell|
|:--------:|------------------------------------|-----------------------------------|
|`3 + 4 * 2`|*11* |*11* |
|`3 + 4 / 2`|*5* |*5* |
|`10 - 2 * 2`|*6* |*6*|
|`10 - 2 / 2`|*9* |*9* |
|`(3 + 4) * 2`|*14* |*14* |
|`(10 - 2) * 2`|*16* |*16* |

ow that you have completed the above table comment on the results in the space below. How do the results relate to your knowledge of Mathematics?


*They seem to relate very well as they all follow basic principals of mathematics (BIDMAS)*


###Task 4
Use the Python shell to investigate the expressions given below, describe what each symbol represents and give the answer provided by the shell.

|Expression|Describe what happens when you enter the expression into the shell|
|:--------:|------------------------------------------------------------------|
|`mark1 = 10`|*when you imput mark1 as a stand alone imput the value becomes 10*|
|`mark2 = 15`|*when you imput mark2 as a stand alone imput the value becomes 15*|
|`mark1 + mark2`|*this command  performed the calculation of 10+15* |

In the space below attempt to explain what has happened with the above expressions:


*When you imput 'mark1=10' you give the command 'mark1' a value of 10, this is the same for the command of 'mark2'*


##Variables
Task four introduced you to the concept of variables. This is a fundamental concept in programming, you must have a good understanding of variables to progress on to more complex concepts.

###Task 5
Read pages 28-29 of the AS Computing textbook, which cover variables and assignment statements. Below, define what is meant by the term variable and some of the considerations you should keep in mind when naming variables.

| | |
|-|-|
|variable defintion: *a location in memory that contains one or more data values*
|consideration 1: *Always choose a meaningful name for the variable (Variable identifier)*  |
|consideration 2: *Use alphanumeric characters (including underscore) and no spaces or other characters* |
|consideration 3: *Follow generally accepted naming conventions, this way other programers can understand the program code* |
|consideration 4: *Dont use single letter variable identifiers unless really appropriate, and make sure you the identifier is sensible and fits with the code* |

###Task 6
Complete the following exercises in Python.

####Python Syntax

```python
print("hello world")
#outputs the text string to the screen

print("Your age is {0}".format(your_age))
#outputs the text string to the screen followed by the value contained in the variable

your_age = 5
#assigns the value 5 to the variable

input_age = int(input("Please enter your age: "))
#assigns the input from the keyboard to the variable
```

1. Write a program that will ask the user for three integers and display the total.
2. Write a program that will ask the user for two integers and display the result of multiplying them together.
3. Ask the user for the length, width and depth of a rectangular swimming pool. Calculate the volume of water required 

Include the source code for each of the tasks in the spaces below.

#Task 6.1
numberA = int(input('Enter a number'))
numberB = int(input('Enter another number'))
numberC = int(input('Enter a final number'))
sum=numberA+numberB+numberC
print(sum)


#Task 6.2
numberA = int(input(Enter a number'))
numberB = int(input('Enter another number'))
sum=numberA*numberB
print(sum)


#Task 6.3
numberA = int(input('What is the depth of the pool (cm)'))
numberB = int(input('What is the width of the pool (cm)'))
numberC = int(input('What is the length of the pool (cm)'))
sum=numberA*numberB*numberC
print(sum)


##Summary
In this R&R you have investigated **assignment statements**. You have seen how **mathematical operators** are used to construct expressions and how values can be stored in **variables**.

Please make sure you have completed this R&R fully before your next programming lesson as it will form the basis of the initial classroom discussion and starter tasks.

