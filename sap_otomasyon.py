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


def sap_siparis_calistir():

    # sap_siparis.exe ve data klasörü, bu script ile aynı dizinde bekleniyor.

    script_dizini = os.path.dirname(os.path.abspath(__file__))

    exe_yolu = os.path.join(script_dizini, "sap_siparis.exe")

    data_klasoru = os.path.join(script_dizini, "data")

    try:

        os.makedirs(data_klasoru, exist_ok=True)

        print("sap_siparis.exe çalıştırılıyor...")

        # Çıktı klasörü pozisyonel argüman olarak veriliyor.
        # Process tamamlanana kadar (kapanana kadar) bekleniyor.
        subprocess.run([exe_yolu, data_klasoru], check=True)

        print(f"sap_siparis.exe tamamlandı. Çıktılar '{data_klasoru}' klasörüne yazıldı.")

        return True

    except subprocess.CalledProcessError as e:

        print("\n!!! sap_siparis.exe HATA İLE SONLANDI !!!")
        print(f"Çıkış kodu: {e.returncode}")

        return False

    except Exception as e:

        print("\n!!! BİR HATA OLUŞTU !!!")
        print(f"Hata detayı: {e}")

        return False


# Kodu çalıştır

if __name__ == "__main__":

    if sap_sisteme_gir():

        sap_siparis_calistir()
