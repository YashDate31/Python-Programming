n = 7



for i in range(n,0,-2):
    for j in range(i):
        if j%2==0:
            print(0,end="")
        else:
            print(1,end="")
    print()
        