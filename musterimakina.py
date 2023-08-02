class MusteriMakina:

    def __init__(self, id, musteri_id, makina_id):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.musteri_id = musteri_id
        self.makina_id = makina_id

    
    @staticmethod
    def musteriMakina(obj):
        liste = []
        
        if isinstance(obj, tuple):
            liste.append(MusteriMakina(obj[0], obj[1], obj[2]))
        else:
            for i in obj:
                liste.append(MusteriMakina(i[0], i[1], i[2]))
        return liste