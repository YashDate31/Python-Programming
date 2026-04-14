'''#Write  a  Python  program  to  create  a  class  to  print  the  area  of  a  square  and  a  rectangle.  The 
class  has  two  methods  with  the  same  name  but  different  number  of  parameters.  The  method 
for  printing  area  of  rectangle  has  two  parameters  which  are  length  and  breadth  respectively 
while the other method for printing area of square has one parameter which is side of square. '''

class area:
    def shape(self,a,b=None):
     if b is None:
        return a*a
     else:
        return a*b
    
o= area()
print(o.shape(10,30))
print(o.shape(5))
