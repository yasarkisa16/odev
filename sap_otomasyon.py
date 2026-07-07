import os
import subprocess
import time

import win32com.client

def sap_sisteme_gir():

    # 1. Değişkenler

    sap_yolu = r"C:\Program Files (x86)\SAP\FrontEnd\SAPGUI\saplogon.exe"

    sistem_adi = "00 - Production - Comp@ss V4 - PARIS/France PTS/Turkey/Egypt [P07]"



    try:

        # 2. SAP Logon'u başlat

        print("SAP Logon başlatılıyor...")

        subprocess.Popen(sap_yolu)



        # SAP Logon penceresinin tam olarak yüklenmesi için 5 saniye bekliyoruz.

        # (Eğer bilgisayarınızda daha yavaş açılıyorsa bu süreyi 7 veya 10 yapabilirsiniz)

        time.sleep(5)



        # 3. SAP Scripting Engine'e bağlan ve sisteme tıkla

        print(f"'{sistem_adi}' sistemine bağlanılıyor...")



        # Çalışan SAP GUI objesini yakala

        SapGuiAuto = win32com.client.GetObject("SAPGUI")

        application = SapGuiAuto.GetScriptingEngine



        # Belirtilen bağlantıyı aç (SSO varsa direkt ana ekrana düşer)

        connection = application.OpenConnection(sistem_adi, True)



        print("Sisteme başarıyla giriş yapıldı! SAP ekranınız şu an açık olmalı.")

        return True

    except Exception as e:

        print("\n!!! BİR HATA OLUŞTU !!!")

        print(f"Hata detayı: {e}")

        print("Not: 'win32com' kütüphanesi kurulu değilse terminale 'pip install pywin32' yazarak kurmayı unutmayın.")

        return False


def sap_siparis_cek():

    # data klasörü, bu script ile aynı dizinde bekleniyor.

    script_dizini = os.path.dirname(os.path.abspath(__file__))

    data_klasoru = os.path.join(script_dizini, "data")

    dosya_adi = "siparis.xlsx"

    try:

        os.makedirs(data_klasoru, exist_ok=True)

        print("SAP GUI bağlantısı kuruluyor...")
        # 1. Açık olan SAP GUI uygulamasını yakala
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine

        # Aktif bağlantı ve oturumu al
        connection = application.Connections(0)
        session = connection.Sessions(0)

        print("SAP penceresi büyütülüyor ve ZP07 işlem koduna gidiliyor...")
        session.findById("wnd[0]").maximize()

        # ZP07'ye giriş yap
        session.findById("wnd[0]/tbar[0]/okcd").text = "zp07"
        session.findById("wnd[0]").sendVKey(0)
        time.sleep(2)  # Ekranın yüklenmesi için kısa bir bekleme

        print("Filtre alanları dolduruluyor...")
        # Filtreleri doldur (VBS kaydındaki alanlar)
        session.findById("wnd[0]/usr/ctxtS_WERKS-LOW").text = "BU10"
        session.findById("wnd[0]/usr/txtP_NUMWW").text = ""
        session.findById("wnd[0]/usr/ctxtP_SCAL").text = "TR"

        # Malzeme çoklu seçim butonuna bas
        session.findById("wnd[0]/usr/btn%_S_MATNR_%_APP_%-VALU_PUSH").press()
        time.sleep(1)

        # Malzeme kodunu gir
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = "587570vd"

        # Seçimleri onayla ve rapora dön (F8 adımları)
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/tbar[0]/btn[8]").press()

        print("Rapor çalıştırılıyor (F8)...")
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        time.sleep(5)  # Raporun yüklenme süresine göre gerekirse artırılabilir

        print("Veriler Excel formatında dışarı aktarılıyor...")
        # Excel dışa aktar menülerini tetikle
        grid_shell = session.findById("wnd[0]/usr/cntlZALV/shellcont/shell")
        grid_shell.pressToolbarContextButton("&MB_EXPORT")
        grid_shell.selectContextMenuItem("&XXL")
        time.sleep(2)

        # 1. onay penceresi (format seçimi - Yeşil tik)
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        time.sleep(1)

        # 2. pencere: kayıt yeri/dosya adı alanları varsa 'data' klasörünü ve
        # sabit dosya adını buraya yazıyoruz. Bu alanlar bu ekranda yoksa
        # (SAP sürümüne göre değişebilir), varsayılan davranışa geri dönülür.
        try:

            session.findById("wnd[1]/usr/ctxtDY_PATH").text = data_klasoru
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = dosya_adi

            print(f"Kayıt yolu '{data_klasoru}' ve dosya adı '{dosya_adi}' olarak ayarlandı.")

        except Exception:

            print("Uyarı: Dizin/dosya adı alanları bu ekranda bulunamadı, SAP'nin varsayılan konumu kullanılacak.")

        # Çıkan onay penceresini geç (Yeşil tik butonu)
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        time.sleep(3)  # Excel'in bilgisayarda açılma süresi için bekleme

        print(f"İşlem başarıyla tamamlandı! Çıktı '{data_klasoru}' klasörüne yazılmaya çalışıldı.")

        return True

    except Exception as e:

        print(f"Bir hata oluştu! Hata detayı: \n{e}")

        return False


# Kodu çalıştır

if __name__ == "__main__":

    if sap_sisteme_gir():

        sap_siparis_cek()
