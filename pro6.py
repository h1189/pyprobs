# To find largest num in an list. 

my_list = [2, 4, 9, 8, 2, 3, 6, 7, 81, 91, 23, 76, 99]
large = my_list[0]
for num in my_list:
    if num > large:
        large = num
print(large)
