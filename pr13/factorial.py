def fact(n):
    fact = 1
    for i in range(1,n):
        fact = fact*i + fact

    print(fact)  

fact(5)