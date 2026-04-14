a = int(input("Enter year:"))

if a%4==0 and a%100!=0:
    print("leap")
else:
    print("not leap")