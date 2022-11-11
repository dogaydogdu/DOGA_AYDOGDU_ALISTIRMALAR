sayi=int(input("3 veya 4 basamakli bir sayi giriniz: "))
k=str(sayi)
l=k[::-1]
if k==l and 99<sayi<10000:
    print(f"{sayi} palindromiktir.")
if k!=l and 99<sayi<10000:
    print(f"{sayi} palindromik değildir.")
if sayi<100 or sayi>9999:
    print(f"3 VEYA 4 BASAMAKLİ SAYİ GİRMELİSİNİZ!")
