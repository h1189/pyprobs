# Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum
def prosum(a,b):
    pro = a * b
    if pro > 1000:
       return pro
    else: 
        add = a + b
        return add

result = prosum(6, 9)
print(f'the result is {result}')