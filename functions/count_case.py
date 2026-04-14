def up_low(sh):
    lower=0
    upper =0
    
    for s in sh:
        if s.isupper():
            upper = upper+1
    
        else:
            lower = lower + 1

    print(lower)
    print(upper)


up_low("yasHHH")
