'''
ini adalah untuk menghitung berapa jumlah pengeluran setiap bulan dari kendaraan 
yang digunakan dalam sebulan dengan memakai kendaraan ganjil genap
dan mengetahui berapa pengeluaran untuk masing kendaraan ganjil dan genap
'''

pengeluaran = 1500000
plat_nomor = [6549, 4567, 2390, 4390, 1987]
hari = 31

ganjil = 0
genap = 0
for i in plat_nomor:
    if i % 2 == 0:
        genap += 1
    else :
        ganjil += 1

i = 1
total = 0

while i <= hari:
    if i % 2 == 0:
        total += (genap*pengeluaran)
    else:
        total += (ganjil*pengeluaran)
i += 1
print(total)