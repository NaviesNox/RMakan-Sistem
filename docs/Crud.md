# 📑 API Spec Rumah Makan

| HTTP Method | URL Path | Kegunaan | Request Body | Expected Response | Butuh Auth |
|-------------|----------|----------|--------------|------------------|------------|
| **GET** | `/customers` | Mendapatkan daftar customer | - | Daftar customer dalam JSON | Yes |
| **POST** | `/customers` | Menambahkan customer baru | `{ "name":"John Doe", "phone":"08123", "email":"john@mail.com" }` | Data customer baru (JSON) | No |
| **GET** | `/customers/{id}` | Mendapatkan detail customer berdasarkan ID | - | Detail customer dalam JSON | Yes |
| **PUT** | `/customers/{id}` | Update data customer | `{ "name":"John Updated" }` | Data customer yang sudah diperbarui | Yes |
| **DELETE** | `/customers/{id}` | Hapus customer | - | Pesan sukses/hapus | Yes |

| **GET** | `/tables` | Mendapatkan daftar meja | - | Daftar meja (status, kapasitas, lokasi) | Yes |
| **POST** | `/tables` | Menambahkan meja baru | `{ "table_number":1, "capacity":4, "location":"indoor" }` | Data meja baru | Yes |

| **GET** | `/reservations` | Mendapatkan daftar reservasi | - | Daftar reservasi | Yes |
| **POST** | `/reservations` | Membuat reservasi baru | `{ "id_customer":1, "id_table":2, "reservation_time":"2025-09-01 18:00", "guest_count":4, "notes":"Ulang tahun" }` | Data reservasi baru | No |
| **PUT** | `/reservations/{id}` | Update status reservasi | `{ "status":"Confirmed" }` | Reservasi dengan status baru | Yes |
| **DELETE** | `/reservations/{id}` | Batalkan reservasi | - | Pesan berhasil batal | Yes |

| **GET** | `/staff` | Mendapatkan daftar staff | - | Daftar staff (nama, role, phone) | Yes |
| **POST** | `/staff` | Menambahkan staff baru | `{ "name":"Budi", "role":"waiter", "phone":"08123" }` | Data staff baru | Yes |

| **GET** | `/payments` | Mendapatkan daftar pembayaran | - | Daftar pembayaran | Yes |
| **POST** | `/payments` | Membuat pembayaran | `{ "id_reservation":1, "amount":200000, "method":"cash" }` | Data pembayaran baru | Yes |

| **GET** | `/feedback` | Mendapatkan daftar feedback | - | Daftar feedback (rating, comment) | Yes |
| **POST** | `/feedback` | Memberikan feedback untuk reservasi | `{ "id_customer":1, "id_reservation":2, "rating":5, "comment":"Mantap!" }` | Data feedback baru | No |

| **POST** | `/reservation-staff` | Menetapkan staff untuk reservasi | `{ "id_reservation":1, "id_staff":2 }` | Data assignment staff ke reservasi | Yes |
