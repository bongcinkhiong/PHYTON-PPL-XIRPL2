# belajar pewarisan (inheritance)
#3 objek = Orang,Pelajar,Pekerja
#masing-masing mempunyai nama,asal,kemampuan untuk introduce ur self
# pelajar mempunyai atribut pelajar di sekolah , pekerja di kantor

class saykocak:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
        print("fungsi init dieksekusi")

    def perkenalan(self):
        print("Perkenalkan nama saya", self.nama, "dari" ,self.asal)


class badut(saykocak):
    def __init__(self, nama, asal , profesi):
        saykocak.__init__(self, nama, asal)
        self.profesi = profesi
    pass

w = saykocak('toto','Zimbabwe')
w.perkenalan()

dd = badut('yonlek','sss','badut')
dd.perkenalan()
print("Saya berprofesi sebagai", dd.profesi,"\n")