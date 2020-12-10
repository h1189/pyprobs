#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#If the number is a multiple of 4, print out a different message.
num = int(input('enter a num:'))
if num%2 == 0:
   print(num,' is an even num')
else:
   print(num,' is an odd num')
check = int(input('enter num to be check weather it is disible by 4 or not:'))
if check % 4 == 0:
   print(check,' is divisible by 4')
else:
   print(check,' is not divisible by 4')