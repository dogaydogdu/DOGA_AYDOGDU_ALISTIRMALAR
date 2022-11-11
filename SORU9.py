k=0
for i in range(10000,100000):
    j=str(i)
    if j[0]==j[4] and j[1]==j[3]:
        k+=1
print(k)        
