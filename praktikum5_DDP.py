
#
list = ["pesawat", "Garuda Indonesia", 142, "putih biru", "6 roda"]
print(list)

list.append("Rp1,59 triliun")
list.append("boeing 737")
print(list)

list.insert(2, "Garuda")
print(list)

#
ket = '''selamat datang di aplikasi menghitung luas bangun datar
masukkan pilihan:
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga
'''

pilih = input(ket)

match pilih:
   case '1':
    print('kamu memilih 1 untuk menghitung luas persegi')
    sisi = int (input('masukkan sisi?'))
    luasP = sisi*sisi
    print ('luas persegi yang sisinya', sisi, 'adalah', luasP)

   case '2':
    print('kamu memilih 2 untuk menghitung luas lingkaran')
    jari2 = float (input('masukkan jari-jari?'))
    luasL = 3.14 * jari2 * jari2
    print('luas lingkaran yang jari-jarinya', jari2, 'adalah', int(luasL))

   case '3':
    print('kamu memilih 3 untuk menghitung luas segitiga')
    alas = int (input('masukkan alas?'))
    tinggi = int (input('masukkan tinggi?'))
    luasS = 0.5 * alas * tinggi
    print('luas segitiga yang', alas, 'dan', tinggi, 'adalah', int(luasS))

   case _:
    print('kamu salah memilih pilihan')