import json
import os
import time
import pwinput
from prettytable import PrettyTable

FILE_AKUN = "akun.json"
FILE_BUKU = "buku.json"

kategori_buku = ("Novel", "Pendidikan", "Komik", "Sejarah", "Horor")

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def input_aman(pesan):
    while True:
        try:
            return input(pesan)
        except KeyboardInterrupt:
            print("\nKalau mau keluar jangan pakai CTRL+C, pilih menu 'Logout' aja.")
        except EOFError:
            print("\nInput tidak tersedia. Silakan coba kembali.")

def password_aman(pesan):
    while True:
        try:
            return pwinput.pwinput(pesan, mask="*")
        except KeyboardInterrupt:
            print("\nKalau mau keluar jangan pakai CTRL+C, pilih menu 'Logout' aja.")
        except EOFError:
            print("\nInput tidak tersedia. Silakan coba kembali.")

def jeda():
    input_aman("\nKlik ENTER kalo mau lanjut")

# Simpan data di JSON (Choni)

def simpan_data(nama_file, data):
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        # Folder tujuan belum ada -> buat dulu, lalu coba simpan lagi
        folder = os.path.dirname(nama_file)
        if folder == "":
            raise
        os.makedirs(folder, exist_ok=True)
        with open(nama_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

# Baca data dari JSON, jika file tidak ada atau rusak, buat baru (Choni)

def baca_data(nama_file, data_awal):
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan. Membuat file baru...")
    except json.JSONDecodeError:
        print(f"File '{nama_file}' rusak/formatnya salah. Membuat ulang file...")
    try:
        simpan_data(nama_file, data_awal)
    except FileNotFoundError:
        print(f"Gagal membuat '{nama_file}': lokasi file tidak ditemukan.")
    except OSError as e:
        print(f"Gagal membuat '{nama_file}': {e}")
    return data_awal

# Data Awal (Choni)

data_awal_buku = [
    {"id": 1, "judul": "Dilan 1990", "penulis": "Pidi Baiq",
    "kategori": "Novel", "stok": 7},
    {"id": 2, "judul": "Naruto", "penulis": "Masashi Kishimoto",
    "kategori": "Komik", "stok": 10},
    {"id": 3, "judul": "Harry Potter", "penulis": "J.K. Rowling",
    "kategori": "Novel", "stok": 12},
    {"id": 4, "judul": "Bulan", "penulis": "Tere LIye",
    "kategori": "Novel", "stok": 9},
    {"id": 5, "judul": "Bumi", "penulis": "Tere Liye",
    "kategori": "Novel", "stok": 8},
    {"id": 6, "judul": "The Shining", "penulis": "Stephen King",
    "kategori": "Horor", "stok": 10},
    {"id": 7, "judul": "Sejarah Lengkap Perang Dunia 1", "penulis": "Alfi Arifian",
    "kategori": "Sejarah", "stok": 15},
    {"id": 8, "judul": "Sekolah itu Candu", "penulis": "Roem Topatimasang",
    "kategori": "Pendidikan", "stok": 5},
    {"id": 9, "judul": "Siapa Orang Asli Palestina?", "penulis": "Zafarul Islam Khan",
    "kategori": "Sejarah", "stok": 6},
    {"id": 10, "judul": "Doraemon", "penulis": "Fujiko F. Fujio",
    "kategori": "Komik", "stok": 18},
]
data_awal_akun = [
    {"username": "admin", "password": "admin123", "role": "admin"}
]

buku = baca_data(FILE_BUKU, data_awal_buku)
akun = baca_data(FILE_AKUN, data_awal_akun)

# Migrasi data lama: key "Stok" -> "stok" (Darell)

if any("Stok" in b for b in buku):
    for b in buku:
        b["stok"] = b.pop("Stok", b.get("stok", 0))
    simpan_data(FILE_BUKU, buku)

# Ini buat pemilihan buku dan kategorinya (Darrell)

def input_angka(pesan, boleh_kosong=False):
    """Minta angka bulat >= 0. Jika boleh_kosong dan kosong -> None."""
    while True:
        nilai = input_aman(pesan).strip()
        if nilai == "" and boleh_kosong:
            return None
        if nilai.isdigit():
            return int(nilai)
        print("Input harus berupa angka!")

def pilih_kategori(boleh_kosong=False):
    """Tampilkan daftar kategori, kembalikan kategori yang dipilih."""
    print("Kategori:")
    for i, k in enumerate(kategori_buku, start=1):
        print(f"  {i}. {k}")

    pesan = f"Pilih kategori 1-{len(kategori_buku)}"
    pesan += " (kosong = tidak diubah): " if boleh_kosong else ": "

    while True:
        nomor = input_angka(pesan, boleh_kosong)
        if nomor is None:
            return None
        if 1 <= nomor <= len(kategori_buku):
            return kategori_buku[nomor - 1]
        print("Nomor kategori tidak valid!")

def tampilkan_tabel(daftar):
    if not daftar:
        print("Data buku tidak ditemukan.")
        return

    tabel = PrettyTable(["ID", "Judul", "Penulis", "Kategori", "Stok"])
    tabel.align["Judul"] = tabel.align["Penulis"] = "l"
    for b in daftar:
        tabel.add_row([b["id"], b["judul"], b["penulis"],
                    b["kategori"], b["stok"]])
    print(tabel)

def pilih_buku(aksi):
    """Tampilkan semua buku, minta ID, kembalikan buku atau None."""
    tampilkan_tabel(buku)
    if not buku:
        return None

    id_buku = input_angka(f"Masukkan ID buku yang {aksi}: ")
    b = next((b for b in buku if b["id"] == id_buku), None)
    if b is None:
        print("Pasang ID Yang Bener!")
    return b

# CRUD Buku (Darell dan Choni)

# CREATE
def tambah_buku():
    print("=== TAMBAH BUKU ===")

    while True:
        judul = input_aman("Judul   : ").strip()
        if judul != "":
            break
        print("Judul tidak boleh kosong!")

    while True:
        penulis = input_aman("Penulis : ").strip()
        if penulis != "":
            break
        print("Nama penulis tidak boleh kosong!")

    buku.append({
        "id": max((b["id"] for b in buku), default=0) + 1,
        "judul": judul,
        "penulis": penulis,
        "kategori": pilih_kategori(),
        "stok": input_angka("Stok    : "),
    })
    simpan_data(FILE_BUKU, buku)
    print("Buku berhasil ditambahkan.")

# READ
def lihat_buku():
    print("=== DAFTAR BUKU PERPUSTAKAAN IPHONE KUPI ===")
    tampilkan_tabel(buku)

def cari_buku():
    print("=== CARI BUKU PEPRUSTAKAAN IPHONE KUPI ===")

    while True:
        kata_kunci = input_aman(
            "Cari judul / penulis: "
        ).strip().lower()

        if kata_kunci != "":
            break
        print("Jangan Dikosongin Boskukkk !")

    tampilkan_tabel([
        b for b in buku
        if kata_kunci in b["judul"].lower()
        or kata_kunci in b["penulis"].lower()
    ])

# UPDATE
def ubah_buku():
    print("=== UBAH BUKU PERPUSTAKAAN IPHONE KUPI ===")
    b = pilih_buku("diubah")
    if b is None:
        return

    print("(Kosongin aja kalau gamau diubah sod)")
    b["judul"] = input_aman(
        f"Judul [{b['judul']}]: "
    ).strip() or b["judul"]

    b["penulis"] = input_aman(
        f"Penulis [{b['penulis']}]: "
    ).strip() or b["penulis"]

    print(f"Kategori saat ini: {b['kategori']}")
    kategori = pilih_kategori(boleh_kosong=True)
    if kategori is not None:
        b["kategori"] = kategori

    stok = input_angka(
        f"Stok [{b['stok']}]: ",
        boleh_kosong=True
    )
    if stok is not None:
        b["stok"] = stok

    simpan_data(FILE_BUKU, buku)
    print("Data buku berhasil diubah.")

# DELETE
def hapus_buku():
    print("=== HAPUS BUKU PERPUSTAKAAN IPHONE KUPI ===")
    b = pilih_buku("dihapus")
    if b is None:
        return

    if input_aman(
        f"Betulan kah mau dihapus '{b['judul']}'? (y/n): "
    ).strip().lower() == "y":
        buku.remove(b)
        simpan_data(FILE_BUKU, buku)
        print("Buku berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

# Menu Admin dan User
# Darell: Tabel
# Choni: Fungsi Menu

def jalankan_menu(judul, opsi):
    """Tampilkan menu dari daftar (nama, fungsi) + Logout di akhir."""
    logout = len(opsi) + 1
    while True:
        bersihkan_layar()
        print(f"=== {judul} ===")

        tabel_menu_admin = PrettyTable(["No.", "Menu"])
        tabel_menu_admin.align["Menu"] = "l"

        for i, (nama, _) in enumerate(opsi, start=1):
            tabel_menu_admin.add_row([i, nama])

        tabel_menu_admin.add_row([logout, "Logout"])
        print(tabel_menu_admin)

        pilihan = input_aman(f"Pilih menu 1-{logout}: ").strip()

        if pilihan == str(logout):
            print("Logout berhasil.")
            time.sleep(1)
            break
        elif pilihan.isdigit() and 1 <= int(pilihan) <= len(opsi):
            bersihkan_layar()
            try:
                opsi[int(pilihan) - 1][1]()
            except FileNotFoundError as e:
                print(f"File tidak ditemukan: {e.filename or e}")
            except (ValueError, KeyError, TypeError) as e:
                print(f"Terjadi kesalahan pada data: {e}")
            except OSError as e:
                print(f"Terjadi kesalahan file: {e}")
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

            jeda()
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)


def menu_admin(user):
    jalankan_menu(f"MENU ADMIN PERPUSTAKAAN IPHONE KUPI{user['username']}", [
        ("Tambah Buku", tambah_buku),
        ("Lihat Buku", lihat_buku),
        ("Cari Buku", cari_buku),
        ("Ubah Buku", ubah_buku),
        ("Hapus Buku", hapus_buku),
    ])

# Ini buat transaksi (Darell)
BIAYA_PINJAM = 5000

def lihat_saldo(user):
    print(f"Saldo kamu: Rp{user.get('saldo', 0):,}")

def topup(user):
    print("=== TOP UP SALDO (SIMULASI) ===")
    lihat_saldo(user)

    nominal = input_angka("Nominal top up (0 = batal): ")
    if nominal == 0:
        print("Top up dibatalkan.")
        return

    user["saldo"] = user.get("saldo", 0) + nominal
    simpan_data(FILE_AKUN, akun)

    print("Top up berhasil.")
    lihat_saldo(user)

# Cetak invoice (Darell)

def cetak_invoice(user, transaksi):
    garis = "=" * 55

    isi_invoice = [
        garis,
        "       INVOICE PEMINJAMAN",
        "    PERPUSTAKAAN DIGITAL IPHONE KUPI",
        garis,
        f"Username     : {user['username']}",
        f"Tanggal      : {transaksi['tanggal']}",
        garis,
        "DETAIL PEMINJAMAN",
        f"ID Buku      : {transaksi['id_buku']}",
        f"Judul Buku   : {transaksi['judul']}",
        f"Biaya Pinjam : Rp{transaksi['biaya']:,}",
        garis,
        f"TOTAL BAYAR  : Rp{transaksi['biaya']:,}",
        "Status       : BERHASIL",
        garis,
        "Terima kasih, Jangan Lupa Dikembalikan Yooo.",
        garis,
    ]

    print("\n" + "\n".join(isi_invoice))

    try:
        os.makedirs("invoice", exist_ok=True) #ini dijadikan 1 sama akun.json
        nama_file = os.path.join("invoice", f"{transaksi['id_invoice']}.txt")

        with open(nama_file, "w", encoding="utf-8") as file:
            file.write("\n".join(isi_invoice))

        print(f"\nInvoice berhasil disimpan di: {nama_file}")
    except FileNotFoundError:
        print("\nInvoice tampil di layar, tetapi folder 'invoice' tidak ditemukan.")
    except OSError as e:
        print(f"\nInvoice tampil di layar, tetapi gagal disimpan: {e}")

# Fungsi Peminjaman Buku (Darell)

def pinjam_buku(user):
    print("=== PEMINJAMAN BUKU ===")
    print(f"Biaya pinjam: Rp{BIAYA_PINJAM:,} per buku")

    lihat_saldo(user)

    b = pilih_buku("dipinjam")
    if b is None:
        return

    if b["stok"] <= 0:
        print("Stok buku habis.")
        return

    if user.get("saldo", 0) < BIAYA_PINJAM:
        print("Saldo tidak cukup. Silakan top up terlebih dahulu.")
        return

    konfirmasi = input_aman(
        f"Pinjam '{b['judul']}' seharga Rp{BIAYA_PINJAM:,}? (y/n): "
    ).strip().lower()

    if konfirmasi != "y":
        print("Peminjaman dibatalkan.")
        return

    user["saldo"] -= BIAYA_PINJAM
    b["stok"] -= 1

    username_aman = "".join(
        karakter if karakter.isalnum() or karakter in ("-", "_") else "_"
        for karakter in user["username"]
    )
    nomor_invoice = (
        f"INV-{time.strftime('%Y%m%d%H%M%S')}-"
        f"{username_aman}-{len(user.get('peminjaman', [])) + 1:03d}"
    )

    transaksi = {
        "id_invoice": nomor_invoice,
        "id_buku": b["id"],
        "judul": b["judul"],
        "tanggal": time.strftime("%Y-%m-%d %H:%M:%S"),
        "biaya": BIAYA_PINJAM,
    }

    user.setdefault("peminjaman", []).append(transaksi)

    simpan_data(FILE_AKUN, akun)
    simpan_data(FILE_BUKU, buku)

    print(f"\nBuku '{b['judul']}' berhasil dipinjam.")
    lihat_saldo(user)
    cetak_invoice(user, transaksi)

# Fungsi Riwayat Peminjaman (Darell)

def riwayat_peminjaman(user):
    print("=== RIWAYAT PEMINJAMAN ===")
    riwayat = user.get("peminjaman", [])

    if not riwayat:
        print("Kamu belum pernah meminjam buku.")
        return

    tabel = PrettyTable(["No", "Judul", "Tanggal", "Biaya"])
    for nomor, transaksi in enumerate(riwayat, start=1):
        tabel.add_row([
            nomor,
            transaksi["judul"],
            transaksi["tanggal"],
            f"Rp{transaksi['biaya']:,}",
        ])
    print(tabel)

# Menu User 
# Darell: Tabel
# Choni: Fungsi Menu User

def menu_user(user):
    while True:
        bersihkan_layar()
        print(f"=== MENU USER {user['username']} | Saldo: Rp{user.get('saldo', 0):,} ===")

        tabel_menu = PrettyTable(["No.", "Menu"])
        tabel_menu.align["Menu"] = "l"
        tabel_menu.add_row(["1", "Lihat Daftar Buku"])
        tabel_menu.add_row(["2", "Pinjam Buku"])
        tabel_menu.add_row(["3", "Top Up Saldo"])
        tabel_menu.add_row(["4", "Keluar"])
        print(tabel_menu)

        pilihan = input_aman("Pilih menu 1-4: ").strip()

        if pilihan == "4":
            print("Keluar dari menu user.")
            break

        try:
            if pilihan == "1":
                lihat_buku()
            elif pilihan == "2":
                pinjam_buku(user)
            elif pilihan == "3":
                topup(user)
            else:
                print("Pilihan tidak valid!")
        except FileNotFoundError as e:
            print(f"File tidak ditemukan: {e.filename or e}")
        except (ValueError, KeyError, TypeError, OSError) as e:
            print(f"Terjadi kesalahan: {e}")

        jeda()

# Fungsi Registrasi dan Login (Choni)

def registrasi(akun):
    print("=== REGISTRASI PEPRUSTAKAAN IPHONE KUPI ===")

    while True:
        username = input_aman("Buat username: ").strip()

        if username == "":
            print("Username tidak boleh kosong!")
        elif any(a["username"] == username for a in akun):
            print("Username sudah digunakan!")
        else:
            break

    while True:
        password = password_aman("Buat password: ")

        if password.strip() == "":
            print("Password tidak boleh kosong!")
        else:
            break

    akun.append({"username": username, "password": password, "role": "user"})
    simpan_data(FILE_AKUN, akun)

    print("Registrasi berhasil, silahkan login.")
    return True

def login(akun):
    print("=== HALAMAN LOGIN PERPUSTAKAAN IPHONE KUPI ===")

    batas_percobaan = 3

    for percobaan in range(1, batas_percobaan + 1):
        print(f"Percobaan login {percobaan}/{batas_percobaan}")

        username = input_aman("Username: ").strip()
        password = password_aman("Password: ")

        if username == "" or password.strip() == "":
            print("Username dan password tidak boleh kosong!")
        else:
            for a in akun:
                if username == a["username"] and password == a["password"]:
                    print(f"Login berhasil! Selamat datang, {a['username']}.")
                    time.sleep(1)
                    return a

            print("Username atau password salah!")

        sisa_percobaan = batas_percobaan - percobaan
        if sisa_percobaan > 0:
            print(f"Kesempatan tersisa: {sisa_percobaan}")
        else:
            print("Login gagal 3 kali. Kesempatan login habis.")

    return None

# Ini menu utama (Darell)

def main():
    while True:
        bersihkan_layar()
        print("=== PERPUSTAKAAN DIGITAL IPHONE KUPI ===")

        tabel_menu_utama = PrettyTable(["No.", "Menu"])
        tabel_menu_utama.align["Menu"] = "l"
        tabel_menu_utama.add_row(["1", "Login"])
        tabel_menu_utama.add_row(["2", "Registrasi"])
        tabel_menu_utama.add_row(["3", "Keluar"])
        print(tabel_menu_utama)

        pilihan = input_aman("Pilih menu 1-3: ").strip()

        bersihkan_layar()
        if pilihan == "1":
            try:
                user = login(akun)
                if user is None:
                    time.sleep(1)
                elif user["role"] == "admin":
                    menu_admin(user)
                else:
                    menu_user(user)
            except FileNotFoundError as e:
                print(f"File tidak ditemukan: {e.filename or e}")
                jeda()
            except (ValueError, KeyError, TypeError) as e:
                print(f"Terjadi kesalahan pada data: {e}")
                jeda()
            except OSError as e:
                print(f"Terjadi kesalahan file: {e}")
                jeda()
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
                jeda()

        elif pilihan == "2":
            try:
                registrasi(akun)
            except FileNotFoundError:
                print(f"Gagal menyimpan akun: file '{FILE_AKUN}' tidak ditemukan.")
            except OSError as e:
                print(f"Gagal menyimpan data akun: {e}")
            except Exception as e:
                print(f"Terjadi kesalahan saat registrasi: {e}")
            time.sleep(1)

        elif pilihan == "3":
            print("Terimakasih telah menggunakan Aplikasi")
            break
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKalau mau keluar, pilih menu 'Keluar' saja.")
        main()
    except FileNotFoundError as e:
        print(f"File tidak ditemukan: {e.filename or e}")
    except Exception as e:
        print(f"Error bro coba lagi nanti {e}")