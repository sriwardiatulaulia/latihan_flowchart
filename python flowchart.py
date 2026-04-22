from collections import deque

# Struktur data
antrian = deque()
riwayat = []  # stack untuk undo

def tambah_pesanan(nama, vip=False):
    pesanan = nama
    if vip:
        antrian.appendleft(pesanan)
        print(f"{nama} (VIP) masuk ke depan antrian")
    else:
        antrian.append(pesanan)
        print(f"{nama} masuk ke antrian biasa")
    
    riwayat.append(pesanan)

def batal_pesanan():
    if riwayat:
        pesanan = riwayat.pop()
        try:
            antrian.remove(pesanan)
            print(f"Pesanan {pesanan} dibatalkan")
        except ValueError:
            print("Pesanan tidak ditemukan")
    else:
        print("Tidak ada pesanan untuk dibatalkan")

def proses_pesanan():
    if antrian:
        pesanan = antrian.popleft()
        print(f"Memproses pesanan: {pesanan}")
    else:
        print("Antrian kosong")

# Contoh penggunaan
tambah_pesanan("Andi")
tambah_pesanan("Budi", vip=True)
tambah_pesanan("Citra")

batal_pesanan()

proses_pesanan()
proses_pesanan()
