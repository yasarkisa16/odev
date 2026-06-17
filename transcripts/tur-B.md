# Tur B — Donatılmış (Tam Yönetişim Katmanı)

> **Kurulum:** Bölüm 3'teki tam yönetişim katmanı aktif:
> Bağlam (Project/Gem) + Kalıcı Talimat (Rule) + Üretim Standardı (Skill/Gem) + Canlı Veri (Connector).
>
> **Amaç:** Aynı senaryoyu kurallı ve tekrarlanabilir biçimde üretmek ve her
> mekanizmanın etkisini transcript'te kanıtlamak.

---

## ⚠️ Bu dosyayı kendi gerçek oturum kaydınızla doldurun

Aşağıdaki kanıtların transcript içinde **görünür** olması gerekir; yoksa ilgili
feature çalışmamış sayılır.

---

### Prompt (kullanıcı)

```
(Buraya promptunuzu yapıştırın. Örn:
"Bağlı Sheet'teki veriyi oku ve OEE dashboard'unu üret. Veriyi koda gömme;
üretim standardını uygula.")
```

### Yanıt (asistan)

```
(Asistanın tam yanıtını / ürettiği kodu buraya yapıştırın.)
```

---

## Kanıt Kontrol Listesi (Tur B)

| Kanıt | Nasıl görünmeli | ✓ |
|-------|-----------------|---|
| **Standart uygulandı** | Çıktı Skill/Gem standardına (renk/anatomi/grafik) uyuyor | ⬜ |
| **Kural etkin** | Bir talimat çıktıyı fiilen kısıtladı (örn. veri gömme reddedildi) | ⬜ |
| **Canlı veri** | Connector bağlı; veri Sheet'ten canlı okundu (gömülü değil) | ⬜ |
| **Bağlam yalın** | Standart/bilgi sohbete yapıştırılmadan Project/Gem'e yüklendi | ⬜ |

> Canlı veri kanıtı için `ekran-goruntuleri/` altına Connector bağlantı ekran
> görüntüsü ekleyin ve transcript'te canlı okumanın görüldüğü anı işaretleyin.
