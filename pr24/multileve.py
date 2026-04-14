class A:
    def printA(self):
        print("hello a")

class B(A):
    def printB(self):
        print("hello b")

class C(B):
    def printC(self):
        print("hello c")


c= C()
c.printA()
c.printB()
c.printC()
