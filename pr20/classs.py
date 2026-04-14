class student:
    def __init__(self):
        self.name="Yash"
        self.roll = 99
    
    def display(self):
        print(self.name,self.roll)


object = student()
object.display()