class Musteri:

    def __init__(self, id, musteri_ad, musteri_bolge):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.musteri_ad = musteri_ad
        self.musteri_bolge = musteri_bolge
        
    
    @staticmethod
    def createMusteri(obj):
        liste = []
        
        if isinstance(obj, tuple):
            liste.append(Musteri(obj[0], obj[1], obj[2]))
        else:
            for i in obj:
                liste.append(Musteri(i[0], i[1], i[2]))
        return liste