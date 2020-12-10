'''Create a program that asks the user to enter their name and their age.
 Print out a message addressed to them that tells them the year that they will turn 100 years old.'''
name = str(input('enter the name of user:'))
age = int(input('enter age:'))
cyear = int(input('mention current year:'))
x = 100 - age
year = cyear + x
print(name + " will turns 100 years by the year",year )   