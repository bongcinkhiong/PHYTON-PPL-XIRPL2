class Agama:
    def __init__(self, nama, cara):
        self.nama = nama
        self.cara = cara
        print("fungsi init dieksekusi")

    def beribadah(self):
        print( self.nama, "beribadah dengan", "melakukan" ,self.cara)

class Budha(Agama):
    def __init__(self, nama, sembahyang):
        Agama.__init__(self,nama, sembahyang)
        self.nama = nama
        self.cara = sembahyang
    pass

class Islam(Agama):
    def __init__(self, nama, Sholat):
        Agama.__init__(self,nama, Sholat)
        self.nama = nama
        self.cara = Sholat
    pass

Bong_cin = Budha('Bongcin','Sembahyang')
Bong_cin.beribadah()

Dava = Islam('Dava','Sholat')
Dava.beribadah()