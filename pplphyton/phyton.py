# Membuat List kosong
# warna = []

# Membuat list dena=gan isi 1 item 
hobi = ["membaca"]

buah = ["jeruk","apel","mangga"]

laci = ["buku",21,True,34.12]

# Kita punya list nama-nama buah
buah = ["apel","anggur","mangga"]

# untuk memanggil buah yang ingin di panggil
print = buah[2]

#buat list untuk menampung nama-nama
my_friends = ["Anggun", "Dian", "Agung", "Adi", "Adam"]

# Tampilkan isi list my_friends dengan nomer indeks 3 
print .format(my_friends[3])
print .format(len(my_friends))
for friend in my_friends:
    print 

#list mula-mula
buah = ["jeruk","apel", "mangga", "duren"]
#mengubah nilai index ke-2
buah[2] ="kelapa"

#list mula-mula
buah =["jeruk", "apel", "mangga", "duren"]
#tambahkan manggis
buah.append("manggis")

#list mula-mula
buah =["jeruk", "apel", "mangga", "duren"]
buah.prepend("anggur")

#list mula-mula
buah = ["jeruk", "apel", "mangga", "duren"]
buah.insert(2,"duren")

#membuat list kosong untuk menampung hobi
hobi =[]
stop = False
i = 0

#mengii hobi
while(not stop):
    hobi_baru = ("inputkan hobi yang ke-{}:". format(i))
    hobi.append(hobi_baru)

    #increment i
    i += 1

    tanya = ("mau isi lagi?(y/t):")
    if(tanya == "t"):
        stop = True

#cetak semua hobi
print  * 10
print .format(len(hobi))
for hb in hobi:
    print .format(hb)

#membuat list
todo_list = [
    "balajar Phyton",
    "balajar django",
    "balajar MongoDB",
    "balajar Sulap",
    "balajar flask"
]

#misalkan kita ingin menghapus "Belajar Sulap"
#yang berasa di indeks ke-3
del todo_list[3]
print  

#mula-mula kita punya list
a = ["a", "b", "c", "d"]
#kemudian kita hapus b
a.remove("b")

print = a

#kita punya list warna
warna = ["merah", "hijau", "kuning", "biru", "pink", "ungu"]
#kita potong dari indeks ke-1 sampai ke-5
print [1:5]

#beberapa list lagu
list_lagu = [
    "No women, No cry",
    "Dear God"
]

#playlist lagu favorit
playlist_favorit = [
    "break Out",
    "Now Loading!!!"
]

#mari kita gabungkan keduanya 
semua_lagu = list_lagu + playlist_favorit
print = semua_lagu


#playlist lagu favorit
playlist_favorit = [
    "Break Out",
    "Now loading!!!"
]

#ulangi sebanyak 5x
ulangi = 5

now_playing = playlist_favorit *ulangi

print = now_playing 

#list minuman dengan 2 dimeni
list_minuman = [
    ["Kopi", "Susu", "Teh"],
    ["jus apel", "Jus Melon" , "jus jeruk"]
    ["Es kopi", "Es campur", "Es Teler"]
]

#cara mengakses list multidimensi
#misalkan kita ingin mengambil "es kopi"
print = list_minuman[2][0]

#list minuman dengan 2 dimeni
list_minuman = [
    ["Kopi", "Susu", "Teh"],
    ["jus apel", "Jus Melon" , "jus jeruk"]
    ["Es kopi", "Es campur", "Es Teler"]
]
