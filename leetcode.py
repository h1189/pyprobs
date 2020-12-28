''' Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.'''


class Solution():
    def addDigits(self,num:int) -> int:
        a = [int(i) for i in str(num)]
        b=0
        for ele in range (0, len(a)):
            b = b + a[ele]
        c = [int(i) for i in str(b)]
        d = 0
        for ele in range (0, len(c)):
            d = d + c[ele]
        e = [int(i) for i in str(d)]
        f = 0
        for ele in range (0, len(e)):
            f = f + e[ele]
        return f

num = input('enter an non negative multi digit integer:')
ret = Solution().addDigits(num)
print(ret)

