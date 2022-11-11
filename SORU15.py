for i in range(10000,100000):
    bolunebilir=False
    for j in range(2,i):
        if i%j==0:
            bolunebilir=True
    if bolunebilir==False:
        print(i)
