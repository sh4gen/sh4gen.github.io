# SH4GEN Static Site (Modular)

Bu repo, `a.py` içerisindeki React/JSX içeriğini basit bir statik site olarak modüler şekilde ayırır.

- `index.html` — ana HTML entry
- `css/style.css` — özel stiller (CustomStyles içeriğinden çıkarıldı)
- `js/app.jsx` — React uygulaması (CDN React + Babel ile tarayıcıda derlenir)
- `CNAME` — hedef GitHub Pages URL: `sh4gen.github.io`

Yerel test:

```powershell
# Windows: açmak için
start .\index.html
```

Yayınlama (özet):

1. GitHub'da yeni bir repo oluşturun ismi: `sh4gen.github.io`.
2. Bu dosyaları commit ve push yapın.
3. GitHub Pages otomatik olarak `main` branch'inden yayınlayacaktır (yaklaşık birkaç dakika).

Not: Bu çözüm hızlı bir statik demo içindir. Daha sağlam bir React projesi isterseniz, `create-react-app` veya Vite ile bir yapılandırma ekleyebilirim.
