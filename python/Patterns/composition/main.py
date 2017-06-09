class Yuz(object):

    def __init__(self, goz_rengi, sac_rengi):
        self.goz_rengi = goz_rengi
        self.sac_rengi = sac_rengi


class Vucut(object):

    def __init__(self, agirlik):
        self.agirlik = agirlik


class Kisi(object):

    def __init__(self, goz_rengi, sac_rengi, agirlik):
        self.yuz = Yuz(goz_rengi, sac_rengi)
        self.Vucut = Vucut(agirlik)

    def print_goz_rengi(self):
        print(self.yuz.goz_rengi)

ali = Kisi('mavi', 'siyah', 163)
ali.print_goz_rengi()
