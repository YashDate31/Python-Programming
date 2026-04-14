#Write a Python class to implement pow(x, n). 
#bhaiiiiiiiiiiii dont forgot to write self 

class power:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def result(self):
        return (self.x**self.y)


obj = power(2,3)
print(obj.result())