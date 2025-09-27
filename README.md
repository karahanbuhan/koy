## KOY

Koy, minimal, mobil uyumlu ve tek kullanıcılı bir **dosya yükleme ve paylaşım** sistemidir. Hem görsel hem de diğer dosya formatlarını destekler ve her yükleme için temiz, paylaşılabilir bağlantılar sunar.

---

### Ekran Görüntüleri

![koy](https://karahanbuhan.com/i/aa14824c1a514741b855899a0c05ec50.png)

---

### Özellikler

* Mobil uyumlu, duyarlı tasarım
* Tek sayfalı arayüz (oturum açma + yükleme)
* Görsel ve dosya paylaşımı için `/i/` ve `/f/` bağlantıları
* Depolama kullanımı izleme (GB ve % cinsinden)
* Caddy proxy sunucusu ile isteğe bağlı HTTPS
* Türkçe arayüz (düğmeler, etiketler)
* Veritabanı gerektirmez, dosya tabanlı — hızlı ve minimal

---

### Teknolojiler

| Teknoloji    | Amaç                                  |
|--------------|---------------------------------------|
| **Flask**    | Arka uç uygulaması                    |
| **Gunicorn** | Üretim WSGI sunucusu                  |
| **Docker**   | İsteğe bağlı konteynerleştirme        |
| **Caddy**    | İsteğe bağlı HTTPS destekli ters vekil |
| **pico.css** | Minimal CSS çerçevesi (modern tasarım) |

---

### Dizin Yapısı

```
koy/
├── src/
│   ├── app.py             # Flask uygulama tanımı
│   ├── config.py          # Çevresel değişkenlerle yapılandırma
│   ├── routes/            # Oturum açma, yükleme, sunum uç noktaları
│   ├── templates/         # index.html (Jinja2, Türkçe arayüz)
│   └── static/            # pico.css ve statik varlıklar
├── uploads/               # Yüklenen dosyalar
├── Dockerfile             # Konteyner tanımı
├── README.md              # Proje bilgisi
```

---

### Kurulum

#### 1. Environment değişkenlerini tanımlayın:

Aşağıdaki değişkenleri doğrudan ortamınıza ayarlayın:

```bash
export KOY_USERNAME=admin
export KOY_PASSWORD=parolanız
export KOY_SECRET_KEY=uzungizlianahtarınız
export KOY_DOMAIN=alanadınız.com
export KOY_MAX_STORAGE_GB=5
```

#### 2. Doğrudan çalıştırın:

```bash
git clone https://github.com/adınız/koy.git
cd koy
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/app.py
```

#### 3. Ya da Docker ile derleyin ve çalıştırın:

```bash
docker build -t koy .
docker run -d --name koy \
  -e KOY_USERNAME=admin \
  -e KOY_PASSWORD=parolanız \
  -e KOY_SECRET_KEY=uzungizlianahtarınız \
  -e KOY_DOMAIN=alanadınız.com \
  -e KOY_MAX_STORAGE_GB=5 \
  -v $(pwd)/uploads:/app/uploads \
  -p 8080:8080 koy
```

---

### Kullanım

1. Alan adınızı ziyaret edin: `http://alanadınız.com/koy`
2. Kimlik bilgilerinizle oturum açın
3. Bir dosya yükleyin
4. Doğrudan bağlantı alın:
  * Görseller: `http://alanadınız.com/i/dosyaadı.png`
  * Diğer: `http://alanadınız.com/f/dosyaadı.pdf`

---

### Güvenlik

* Tek kullanıcılı sistem
* Kimlik doğrulama bilgileri yalnızca çevresel değişkenler üzerinden
* Güçlü bir `SECRET_KEY` gereklidir
* HTTPS (Caddy + Let’s Encrypt ile)
* **Uyarı:** Kimlik doğrulama sistemi, yanlış girişlerde bekleme süresi (cooldown) gibi ek güvenlik önlemleri içermediğinden aşırı güvenli değildir. İş amaçlı kullanım için önerilmez.

---

### Notlar

* Dosyalar `uploads/` dizininde saklanır — veritabanı kullanılmaz
* İsteğe bağlı: favicon, robots.txt, erişim günlükleri vb. eklenebilir

---

### Lisans

[MIT Lisansı](https://opensource.org/licenses/MIT)