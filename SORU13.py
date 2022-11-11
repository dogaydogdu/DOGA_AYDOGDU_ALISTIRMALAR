for a in range(10,100):
    x=str(a)
    for b in range(10,100):
        y=str(b)
        if int(x+y)==(a+b)*11:
            print(a,b)
