# KELOMPOK E - EMBEDDED / IoT
# MONITORING KELEMBAPAN TANAH & AKSI POMPA

# 15 DATA INTI
data_kelembapan = [
    22, 28, 34, 41, 55,
    63, 72, 78, 31, 47,
    66, 81, 19, 58, 69
]

# 5 DATA TAMBAHAN
# 35 dan 70 untuk menguji batas NORMAL
# 71 untuk menguji kategori BASAH
# 10 untuk menguji kelembapan rendah
# 50 untuk variasi nilai NORMAL
data_tambahan = [35, 70, 71, 10, 50]

# Menggabungkan data menjadi 20 data
data_kelembapan.extend(data_tambahan)


# FUNGSI 1: MENENTUKAN STATUS SENSOR
def status_sensor(nilai):
    if nilai < 35:
        return "KERING"
    elif nilai <= 70:
        return "NORMAL"
    else:
        return "BASAH"


# FUNGSI 2: MENENTUKAN AKSI POMPA
def aksi_pompa(status):
    if status == "KERING":
        return "POMPA ON"
    else:
        return "POMPA OFF"


# FUNGSI 3: MENGHITUNG RATA-RATA
def rata_rata(data):
    return sum(data) / len(data)


# PROGRAM UTAMA
print("====================================")
print(" MONITORING KELEMBAPAN TANAH")
print("          KELOMPOK E")
print("====================================")

print("Jumlah Data:", len(data_kelembapan))
print("------------------------------------")

# Menampilkan setiap data
for nomor, nilai in enumerate(data_kelembapan, start=1):
    status = status_sensor(nilai)
    pompa = aksi_pompa(status)

    print(
        "Data", nomor,
        ":", nilai, "%",
        "|", status,
        "|", pompa
    )

# Menghitung jumlah status
kering = 0
normal = 0
basah = 0

for nilai in data_kelembapan:
    status = status_sensor(nilai)

    if status == "KERING":
        kering += 1
    elif status == "NORMAL":
        normal += 1
    else:
        basah += 1

# Menampilkan hasil akhir
print("------------------------------------")
print("HASIL MONITORING")
print("Jumlah KERING :", kering)
print("Jumlah NORMAL :", normal)
print("Jumlah BASAH  :", basah)

print(
    "Rata-rata Kelembapan:",
    round(rata_rata(data_kelembapan), 2),
    "%"
)

print("====================================")
print("Program selesai.")