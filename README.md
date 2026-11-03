# Aplikasi Perpustakaan Digital

Kelompok: 9 <br>
|     Nama Anggota     |    NIM     |  Peran   |
| -------------------- | ---------- | -------- |                                                                                          
| Fiona Deandra Liani  | 2609116053 |  Ketua   |
| Darrel Faiz Sinatria | 2609116055 | Anggota  |
| Putrika Juliya Sari  | 2609116057 | Anggota  |
| Choni Yudhistira     | 2609116074 | Anggota  |
------------------------------------------------

**Deskripsi** <br>
-------------------
Aplikasi Perpustakaan Digital merupakan sebuah program yang dirancang untuk membantu proses pengelolaan perpustakaan secara digital. Aplikasi ini menyediakan berbagai fitur yang dapat digunakan oleh pengguna untuk mengakses informasi buku, melakukan pencarian buku, serta melakukan peminjaman dengan sistem pembayaran menggunakan saldo digital.

Aplikasi ini memiliki dua jenis hak akses pengguna, yaitu Admin dan User. Admin memiliki hak akses penuh untuk mengelola data buku, seperti menambahkan, menampilkan, mengubah, dan menghapus data buku. Sementara itu, User dapat melakukan registrasi dan login, melihat serta mencari buku, melakukan top up saldo, meminjam buku, dan mendapatkan invoice sebagai bukti transaksi.

Dalam proses pengelolaan datanya, aplikasi ini menggunakan file JSON sebagai media penyimpanan data pengguna dan data buku agar informasi tetap tersimpan meskipun program telah ditutup. Selain itu, aplikasi dilengkapi dengan validasi input dan penanganan kesalahan untuk mengurangi terjadinya kesalahan selama penggunaan program.

Melalui aplikasi ini, diharapkan proses pengelolaan perpustakaan menjadi lebih praktis, terstruktur, dan efisien dengan memanfaatkan teknologi digital.

**Tujuan** <br>
---------------
- Berdasarkan rumusan masalah, tujuan yang ingin dicapai adalah sebagai berikut: 

- Mengembangkan program Aplikasi Perpustakaan Digital menggunakan bahasa pemrograman Python. 

- Menerapkan registrasi dan login dengan pembagian hak akses admin dan pelanggan. 

- Menerapkan pengelolaan data buku melalui operasi tambah, lihat, ubah, dan hapus dan menerapkan penyimpanan data menggunakan JSON. 

- Mengembangkan simulasi top-up saldo dan transaksi peminjaman buku dengan validasi stok dan saldo. 

- Menerapkan konsep dasar pemrograman, seperti struktur data, fungsi, percabangan, perulangan, dan penanganan kesalahan.

---------------

# FLOWCHART
---------------
## MENU UTAMA: 

<img width="1913" height="1042" alt="FLOWCHART PA KEL 9 final-Utama drawio" src="https://github.com/user-attachments/assets/373015e8-d602-41b6-a7b7-d35e2a255a61" />

<br>Deskripsi: Flowchart menu utama ini menggambarkan alur utama aplikasi perpustakaan digital, mulai dari login, registrasi, hingga keluar. Pengguna dapat membuat akun baru atau masuk menggunakan akun yang sudah ada. Setelah login, sistem membedakan antara akses admin dan user sesuai perannya.

## MENU ADMIN: 

<img width="2082" height="1377" alt="FLOWCHART PA KEL 9 final-Admin drawio" src="https://github.com/user-attachments/assets/e2ad4997-2141-47af-b4ff-46de89941f1e" />

<br>Deskripsi: Flowchart menu admin ini menggambarkan proses CRUD (Create, Read, Update, Delete) pada sistem admin. Admin dapat menambah, melihat, mencari, mengubah, dan menghapus data yang tersimpan di file JSON. Setiap tindakan divalidasi dengan pengecekan ID, judul atau penulis dan menampilkan pesan keberhasilan atau kesalahan sesuai hasil proses.

## MENU USER:

<img width="2186" height="1227" alt="FLOWCHART PA KEL 9 final-User drawio" src="https://github.com/user-attachments/assets/0e9e03b3-b08f-48d7-b196-89d5be162a58" />

