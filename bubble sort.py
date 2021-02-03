def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        flag = 0
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                flag = 1

        if flag == 0:
            break

    print(f"sorted array is {a}")


a = [8, 9, 30, 12, 11, 5]
bubble_sort(a)