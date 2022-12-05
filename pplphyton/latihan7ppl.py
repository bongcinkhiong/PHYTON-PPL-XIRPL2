# ada 3 kategori enkapsulasi yaitu : Public, Protected, Private

#contoh kelas public
class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0,5 * alas * tinggi
    
    
#contoh kelas protected 
class mobil:
    def __init__(self, merk):
        self._merk = merk

class mobilefwan(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self._total_gear = total_gear

#Akses _merk dari subclass (kelas turunan)
    def pamer(self):
        print(f'mobil{self._merk} dengan total gear{self._total_gear}')

redbull = mobilefwan('Redbull Racing',8)
redbull.pamer()

#class si paling sulid di akses (private)
class pesawat:
    def __init__(self,merk):
        self.__merk = merk

    def tampilkan_merk(self):
        print(f'Merk pesawatnya : {self.__merk}')
    
pesawat = pesawat('Hondasuzukitoyotaferari')
pesawat.tampilkan_merk()
# sedan = mobil('Toyota')

#tampilan merk dari luar kelas
# print(f'Merk Mobil : {sedan._merk}')