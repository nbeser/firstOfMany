class Analiz:

    def __init__(self, id, makina_id, musteri_id, FossGiris_nem, FossGiris_YasPrina, FossGiris_KuruPrina, FossCikis_nem, FossCikis_YasPrina, FossCikis_KuruPrina, SoxhletGiris_nem, SoxhletGiris_YasPrina, SoxhletGiris_KuruPrina, SoxhletCikis_nem, SoxhletCikis_YasPrina, SoxhletCikis_KuruPrina, Karasu_nem, Karasu_yag, Tarih, Zeytin_tipi, Malaksor_sicaklik, Ilave_su_lt_dk, Hamur_pompa_kapasite_Hrz, Hamur_pompa_devri, Ileti_d_d, Helezon_devri_d_d, Govde_devri_d_d, Tork_kNm, Dekantor_helezon_motor_amperi, Dekantor_govde_motor_amperi, boru_uzunlugu, faz, su_yollari_mm, beck_mm):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.makina_id = makina_id
        self.musteri_id = musteri_id
        self.FossGiris_nem = FossGiris_nem
        self.FossGiris_YasPrina = FossGiris_YasPrina
        self.FossGiris_KuruPrina = FossGiris_KuruPrina
        self.FossCikis_nem = FossCikis_nem
        self.FossCikis_YasPrina = FossCikis_YasPrina
        self.FossCikis_KuruPrina = FossCikis_KuruPrina
        self.SoxhletGiris_nem = SoxhletGiris_nem
        self.SoxhletGiris_YasPrina = SoxhletGiris_YasPrina
        self.SoxhletGiris_KuruPrina = SoxhletGiris_KuruPrina
        self.SoxhletCikis_nem = SoxhletCikis_nem
        self.SoxhletCikis_YasPrina = SoxhletCikis_YasPrina
        self.SoxhletCikis_KuruPrina = SoxhletCikis_KuruPrina
        self.Karasu_nem = Karasu_nem
        self.Karasu_yag = Karasu_yag
        self.Tarih = Tarih
        self.Zeytin_tipi = Zeytin_tipi
        self.Malaksor_sicaklik = Malaksor_sicaklik
        self.Ilave_su_lt_dk = Ilave_su_lt_dk
        self.Hamur_pompa_kapasite_Hrz = Hamur_pompa_kapasite_Hrz
        self.Hamur_pompa_devri = Hamur_pompa_devri
        self.Ileti_d_d = Ileti_d_d
        self.Helezon_devri_d_d = Helezon_devri_d_d
        self.Govde_devri_d_d = Govde_devri_d_d
        self.Tork_kNm = Tork_kNm
        self.Dekantor_helezon_motor_amperi = Dekantor_helezon_motor_amperi
        self.Dekantor_govde_motor_amperi = Dekantor_govde_motor_amperi
        self.boru_uzunlugu = boru_uzunlugu
        self.faz = faz
        self.su_yollari_mm = su_yollari_mm
        self.beck_mm = beck_mm
    

    @staticmethod
    def createAnaliz(analizler):
        liste = []
        
        if isinstance(analizler, tuple):
            liste.append(Analiz(analizler[0], analizler[1], analizler[2], analizler[3], analizler[4], analizler[5], analizler[6], analizler[7], analizler[8], analizler[9], analizler[10], analizler[11], analizler[12], analizler[13], analizler[14], analizler[15], analizler[16], analizler[17], analizler[18], analizler[19], analizler[20], analizler[21], analizler[22], analizler[23], analizler[24], analizler[25], analizler[26], analizler[27], analizler[28], analizler[29], analizler[30], analizler[31], analizler[32]))
        else:
            for i in analizler:
                liste.append(Analiz(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28], i[29], i[30], i[31], i[32]))
        return liste
