# eProcurement
Aplikasi eProcurement.
Terdapat dua jenis user , yaitu pembuat lelang pekerjaan dan peserta lelang pekerjaan.
1. Pembuat lelang pekerjaan membuat lelang pekerjaan
2. Peserta lelang pekerjaan melihat-lihat lelang pekerjaan yang tersedia, lalu mendaftar ke salah satu lelang pekerjaan
3. Pembuat lelang pekerjaan melihat daftar peserta lelang yang mendaftar ke lelang miliknya, lalu memilih satu pemenang.
4. Lelang berstatus "ditutup" apabila pemenang telah ditentukan

## Cara Menggunakan
Jalankan file eproc.py dengan command berikut

### Registrasi User Baru
reg *username* *password*

### Login
login *username* *password*
  
### Logout
logout

### Buat "Lelang Pekerjaan" Baru
create *nama pekerjaan*
  
### Lihat Daftar "Lelang Pekerjaan" Milik Saya
mylist

### Lihat Semua Daftar "Lelang Pekerjaan"
list

### Lihat Semua Daftar "Lelang Pekerjaan" yang Statusnya "Ditutup"
closedlist

### Lihat Detil "Lelang Pekerjaan:
getdetail *idtor*
untuk melihat idTOR , gunakan command "list"
  
### Pasang Proposal Keikutsertaan Pada Suatu "Lelang Pekerjaan"
join *idtor* *detil*
 
### Pilih Pemenang Lelang
choosewinner *id_peserta_lelang*
Untuk melihat id peserta lelang, gunakan command "getdetail *idtor*"
  
  
## TODO
Waktu "create" sama "join", perlu ada cara supaya user bisa input data yang lumayan terstruktur mengenai informasi lelang&proposalnya....

Perbaiki/tambah command-command yang kiranya perlu di eproc.py (?)

Buat webservice untuk command-command di eproc.py. 
Jadi, setiap command di eproc.py bisa diakses via REST
contoh
getdetail 23 -> host.com/getdetail/23

Buat aplikasi web... yang menggunakan webservice tadi...
