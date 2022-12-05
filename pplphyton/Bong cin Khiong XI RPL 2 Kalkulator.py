class angka:
    def __init__(self, angka,objek):
        self.angka = angka
        self.objek = objek

    def __str__(self):
        luas =  self.angka + self.objek
        return f'Hasil dari {self.angka} + {self.objek} adalah {luas}'

luas = angka(int(input("Masukkan angka1:")), int(input("Masukkan angka2:")))
print(luas)