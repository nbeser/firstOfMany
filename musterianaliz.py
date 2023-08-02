class MusteriAnaliz:

    def __init__(self, id, musteri_id, analiz_id):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.musteri_id = musteri_id
        self.analiz_id = analiz_id

    @staticmethod
    def musteriAnaliz(obj):
        liste = []
        
        if isinstance(obj, tuple):
            liste.append(MusteriAnaliz(obj[0], obj[1], obj[2]))
        else:
            for i in obj:
                liste.append(MusteriAnaliz(i[0], i[1], i[2]))
        return liste