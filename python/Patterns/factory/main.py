from random import randrange


class Silah(object):
    adi = None
    maliyet = None

    @staticmethod
    def get_Silah(x):
        if x == 0:
            return Bicak()
        if x == 1:
            return Tabanca()


class Bicak(Silah):
    adi = 'Bicak'
    maliyet = 20.00


class Tabanca(Silah):
    adi = 'Tabanca'
    maliyet = 300.00


#   25 random Silah üret
for _ in range(25):
    w = Silah.get_Silah(randrange(2))
    print(w.adi, w.maliyet)
