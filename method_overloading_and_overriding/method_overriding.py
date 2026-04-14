class A:
    def showA(self):
        print("Class A")

class B(A):
    def showA(self):
        print("Class B")

o = B()
o.showA()