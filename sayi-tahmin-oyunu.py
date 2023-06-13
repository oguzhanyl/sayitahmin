import random
tahmin_edilecek_sayi = random.randint(1,100)

deneme_hakki = 5

while deneme_hakki>0:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin : "))
    if tahmin == tahmin_edilecek_sayi:
        print("Tebrikler, sayıyı bildiniz.")
        break
    elif tahmin < tahmin_edilecek_sayi:
        print("Daha büyük bir sayı giriniz.")
    else:
        print("Daha küçük bir sayı girin.")
    deneme_hakki -=1
else:
    print(f"Deneme hakkınız kalmadı. Doğru cevap {tahmin_edilecek_sayi} idi")

