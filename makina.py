class Makina:

    def __init__(self, id, makina_ad, makina_uretim_tarihi, makina_seri_num):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.makina_ad = makina_ad
        self.makina_uretim_tarihi = makina_uretim_tarihi
        self.makina_seri_num = makina_seri_num

    @staticmethod
    def createMakina(makinalar):
        liste = []
        
        if isinstance(makinalar, tuple):
            liste.append(Makina(makinalar[0], makinalar[1], makinalar[2], makinalar[3]))
        else:
            for i in makinalar:
                liste.append(Makina(i[0], i[1], i[2], i[3]))
        return liste