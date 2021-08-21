print("""

HESAP MAKİNESİ PROGRAMI

İşlemler

1)ÇARPMA İŞLEMİ
2)BÖLME İŞLEMİ
3)TOPLAMA İŞLEMİ
4)ÇIKARMA İŞLEMİ

""")

a = int(input("Birinci Sayı: "))
b = int(input("İkinci Sayı: "))

islem = input("İslemi giriniz: ")

if islem == "1":
    print("{} ile {} çarpımı {} dir.".format(a,b, a*b))
elif islem == "2":
    print("{} ile {} bölümü {} dür.".format(a,b, a/b))
elif islem == "3":
    print("{} ile {} toplamı {} dır.".format(a,b, a+b))
elif islem == "4":
    print("{} ile {} farkı {} dır.".format(a,b, a-b))
else:
    print("Geçersiz işlem..")











