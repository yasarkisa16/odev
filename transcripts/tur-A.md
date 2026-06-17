# Tur A — Donatımsız (Kontrol Turu)

> **Kurulum:** Boş sohbet. Project/Gem **YOK**, Kalıcı Talimat **YOK**, Connector **YOK**.
> Tek serbest promptla dashboard üretilir.
>
> **Amaç:** Yönetişim katmanı olmadan çıktının nasıl olduğunu (tutarsızlık, kural
> ihlali, gömülü veri) belgelemek — Tur B ile karşılaştırma için kontrol grubu.

**Araç:** Claude (claude.ai) · **Senaryo:** S1 — OEE Panosu

---

## Paylaşılan sohbet linki

https://claude.ai/share/1b3ba858-ff98-49dc-ad40-c5b779fe6f08

---

## Üretim 1

### Prompt (kullanıcı)

```
VALEO üretim hattı için bir OEE (Genel Ekipman Etkinliği) dashboard'u üret.
Üretim Müdürü için olsun; hat ve vardiya bazında OEE, kullanılabilirlik,
performans, kalite ve duruş nedenlerini göstersin. Tek dosyada HTML/CSS/JS
olarak ver.
```

### Çıktı

Tek dosya HTML/CSS/JS dashboard üretildi → [`../dashboard/tur-A/valeo-oee-dashboard.html`](../dashboard/tur-A/valeo-oee-dashboard.html)

> ⬜ _(Sohbetin tam metnini buraya yapıştırın — Claude'un yanıtı dahil, kesintisiz.)_

---

## Üretim 2 (tekrarlanabilirlik kontrolü)

> ⬜ Aynı promptu **boş yeni bir sohbette** 2. kez çalıştırın ve çıktıyı buraya ekleyin.
> Beklenen: yapı/tasarım **sapar** (farklı renk paleti, farklı bölüm düzeni, farklı grafik seçimi).

```
(2. üretimin çıktısı / farklılık notu)
```

---

## Gözlem Notları (Tur A — gerçek çıktıdan)

| Gözlem | Durum | Kanıt |
|--------|-------|-------|
| Veri koda gömülü mü? | ❌ **Gömülü** (beklenen) | `mulberry32` seeded RNG + `generateDataset(30)` ile veri JS içinde üretiliyor; bağlı kaynak yok |
| Inline CSS / `<script>`? | ❌ **Var** (beklenen) | Tüm stil ve script tek dosyada gömülü |
| Dekoratif efekt? | ⚠️ Var | `radial-gradient` arka plan + gölgeler — standartla çelişir |
| Türkçe etiket | ✅ Var | ama kural zorlamadı; araç kendiliğinden yaptı |
| Boş-durum mesajı | ✅ Var | "Seçili filtreyle eşleşen veri yok" |
| Tekrarlanabilirlik | ⚠️ Garanti değil | yönetişim yok → 2. üretimde yapı/tasarım sapar |

**Sonuç:** Çıktı görsel olarak başarılı; ancak veri gömülü, stil ayrık değil ve
tekrarlanabilirlik garanti edilmiyor. Bu eksiklikler Tur B'de yönetişim katmanıyla
giderilecek (bkz. `tur-B.md`).
