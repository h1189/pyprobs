'''Take two lists and write a program that returns a list that contains only the elements that are common between 
   the lists (without duplicates). Make sure your program works on two lists of different sizes.''' 
a = [2, 4, 5, 3, 6, 7, 4]
b = [2, 3, 5, 9, 7, 0, 19, 11] 
c = []
for element in a:
    if element in b:
        c.append(element)
print(a)
print(b)
print(c)