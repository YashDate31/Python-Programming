def total(*num):
    s = 0
    for i in num:
        s += i
    print("Total:", s)

total(10, 20)
total(5, 10, 15)