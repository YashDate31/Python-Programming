from functools import reduce

number =[10,20,30]

y= reduce(lambda x ,y :x +y,number)
print(y)