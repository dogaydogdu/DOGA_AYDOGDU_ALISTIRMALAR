for i in range(100,1000):
    k=str(i)
    l=k[::-1]
    if k==l:
        print(k)
#other method
for i in range(100,1000):
    k=str(i)
    if str(k[0])==str(k[2]):
        print(k)
