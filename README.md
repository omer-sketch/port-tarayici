======================================================================
         COSPA TECH: PORT TARAYICI V1 (TEMEL MOTOR)
======================================================================

1. ARACIN GÖREVİ
----------------
Bu araç, siber güvenlik dünyasındaki "Ağ Keşfi" (Network Reconnaissance) 
aşamasının en temel motorudur. Belirlenen bir IP adresine giderek, o sistemin 
dış dünyaya açık olan kapılarını (portlarını) tek tek çalar. Eğer kapı 
açıksa bize bildirir. Bu işlem, hedef sistemde hangi servislerin (Web, 
SSH, FTP vb.) çalıştığını anlamamızı sağlar.

2. ÇALIŞTIRMA KOMUTU
--------------------
Bu ilk sürüm, doğrudan TCP bağlantı isteği (3'lü el sıkışma) başlattığı ve 
ham ağ kartı müdahalesi gerektirmediği için yönetici (root) hakları olmadan, 
normal kullanıcı yetkisiyle doğrudan çalıştırılabilir:

    python3 tarayici.py

3. ÇALIŞMA PRENSİBİ VE ÖNEMLİ KOD MANTIĞI
-----------------------------------------
Program, Python'un yerleşik "socket" kütüphanesindeki şu özel fonksiyonu 
kullanarak çalışır:
    
    sonuc = soket.connect_ex((hedef_ip, port))

* Eğer "sonuc" değeri "0" (sıfır) dönerse: O kapı AÇIKTIR ve içeride bizi 
  bekleyen bir servis vardır.
* Eğer "sonuc" değeri sıfırdan farklı bir hata kodu dönerse: O kapı KAPALIDIR 
  veya bir güvenlik duvarı (Firewall) tarafından engellenmiştir.

4. COSPA-OÇA LABORATUVAR DENEYİ NOTU
-------------------------------------
* Yapılan Deney  : Bir uç birimde (terminalde) "nc -lvp 4444" komutuyla 
  yapay bir dinleme kapısı açılmış, ardından bu tarayıcı v1 motoru kendi 
  yerel bilgisayarımızda (127.0.0.1) ateşlenmiştir.
* Başarı Durumu : Tarayıcımız, ağdaki binlerce olasılık arasından 4444 
  portunun açık olduğunu tık diye tespit etmiş ve ilk başarılı sızma öncesi 
  keşif görevini tamamlamıştır.

5. SİBER GÜVENLİK UZMANI DEĞERLENDİRMESİ
----------------------------------------
Bu v1 motoru çok kararlı çalışır ancak her kapıyı tam olarak açıp kapatmaya 
çalıştığı için (Full TCP Connect) hedef sistemin günlük kayıtlarında (log) 
yakalanma ihtimali yüksektir. İleride deneyeceğimiz profesyonel Nmap aracı, 
burada öğrendiğimiz mantığın üzerine inşa edilmiş daha gizli tarama türleri 
(SYN Stealth gibi) gerçekleştirecektir.

(Not:Terminalde dosyaya çalışma izni vermeyi unutmayın)

======================================================================
