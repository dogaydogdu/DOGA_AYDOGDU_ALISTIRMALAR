k=0
for i in range(100,1000):
    j=str(i)
    if int(j[0])+int(j[1]) == int(j[2]):
        print(i)
        k+=1
print(f"Kosulu saglayan {k} tane sayi vardir.")

