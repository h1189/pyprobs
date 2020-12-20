# Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number
n = 0
for i in range (0, 10, 1):
    res = n + i
    print(f'current number {i}, previous number {n} and result is {res}')
    n = i