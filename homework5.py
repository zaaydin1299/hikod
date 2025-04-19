# Başlangıçta tanımlı öğrenci notları
ogrenciler = {
    "Ahmet": {"Matematik": 85, "Fizik": 90, "Kimya": 78},
    "Ayşe": {"Matematik": 92, "Fizik": 88, "Kimya": 95},
    "Mehmet": {"Matematik": 76, "Fizik": 85, "Kimya": 80}
}

# Öğrenci ve ders notunu sorgulama
isim = input("Öğrenci ismi girin (örnek: Ahmet): ")
ders = input("Ders ismi girin (Matematik, Fizik, Kimya): ")

if isim in ogrenciler and ders in ogrenciler[isim]:
    print(f"{isim} adlı öğrencinin {ders} notu: {ogrenciler[isim][ders]}")
else:
    print("Geçersiz öğrenci veya ders ismi girdiniz.")

# Yeni öğrenci ekleme
yeni_isim = input("\nYeni öğrenci ismi girin: ")
mat = int(input(f"{yeni_isim} için Matematik notu: "))
fzk = int(input(f"{yeni_isim} için Fizik notu: "))
kmy = int(input(f"{yeni_isim} için Kimya notu: "))
ogrenciler[yeni_isim] = {"Matematik": mat, "Fizik": fzk, "Kimya": kmy}
print(f"{yeni_isim} başarıyla eklendi.")

# Var olan öğrencinin notunu güncelleme
guncellenecek_isim = input("\nNotunu güncellemek istediğiniz öğrenci: ")
guncellenecek_ders = input("Güncellenecek ders (Matematik, Fizik, Kimya): ")
yeni_not = int(input("Yeni not: "))

if guncellenecek_isim in ogrenciler and guncellenecek_ders in ogrenciler[guncellenecek_isim]:
    ogrenciler[guncellenecek_isim][guncellenecek_ders] = yeni_not
    print(f"{guncellenecek_isim}'in {guncellenecek_ders} notu {yeni_not} olarak güncellendi.")
else:
    print("Geçersiz bilgi girdiniz.")

# Kullanıcının istediği öğrenci ve dersi tekrar sorma
isim = input("\nBilgi almak istediğiniz öğrenci ismi: ")
ders = input("Bilgi almak istediğiniz ders ismi: ")

if isim in ogrenciler and ders in ogrenciler[isim]:
    print(f"{isim} adlı öğrencinin {ders} notu: {ogrenciler[isim][ders]}")
else:
    print("Geçersiz öğrenci veya ders ismi.")