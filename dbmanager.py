import mysql.connector
from connection import connection
import datetime
from analiz import Analiz
from makina import Makina
from musteri import Musteri
from musterianaliz import MusteriAnaliz
from musterimakina import MusteriMakina


class DbManager:
    
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()




    def musteri(self):
        self.cursor.execute("Select * from musteri")
        try:
            obj = self.cursor.fetchall()
            return obj
        except mysql.connector.Error as er:
            print('Hata: '+er)
    def musteriColumnnames(self):
        self.cursor.execute("Select * from information_schema.columns where table_name = N'musteri'")
        try:
            obj = self.cursor.fetchall()
            return obj
        except mysql.connector.Error as er:
            print('Hata: '+er)

    def makina(self):
        self.cursor.execute("Select id, makina_ad, makina_seri_num from makina")
        try:
            makinalar = self.cursor.fetchall()
            return makinalar
        except mysql.connector.Error as er:
            print("Hata: "+er)
    
    def analiz(self, musteri_id):
        sql = "Select * from analiz where musteri_id = %s"
        value = (musteri_id, )
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return obj
        except mysql.connector.Error as er:
            print('Hata: '+er)
    







    def musteriGenel(self):
        self.cursor.execute("Select * from musteri")
        try:
            obj = self.cursor.fetchall()
            return Musteri.createMusteri(obj)
        except mysql.connector.Error as er:
            print('Hata: '+er)

    def getMusteriById(self, id):
        sql = "Select * from musteri where id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Musteri.createMusteri(obj)
        except mysql.connector.Error as er:
            print("Hata: "+ er)
       

    def makinaGenel(self):
        self.cursor.execute("Select * from makina")
        try:
            makinalar = self.cursor.fetchall()
            return Makina.createMakina(makinalar)
        except mysql.connector.Error as er:
            print("Hata: "+er)
        # finally:
        #     self.connection.close()
    
    def musteriMakina(self, musteri_id):
        sql = "Select * from musterimakina where musteri_id= %s"
        value = (musteri_id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return MusteriMakina.musteriMakina(obj)
        except mysql.connector.Error as er:
            print("Hata: "+ er)
        # finally:
        #     self.connection.close()
    
    def makinaListById(self, makina_id):
        sql = "Select * from makina where id = %s"
        value = (makina_id,)
        self.cursor.execute(sql, value)
        try:
            makinalar = self.cursor.fetchone()
            return Makina.createMakina(makinalar)         
        except mysql.connector.Error as er:
            print("Hata: " +er)
        # finally:
        #     self.connection.close()
    
    def analizGenel(self):
        self.cursor.execute("Select * from analiz")
        try:
            analizler = self.cursor.fetchall()
            return Analiz.createAnaliz(analizler)
        except mysql.connector.Error as er:
            print("Hata: "+er)
        # finally:
        #     self.connection.close()

    
    def analizByMusteriId(self, musteri_id):
        sql = "Select * From analiz Where musteri_id = %s"
        value = (musteri_id,)
        self.cursor.execute(sql, value)
        try:
            analizler = self.cursor.fetchall()
            return Analiz.createAnaliz(analizler)
        except mysql.connector.Error as er:
            print("Hata: "+er)
 



    def addMusteri(self, musteri: Musteri):
        sql = "INSERT INTO musteri(musteri_ad, musteri_bolge) VALUES(%s, %s)"
        value = (musteri.musteri_ad, musteri.musteri_bolge)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            # print(f"{self.cursor.rowcount} tane müşteri kaydı eklendi.")
        except mysql.connector.Error as er:
            print("Hata: "+er)
        






    def addMakina(self, makina: Makina):
        sql = "INSERT INTO makina(makina_ad, makina_uretim_tarihi, makina_seri_num) VALUES(%s, %s, %s)"
        value = (makina.makina_ad, makina.makina_uretim_tarihi, makina.makina_seri_num)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            # print(f"{self.cursor.rowcount} tane makina kaydı eklendi.")
        except mysql.connector.Error as er:
            print("Hata: "+er)
    


    def addAnalizMany(self, list: Analiz):
        sql = "INSERT INTO analiz(makina_id, musteri_id, FossGiris_nem, FossGiris_YasPrina, FossGiris_KuruPrina, FossCikis_nem, FossCikis_YasPrina, FossCikis_KuruPrina, SoxhletGiris_nem, SoxhletGiris_YasPrina, SoxhletGiris_KuruPrina, SoxhletCikis_nem, SoxhletCikis_YasPrina, SoxhletCikis_KuruPrina, Karasu_nem, Karasu_yag, Tarih, Zeytin_tipi, Malaksor_sicaklik, Ilave_su_lt_dk, Hamur_pompa_kapasite_Hrz, Hamur_pompa_devri, Ileti_d_d, Helezon_devri_d_d, Govde_devri_d_d, Tork_kNm, Dekantor_helezon_motor_amperi, Dekantor_govde_motor_amperi, boru_uzunlugu, faz, su_yollari_mm, beck_mm) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = []
        for analiz in list:
            a = (analiz.makina_id, analiz.musteri_id, analiz.FossGiris_nem, analiz.FossGiris_YasPrina, analiz.FossGiris_KuruPrina, analiz.FossCikis_nem, analiz.FossCikis_YasPrina, analiz.FossCikis_KuruPrina, analiz.SoxhletGiris_nem, analiz.SoxhletGiris_YasPrina, analiz.SoxhletGiris_KuruPrina, analiz.SoxhletCikis_nem, analiz.SoxhletCikis_YasPrina, analiz.SoxhletCikis_KuruPrina, analiz.Karasu_nem, analiz.Karasu_yag, analiz.Tarih, analiz.Zeytin_tipi, analiz.Malaksor_sicaklik, analiz.Ilave_su_lt_dk, analiz.Hamur_pompa_kapasite_Hrz, analiz.Hamur_pompa_devri, analiz.Ileti_d_d, analiz.Helezon_devri_d_d, analiz.Govde_devri_d_d, analiz.Tork_kNm, analiz.Dekantor_helezon_motor_amperi, analiz.Dekantor_govde_motor_amperi, analiz.boru_uzunlugu, analiz.faz, analiz.su_yollari_mm, analiz.beck_mm)
            values.append(a)
        self.cursor.executemany(sql, values)
        try:
            self.connection.commit()
            # print(f"{self.cursor.rowcount} tane analiz kaydı eklendi.")
        except mysql.connector.Error as er:
            print("Hata: "+er)


    def addMusteriMakina(self, musterimakina: MusteriMakina):
        sql = "INSERT INTO musterimakina(musteri_id, makina_id) VALUES(%s, %s)"
        value = (musterimakina.musteri_id, musterimakina.makina_id)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            # print(f"{self.cursor.rowcount} tane müşteri-makina verisi eklendi.")
        except mysql.connector.Error as er:
            print("Hata: "+er)


    def addMusteriAnaliz(self, musterianaliz: MusteriAnaliz):
        sql = "INSERT INTO musterianaliz(musteri_id, analiz_id) VALUES(%s, %s)"
        value = (musterianaliz.musteri_id, musterianaliz.analiz_id)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            # print(f"{self.cursor.rowcount} tane müşteri-analiz verisi eklendi.")
        except mysql.connector.Error as er:
            print("Hata: "+er)




    def upDateMusteri(self, musteri: Musteri):
        sql = "Update musteri Set musteri_ad=%s, musteri_bolge=%s where id=%s"
        values = (musteri.musteri_ad, musteri.musteri_bolge, musteri.id)
        self.cursor.execute(sql, values)
        try:
            self.connection.commit()
        except mysql.connector.Error as er:
            print(er)

    def upDateMakina(self, makina: Makina):
        sql = "Update makina Set makina_ad=%s, makina_uretim_tarihi=%s, makina_seri_num=%s where id=%s"
        values = (makina.makina_ad,makina.makina_uretim_tarihi, makina.makina_seri_num, makina.id)
        self.cursor.execute(sql, values)
        try:
            self.connection.commit()
        except mysql.connector.Error as er:
            print(er)
    
    def upDateAnaliz(self, analiz: Analiz):
        sql = "Update analiz Set makina_id=%s, FossGiris_nem=%s, FossGiris_YasPrina=%s, FossGiris_KuruPrina=%s, FossCikis_nem=%s, FossCikis_YasPrina=%s, FossCikis_KuruPrina=%s, SoxhletGiris_nem=%s, SoxhletGiris_YasPrina=%s, SoxhletGiris_KuruPrina=%s, SoxhletCikis_nem=%s, SoxhletCikis_YasPrina=%s, SoxhletCikis_KuruPrina=%s, Karasu_nem=%s, Karasu_yag=%s, Tarih=%s, Zeytin_tipi=%s, Malaksor_sicaklik=%s, Ilave_su_lt_dk=%s, Hamur_pompa_kapasite_Hrz=%s, Hamur_pompa_devri=%s, Ileti_d_d=%s, Helezon_devri_d_d=%s, Govde_devri_d_d=%s, Tork_kNm=%s, Dekantor_helezon_motor_amperi=%s, Dekantor_govde_motor_amperi=%s, boru_uzunlugu=%s, faz=%s, su_yollari_mm=%s, beck_mm=%s where id=%s"
        values = (analiz.makina_id, analiz.FossGiris_nem, analiz.FossGiris_YasPrina, analiz.FossGiris_KuruPrina, analiz.FossCikis_nem, analiz.FossCikis_YasPrina, analiz.FossCikis_KuruPrina, analiz.SoxhletGiris_nem, analiz.SoxhletGiris_YasPrina, analiz.SoxhletGiris_KuruPrina, analiz.SoxhletCikis_nem, analiz.SoxhletCikis_YasPrina, analiz.SoxhletCikis_KuruPrina, analiz.Karasu_nem, analiz.Karasu_yag, analiz.Tarih, analiz.Zeytin_tipi, analiz.Malaksor_sicaklik, analiz.Ilave_su_lt_dk, analiz.Hamur_pompa_kapasite_Hrz, analiz.Hamur_pompa_devri, analiz.Ileti_d_d, analiz.Helezon_devri_d_d, analiz.Govde_devri_d_d, analiz.Tork_kNm, analiz.Dekantor_helezon_motor_amperi, analiz.Dekantor_govde_motor_amperi, analiz.boru_uzunlugu, analiz.faz, analiz.su_yollari_mm, analiz.beck_mm, analiz.id)
        self.cursor.execute(sql, values)
        try:
            self.connection.commit()
        except mysql.connector.Error as er:
            print(er)



    def analizIdFromMakinaId(self, makina_id):
        sql = "Select id from analiz where makina_id = %s"
        value = (makina_id, )
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return obj
        except mysql.connector.Error as er:
            print("Hata: "+ er)



    def deleteMusteriAnaliz(self, musteri_id):
        sql = "delete from musterianaliz where musteri_id=%s"
        value = (musteri_id, )
        self.cursor.execute(sql, value)         
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Hata: ", err)
    
    
    def deleteMusteriAnalizByAnalizId(self, analiz_id):
        sql = "delete from musterianaliz where analiz_id=%s"
        value = (analiz_id, )
        self.cursor.execute(sql, value)         
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Hata: ", err)
    
    def deleteAnalizByMusteriId(self, musteri_id):
        sql = "delete from analiz where musteri_id=%s"
        value = (musteri_id, )
        self.cursor.execute(sql, value)         
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def deleteAnalizByMakinaId(self, makina_id):
        sql = "delete from analiz where makina_id=%s"
        value = (makina_id, )
        self.cursor.execute(sql, value)         
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def deleteAnalizById(self, id):
        sql = "delete from analiz where id=%s"
        value = (id, )
        self.cursor.execute(sql, value)         
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def deleteMusteriMakina(self, musteri_id):
        sql = "delete from musterimakina where musteri_id=%s"
        value = (musteri_id, )
        self.cursor.execute(sql, value)         
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Hata: ", err)
    
    def deleteMakinaFrommusterimakina(self, makina_id):
        sql = "delete from musterimakina where makina_id=%s"
        value = (makina_id, )
        self.cursor.execute(sql, value)         
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def deleteMakina(self, id):
        sql = "delete from makina where id=%s"
        value = (id, )
        self.cursor.execute(sql, value)         
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def deleteMusteri(self, id):
        sql = "delete from musteri where id=%s"
        value =  (id, )
        self.cursor.execute(sql, value)         
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Hata: ", err)
    
    
    
    
    
    

    
    

    def deleteMakinaById(self, makina_id):
        sql = "delete from makina whereid=%s"
        value = makina_id
        self.cursor.execute(sql, value)         
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Hata: ", err)


    # def __del__(self):
    #     print('Server kapatıldı')
    #     self.connection.close()

