import socket

# Basit bir zafiyet veritabanı (AI gibi devasa sözlükler yerine daha pratik)
db = {
    "python": "Python SimpleHTTP Server - Bilgi Sizintisi Olabilir",
    "apache/2.4.49": "CVE-2021-41773 (Path Traversal & RCE Riski)",
    "nginx/1.18.0": "Eski Versiyon: Bilgi Sizintisi Potansiyeli"
}

def banner_cek(ip, port):
    try:
        s = socket.socket()
        s.settimeout(4) # Biraz daha toleransli bir sure
        s.connect((ip, port))
        
        # Sunucuyu cevap vermeye zorla (HTTP Request)
        istek = f"GET / HTTP/1.1\r\nHost: {ip}\r\nConnection: close\r\n\r\n"
        s.sendall(istek.encode())
        
        cevap = s.recv(1024).decode(errors='ignore').strip()
        s.close()
        return cevap
    except:
        return None

def analiz_et(banner):
    if not banner:
        print("[!] Yanit yok: Port kapali veya firewall engelliyor.")
        return
    
    satirlar = banner.split('\n')
    server_info = satirlar[0]
    print(f"\n[*] Sunucu Donusu:\n{'-'*35}\n{server_info}\n{'-'*35}")
    
    eslesme = False
    for anahtar, mesaj in db.items():
        if anahtar in banner.lower():
            print(f"[!!!] TESPIT EDILEN RISK: {mesaj}")
            eslesme = True
            
    if not eslesme:
        print("[+] Kritik bir versiyon eslesmesi bulunamadi.")

if __name__ == "__main__":
    print("\n--- VERSION SCANNER v1.2 ---")
    hedef_ip = input("[?] IP Adresi: ")
    hedef_port = int(input("[?] Port (Orn: 80, 8000): "))
    
    print(f"[*] {hedef_ip}:{hedef_port} taranıyor...")
    sonuc = banner_cek(hedef_ip, hedef_port)
    analiz_et(sonuc)