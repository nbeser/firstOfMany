import pandas as pd
from dbmanager import DbManager
from upToDate import analizBilgiler
import datetime
import os


class Excel:
    def __init__(self):
        self.db = DbManager()
        self.analizBaslik = analizBilgiler
        self.path = os.path.expanduser("~/Desktop")

    def musteriListesi(self):
        data = []
        for i in self.db.musteri():
            data.append(i)
        
        columns = self.db.musteriColumnnames()
        column_names = []
        for i in columns:
            column_names.append(i[3])         
        
        indexNumaralari = []
        musteri_sayisi =  len(data)+1
        counter = 1
        while counter != musteri_sayisi:
            indexNumaralari.append(counter)
            counter += 1

        df = pd.DataFrame(data, index=indexNumaralari, columns=column_names, dtype=float)
        df.to_excel(f"{self.path}/musteriListesi.xlsx", sheet_name="müşteri")    

    def makinaListesi(self, musteri_id, musteri_ad):
        makina_column_names = ["id", "Makina Adı", "Makina seri Numarası"]        
        musteri_makina_idleri = []
        for z in self.db.musteriMakina(musteri_id):
            musteri_makina_idleri.append(z.makina_id)
        makinalar_raw = self.db.makina()
        makina_df = []
        for i in makinalar_raw:
            if i[0] in musteri_makina_idleri:
                makina_df.append(i)
            else:
                pass
        
        indexNumaralari = []
        makina_sayisi =  len(makina_df)+1
        counter = 1
        while counter != makina_sayisi:
            indexNumaralari.append(counter)
            counter += 1
        
        df = pd.DataFrame(makina_df, index=indexNumaralari, columns=makina_column_names)
        df.to_excel(f"{self.path}/{musteri_ad}_MakinaListesi.xlsx", sheet_name="makinalar")
    
    def analizListesi(self, musteri_id, musteri_ad):
        colunm_names = analizBilgiler

        analizlerRaw = self.db.analiz(musteri_id)
        analizler_düzenli = []
        for i in analizlerRaw:
            i = list(i)
            unwanted = [0, 2]
            for z in sorted(unwanted, reverse=True):
                del i[z]

            date_raw = i[15]
            yil = date_raw.strftime("%Y")
            ay = date_raw.strftime("%m")
            gun = date_raw.strftime("%d")
            date = (gun+"."+ay+"."+yil)
            i[15] = date   
                     
            i = tuple(i)
            analizler_düzenli.append(i)

        indexNumaralari = []
        analiz_sayisi =  len(analizler_düzenli)+1
        counter = 1
        while counter != analiz_sayisi:
            indexNumaralari.append(counter)
            counter += 1
        df = pd.DataFrame(analizler_düzenli, index=indexNumaralari, columns=colunm_names, dtype=float)
        df.to_excel(f"{self.path}/{musteri_ad}_AnalizListesi.xlsx", sheet_name="analizler")
        
        
