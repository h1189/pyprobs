class test():
    def armstrong(self, num):
        a = [int(char) for char in str(num)]
        res = 0
        for n in a:
            res = res + n**3
        if res == num:
            print(f'{num} is an armstrong number')
        else:
            print(f'{num} is not an armstrong number')

num = int(input('enter a num:'))
check = test().armstrong(num)