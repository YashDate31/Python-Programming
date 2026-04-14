class rev:
    def __init__(self,text):
        self.str= text

    def reverse(self):
        return self.str[::-1]
    

obj = rev("yash")
print(obj.reverse())
