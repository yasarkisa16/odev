# Rapor — Ödev #1: Yönetişimli Dashboard Üretim Hattı

> Rapor, çıktıyı betimlemekten çok **tasarım kararlarınızı** açıklamalıdır.
> Yönetişim mimarisi için bir **diyagram zorunludur**.
> Bu `.md` tamamlandıktan sonra PDF'e çevrilip `rapor.pdf` olarak da eklenmelidir.

---

## Kapak

| Alan | Değer |
|------|-------|
| Ad-Soyad | _(doldurun)_ |
| Ekip | _(Ar-Ge / Tasarım / After-Market)_ |
| Seçilen Araç | _(Gemini / Claude)_ |
| Senaryo | **S1 — Hat Verimi & OEE Panosu** |

---

## 1. Senaryo & Persona

- **Persona:** Üretim Müdürü
- **Pano kimin, hangi karar için:** Üretim Müdürü'nün vardiya/hat verimliliğini izleyip
  duruş kayıplarına müdahale kararı vermesi için.
- **Cevapladığı 3 soru:**
  1. Hangi hat / vardiya OEE hedefinin altında?
  2. Toplam duruşun başlıca nedenleri neler?
  3. OEE trendi iyileşiyor mu?

---

## 2. Yönetişim Mimarisi (DİYAGRAM ZORUNLU)

Bağlam / Kalıcı Talimat / Skill-Gem / Canlı Veri nasıl birlikte çalışıyor:

```mermaid
flowchart TD
    subgraph Asistan Kabı["Bağlam — Project / Gem"]
        R["Kalıcı Talimat (Rule)\n₺ biçimi · Türkçe · veri gömme · erişilebilirlik"]
        S["Üretim Standardı (Skill/Gem)\ntasarım sistemi · ekran anatomisi · grafik seçimi"]
    end
    D[("Canlı Veri\nGoogle Sheet / Connector (MCP)")]
    P["Kullanıcı promptu\n(kısa & odaklı)"]
    O["Dashboard çıktısı\n4 ekran · kurallı · tekrarlanabilir"]

    P --> Asistan Kabı
    D -- "canlı okuma" --> Asistan Kabı
    R --> O
    S --> O
    Asistan Kabı --> O
```

> Diyagramı kendi mimarinize göre güncelleyin (Mermaid yerine görsel de eklenebilir).

---

## 3. Context Bütçe Notu

Bağlamı nasıl yalın tuttunuz + neden önemli:

- Üretim standardını **her sohbete yapıştırmak yerine** Project/Gem **bilgisine** yükledim.
- Kuralları **kalıcı talimat** alanına taşıdım; sohbet kısa ve odaklı kaldı.
- Sohbet uzayınca **özetleyip yeni sohbete** geçtim.
- **Neden önemli:** Bağlam şişkinliği token yakar, odağı dağıtır ve tutarlılığı düşürür
  (Bölüm 9: bağlam şişkinliği -20).
- _(Mümkünse önce/sonra ekran görüntüsü ekleyin → `ekran-goruntuleri/`)_

---

## 4. Tur A vs Tur B Karşılaştırması

| Eksen | Tur A (Donatımsız) | Tur B (Donatılmış) |
|-------|--------------------|--------------------|
| Tasarım tutarlılığı | _(genelde tutarsız)_ | _(standart sayesinde tutarlı)_ |
| Kural uyumu | _(kural yok)_ | _(₺/Türkçe/erişilebilirlik uygulandı)_ |
| Veri bağlama | _(kopyala-yapıştır / gömülü)_ | _(canlı Sheet bağlantısı)_ |
| Tekrarlanabilirlik | _(sapar)_ | _(kararlı)_ |

---

## 5. En Etkili 3–5 Prompt

1. `(tam metin + varsa öncesi/sonrası iyileştirme)`
2. `...`
3. `...`

---

## 6. Engeller & Çözümler (en az 2)

1. **Engel:** _(örn. asistan veriyi koda gömmeye çalıştı)_ → **Çözüm:** _(kalıcı talimata "veri gömme" kuralı eklendi)_
2. **Engel:** _(örn. bağlam şişkinliği)_ → **Çözüm:** _(standart Project/Gem bilgisine taşındı)_

---

## 7. Öz-Değerlendirme

- Kalite kontrol listesi sonucu: _(README Bölüm 5 kanıt tablosu)_
- Geliştirilecek 1 alan: _(doldurun)_
