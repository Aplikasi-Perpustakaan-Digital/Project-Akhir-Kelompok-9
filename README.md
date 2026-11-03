# Aplikasi Perpustakaan Digital

Kelompok: 9 <br>
Nama Anggota:
1. Fiona Deandra Liani | 2609116053
2. Darrell Faiz Sinatria | 2609116055
3. Putrika Juliya Sari | 2609116057
4. Choni Yudhistira | 2609116074 <br>

-----------------------------------------------------------------------------------------------------------

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

<img width="1913" height="1042" alt="FLOWCHART PA KEL 9 final-Utama drawio" src="https://github.com/user-attachments/assets/18022a09-3b52-496d-926f-c1e6318146d6" />
<br>Deskripsi: Flowchart menu utama ini menggambarkan alur utama aplikasi perpustakaan digital, mulai dari login, registrasi, hingga keluar. Pengguna dapat membuat akun baru atau masuk menggunakan akun yang sudah ada. Setelah login, sistem membedakan antara akses admin dan user sesuai perannya.

## MENU ADMIN: 

<img width="2082" height="1377" alt="FLOWCHART PA KEL 9 final-Admin drawio" src="https://github.com/user-attachments/assets/5d72085b-aadd-473f-8c82-de7012181474" />
<br>Deskripsi: Flowchart menu admin ini menggambarkan proses CRUD (Create, Read, Update, Delete) pada sistem admin. Admin dapat menambah, melihat, mencari, mengubah, dan menghapus data yang tersimpan di file JSON. Setiap tindakan divalidasi dengan pengecekan ID, judul atau penulis dan menampilkan pesan keberhasilan atau kesalahan sesuai hasil proses.

## MENU USER:

<img width="2186" height="1227" alt="FLOWCHART PA KEL 9 final-User drawio" src="https://github.com/user-attachments/assets/9617a8eb-a0ed-4a77-b2de-5c7a5817524a" />
<br>Deskripsi: Flowchart menu user ini menjelaskan alur aktivitas pengguna dalam aplikasi perpustakaan digital, mulai dari melihat buku, meminjam buku dan melihat invoice, hingga top-up saldo. Setiap proses mencakup pengecekan data, validasi saldo ke file JSON. Setelah transaksi selesai, sistem menampilkan invoice atau saldo terbaru pengguna.

# Aplikasi Perpustakaan Digital Berdasarkan Role
---------------
## Menu Admin
** Login Sebagai admin  **

<img width="297" height="149" alt="Screenshot 2026-11-03 1532333" src="https://github.com/user-attachments/assets/c2620ecf-70d6-421f-9939-3529f817e8fa" />

<br>Program akan menampilkan beberapa pilihan setelah Admin memilih menu Login dan memasukkan datanya dengan benar dari menu utama Admin. Pada bagian ini, sistem menampilkan lima fitur utama yang berfungsi untuk mengelola data dari perpustakaan digital, yaitu:

- Tambah Buku –  Menambahkan data buku baru ke dalam database. 

- Lihat Buku –  Menampilkan daftar buku yang tersedia dalam sistem.

- Cari Buku – Mencari buku berdasarkan daftar buku yang tersedia di dalam sistem.

- Ubah Buku – Mengubah informasi buku yang sudah terdaftar.

- Hapus Buku – Menghapus buku dari sistem.
  
- Keluar - Mengembalikan pengguna ke menu Admin sebelumnya.

***1. Tambah Buku***
<br><img width="411" height="206" alt="Screenshot 2026-11-03 153357" src="https://github.com/user-attachments/assets/7a011f41-e230-4232-9c12-552f439c2acb" />

Program  ini menampilkan hasil dari pilihan menu yaitu “Tambah Buku”. Pada tahap ini, sistem menampilkan tabel berisi seluruh data buku yang tersimpan di database, dengan isi sebagai berikut:

- ID – Kode unik untuk setiap buku.
  
- Judul Buku – Nama buku yang tersedia di perpustakaan.
  
- Penulis – Nama dari penulis buku.

- Kategori – Jenis atau genre dari buku yang tersedia di perpustakaan.

- Stok – Jumlah buku yang tersedia perpustakaan.

*** 2. Lihat Buku ***

*** 3. Cari Buku ***

*** 4. Ubah Buku ***

*** 5. Hapus Buku ***

*** 6. Keluar ***

## Login Sebagai User

# Output Dan Penjelasan
- Menu Utama
<img width="188" height="104" alt="image" src="https://github.com/user-attachments/assets/684b2419-c6a5-4e6b-83af-2c1cdfaeb1cd" />

-Login: Digunakan oleh pengguna yang sudah memiliki akun untuk masuk ke dalam sistem perpustakaan digital.
-Registrasi: Digunakan oleh pengguna baru untuk membuat akun agar dapat mengakses sistem.
-Keluar: Digunakan untuk mengakhiri atau menutup program.
Ketika pengguna memilih 1-3 maka akan lanjut ke menu selanjutnya berdasarkan penjelasan diatas.


