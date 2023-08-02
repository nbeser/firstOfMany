from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox, QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys
from _polatLab import Ui_MainWindow
from app import App
from dbmanager import DbManager
from PyQt5.QtGui import QPalette, QColor, QIcon
from _musteriEkleme import Ui_widget_musteriEkle
from _makinaEkleme import Ui_widget_makinaEkle
from _analizEkleme import Ui_AnalizEkleme
import datetime
from _guncelleme import Ui_Guncelleme
from upToDate import *
from _silmek import Ui_Silmek
from pandasExcel import Excel
from analiz import Analiz





class Window(QtWidgets.QMainWindow):
    
    
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.app = App()
        self.db = DbManager()
        self.ex = Excel()
               

        # Analiz ekleme kısmı için bu kısım yazıldı
        # self.analizOngoingDic = analizVerileriDictionary
        self.analizler = []
        
        # makina ekleme
        self.id_index_text_makina_ekleme = ""

        # müşteri güncelleme için
        self.musteriBilgiler = musteriBilgiler
        self.musteriOngoing = {}

        # makina güncelleme için
        self.makinaBilgiler = makinaBilgiler

        # analiz güncelleme içim
        self.analizBilgiler = analizBilgiler

        # müşteri makina id listesi
        self.musteriMakinaId = []
        
        # excel için kod
        self.excelKodu = ""
        self.excelMusteriId = 0
        self.excelMusteriAd = ""


        self.ui.btnMusteriListesi.clicked.connect(self.musteriListesi)
        self.ui.btnMusteriAnaliz.clicked.connect(self.musteriAnaliz)
        self.ui.pushButton_2.clicked.connect(self.ekranTemizle)
        self.ui.btnMusteriMakinaListesi.clicked.connect(self.musteriMakinaListesi)

        self.ui.btnMusteriEkle.clicked.connect(self.musteriEkle)
        self.ui.btnMakinaEkle.clicked.connect(self.makinaEkle)
        self.ui.btnAnalizEkle.clicked.connect(self.analizEkle)
        self.ui.btnGuncelleme.clicked.connect(self.guncelleme)
        self.ui.btnSilme.clicked.connect(self.silmek)
       


    def ekranTemizle(self):
        self.ui.listWidget.clear()

    def musteriListesi(self):
        self.ui.comboBox.clear()
        self.ui.listWidget.clear()
        musteri_listesi = self.app.musteriListesi()
        self.ui.listWidget.addItems(musteri_listesi)
        self.excelKodu = "musteri"
        self.ui.excel.clicked.connect(self.toExcel)
        self.ui.label.clear()


    def labelAlert(self, alert):
        self.ui.label.setText(str(alert))
        self.ui.label.setStyleSheet("color: red")

    
    def musteriAnaliz(self):
        self.ui.comboBox.clear()
        musteri_listesi = self.app.musteriListesi()
        self.ui.listWidget.clear()

        self.ui.comboBox.addItems(musteri_listesi)
        alert1 = "Lütfen analiz için listeden bir müşteri seçiniz ve seç tuşuna tıklayınız."
        self.labelAlert(alert1)
        self.ui.pushButton.clicked.connect(self.musteriIdAnaliz)
    
    def musteriIdAnaliz(self):
        self.ui.listWidget.clear()
        id_index = int(self.ui.comboBox.currentIndex())
        id = self.db.musteriGenel()[id_index].id
        analizler = self.app.analizByMusteriId(id)
        self.ui.listWidget.addItems(analizler)
        self.excelKodu = "analiz"
        self.excelMusteriAd = self.db.musteriGenel()[id_index].musteri_ad
        self.excelMusteriId = id
        self.ui.excel.clicked.connect(self.toExcel)
        
    
    def musteriMakinaListesi(self):
        self.ui.comboBox.clear()
        musteri_listesi = self.app.musteriListesi()
        self.ui.listWidget.clear()
        self.ui.comboBox.addItems(musteri_listesi)
        alert = "Lütfen makina listesi için listeden müşteri seçimi yapınız ve seç tuşuna tıklayınız."
        self.labelAlert(alert)
        self.ui.pushButton.clicked.connect(self.musteriListeGoruntuleme)
    
    def musteriListeGoruntuleme(self):
        self.ui.listWidget.clear()
        id_index = int(self.ui.comboBox.currentIndex())
        id = self.db.musteriGenel()[id_index].id
        makineler = self.app.musteriMakinaListesi(id)
        self.ui.listWidget.addItems(makineler)
        self.excelKodu = "makina"
        self.excelMusteriAd = self.db.musteriGenel()[id_index].musteri_ad
        self.excelMusteriId = id
        self.ui.excel.clicked.connect(self.toExcel)


 
    def musteriEkle(self):
        self.widgetMusteri = QtWidgets.QWidget()
        self.widgetMusteri.setParent(None)
        self.ui_me = Ui_widget_musteriEkle()
        self.ui_me.setupUi(self.widgetMusteri)
        self.widgetMusteri.setWindowTitle("Müşteri Ekleme")
        self.widgetMusteri.setWindowIcon(QIcon("polatIcon.jpg"))
        self.widgetMusteri.show()
        self.ui.btnAnalizEkle.clicked.connect(lambda:self.widgetMusteri.close())
        self.ui.btnMakinaEkle.clicked.connect(lambda:self.widgetMusteri.close())
        alert = ""
        self.labelAlert(alert)

        self.ui_me.pushButton.clicked.connect(self.senderMusteri)
        
    def senderMusteri(self):
        buton_text = self.ui_me.pushButton.sender().text()

        if buton_text == "Kaydet":
            if (self.ui_me.ln_musteriAd.text() == '') or (self.ui_me.ln_musteriBolge.text() == ''):
                self.ui_me.lbl.setText("Lütfen bilgileri eksiksiz giriniz.")
            else:
                self.musteriKayit()
                # self.widgetMusteri.close()
        else:
            pass

    def musteriKayit(self):
        musteriler = []
        for i in self.db.musteriGenel():
            musteriler.append(i.musteri_ad)
        musteri_adi = self.ui_me.ln_musteriAd.text()
        musteri_bolge = self.ui_me.ln_musteriBolge.text()        
        if musteri_adi not in musteriler:
            self.app.addMusteri(musteri_adi, musteri_bolge)
            self.ui_me.lbl.setText("Müşteri ekleme tamamlandı.")
            self.ui_me.ln_musteriAd.clear()
            self.ui_me.ln_musteriBolge.clear()
        else:                
            self.ui_me.lbl.setText("Müşteri kaydı mevcuttur.")

        

    def makinaEkle(self):
        self.widgetMakina = QtWidgets.QWidget()
        self.widgetMakina.setParent(None)
        self.ui_mak = Ui_widget_makinaEkle()
        self.ui_mak.setupUi(self.widgetMakina)
        self.widgetMakina.setWindowTitle("Makina Ekleme")
        self.widgetMakina.setWindowIcon(QIcon("polatIcon.jpg"))
        self.widgetMakina.show()
        self.ui.btnAnalizEkle.clicked.connect(lambda:self.widgetMakina.close())
        self.ui.btnMusteriEkle.clicked.connect(lambda:self.widgetMakina.close())
        self.ui_mak.ln_gun.setPlaceholderText("Gün")
        self.ui_mak.ln_ay.setPlaceholderText("Ay")
        self.ui_mak.ln_yil.setPlaceholderText("Yıl")
        self.ui_mak.ln_makinaAd.setPlaceholderText("Makina adı")
        self.ui_mak.ln_makinaSeriNum.setPlaceholderText("Makina seri numarası")
        self.ui_mak.lbl_makinaEklemeTalimatlar.setText("Makina eklemek için öncelikle listeden müşteri seçiniz ve 'Müşteri Seç' butonuna basınız")
        alert = ""
        self.labelAlert(alert)

        musteri_listesi = self.app.musteriListesi()
        self.ui_mak.comboBox_musteriler.addItems(musteri_listesi)
        self.ui_mak.btnMusteriSec.clicked.connect(self.idIndex)
        self.ui_mak.btnSave.clicked.connect(self.secim)

    def secim(self):
        if self.id_index_text_makina_ekleme == "Seçim":
            self.makinaEkleme_islem1()            
        else:
            self.uyariMakinaSecimi()

    def idIndex(self):
        self.id_index_text_makina_ekleme = self.ui_mak.btnMusteriSec.sender().text()
        self.ui_mak.lbl_makinaEklemeTalimatlar.setText(self.db.musteriGenel()[self.ui_mak.comboBox_musteriler.currentIndex()].musteri_ad+" Müşterisi Seçildi")

    def uyariMakinaSecimi(self):
        self.ui_mak.lbl_makinaEklemeTalimatlar.setText("Listeden müşteri seçiniz ve ardından 'Müşteri Seç' butonuna basınız")
        print(self.id_index_text_makina_ekleme)

    def makinaEkleme_islem1(self):
        id_index = self.ui_mak.comboBox_musteriler.currentIndex()      
        musteri_id = self.db.musteriGenel()[id_index].id
        gun = self.ui_mak.ln_gun.text() or 1
        ay = self.ui_mak.ln_ay.text() or 1
        yil = self.ui_mak.ln_yil.text() or 2000
        makina_uretim_tarihi = datetime.date(int(yil), int(ay), int(gun))
        makina_ad = self.ui_mak.ln_makinaAd.text()
        makina_seri_num = self.ui_mak.ln_makinaSeriNum.text()
        self.app.addMakina(musteri_id, makina_ad, makina_seri_num, makina_uretim_tarihi)
        self.ui_mak.lbl_makinaEklemeTalimatlar.setText(f"{self.db.musteriGenel()[id_index].musteri_ad} müşterisine {makina_seri_num} seri numaralı makina eklenmiştir.")
        self.id_index_text_makina_ekleme = ""
        self.ui_mak.ln_makinaAd.clear()
        self.ui_mak.ln_makinaSeriNum.clear()
        self.ui_mak.ln_gun.clear()
        self.ui_mak.ln_ay.clear()
        self.ui_mak.ln_yil.clear()





    def analizEkle(self):
        self.widgetAnalizEkleme = QtWidgets.QWidget()
        self.widgetAnalizEkleme.setParent(None)
        self.ui_analiz = Ui_AnalizEkleme()
        self.ui_analiz.setupUi(self.widgetAnalizEkleme)
        self.widgetAnalizEkleme.setWindowTitle("Analiz Ekleme")
        self.widgetAnalizEkleme.setWindowIcon(QIcon("polatIcon.jpg"))
        self.widgetAnalizEkleme.show()
        self.ui.btnMusteriEkle.clicked.connect(lambda:self.widgetAnalizEkleme.close())
        self.ui.btnMakinaEkle.clicked.connect(lambda:self.widgetAnalizEkleme.close())
        self.ui_analiz.ln_degerGiris.setPlaceholderText("Gün")
        self.ui_analiz.ln_degerGiris_2.setPlaceholderText("Ay")
        self.ui_analiz.ln_degerGiris_3.setPlaceholderText("Yıl")
        self.ui_analiz.ln_degerGiris_4.setPlaceholderText("Foss Giriş Nem")
        self.ui_analiz.ln_degerGiris_5.setPlaceholderText("Foss Giriş Yaş Yağ")
        self.ui_analiz.ln_degerGiris_6.setPlaceholderText("Foss Giriş Kuru Yağ")
        self.ui_analiz.ln_degerGiris_7.setPlaceholderText("Foss Çıkış Nem")
        self.ui_analiz.ln_degerGiris_8.setPlaceholderText("Foss Çıkış Yaş Yağ")
        self.ui_analiz.ln_degerGiris_9.setPlaceholderText("Foss Çıkış Kuru Yağ")
        self.ui_analiz.ln_degerGiris_10.setPlaceholderText("Soxhlet Giriş Nem")
        self.ui_analiz.ln_degerGiris_11.setPlaceholderText("Soxhlet Giriş Yaş Yağ")
        self.ui_analiz.ln_degerGiris_12.setPlaceholderText("Soxhlet Giriş Kuru Yağ")
        self.ui_analiz.ln_degerGiris_13.setPlaceholderText("Soxhlet Çıkış Nem")
        self.ui_analiz.ln_degerGiris_14.setPlaceholderText("Soxhlet Çıkış Yaş Yağ")
        self.ui_analiz.ln_degerGiris_15.setPlaceholderText("Soxhlet Çıkış Kuru Yağ")
        self.ui_analiz.ln_degerGiris_16.setPlaceholderText("Karasu Nem")
        self.ui_analiz.ln_degerGiris_17.setPlaceholderText("Karasu Yağ")
        self.ui_analiz.ln_degerGiris_18.setPlaceholderText("Malaksör Sıcaklığı")
        self.ui_analiz.ln_degerGiris_19.setPlaceholderText("İlave su (lt)")
        self.ui_analiz.ln_degerGiris_20.setPlaceholderText("Hamur pompa kapasitesi")
        self.ui_analiz.ln_degerGiris_21.setPlaceholderText("Hamur pompa devri")
        self.ui_analiz.ln_degerGiris_22.setPlaceholderText("İleti (d/d)")
        self.ui_analiz.ln_degerGiris_23.setPlaceholderText("Helezon devri (d/d)")
        self.ui_analiz.ln_degerGiris_24.setPlaceholderText("Gövde devri (d/d)")
        self.ui_analiz.ln_degerGiris_25.setPlaceholderText("Tork (kNm)")
        self.ui_analiz.ln_degerGiris_26.setPlaceholderText("Helezon motor amperi")
        self.ui_analiz.ln_degerGiris_27.setPlaceholderText("Gövde motor amperi")
        self.ui_analiz.ln_degerGiris_28.setPlaceholderText("Boru uzunluğu")
        self.ui_analiz.ln_degerGiris_29.setPlaceholderText("Faz")
        self.ui_analiz.ln_degerGiris_30.setPlaceholderText("Su yolları (mm)")
        self.ui_analiz.ln_degerGiris_31.setPlaceholderText("Beck (mm)")
        self.ui_analiz.ln_degerGiris_32.setPlaceholderText("Zeytin Tipi")


        self.ui_analiz.lbl_talimat.setText("-- Öncelikle listeden analizi eklenecek müşteriyi seçiniz --")
        self.ui_analiz.lbl_talimat.setStyleSheet("color: red")

        self.ui_analiz.btnEkle.setStyleSheet("background-color: lightblue")
        self.ui_analiz.btnKaydet.setStyleSheet("background-color: lightgreen")
        self.ui_analiz.btnIptal.setStyleSheet("background-color: yellow")
        alert = ""
        self.labelAlert(alert)

        self.analizler = []
        
        musteri_listesi = self.app.musteriListesi()
        self.ui_analiz.cmbBoxMusteri.addItems(musteri_listesi)
        self.ui_analiz.btnSecimMusteri.clicked.connect(self.AnalizIcinMakinaSirala)   

        
        self.ui_analiz.btnEkle.clicked.connect(self.analizVeriUpdate)
        self.ui_analiz.btnIptal.clicked.connect(self.analizEmpty)
        self.ui_analiz.btnKaydet.clicked.connect(self.analizKayit)
    
    def analizEmpty(self):
        self.analizler = []
        self.ui_analiz.lbl_talimat.setText("Eklenen analizler kayıt edilmeden silinmiştir!")


    def AnalizIcinMakinaSirala(self):
        id_index = int(self.ui_analiz.cmbBoxMusteri.currentIndex())
        id = self.db.musteriGenel()[id_index].id
        ad = self.db.musteriGenel()[id_index].musteri_ad
        self.musteriOngoing["id"] = id
        self.musteriOngoing["musteri_ad"] = ad
        self.ui_analiz.cmbBoxMusteri.clear()
        self.ui_analiz.cmbBoxMakina.clear()
        

        self.ui_analiz.lbl_talimat.setText(f"Şimdi, {ad} müşterisine ait makinayı listeden seçiniz.")
        makineler = self.app.musteriMakinaListesi(id)
        self.ui_analiz.cmbBoxMakina.addItems(makineler) 
        self.ui_analiz.btnSecimMakina.clicked.connect(self.analizMusterMakina)


    def analizMusterMakina(self):
       
        makina_id_index = int(self.ui_analiz.cmbBoxMakina.currentIndex())
        musteri_makina_liste = []
        for z in self.db.musteriMakina(self.musteriOngoing["id"]):
            musteri_makina_liste.append(z.makina_id)
        makina_id = int(musteri_makina_liste[makina_id_index])

        seri_num_raw = self.db.makinaListById(makina_id)
        makina_seriNumara = seri_num_raw[0].makina_seri_num        

        self.musteriOngoing["makina_id"] = makina_id
        self.ui_analiz.lbl_talimat.setText(f"Seçili müşterinin {makina_seriNumara} seri numaralı makinasına kayıt edilecek analiz değerlerini giriniz.")



    def analizVeriUpdate(self):
        
        gun = self.ui_analiz.ln_degerGiris.text() or 1
        ay = self.ui_analiz.ln_degerGiris_2.text() or 1
        yil = self.ui_analiz.ln_degerGiris_3.text() or 2022

        FossGiris_nem = self.ui_analiz.ln_degerGiris_4.text() or None
        FossGiris_YasPrina = self.ui_analiz.ln_degerGiris_5.text() or None
        FossGiris_KuruPrina = self.ui_analiz.ln_degerGiris_6.text() or None
        FossCikis_nem = self.ui_analiz.ln_degerGiris_7.text() or None
        FossCikis_YasPrina = self.ui_analiz.ln_degerGiris_8.text() or None
        FossCikis_KuruPrina = self.ui_analiz.ln_degerGiris_9.text() or None
        SoxhletGiris_nem = self.ui_analiz.ln_degerGiris_10.text() or None
        SoxhletGiris_YasPrina = self.ui_analiz.ln_degerGiris_11.text() or None
        SoxhletGiris_KuruPrina = self.ui_analiz.ln_degerGiris_12.text() or None
        SoxhletCikis_nem = self.ui_analiz.ln_degerGiris_13.text() or None
        SoxhletCikis_YasPrina = self.ui_analiz.ln_degerGiris_14.text() or None
        SoxhletCikis_KuruPrina = self.ui_analiz.ln_degerGiris_15.text() or None
        Karasu_nem = self.ui_analiz.ln_degerGiris_16.text() or None
        Karasu_yag = self.ui_analiz.ln_degerGiris_17.text() or None
        Malaksor_sicaklik = self.ui_analiz.ln_degerGiris_18.text() or None
        Ilave_su_lt_dk = self.ui_analiz.ln_degerGiris_19.text() or None
        Hamur_pompa_kapasite_Hrz = self.ui_analiz.ln_degerGiris_20.text() or None
        Hamur_pompa_devri = self.ui_analiz.ln_degerGiris_21.text() or None
        Ileti_d_d = self.ui_analiz.ln_degerGiris_22.text() or None
        Helezon_devri_d_d = self.ui_analiz.ln_degerGiris_23.text() or None
        Govde_devri_d_d = self.ui_analiz.ln_degerGiris_24.text() or None
        Tork_kNm = self.ui_analiz.ln_degerGiris_25.text() or None
        Dekantor_helezon_motor_amperi = self.ui_analiz.ln_degerGiris_26.text() or None
        Dekantor_govde_motor_amperi = self.ui_analiz.ln_degerGiris_27.text() or None
        boru_uzunlugu = self.ui_analiz.ln_degerGiris_28.text() or None
        faz = self.ui_analiz.ln_degerGiris_29.text() or None
        su_yollari_mm = self.ui_analiz.ln_degerGiris_30.text() or None
        beck_mm = self.ui_analiz.ln_degerGiris_31.text() or None
        Zeytin_tipi = self.ui_analiz.ln_degerGiris_32.text() or None
        makina_id = int(self.musteriOngoing["makina_id"])
        musteri_id = int(self.musteriOngoing["id"])

        Tarih = datetime.date(int(yil), int(ay), int(gun))
        
        analiz = Analiz(None, makina_id, musteri_id, FossGiris_nem, FossGiris_YasPrina, FossGiris_KuruPrina, FossCikis_nem, FossCikis_YasPrina, FossCikis_KuruPrina, SoxhletGiris_nem, SoxhletGiris_YasPrina, SoxhletGiris_KuruPrina, SoxhletCikis_nem, SoxhletCikis_YasPrina, SoxhletCikis_KuruPrina, Karasu_nem, Karasu_yag, Tarih, Zeytin_tipi, Malaksor_sicaklik, Ilave_su_lt_dk, Hamur_pompa_kapasite_Hrz, Hamur_pompa_devri, Ileti_d_d, Helezon_devri_d_d, Govde_devri_d_d, Tork_kNm, Dekantor_helezon_motor_amperi, Dekantor_govde_motor_amperi, boru_uzunlugu, faz, su_yollari_mm, beck_mm)
        self.analizler.append(analiz)
        self.ui_analiz.lbl_talimat.setText(f"{len(self.analizler)} adet kayıt alınmıştır alınmıştır. Devam edebilir ya da girilen analizleri kaydedebilirsiniz.")

        self.ui_analiz.ln_degerGiris.clear()
        self.ui_analiz.ln_degerGiris_2.clear()
        self.ui_analiz.ln_degerGiris_3.clear()
        self.ui_analiz.ln_degerGiris_4.clear()
        self.ui_analiz.ln_degerGiris_5.clear()
        self.ui_analiz.ln_degerGiris_6.clear()
        self.ui_analiz.ln_degerGiris_7.clear()
        self.ui_analiz.ln_degerGiris_8.clear()
        self.ui_analiz.ln_degerGiris_9.clear()
        self.ui_analiz.ln_degerGiris_10.clear()
        self.ui_analiz.ln_degerGiris_11.clear()
        self.ui_analiz.ln_degerGiris_12.clear()
        self.ui_analiz.ln_degerGiris_13.clear()
        self.ui_analiz.ln_degerGiris_14.clear()
        self.ui_analiz.ln_degerGiris_15.clear()
        self.ui_analiz.ln_degerGiris_16.clear()
        self.ui_analiz.ln_degerGiris_17.clear()
        self.ui_analiz.ln_degerGiris_18.clear()
        self.ui_analiz.ln_degerGiris_19.clear()
        self.ui_analiz.ln_degerGiris_20.clear()
        self.ui_analiz.ln_degerGiris_21.clear()
        self.ui_analiz.ln_degerGiris_22.clear()
        self.ui_analiz.ln_degerGiris_23.clear()
        self.ui_analiz.ln_degerGiris_24.clear()
        self.ui_analiz.ln_degerGiris_25.clear()
        self.ui_analiz.ln_degerGiris_26.clear()
        self.ui_analiz.ln_degerGiris_27.clear()
        self.ui_analiz.ln_degerGiris_28.clear()
        self.ui_analiz.ln_degerGiris_29.clear()
        self.ui_analiz.ln_degerGiris_30.clear()
        self.ui_analiz.ln_degerGiris_31.clear()
        self.ui_analiz.ln_degerGiris_32.clear()

    def analizKayit(self):
        self.db.addAnalizMany(self.analizler)
        musterinin_adi = self.musteriOngoing["musteri_ad"]
        self.ui_analiz.lbl_talimat.setText(f"{musterinin_adi} müşterisine {len(self.analizler)} adet analiz eklenmiştir.")
        self.analizler = []




    def guncelleme(self):
        self.widgetGuncelleme = QtWidgets.QWidget()
        self.widgetGuncelleme.setParent(None)
        self.ui_guncel = Ui_Guncelleme()
        self.ui_guncel.setupUi(self.widgetGuncelleme)
        self.widgetGuncelleme.setWindowTitle("Güncelleme")
        self.widgetGuncelleme.setWindowIcon(QIcon("polatIcon.jpg"))
        self.ui.btnMusteriEkle.clicked.connect(lambda:self.widgetGuncelleme.close())
        self.ui.btnMakinaEkle.clicked.connect(lambda:self.widgetGuncelleme.close())
        self.ui.btnAnalizEkle.clicked.connect(lambda:self.widgetGuncelleme.close())
        self.ui_guncel.btnKaydet.setStyleSheet("background-color: lightgreen")
        seciliGuncelleme = ""
        items = self.ui.groupBoxGuncelleme.findChildren(QtWidgets.QRadioButton)
        for i in items:
            if i.isChecked():
                seciliGuncelleme = i.text()
                self.widgetGuncelleme.show()
            else:
                pass
        self.ui_guncel.lblTakip.setText(seciliGuncelleme)
        
        if seciliGuncelleme == "Müşteri Güncelle":
            self.musteriGuncelle()

        if seciliGuncelleme == "Makina Güncelle":
            self.makinaGuncelle()

        if seciliGuncelleme == "Analiz Güncelle":
            self.analizGuncelle()





    def musteriGuncelle(self):
        self.ui_guncel.lnVeriGiris.setPlaceholderText("Yeni değeri buraya giriniz.")
        self.ui_guncel.lblTalimat.setText("Öncelikle güncellemek istediğiniz müşteriyi seçiniz.")
        self.ui_guncel.lblTalimat.setStyleSheet("color: red")
        self.ui_guncel.cmbxListe.addItems(self.app.musteriListesi())
        
        self.ui_guncel.btnSecim.clicked.connect(self.musteriGuncellemeSecim)

    def musteriGuncellemeSecim(self):
        id_index = int(self.ui_guncel.cmbxListe.currentIndex())
        id = self.db.musteriGenel()[id_index].id
        ad = self.db.musteriGenel()[id_index].musteri_ad
        self.musteriOngoing["id"] = id
        self.musteriOngoing["musteri_ad"] = ad

        self.ui_guncel.lblTalimat.setText(f"{ad} müşterisinin güncellenecek bilgilerini listeden seçiniz")
        self.ui_guncel.cmbxVeriler.addItems(self.musteriBilgiler)

        self.ui_guncel.btnKaydet.clicked.connect(self.musteriGuncellemeKayit)
    
    def musteriGuncellemeKayit(self):
        id = int(self.musteriOngoing["id"])
        musteri = self.db.getMusteriById(id)
        ad = self.musteriOngoing["musteri_ad"]
        etiket = ""
        deger_ilk = self.ui_guncel.cmbxVeriler.currentText()
        if deger_ilk == "Müşteri Ad":
            musteri[0].musteri_ad = self.ui_guncel.lnVeriGiris.text()
            etiket = "Müşteri Ad"
        else:
            musteri[0].musteri_ad = musteri[0].musteri_ad

        if deger_ilk == "Müşteri Bölge":
            musteri[0].musteri_bolge = self.ui_guncel.lnVeriGiris.text()
            etiket = "Müşteri Bölge"
        else:
            musteri[0].musteri_bolge = musteri[0].musteri_bolge
        
        self.db.upDateMusteri(musteri[0])
        self.ui_guncel.lblTalimat.setText(f"{ad} müşterisinin '{etiket}' bilgisi güncellenmiştir.")  
     
        

    def makinaGuncelle(self):
        self.ui_guncel.lnVeriGiris.setPlaceholderText("Yeni değeri buraya giriniz.")
        self.ui_guncel.lblTalimat.setText("Öncelikle makinasını güncellemek istediğiniz müşteriyi seçiniz.")
        self.ui_guncel.lblTalimat.setStyleSheet("color: red")
        self.ui_guncel.cmbxListe.addItems(self.app.musteriListesi())
        
        self.ui_guncel.btnSecim.clicked.connect(self.makinaGuncellemeMakinaListe)

    def makinaGuncellemeMakinaListe(self):
        id_index = int(self.ui_guncel.cmbxListe.currentIndex())
        id = self.db.musteriGenel()[id_index].id
        ad = self.db.musteriGenel()[id_index].musteri_ad
        self.musteriOngoing["id"] = id
        self.musteriOngoing["musteri_ad"] = ad
        self.ui_guncel.cmbxListe.clear()
        makineler = self.app.musteriMakinaListesi(id)
        self.ui_guncel.cmbxListe_2.addItems(makineler)
        self.ui_guncel.lblTalimat.setText(f"Şimdi {ad} müşterisinin güncellenecek makinasını seçiniz.")

        self.ui_guncel.btnSecim_2.clicked.connect(self.makinaGuncellemeVeriGirme)

    def makinaGuncellemeVeriGirme(self):
        self.ui_guncel.lblTalimat.setText(f"Şimdi güncellenecek bilgiyi listeden seçiniz.")
        self.ui_guncel.cmbxVeriler.addItems(self.makinaBilgiler)
        self.ui_guncel.btnKaydet.clicked.connect(self.makinaGuncellemeKayit)

    
    def makinaGuncellemeKayit(self):

        makina_id_index = int(self.ui_guncel.cmbxListe_2.currentIndex())
        musteri_id = int(self.musteriOngoing["id"])
        musteri_ad = self.musteriOngoing["musteri_ad"]
        musteri_makina_liste = []
        for z in self.db.musteriMakina(musteri_id):
            musteri_makina_liste.append(z.makina_id)
        makina_id = musteri_makina_liste[makina_id_index]

        etiket = ""
        makinalar = self.db.makinaListById(makina_id)
        deger_ilk = self.ui_guncel.cmbxVeriler.currentText()
        if deger_ilk == "Makina Adı":
            makinalar[0].makina_ad = self.ui_guncel.lnVeriGiris.text()
            etiket = "Makina Adı"
        else:
            makinalar[0].makina_ad = makinalar[0].makina_ad
        
        if deger_ilk == "Makina Üretim Tarihi":
            makinalar[0].makina_uretim_tarihi = self.ui_guncel.lnVeriGiris.text()
            etiket = "Makina Üretim Tarihi"
        else:
            makinalar[0].makina_uretim_tarihi = makinalar[0].makina_uretim_tarihi

        if deger_ilk == "Makina Seri Numarası":
            makinalar[0].makina_seri_num = self.ui_guncel.lnVeriGiris.text()
            etiket = "Makina Seri Numarası"
        else:
            makinalar[0].makina_seri_num = makinalar[0].makina_seri_num
        makinalar[0].id = makina_id

        self.db.upDateMakina(makinalar[0])        
        self.ui_guncel.lblTalimat.setText(f"{musteri_ad} müşterisinin seçili makinasının '{etiket}' bilgisi güncellenmiştir.")  

    


    def analizGuncelle(self):
        self.ui_guncel.lnVeriGiris.setPlaceholderText("Yeni değeri buraya giriniz.")
        self.ui_guncel.lblTalimat.setText("Öncelikle analizini güncellemek istediğiniz müşteriyi seçiniz.")
        self.ui_guncel.lblTalimat.setStyleSheet("color: red")
        self.ui_guncel.cmbxListe.addItems(self.app.musteriListesi())

        self.ui_guncel.btnSecim.clicked.connect(self.analizGuncellemeAnalizListe)
    
    def analizGuncellemeAnalizListe(self):
        id_index = int(self.ui_guncel.cmbxListe.currentIndex())
        id = self.db.musteriGenel()[id_index].id
        ad = self.db.musteriGenel()[id_index].musteri_ad
        self.musteriOngoing["id"] = id
        self.musteriOngoing["musteri_ad"] = ad
        self.ui_guncel.cmbxListe.clear()
        analizler = self.app.analizByMusteriId(id)
        self.ui_guncel.cmbxListe_2.addItems(analizler)
        self.ui_guncel.lblTalimat.setText(f"Şimdi {ad} müşterisinin güncellenecek analizini seçiniz.")

        self.ui_guncel.btnSecim_2.clicked.connect(self.analizGuncellemeVeriGirme)

    def analizGuncellemeVeriGirme(self):
        self.ui_guncel.lblTalimat.setText(f"Şimdi güncellenecek bilgiyi listeden seçiniz.")
        self.ui_guncel.cmbxVeriler.addItems(self.analizBilgiler)
        self.ui_guncel.btnKaydet.clicked.connect(self.analizGuncellemeKayit)

    def analizGuncellemeKayit(self):
        analiz_id_index = int(self.ui_guncel.cmbxListe_2.currentIndex())
        musteri_id = int(self.musteriOngoing["id"])
        musteri_ad = self.musteriOngoing["musteri_ad"]

        analiz_id_liste = []
        musteri_analizleri = self.db.analizByMusteriId(musteri_id)
        for i in musteri_analizleri:
            analiz_id_liste.append(i.id)
        analizId = analiz_id_liste[analiz_id_index]
        
        
        etiket = ""
        deger_ilk = self.ui_guncel.cmbxVeriler.currentText()
        if deger_ilk == "Makina id":
            musteri_analizleri[analiz_id_index].makina_id = self.ui_guncel.lnVeriGiris.text()
            etiket = "Makiba id"
        else:
            musteri_analizleri[analiz_id_index].makina_id = musteri_analizleri[analiz_id_index].makina_id
        if deger_ilk == "Foss Giriş Nem":
            musteri_analizleri[analiz_id_index].FossGiris_nem = self.ui_guncel.lnVeriGiris.text()
            etiket = "Foss Giriş Nem"
        else:
            musteri_analizleri[analiz_id_index].FossGiris_nem = musteri_analizleri[analiz_id_index].FossGiris_nem
        if deger_ilk == "Foss Giriş Yaş Prina Yağ":
            musteri_analizleri[analiz_id_index].FossGiris_YasPrina = self.ui_guncel.lnVeriGiris.text()
            etiket = "Foss Giriş Yaş Prina Yağ"
        else:
            musteri_analizleri[analiz_id_index].FossGiris_YasPrina = musteri_analizleri[analiz_id_index].FossGiris_YasPrina
        if deger_ilk == "Foss Giriş Kuru Prina Yağ":
            musteri_analizleri[analiz_id_index].FossGiris_KuruPrina = self.ui_guncel.lnVeriGiris.text()
            etiket = "Foss Giriş Kuru Prina Yağ"
        else:
            musteri_analizleri[analiz_id_index].FossGiris_KuruPrina = musteri_analizleri[analiz_id_index].FossGiris_KuruPrina
        if deger_ilk == "Foss Çıkış Nem":
            musteri_analizleri[analiz_id_index].FossCikis_nem = self.ui_guncel.lnVeriGiris.text()
            etiket = "Foss Çıkış Nem"
        else:
            musteri_analizleri[analiz_id_index].FossCikis_nem = musteri_analizleri[analiz_id_index].FossCikis_nem
        if deger_ilk == "Foss Çıkış Yaş Prina Yağ":
            musteri_analizleri[analiz_id_index].FossCikis_YasPrina = self.ui_guncel.lnVeriGiris.text()
            etiket = "Foss Çıkış Yaş Prina Yağ"
        else:
            musteri_analizleri[analiz_id_index].FossCikis_YasPrina = musteri_analizleri[analiz_id_index].FossCikis_YasPrina
        if deger_ilk == "Foss Çıkış Kuru Prina Yağ":
            musteri_analizleri[analiz_id_index].FossCikis_KuruPrina = self.ui_guncel.lnVeriGiris.text()
            etiket = "Foss Çıkış Kuru Prina Yağ"
        else:
            musteri_analizleri[analiz_id_index].FossCikis_KuruPrina = musteri_analizleri[analiz_id_index].FossCikis_KuruPrina
        if deger_ilk == "Soxhlet Giriş Nem":
            musteri_analizleri[analiz_id_index].SoxhletGiris_nem = self.ui_guncel.lnVeriGiris.text()
            etiket = "Soxhlet Giriş Nem"
        else:
            musteri_analizleri[analiz_id_index].SoxhletGiris_nem = musteri_analizleri[analiz_id_index].SoxhletGiris_nem
        if deger_ilk == "Soxhlet Giriş Yaş Prina Yağ":
            musteri_analizleri[analiz_id_index].SoxhletGiris_YasPrina = self.ui_guncel.lnVeriGiris.text()
            etiket = "Soxhlet Giriş Yaş Prina Yağ"
        else:
            musteri_analizleri[analiz_id_index].SoxhletGiris_YasPrina = musteri_analizleri[analiz_id_index].SoxhletGiris_YasPrina
        if deger_ilk == "Soxhlet Giriş Kuru Prina Yağ":
            musteri_analizleri[analiz_id_index].SoxhletGiris_KuruPrina = self.ui_guncel.lnVeriGiris.text()
            etiket = "Soxhlet Giriş Kuru Prina Yağ"
        else:
            musteri_analizleri[analiz_id_index].SoxhletGiris_KuruPrina = musteri_analizleri[analiz_id_index].SoxhletGiris_KuruPrina
        if deger_ilk == "Soxhlet Çıkış Nem":
            musteri_analizleri[analiz_id_index].SoxhletCikis_nem = self.ui_guncel.lnVeriGiris.text()
            etiket = "Soxhlet Çıkış Nem"
        else:
            musteri_analizleri[analiz_id_index].SoxhletCikis_nem = musteri_analizleri[analiz_id_index].SoxhletCikis_nem
        if deger_ilk == "Soxhlet Çıkış Yaş Prina Yağ":
            musteri_analizleri[analiz_id_index].SoxhletCikis_YasPrina = self.ui_guncel.lnVeriGiris.text()
            etiket = "Soxhlet Çıkış Yaş Prina Yağ"
        else:
            musteri_analizleri[analiz_id_index].SoxhletCikis_YasPrina = musteri_analizleri[analiz_id_index].SoxhletCikis_YasPrina
        if deger_ilk == "Soxhlet Çıkış Kuru Prina Yağ":
            musteri_analizleri[analiz_id_index].SoxhletCikis_KuruPrina = self.ui_guncel.lnVeriGiris.text()
            etiket = "Soxhlet Çıkış Kuru Prina Yağ"
        else:
            musteri_analizleri[analiz_id_index].SoxhletCikis_KuruPrina = musteri_analizleri[analiz_id_index].SoxhletCikis_KuruPrina
        if deger_ilk == "Karasu Nem":
            musteri_analizleri[analiz_id_index].Karasu_nem = self.ui_guncel.lnVeriGiris.text()
            etiket = "Karasu Nem"
        else:
            musteri_analizleri[analiz_id_index].Karasu_nem = musteri_analizleri[analiz_id_index].Karasu_nem
        if deger_ilk == "Karasu Yağ":
            musteri_analizleri[analiz_id_index].Karasu_yag = self.ui_guncel.lnVeriGiris.text()
            etiket = "Karasu Yağ"
        else:
            musteri_analizleri[analiz_id_index].Karasu_yag = musteri_analizleri[analiz_id_index].Karasu_yag
        if deger_ilk == "Tarih: Yıl-Ay-Gün (2022-01-31)":
            musteri_analizleri[analiz_id_index].Tarih = self.ui_guncel.lnVeriGiris.text()
            etiket = "Tarih"
        else:
            musteri_analizleri[analiz_id_index].Tarih = musteri_analizleri[analiz_id_index].Tarih
        if deger_ilk == "Zeytin Tipi":
            musteri_analizleri[analiz_id_index].Zeytin_tipi = self.ui_guncel.lnVeriGiris.text()
            etiket = "Zeytin Tipi"
        else:
            musteri_analizleri[analiz_id_index].Zeytin_tipi = musteri_analizleri[analiz_id_index].Zeytin_tipi
        if deger_ilk == "Malaksör Sıcaklığı":
            musteri_analizleri[analiz_id_index].Malaksor_sicaklik = self.ui_guncel.lnVeriGiris.text()
            etiket = "Malaksör Sıcaklığı"
        else:
            musteri_analizleri[analiz_id_index].Malaksor_sicaklik = musteri_analizleri[analiz_id_index].Malaksor_sicaklik
        if deger_ilk == "Dakikada ilave edilen su miktarı (lt)":
            musteri_analizleri[analiz_id_index].Ilave_su_lt_dk = self.ui_guncel.lnVeriGiris.text()
            etiket = "Dakikada ilave edilen su"
        else:
            musteri_analizleri[analiz_id_index].Ilave_su_lt_dk = musteri_analizleri[analiz_id_index].Ilave_su_lt_dk
        if deger_ilk == "Hamur pompa kapasitesi (Hrz)":
            musteri_analizleri[analiz_id_index].Hamur_pompa_kapasite_Hrz = self.ui_guncel.lnVeriGiris.text()
            etiket = "Hamur pompa kapasitesi"
        else:
            musteri_analizleri[analiz_id_index].Hamur_pompa_kapasite_Hrz = musteri_analizleri[analiz_id_index].Hamur_pompa_kapasite_Hrz
        if deger_ilk == "Hamur pompa devri":
            musteri_analizleri[analiz_id_index].Hamur_pompa_devri = self.ui_guncel.lnVeriGiris.text()
            etiket = "Hamur pompa devri"
        else:
            musteri_analizleri[analiz_id_index].Hamur_pompa_devri = musteri_analizleri[analiz_id_index].Hamur_pompa_devri
        if deger_ilk == "İleti (d/d)":
            musteri_analizleri[analiz_id_index].Ileti_d_d = self.ui_guncel.lnVeriGiris.text()
            etiket = "İleti"
        else:
            musteri_analizleri[analiz_id_index].Ileti_d_d = musteri_analizleri[analiz_id_index].Ileti_d_d
        if deger_ilk == "Helezon devri (d/d)":
            musteri_analizleri[analiz_id_index].Helezon_devri_d_d = self.ui_guncel.lnVeriGiris.text()
            etiket = "Helezon devri"
        else:
            musteri_analizleri[analiz_id_index].Helezon_devri_d_d = musteri_analizleri[analiz_id_index].Helezon_devri_d_d
        if deger_ilk == "Gövde devri (d/d)":
            musteri_analizleri[analiz_id_index].Govde_devri_d_d = self.ui_guncel.lnVeriGiris.text()
            etiket = "Gövde devri"
        else:
            musteri_analizleri[analiz_id_index].Govde_devri_d_d = musteri_analizleri[analiz_id_index].Govde_devri_d_d
        if deger_ilk == "Tork (kNm)":
            musteri_analizleri[analiz_id_index].Tork_kNm = self.ui_guncel.lnVeriGiris.text()
            etiket = "Tork"
        else:
            musteri_analizleri[analiz_id_index].Tork_kNm = musteri_analizleri[analiz_id_index].Tork_kNm
        if deger_ilk == "Dekantör helezon motor amperi":
            musteri_analizleri[analiz_id_index].Dekantor_helezon_motor_amperi = self.ui_guncel.lnVeriGiris.text()
            etiket = "Dekantör helezon motor amperi"
        else:
            musteri_analizleri[analiz_id_index].Dekantor_helezon_motor_amperi = musteri_analizleri[analiz_id_index].Dekantor_helezon_motor_amperi
        if deger_ilk == "Dekantör gövde motor amperi":
            musteri_analizleri[analiz_id_index].Dekantor_govde_motor_amperi = self.ui_guncel.lnVeriGiris.text()
            etiket = "Dekantör gövde motor amperi"
        else:
            musteri_analizleri[analiz_id_index].Dekantor_govde_motor_amperi = musteri_analizleri[analiz_id_index].Dekantor_govde_motor_amperi
        if deger_ilk == "Boru uzunluğu":
            musteri_analizleri[analiz_id_index].boru_uzunlugu = self.ui_guncel.lnVeriGiris.text()
            etiket = "Boru uzunluğu"
        else:
            musteri_analizleri[analiz_id_index].boru_uzunlugu = musteri_analizleri[analiz_id_index].boru_uzunlugu
        if deger_ilk == "Faz":
            musteri_analizleri[analiz_id_index].faz = self.ui_guncel.lnVeriGiris.text()
            etiket = "Faz"
        else:
            musteri_analizleri[analiz_id_index].faz = musteri_analizleri[analiz_id_index].faz
        if deger_ilk == "Su yolları (mm)":
            musteri_analizleri[analiz_id_index].su_yollari_mm = self.ui_guncel.lnVeriGiris.text()
            etiket = "Su yolları"
        else:
            musteri_analizleri[analiz_id_index].su_yollari_mm = musteri_analizleri[analiz_id_index].su_yollari_mm
        if deger_ilk == "Beck (mm)":
            musteri_analizleri[analiz_id_index].beck_mm = self.ui_guncel.lnVeriGiris.text()
            etiket = "Beck"
        else:
            musteri_analizleri[analiz_id_index].beck_mm = musteri_analizleri[analiz_id_index].beck_mm
        musteri_analizleri[analiz_id_index].id = analizId
        
        self.db.upDateAnaliz(musteri_analizleri[analiz_id_index])
        self.ui_guncel.lblTalimat.setText(f"{musteri_ad} müşterisinin seçili analizinin '{etiket}' bilgisi güncellenmiştir.")
        

    

    def silmek(self):
        self.widgetSilmek = QtWidgets.QWidget()
        self.widgetSilmek.setParent(None)
        self.ui_silmek = Ui_Silmek()
        self.ui_silmek.setupUi(self.widgetSilmek)
        self.widgetSilmek.setWindowTitle("Silmek")
        self.widgetSilmek.setWindowIcon(QIcon("polatIcon.jpg"))
        self.ui_silmek.btnSil.setStyleSheet("background-color: lightblue")
        

        seciliSilme = ""
        items = self.ui.groupBoxSilme.findChildren(QtWidgets.QRadioButton)
        for i in items:
            if i.isChecked():
                seciliSilme = i.text()
                self.widgetSilmek.show()
            else:
                pass
        self.ui_silmek.lblSilmek.setText(seciliSilme)
        
        if seciliSilme == "Müşteri Sil":
            self.musteriSil()

        if seciliSilme == "Makina Sil":
            self.makinaSil()

        if seciliSilme == "Analiz Sil":
            self.analizSil()

    def musteriSil(self):
        self.ui_silmek.cmbSilmek1.addItems(self.app.musteriListesi())
        self.ui_silmek.lblSilmek.setText("Müşteri")
        self.ui_silmek.lblTalimat.setText("Silinecek müşteriyi listeden seçiniz.")
        self.ui_silmek.lblTalimat.setStyleSheet("color: red")
        self.ui_silmek.btnSecimSil.clicked.connect(self.musterininSilinmesiAra)
    
    def musterininSilinmesiAra(self):
        id_index = int(self.ui_silmek.cmbSilmek1.currentIndex())
        id = self.db.musteriGenel()[id_index].id
        ad = self.db.musteriGenel()[id_index].musteri_ad
        self.musteriOngoing["id"] = id
        self.musteriOngoing["musteri_ad"] = ad
        self.ui_silmek.cmbSilmek1.clear()
        self.ui_silmek.lblTalimat.setText(f"Silmek için {ad} müşterisini seçtiniz. Tamamlamak için 'Sil' tuşuna basınız.")
        self.ui_silmek.btnSil.clicked.connect(self.musterininSilinmesiSon)
        
        self.musteriMakinaId = []
        makina_id_liste = self.app.musteriMakinaIdListesi(id)
        for i in makina_id_liste:
            self.musteriMakinaId.append(int(i))
    
    def musterininSilinmesiSon(self):
        musteri_id = int(self.musteriOngoing["id"])
        musteri_ad = self.musteriOngoing["musteri_ad"]        
        self.db.deleteMusteriAnaliz(musteri_id)
        self.db.deleteAnalizByMusteriId(musteri_id)        
        self.db.deleteMusteriMakina(musteri_id)
        
        for i in self.musteriMakinaId:
            self.db.deleteMakina(i)
        self.db.deleteMusteri(musteri_id)
        self.ui_silmek.lblTalimat.setText(f"{musteri_ad} müşterisi silinmiştir.")
    

    def makinaSil(self):
        self.ui_silmek.cmbSilmek1.addItems(self.app.musteriListesi())
        self.ui_silmek.lblSilmek.setText("Müşteri")
        self.ui_silmek.lblTalimat.setText("Öncelikle müşteriyi listeden seçiniz.")
        self.ui_silmek.lblTalimat.setStyleSheet("color: red")

        self.ui_silmek.btnSecimSil.clicked.connect(self.makinaninSilinmesiAra)
    
    def makinaninSilinmesiAra(self):
        id_index = int(self.ui_silmek.cmbSilmek1.currentIndex())
        id = self.db.musteriGenel()[id_index].id
        ad = self.db.musteriGenel()[id_index].musteri_ad
        self.musteriOngoing["id"] = id
        self.musteriOngoing["musteri_ad"] = ad
        self.ui_silmek.cmbSilmek1.clear()
        makineler = self.app.musteriMakinaListesi(id)
        self.ui_silmek.cmbSilmek2.addItems(makineler)
        self.musteriMakinaId = []
        makina_id_liste = self.app.musteriMakinaIdListesi(id)
        for i in makina_id_liste:
            self.musteriMakinaId.append(int(i))
        
        self.ui_silmek.btnSil.clicked.connect(self.makinaSilinmesiSon)
    
    def makinaSilinmesiSon(self):
        seciliMakina_index = int(self.ui_silmek.cmbSilmek2.currentIndex())
        if seciliMakina_index < 0:
            pass
        else:
            seciliMakina_id = self.musteriMakinaId[seciliMakina_index]
            self.db.deleteMakinaFrommusterimakina(seciliMakina_id)
            analiz_id_index = self.db.analizIdFromMakinaId(seciliMakina_id)
            analizID = []
            for i in analiz_id_index:
                analizID.append(i[0])
            for z in analizID:
                self.db.deleteMusteriAnalizByAnalizId(z)
                self.db.deleteAnalizById(z)        
            self.db.deleteMakina(seciliMakina_id)
            musteri = self.musteriOngoing["musteri_ad"]
            self.ui_silmek.lblTalimat.setText(f"{musteri} müşterisinin makinası silinmiştir.")
            self.ui_silmek.cmbSilmek2.clear()
            id = int(self.musteriOngoing["id"])
            makineler = self.app.musteriMakinaListesi(id)
            self.ui_silmek.cmbSilmek2.addItems(makineler)
            self.musteriMakinaId = []
            makina_id_liste = self.app.musteriMakinaIdListesi(id)
            for i in makina_id_liste:
                self.musteriMakinaId.append(int(i))
        
        

    
    def analizSil(self):
        self.ui_silmek.cmbSilmek1.addItems(self.app.musteriListesi())
        self.ui_silmek.lblSilmek.setText("Müşteri")
        self.ui_silmek.lblTalimat.setText("Öncelikle müşteriyi listeden seçiniz.")
        self.ui_silmek.lblTalimat.setStyleSheet("color: red")

        self.ui_silmek.btnSecimSil.clicked.connect(self.analizinSilinmesiAra)

    def analizinSilinmesiAra(self):       
        id_index = int(self.ui_silmek.cmbSilmek1.currentIndex())
        id = self.db.musteriGenel()[id_index].id
        ad = self.db.musteriGenel()[id_index].musteri_ad
        self.musteriOngoing["id"] = id
        self.musteriOngoing["musteri_ad"] = ad
        analizler = self.app.analizByMusteriId(id)
        self.ui_silmek.cmbSilmek2.addItems(analizler)
        self.ui_silmek.lblTalimat.setText(f"{ad} müşterisinin silinecek analizini listeden seçiniz.")
        self.ui_silmek.btnSil.clicked.connect(self.analizSilinmesiSon)

    def analizSilinmesiSon(self):
        analiz_id_index = int(self.ui_silmek.cmbSilmek2.currentIndex())
        if analiz_id_index < 0:
            pass
        else:
            musteri_id = int(self.musteriOngoing["id"])
            analizIdListe = self.app.analizIdByMusteriId(musteri_id)
            analiz_id = int(analizIdListe[analiz_id_index])
            self.db.deleteMusteriAnalizByAnalizId(analiz_id)
            self.db.deleteAnalizById(analiz_id)
            ad = self.musteriOngoing["musteri_ad"]
            self.ui_silmek.lblTalimat.setText(f"{ad} müşterisinin {analiz_id} id numaralı analizi silinmiştir.")
            self.ui_silmek.cmbSilmek2.clear()
            id = int(self.musteriOngoing["id"])
            analizler = self.app.analizByMusteriId(id)
            self.ui_silmek.cmbSilmek2.addItems(analizler)


    def toExcel(self):
        musteri_id = self.excelMusteriId
        if self.excelKodu == "musteri":
            self.ex.musteriListesi()
            alert = "Masaüstüne müşteri listesi dosyası oluşturulmuştur."
            self.labelAlert(alert)
        elif self.excelKodu == "makina":
            self.ex.makinaListesi(musteri_id, self.excelMusteriAd)
            alert = f"Masaüstüne {self.excelMusteriAd} müşterisinin makina listesi dosyası oluşturulmuştur."
            self.labelAlert(alert)
        elif self.excelKodu == "analiz":
            self.ex.analizListesi(musteri_id, self.excelMusteriAd)
            alert = f"Masaüstüne {self.excelMusteriAd} müşterisinin analiz listesi dosyası oluşturulmuştur."
            self.labelAlert(alert)
        



app = QtWidgets.QApplication(sys.argv)
win = Window()
# win.setStyleSheet("background-color:#F9F8F2")
win.setWindowTitle("Deneme")
win.setWindowIcon(QIcon("polatIcon.jpg"))
win.show()
sys.exit(app.exec_())

