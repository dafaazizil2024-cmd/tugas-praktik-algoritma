# input
# nilai mahasiswa
nilai_tugas = 80
nilai_uts = 80
nilai_uas  = 90
kehadiran = 95

tugas = float(input("nilai tugas :, "))
uts = float(input("nilai uts :, "))
uas = float(input("nilai uas :, "))
kehadiran = float(input("kehadiran :, "))

# nilai akhir
nilai_akhir =(0.2 * tugas) + (0.3 * uts) + (0.5  * uas)
nilai_akhir =(0.2 * 80) + (0.3 * 80) + (0.5  * 90)

if nilai_akhir >= 85 and kehadiran >= 90 and int(nilai_akhir) % 2 == 0:
    status = "LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "LULUS"
else:
    status = "BELUM LULUS"

# output
print(f"Nilai Akhir : {nilai_akhir}")
print(f"Status : {status}")



