'''Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number.'''

def fizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0:
        y = "Fizz_Buzz"
        return y
    elif x % 3 == 0:
        y = "Fizz"
        return y
    elif x % 5 == 0:
        y = "Buzz"
        return y
    else:
        return x

num = int(input('enter a num :'))
c = fizz_buzz(num)
print(c)