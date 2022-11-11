k=[]
for i in range(1,350):
    if 125 % i == 200 % i and  125 % i == 350 % i and 200 % i == 350 % i:
        k+=[i]
print(max(k)) 
