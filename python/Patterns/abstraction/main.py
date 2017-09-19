class Dortgen(object):

    @staticmethod
    def Alan_Hesapla(width, height):
        return width * height
    
    @staticmethod
    def Cevre_hesapla(width, height):
        return 2*(width+height)


# User does not need to know formula to get area of Rectangle
alan = Dortgen.Alan_Hesapla(5, 7)
print(alan)
cevre=Dortgen.Cevre_hesapla(5,7)
print(cevre)

 