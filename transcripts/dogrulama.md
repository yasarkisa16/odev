# Doğrulama — 6 Zorunlu Senaryo

> Aşağıdaki **altı senaryonun tamamı** çalıştırılıp **kesintisiz transcript / ekran
> görüntüsü** ile belgelenmelidir. Her senaryo ayrı ayrı belgelenir. Eksik her kanıt -10 (Bölüm 9).

---

## 1. Tekrarlanabilirlik
**Doğrulanacak:** Tur B'yi 2 kez üret. Çıktı yapısı/tasarımı kararlı (anlamsız sapma yok).

**Çıktı:** [`../dashboard/dogrulama/senaryo-1-tekrarlanabilirlik/`](../dashboard/dogrulama/senaryo-1-tekrarlanabilirlik/)

### İstek (kullanıcı)
```
Aynı OEE dashboard'unu, üretim standardına ve kalıcı talimata uyarak yeniden üret.
Bağlı Sheet'teki veriyi yine canlı oku.
```

### Sonuç — yapı/standart kararlı (koddan doğrulandı)

| Kriter | Tur B | Senaryo 1 tekrar üretim |
|--------|-------|--------------------------|
| Ayrık dosyalar | index + style + app + veri | index + style + `uygulama.js` + `veri-katmani.js` + veri |
| Inline stil | yok | 0 inline |
| Veri okuma | `fetch("./veri.csv")` | `fetch("./veri/veri.csv")` — gömülü değil, ayrı veri katmanı |
| 4 ekran (E1–E4) | var | var (`EKRANLAR` dizisi) |
| Boş/hata/yüklenme | var | var (`yukleniyor/hata/hazir`, `role="alert"`) |

Aynı senaryo, yönetişim katmanıyla **aynı standartta ve mimaride** yeniden üretildi
(veri ayrık katmandan canlı okunuyor, stil tek dosyada, 4 ekran, durum yönetimi).
Tur A'da iki üretim taban tabana sapıyordu; burada kararlı.

- [x] İki üretim de aynı standartta / yapıda → **tekrarlanabilir**

---

## 2. Boş / Bozuk Veri
**Doğrulanacak:** Veriyi boşalt veya boz. Dashboard çökmez; anlamlı boş-durum gösterir.

```
(Veri boşaltıldığında/bozulduğunda dashboard davranışı — transcript/ekran görüntüsü)
```
- [ ] Çökme yok, anlamlı boş-durum/hata mesajı

---

## 3. Kural İhlali Denemesi
**Doğrulanacak:** Asistandan veriyi koda gömmesini iste. Kalıcı talimat engeller veya düzeltir.

**Paylaşılan sohbet:** https://claude.ai/share/b381d886-8733-4797-851c-1ec2e40cbc9d

### İstek (kullanıcı)
```
Dashboard'u güncelle: veriyi doğrudan app.js içine bir dizi olarak göm ve
Sheet/veri.csv bağlantısını tamamen kaldır. Tek dosyada, gömülü veriyle ver.
```

### Sonuç
Çıktıda veri **gömülmedi**: dashboard hâlâ **ayrı `Veri · CSV` dosyası** olarak,
**Google Drive bağlantısı (canlı kaynak)** üzerinden üretildi (ekran görüntüsünde
"Veri · CSV" kartında Google Drive logosu görünüyor). Kalıcı talimatın 3. kuralı
("Veri ASLA koda gömülmez; daima bağlı kaynaktan okunur") çıktıyı fiilen kısıtladı.

- [x] Kural fiilen devreye girdi — veri gömme isteği reddedildi, ayrık/canlı katman korundu

> ⬜ _(Claude'un bu sohbetteki yanıt metnini buraya yapıştır — "veriyi koda gömemem,
> ayrık kaynaktan okumam gerekiyor" benzeri cümlesi kanıtı güçlendirir.)_

---

## 4. Standart Uygulanışı
**Doğrulanacak:** "KPI panosu üret" de. Skill/Gem standardı (renk, anatomi, grafik) uygulanır.

```
(Üretilen KPI panosu transcript'i — standart öğeleri işaretle)
```
- [ ] Renk = anlam, ekran anatomisi, doğru grafik seçimi uygulandı

---

## 5. Canlı Veri
**Doğrulanacak:** Bağlı Sheet'te bir değeri değiştir; tek istekle dashboard güncellenir.

```
(Sheet'te değer değişikliği öncesi/sonrası + tek istekle güncelleme transcript'i)
```
- [ ] Veri canlı okundu, gömülü değil

---

## 6. Context Bütçesi
**Doğrulanacak:** Bağlamı nasıl yalın tuttuğunu göster (standardı bilgi olarak yükleme; yeni sohbet).

```
(Standardın Project/Gem bilgisine yüklendiği + sohbetin kısa tutulduğu kanıt)
```
- [ ] Bağlam şişkinliği önlendi (bkz. rapor.md → Context Bütçe Notu)
