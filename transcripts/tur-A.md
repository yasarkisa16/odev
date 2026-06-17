# Tur A — Donatımsız (Kontrol Turu)

> **Kurulum:** Boş sohbet. Project/Gem **YOK**, Kalıcı Talimat **YOK**, Connector **YOK**.
> Tek serbest promptla dashboard üretilir.
>
> **Amaç:** Yönetişim katmanı olmadan çıktının nasıl olduğunu (tutarsızlık, kural
> ihlali, gömülü veri) belgelemek — Tur B ile karşılaştırma için kontrol grubu.

---

## ⚠️ Bu dosyayı kendi gerçek oturum kaydınızla doldurun

Aşağıdaki şablonu, seçtiğiniz araçtan (Claude/Gemini) aldığınız **kesintisiz**
oturum kaydıyla değiştirin. Kırpılmış/düzenlenmiş transcript kanıt sayılmaz (Bölüm 9, -80).

---

### Prompt (kullanıcı)

```
(Buraya tek serbest promptunuzu yapıştırın. Örn:
"VALEO üretim hattı için OEE dashboard'u üret.")
```

### Yanıt (asistan)

```
(Asistanın tam yanıtını / ürettiği kodu buraya yapıştırın.)
```

---

## Gözlem Notları (Tur A)

- [ ] Para birimi / dil tutarlı mı? _(beklenen: tutarsız)_
- [ ] Veri koda gömülü mü? _(beklenen: evet — gömülü)_
- [ ] Tasarım standardına uyuyor mu? _(beklenen: hayır)_
- [ ] İki kez üretildiğinde çıktı sapıyor mu? _(beklenen: evet — sapar)_

> Tekrarlanabilirlik kontrolü: Aynı promptu 2 kez çalıştırın; çıktının nasıl
> saptığını kısaca not edin.
