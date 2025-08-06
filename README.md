## 📦 KOY

Koy is a minimal, mobile-friendly, and single-user **file upload and sharing** system.
It supports both image and file formats, and provides clean, shareable links for each upload.

---

### 📄 Screenshots

![koy](https://karahanbuhan.com/i/aa14824c1a514741b855899a0c05ec50.png)

---

### ✨ Features

* ✅ Mobile-friendly responsive design
* ✅ Single-page interface (login + upload)
* ✅ Image and file sharing via `/i/` and `/f/` links
* ✅ Storage usage monitoring (in GB and %)
* ✅ Optional HTTPS via Caddy reverse proxy
* ✅ Turkish UI (buttons, labels)
* ✅ No database required — fast and minimal

---

### 💪 Tech Stack

| Technology   | Purpose                               |
| ------------ | ------------------------------------- |
| **Flask**    | Backend application                   |
| **Gunicorn** | Production WSGI server                |
| **Docker**   | Optional containerization             |
| **Caddy**    | Optional HTTPS-enabled reverse proxy  |
| **pico.css** | Minimal CSS framework (modern design) |

---

### 📁 Directory Structure

```
koy/
├── src/
│   ├── app.py             # Flask app definition
│   ├── config.py          # Config via environment variables
│   ├── routes/            # Login, upload, serve endpoints
│   ├── templates/         # index.html (Jinja2, Turkish interface)
│   └── static/            # pico.css and static assets
├── uploads/               # Uploaded files
├── Dockerfile             # Container definition
├── README.md              # Project info
```

---

### ⚙️ Setup

#### 1. Define environment variables:

Set these directly in your environment:

```bash
export KOY_USERNAME=admin
export KOY_PASSWORD=yourpassword
export KOY_SECRET_KEY=yourlongsecretkey
export KOY_DOMAIN=yourdomain.com
export KOY_MAX_STORAGE_GB=5
```

#### 2. Run directly:

```bash
git clone https://github.com/yourname/koy.git
cd koy
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/app.py
```

#### 3. Or build and run with Docker:

```bash
docker build -t koy .
docker run -d --name koy \
  -e KOY_USERNAME=admin \
  -e KOY_PASSWORD=yourpassword \
  -e KOY_SECRET_KEY=yourlongsecretkey \
  -e KOY_DOMAIN=yourdomain.com \
  -e KOY_MAX_STORAGE_GB=5 \
  -v $(pwd)/uploads:/app/uploads \
  -p 8080:8080 koy
```

---

### 🌐 Usage

* Visit your domain: `http://yourdomain.com/koy`
* Login with your credentials
* Upload a file
* Get a direct link:

  * Images: `http://yourdomain.com/i/filename.png`
  * Other: `http://yourdomain.com/f/filename.pdf`

---

### 🔐 Security

* Single-user system
* Auth credentials via environment only
* Strong `SECRET_KEY` required
* Optional HTTPS via Caddy + Let’s Encrypt

---

### 📌 Notes

* Files are stored in `uploads/` — no database used
* Turkish interface throughout
* Optional: add favicon, robots.txt, access logs, etc.

---

### License

[MIT License](https://opensource.org/licenses/MIT)
