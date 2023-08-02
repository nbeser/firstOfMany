from dbmanager import DbManager
import datetime
from makina import Makina
from musteri import Musteri
from analiz import Analiz
from musterianaliz import MusteriAnaliz
from musterimakina import MusteriMakina

class App:
    def __init__(self):
        self.db = DbManager()
        

    def musteriListesi(self):  
        liste = []
        for i in self.db.musteriGenel():
            liste.append(f"{i.musteri_ad} - Bölge: {i.musteri_bolge}")
        return liste

    def musteriMakinaIdListesi(self, musteri_id):        
        if musteri_id in (i.id for i in self.db.musteriGenel()):
            musteri_makina_liste = []
            for z in self.db.musteriMakina(musteri_id):
                musteri_makina_liste.append(z.makina_id)
        return musteri_makina_liste

    
    def musteriMakinaListesi(self, musteri_id):        
        if musteri_id in (i.id for i in self.db.musteriGenel()):
            musteri_makina_liste = []
            for z in self.db.musteriMakina(musteri_id):
                musteri_makina_liste.append(z.makina_id)    # makina_id leri listeledim
            
            makinelerToplam = []
            for i in musteri_makina_liste:
                makinelerToplam.append(self.db.makinaListById(i))
            
            makineler = []
            a = 0
            for a in range(len(makinelerToplam)):
                for b in makinelerToplam[a]:
                    makineler.append(f"Makina {a+1}: {b.makina_ad}; Makina Seri Numarası: {b.makina_seri_num}; Makina id: {b.id}")
                a = a+1
        else:
            # print("Hatalı id numarası.")
            pass
        return makineler


    def analizByMusteriId(self, id):     

        if id in (i.id for i in self.db.musteriGenel()):
            analizListe = []
            for j in self.db.analizByMusteriId(id):
                analizListe.append(j)
            analizler = []
            for k in analizListe:
                analizler.append(f"Analiz Tarih: {k.Tarih}; Foss Giriş Nem: {k.FossGiris_nem}; Foss Giriş Yas Prina Yağ: {k.FossGiris_YasPrina}; Foss Giriş Kuru Prina Yağ: {k.FossGiris_KuruPrina}; Foss Çıkış Nem: {k.FossCikis_nem}; Foss Çıkış Yas Prina Yağ: {k.FossCikis_YasPrina}; Foss Çıkış Kuru Prina Yağ: {k.FossCikis_KuruPrina}; Soxhlet Giriş Nem: {k.SoxhletGiris_nem}; Soxhlet Giriş Yaş Prina: {k.SoxhletGiris_YasPrina}; Soxhlet Giriş Kuru Prina: {k.SoxhletGiris_KuruPrina}; Soxhlet Çıkış Nem: {k.SoxhletCikis_nem}; Soxhlet Çıkış Yaş Prina: {k.SoxhletCikis_YasPrina}; Soxhlet Çıkış Kuru Prina: {k.SoxhletCikis_KuruPrina}; Malaksör Sıcaklığı: {k.Malaksor_sicaklik}; İlave Su (lt): {k.Ilave_su_lt_dk}; Hamur Pompa Kapasitesi (Hrz): {k.Hamur_pompa_kapasite_Hrz}; Hamur Pompa Devri: {k.Hamur_pompa_devri}; İleti: {k.Ileti_d_d}; Helezon Devri: {k.Helezon_devri_d_d}; Gövde Devri: {k.Govde_devri_d_d}; Tork: {k.Tork_kNm}; Dekantör Helezon Motor Amperi: {k.Dekantor_helezon_motor_amperi}; Dekantör Gövde Motor Amperi: {k.Dekantor_govde_motor_amperi}; Boru Uzunluğu: {k.boru_uzunlugu}; Su Yolları: {k.su_yollari_mm}; Beck: {k.beck_mm}")
        return analizler

    def analizIdByMusteriId(self, id):
        if id in (i.id for i in self.db.musteriGenel()):
            analizListe = []
            for j in self.db.analizByMusteriId(id):
                analizListe.append(j)
            analizler = []
            for k in analizListe:
                analizler.append(k.id)
        return analizler


    def addMusteri(self, musteri_ad, musteri_bolge):
        musteri = Musteri(None, musteri_ad, musteri_bolge)
        self.db.addMusteri(musteri)
    


    def makinaListesi(self):
        for i in self.db.makinaGenel():
            print(f"Makina adı: {i.makina_ad}; Seri Numarası: {i.makina_seri_num}") 

    def addMakina(self, musteri_id, makina_ad, makina_seri_num, makina_uretim_tarihi):
        
        makina = Makina(None, makina_ad, makina_uretim_tarihi, makina_seri_num)
        self.db.addMakina(makina)


        makinalar = self.db.makinaGenel()
        makina_id = makinalar[-1].id
        musterimakina = MusteriMakina(None, musteri_id, makina_id)
        self.db.addMusteriMakina(musterimakina)

        

    def addAnaliz(self, makina_id, musteri_id, FossGiris_nem, FossGiris_YasPrina, FossGiris_KuruPrina, FossCikis_nem, FossCikis_YasPrina, FossCikis_KuruPrina, SoxhletGiris_nem, SoxhletGiris_YasPrina, SoxhletGiris_KuruPrina, SoxhletCikis_nem, SoxhletCikis_YasPrina, SoxhletCikis_KuruPrina, Karasu_nem, Karasu_yag, yil, ay, gun, Zeytin_tipi, Malaksor_sicaklik, Ilave_su_lt_dk, Hamur_pompa_kapasite_Hrz, Hamur_pompa_devri, Ileti_d_d, Helezon_devri_d_d, Govde_devri_d_d, Tork_kNm, Dekantor_helezon_motor_amperi, Dekantor_govde_motor_amperi, boru_uzunlugu, faz, su_yollari_mm, beck_mm):
        Tarih = datetime.date(yil, ay, gun)
        
        analiz = Analiz(None, makina_id, musteri_id, FossGiris_nem, FossGiris_YasPrina, FossGiris_KuruPrina, FossCikis_nem, FossCikis_YasPrina, FossCikis_KuruPrina, SoxhletGiris_nem, SoxhletGiris_YasPrina, SoxhletGiris_KuruPrina, SoxhletCikis_nem, SoxhletCikis_YasPrina, SoxhletCikis_KuruPrina, Karasu_nem, Karasu_yag, Tarih, Zeytin_tipi, Malaksor_sicaklik, Ilave_su_lt_dk, Hamur_pompa_kapasite_Hrz, Hamur_pompa_devri, Ileti_d_d, Helezon_devri_d_d, Govde_devri_d_d, Tork_kNm, Dekantor_helezon_motor_amperi, Dekantor_govde_motor_amperi, boru_uzunlugu, faz, su_yollari_mm, beck_mm)
        self.db.addAnaliz(analiz)



    # def addMusteriAnaliz(self):
        analizler = self.db.analizGenel()
        analiz_id = analizler[-1].id
        musteri_id = analizler[-1].musteri_id

        musterianaliz = MusteriAnaliz(None, musteri_id, analiz_id)
        self.db.addMusteriAnaliz(musterianaliz)


    
