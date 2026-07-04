#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

# Hedef ve port listesi tanımı
hedef_ip = "127.0.0.1"
portlar = [21, 22, 23, 25, 53, 80, 139, 443, 445, 3389, 8080]

print("-" * 50)
print(f"[+] Hedef: {hedef_ip}")
print(f"[+] Tarama Başlangıcı: {str(datetime.now())}")
print("-" * 50)

try:
    for port in portlar:
        # AF_INET = IPv4, SOCK_STREAM = TCP bağlantısı demektir
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # i5 sistem için 1 saniyelik hızlı tepki süresi
        
        # Bağlantıyı dene
        sonuc = s.connect_ex((hedef_ip, port))
        
        if sonuc == 0:
            print(f"[!] Port {port}: AÇIK (Risk Noktası Olabilir)")
        else:
            print(f"[-] Port {port}: Kapalı")
            
        s.close() # Her taramadan sonra bağlantıyı güvenlice kapat

except KeyboardInterrupt:
    print("\n[-] Tarama kullanıcı tarafından iptal edildi (Ctrl+C).")
    sys.exit()

except socket.gaierror:
    print("\n[-] Alan adı çözülemedi.")
    sys.exit()

print("-" * 50)
print("[+] Tarama başarıyla tamamlandı.")

