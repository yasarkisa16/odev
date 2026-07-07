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


def siparis_duzenle():

    # sap_siparis_cek() tarafından üretilen dosya üzerinde çalışılıyor.

    script_dizini = os.path.dirname(os.path.abspath(__file__))

    data_klasoru = os.path.join(script_dizini, "data")

    dosya_yolu = os.path.join(data_klasoru, "siparis.xlsx")

    # Excel sabitleri (late binding kullanıldığı için elle tanımlandı)
    XL_UP = -4162
    XL_TO_LEFT = -4159
    XL_DATABASE = 1
    XL_ROW_FIELD = 1
    XL_PAGE_FIELD = 3
    XL_SUM = -4157

    excel = None
    wb = None

    try:

        # SAP export'un dosyayı diske yazmasını bekliyoruz (yarış durumuna karşı).
        bekleme_sayaci = 0

        while not os.path.exists(dosya_yolu) and bekleme_sayaci < 10:

            time.sleep(1)

            bekleme_sayaci += 1

        if not os.path.exists(dosya_yolu):

            print(f"Hata: '{dosya_yolu}' bulunamadı. sap_siparis_cek() dosyayı bu konuma yazmamış olabilir.")

            return False

        print("siparis.xlsx düzenleniyor...")

        # DispatchEx: mevcut/askıda kalmış bir Excel örneğine bağlanmak yerine
        # her zaman yeni ve izole bir Excel örneği başlatır.
        excel = win32com.client.DispatchEx("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False

        wb = excel.Workbooks.Open(dosya_yolu, UpdateLinks=0, ReadOnly=False, IgnoreReadOnlyRecommended=True)
        ws = wb.Worksheets(1)

        son_satir = ws.Cells(ws.Rows.Count, 1).End(XL_UP).Row
        son_sutun = ws.Cells(1, ws.Columns.Count).End(XL_TO_LEFT).Column

        basliklar = {ws.Cells(1, c).Value: c for c in range(1, son_sutun + 1)}

        figures_sutunu = basliklar["Figures"]
        stockback_sutunu = basliklar["Stock/Back"]

        tum_alan = ws.Range(ws.Cells(1, 1), ws.Cells(son_satir, son_sutun))

        # Önceden kalmış bir AutoFilter durumu varsa temizle (aksi halde
        # parametresiz AutoFilter() çağrısı filtreyi kapatabilir).
        if ws.AutoFilterMode:

            ws.AutoFilterMode = False

        # 1 ve 2 tek adımda: tüm başlıklara filtre oku eklenir ve aynı anda
        # Figures sütunu "Customer demand" değerine göre filtrelenir.
        tum_alan.AutoFilter(Field=figures_sutunu, Criteria1="Customer demand")

        print("Filtreler uygulandı (tüm başlıklarda filtre oku + Figures = Customer demand).")

        # 3. Pivot tablo mantığında yeni sekme: satırlarda Material,
        # değerlerde Stock/Back + tüm ay sütunlarının toplamı (Sum).
        pivot_sekme_adi = "siparis_pivot"

        mevcut_sekme_adlari = [sh.Name for sh in wb.Worksheets]

        if pivot_sekme_adi in mevcut_sekme_adlari:

            wb.Worksheets(pivot_sekme_adi).Delete()

        pivot_ws = wb.Worksheets.Add()
        pivot_ws.Name = pivot_sekme_adi

        pivot_cache = wb.PivotCaches().Create(SourceType=XL_DATABASE, SourceData=tum_alan)
        pivot_tablo = pivot_cache.CreatePivotTable(TableDestination=pivot_ws.Range("A3"), TableName="SiparisPivot")

        # Figures alanı rapor filtresine konuyor, sadece "Customer demand" seçili kalıyor.
        figures_alani = pivot_tablo.PivotFields("Figures")
        figures_alani.Orientation = XL_PAGE_FIELD
        figures_alani.CurrentPage = "Customer demand"

        # Satır etiketi: Material
        pivot_tablo.PivotFields("Material").Orientation = XL_ROW_FIELD

        # Veri alanları: Stock/Back + tüm ay sütunları (Sum)
        for c in range(stockback_sutunu, son_sutun + 1):

            alan_adi = ws.Cells(1, c).Value

            pivot_tablo.AddDataField(pivot_tablo.PivotFields(alan_adi), f"Sum of {alan_adi}", XL_SUM)

        wb.Save()

        degisiklik_zamani = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(dosya_yolu)))

        print(f"'{pivot_sekme_adi}' sekmesinde pivot tablo oluşturuldu ve dosya kaydedildi.")
        print(f"Dosya yolu: {dosya_yolu}")
        print(f"Son değişiklik zamanı: {degisiklik_zamani}")

        return True

    except Exception as e:

        print(f"Bir hata oluştu! Hata detayı: \n{e}")

        return False

    finally:

        try:

            if wb is not None:

                wb.Close(SaveChanges=False)

        except Exception as e:

            print(f"Uyarı: Çalışma kitabı kapatılırken hata oluştu: {e}")

        try:

            if excel is not None:

                excel.Quit()

        except Exception as e:

            print(f"Uyarı: Excel kapatılırken hata oluştu: {e}")


# Kodu çalıştır

if __name__ == "__main__":

    if sap_sisteme_gir():

        if sap_siparis_cek():

            siparis_duzenle()
