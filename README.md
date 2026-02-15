VersionScanner-Py
Bu araç, ağ üzerindeki servislerin "Banner" bilgilerini yakalayarak versiyon analizi yapan basit bir tarayıcıdır. Siber güvenlik çalışmalarımda servislerin zafiyetli olup olmadığını hızlıca kontrol etmek için geliştirdim.

🚀 Özellikler
Banner Grabbing: Hedef servisin kimlik bilgisini (Server Header) çeker.

Force-Talk: Yanıt vermeyen HTTP sunucularını konuşmaya zorlamak için otomatik GET isteği gönderir.

Basic Vuln-DB: Yakalanan versiyonları bilinen kritik CVE'lerle (örneğin Apache 2.4.49 zafiyeti) karşılaştırır.

🛠️ Kurulum ve Kullanım
Kod herhangi bir harici kütüphane gerektirmez, standart Python kütüphaneleriyle çalışır.

python scanner.py komutuyla çalıştırın.

Hedef IP ve Port bilgisini girin.

Çıkan sonucu analiz edin.
