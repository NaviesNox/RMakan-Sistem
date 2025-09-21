# Rmakan Sistem Analis
 ---
 * Berisikan document analisa dari sebuah sistem reservasi meja disebuah rumah makan, catatan ini dibuat dengan adanya bantuan AI, saya berusaha untuk memastikan bahwa ini setidaknya sudah dianggap "layak" untuk menjadi sebuah catatan.

 * Apabila ada sesuatu yang off/kurang benar atau tidak jelas maka itu pure dari saya, dan saya menerima bantuan dari semua orang yg melihat repo ini.


 # 12/09/2025
 * Ini belum pakai database jadi saya pake variable sementara untuk testing datanya masuk atau tidak, dan di docs sudah berfungsi.


 # 16/09/2025
 * tanpa Relasi kondisi CRUD
| Entitas | Keterangan    | Create | Read | Update | Delete |
|:--------|:--------------|:------:|:----:|:------:|:------:|
| Meja    | Tabel Meja    | Bisa   | Bisa | Bisa   |Bisa    |
| Staff   | Tabel Staff   | Bisa   | Bisa | Bisa   |Bisa    |
|Reservasi| Tabel reser   | -      | -    | -      |-       |
| payment | Tabel paymnt  | -      | -    | -      |-       |
| Feedback| Tabel fdback  | -      | -    | -      |-       |
| customer| Tabel custmer | -      | -    | -      |-       |

 # 17/09/2025
 * Sudah Relasi kondisi CRUD
| Entitas | Keterangan    | Create | Read | Update | Delete |
|:--------|:--------------|:------:|:----:|:------:|:------:|
| Meja    | Tabel Meja    | Bisa   | Bisa | Bisa   |Bisa    |
| Staff   | Tabel Staff   | Bisa   | Bisa | Bisa   |Bisa    |
|Reservasi| Tabel reser   | Bisa   | Bisa | Bisa   |Bisa    |
| payment | Tabel paymnt  | Bisa   | Bisa | Bisa   |Bisa    |
| Feedback| Tabel fdback  | Bisa   | Bisa | Bisa   | Bisa   |
| customer| Tabel custmer | Bisa   | Bisa | Bisa   | Bisa   |