<br>Deskripsi: Flowchart menu user ini menjelaskan alur aktivitas pengguna dalam aplikasi perpustakaan digital, mulai dari melihat buku, meminjam buku dan melihat invoice, hingga top-up saldo. Setiap proses mencakup pengecekan data, validasi saldo ke file JSON. Setelah transaksi selesai, sistem menampilkan invoice atau saldo terbaru pengguna.

# Aplikasi Perpustakaan Digital Berdasarkan Role
---------------
## Login Sebagai admin 

<img width="297" height="149" alt="Screenshot 2026-11-03 1532333" src="https://github.com/user-attachments/assets/c2620ecf-70d6-421f-9939-3529f817e8fa" />

<br>Program akan menampilkan beberapa pilihan setelah Admin memilih menu Login dan memasukkan datanya dengan benar dari menu utama Admin. Pada bagian ini, sistem menampilkan lima fitur utama yang berfungsi untuk mengelola data dari perpustakaan digital, yaitu:

- Tambah Buku –  Menambahkan data buku baru ke dalam database. 

- Lihat Buku –  Menampilkan daftar buku yang tersedia dalam sistem.

- Cari Buku – Mencari buku berdasarkan daftar buku yang tersedia di dalam sistem.

- Ubah Buku – Mengubah informasi buku yang sudah terdaftar.

- Hapus Buku – Menghapus buku dari sistem.
  
- Keluar - Mengembalikan pengguna ke menu Admin sebelumnya.

**1. Tambah Buku**
<br><img width="411" height="206" alt="Screenshot 2026-11-03 153357" src="https://github.com/user-attachments/assets/7a011f41-e230-4232-9c12-552f439c2acb" />

Saat admin menginput angka 1 program  ini menampilkan hasil dari pilihan menu yaitu “Tambah Buku”. Pada tahap ini, sistem menampilkan tabel berisi seluruh data buku yang tersimpan di database, dengan isi sebagai berikut:

- ID – Kode unik untuk setiap buku.
  
- Judul Buku – Nama buku yang tersedia di perpustakaan.
  
- Penulis – Nama dari penulis buku.

- Kategori – Jenis atau genre dari buku yang tersedia di perpustakaan.

- Stok – Jumlah buku yang tersedia perpustakaan.

**2. Lihat Buku**

<img width="689" height="245" alt="Screenshot 2026-11-03 172946" src="https://github.com/user-attachments/assets/4532226e-8f11-4c1b-abc8-cd70ba0b0076" />


Saat admin menginput angka 2 program akan menampilkan output daftar buku yang tersedia di dalam perpustakaan dalam bentuk tabel yang tersusun rapi. Pada tabel tersebut daftar bukunya berisi ID, Judul, Penulis, Kategori, dan Stok.

**3. Cari Buku**

<img width="698" height="128" alt="Screenshot 2026-11-03 173010" src="https://github.com/user-attachments/assets/8413014f-9879-4e11-a032-4e3878cbba7b" />

Saat admin menginput angka 3 program akan meminta admin untuk menginput judul/penulis yang ingin dicari, lalu akan menampilkan data dalam bentuk tabel yang berisi ID, Judul, Penulis, Kategori, dan Stok hanya dari data yang ingin dicari.

**4. Ubah Buku**

<img width="684" height="432" alt="Screenshot 2026-11-03 173109" src="https://github.com/user-attachments/assets/c8694a60-514a-4e0c-abe4-ba7e25e2d0d6" />

Saat admin menginput angka 4 program akan menampilkan daftar buku yang sedang tersedia, lalu program akan meminta admin untuk menginput ID, Judul, Penulis, Kategori, dan stok buku. Lalu program akan mengeluarkan output "Data buku berhasil diubah"

**5. Hapus Buku**

<img width="689" height="282" alt="Screenshot 2026-11-03 173142" src="https://github.com/user-attachments/assets/c4efed5c-7af4-4739-b7ab-8d5dfe58d03a" />

Saat admin menginput angka 5 program akan menampilkan daftar buku yang sedang tersedia, lalu meminta admin untuk menguinput ID buku yang ingin dihapus. Program akan bertanya kembali untuk memastikan apakah admin ingin menghapus atau tidak, jika mengetik y maka buku berhasil dihapus.

**6. Keluar**

<img width="959" height="290" alt="Screenshot 2026-11-03 173253" src="https://github.com/user-attachments/assets/ae8b4286-aabe-4b07-9cac-5709c696e86a" />

