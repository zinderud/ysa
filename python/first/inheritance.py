 


class Hayvan:
    def __init__(self,isim, renk):
        self.isim=isim
        self.renk=renk

    def yuru(self):
        print(self.isim+" yurumeye basladi")
    
    def ye(self):
        print(self.isim+" yemeye basladi")


class Fare(Hayvan):
    def __init__(self,isim,renk):
        super().__init__(isim,renk)

    def yuru(self):
        print(self.isim+" hizlica yurudu")


my_fare=Fare("siyah Avrasya sert sicani ","mavi")

my_fare.yuru();
my_fare.ye()