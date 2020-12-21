# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

b = [34, 50, 35, 54, 90, 20, 48, 87, 99, 25]
print (b)
print('numbers divisible by 5 in list are :')
for i in b:
    if i % 5 == 0:
        print (i)
        