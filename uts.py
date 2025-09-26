nama = input("nama lengkap siswa: ")
kkm = int(input("nilai KKM: "))
uts = int(input("nilai UTS (0-100): "))
uas = int(input("nilai UAS (0-100): "))

nilai_akhir = (0.4 * uts) + (0.6 * uas)

if nilai_akhir >= 60 and uts >= 40 and uas >= 40:
    status = "LULUS"
    alasan = "Nilai akhir memenuhi syarat dan semua nilai >= 40."

elif nilai_akhir < 60 or uts < 40 or uas < 40:
    status = "GAGAL"

    if uts < 40:
        alasan = "Nilai UTS kurang dari 40."
    elif uas < 40:
        alasan = "Nilai UAS kurang dari 40."
    else:
        alasan = "Nilai akhir kurang dari 60."
else:
    status = "GAGAL"
    alasan = "Tidak memenuhi kriteria."

print("\n=== HASIL PENILAIAN SEMESTER ===")
print("Nama Siswa     :", nama)
print("Nilai KKM      :", kkm)
print("Nilai UTS      :", uts)
print("Nilai UAS      :", uas)
print("Nilai Akhir    :", nilai_akhir)
print("Status         :", status)
print("Keterangan     :", alasan)