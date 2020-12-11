#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
num = int(input("Enter number: "))
divisors = []
i = 1
for i in range(1, num // 2 + 1):
    if num % i == 0:
        divisors.append(i)
print ("divisors of given num are",divisors)