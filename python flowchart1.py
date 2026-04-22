from collections import deque

antrian = deque()
riwayat = []

while True:
    print("\n=== MENU RESTORAN ===")
    print("1. Tambah pelanggan")
    print("2. Batalkan pesanan (Undo)")
    print("3. Proses pesanan")
    print("4. Lihat antrian")
    print("5. Keluar")

    pilih = input("Masukkan pilihan: ")

    if pilih == "1":
        nama = input("Nama pelanggan: ")
        vip = input("VIP? (y/n): ")

        if vip.lower() == "y":
            antrian.appendleft(nama)
            print(f"{nama} (VIP) masuk ke depan")
        else:
            antrian.append(nama)
            print(f"{nama} masuk ke belakang")

        riwayat.append(nama)

    elif pilih == "2":
        if riwayat:
            batal = riwayat.pop()
            if batal in antrian:
                antrian.remove(batal)
                print(f"Pesanan {batal} dibatalkan")
        else:
            print("Tidak ada pesanan")

    elif pilih == "3":
        if antrian:
            proses = antrian.popleft()
            print(f"Memproses: {proses}")
        else:
            print("Antrian kosong")

    elif pilih == "4":
        print("Antrian:", list(antrian))

    elif pilih == "5":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