Saat admin mengetik angka 6 program akan menampilkan output "Logout berhasil", lalu admin akan menuju ke menu utama.

## Login Sebagai User

<img width="704" height="155" alt="Screenshot 2026-11-03 174943" src="https://github.com/user-attachments/assets/a280944d-6362-44c7-a0c3-c631108b7837" />

Program akan menampilkan beberapa pilihan setelah User memilih menu Login dan memasukkan datanya dengan benar dari menu utama User. Pada bagian ini, sistem menampilkan empat fitur utama yang berfungsi untuk mengelola data dari perpustakaan digital, yaitu:

- Lihat Daftar Buku – Menampilkan daftar buku yang tersedia dalam sistem. 

- Pinjam Buku –  Menampilkan daftar buku yang tersedia dalam sistem.

- Top Up Saldo – Menampilkan menu top up yang berisi nominal dan saldo (awal dan akhir).
  
- Keluar - Mengembalikan pengguna ke menu utama sebelumnya.

**1.Lihat Daftar Buku**

<img width="694" height="365" alt="Screenshot 2026-11-03 174956" src="https://github.com/user-attachments/assets/abe3e659-d29d-42d6-a998-b129686edbac" />

Saat user menginput angka 1 program  ini menampilkan hasil dari pilihan menu yaitu “lIHAT Buku”. Pada tahap ini, sistem menampilkan tabel berisi seluruh data buku yang tersimpan di database, dengan isi sebagai berikut:

- ID – Kode unik untuk setiap buku.
  
- Judul Buku – Nama buku yang tersedia di perpustakaan.
  
- Penulis – Nama dari penulis buku.

- Kategori – Jenis atau genre dari buku yang tersedia di perpustakaan.

- Stok – Jumlah buku yang tersedia perpustakaan.

**2. Pinjam Buku**

<img width="895" height="479" alt="Screenshot 2026-11-03 175208" src="https://github.com/user-attachments/assets/aae3b37f-7887-40d5-a1b6-a09779e2c692" />

Saat user mengetik angka 2 program akan meminta input ID Buku yang ingin dipinjam dengan harga(RP5.000) per buku dan menampilkan saldo yang dimiliki. Lalu program akan meampilkan daftar buku yang berisi ID, Judul, Penulis, Kategori, dan Stok. Setelah itu program akan meminta input ID dan memastikan ulang apakah benar-benar ingin dihapus. Setelah buku berhasil dipinjam program akan menampilkan saldo setelah peminjaman buku

- Invoice
  
<img width="929" height="283" alt="Screenshot 2026-11-03 175245" src="https://github.com/user-attachments/assets/74ad7360-fc44-4be0-952e-4a1d3b1a1995" />

Program akan menampilkan invoice yang berisi:
- username dan tanggal
- Detail pemesanan - Detail pemesanan yang berisi ID, buku, Judul buku, dan biaya pinjam
- Total pembayaran dan status(berhasil/gagal)
- Ucapan "terima kasih, jangan lupa dikembalikan yooo"
Lalu invoice berhasil disimpan di Database 

**3. Top Up Saldo**

- Input saldo dan data saldo
<img width="698" height="253" alt="Screenshot 2026-11-03 175031" src="https://github.com/user-attachments/assets/cc4ef106-a165-471f-8c88-eac4f39a7908" />

Saat user menginput angka 3 program akan menampilkan saldo awal, nominal topup (0 = batal), output "topup berhasil", dan saldo akhir setelah top up

**4. Keluar**
Ketika User menginput angka 4 program akan melakukan Log Out dan kembali ke menu utama

**Menu Utama**

<img width="199" height="117" alt="Screenshot 2026-11-03 161824" src="https://github.com/user-attachments/assets/61042d7e-5262-455b-a5d7-ab97ebbe39ac" />

-Login: Digunakan oleh pengguna yang sudah memiliki akun untuk masuk ke dalam sistem perpustakaan digital.

-Registrasi: Digunakan oleh pengguna baru untuk membuat akun agar dapat mengakses sistem.

-Keluar: Digunakan untuk mengakhiri atau menutup program.

Ketika pengguna memilih 1-3 maka akan lanjut ke menu selanjutnya berdasarkan penjelasan diatas.

