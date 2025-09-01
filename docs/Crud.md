# API Endpoint Documentation

## Customer
| HTTP Method | URL Path          | Kegunaan                          | Request Body                                                                 | Expected Response                     | Butuh Auth |
|-------------|------------------|-----------------------------------|------------------------------------------------------------------------------|---------------------------------------|------------|
| GET         | /customers       | Mendapatkan daftar customer       | -                                                                            | Daftar customer dalam bentuk JSON     | Yes        |
| GET         | /customers/{id}  | Mendapatkan detail customer       | -                                                                            | Detail customer dalam bentuk JSON     | Yes        |
| POST        | /customers       | Menambahkan customer baru         | `{ "name": "John Doe", "phone": "0812...", "email": "john@mail.com" }`        | Customer berhasil dibuat (JSON)       | No         |
| PUT         | /customers/{id}  | Update data customer              | `{ "name": "John Doe", "phone": "0812...", "email": "john@mail.com" }`        | Customer berhasil diupdate (JSON)     | Yes        |
| DELETE      | /customers/{id}  | Hapus customer                    | -                                                                            | Pesan sukses (JSON)                   | Yes        |

---

## Meja
| HTTP Method | URL Path     | Kegunaan                     | Request Body                                                                 | Expected Response               | Butuh Auth |
|-------------|-------------|------------------------------|------------------------------------------------------------------------------|---------------------------------|------------|
| GET         | /meja       | Mendapatkan daftar meja      | -                                                                            | Daftar meja (JSON)              | Yes        |
| GET         | /meja/{id}  | Mendapatkan detail meja      | -                                                                            | Detail meja (JSON)              | Yes        |
| POST        | /meja       | Tambah meja baru             | `{ "table_number": 1, "capacity": 4, "location": "indoor", "status": "tersedia" }` | Meja berhasil dibuat (JSON)     | Yes        |
| PUT         | /meja/{id}  | Update data meja             | `{ "capacity": 6, "status": "tidak tersedia" }`                              | Meja berhasil diupdate (JSON)   | Yes        |
| DELETE      | /meja/{id}  | Hapus meja                   | -                                                                            | Pesan sukses (JSON)             | Yes        |

---

## Reservasi
| HTTP Method | URL Path           | Kegunaan                           | Request Body                                                                                          | Expected Response                    | Butuh Auth |
|-------------|-------------------|------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------|------------|
| GET         | /reservations     | Mendapatkan daftar reservasi       | -                                                                                                     | Daftar reservasi (JSON)              | Yes        |
| GET         | /reservations/{id}| Mendapatkan detail reservasi       | -                                                                                                     | Detail reservasi (JSON)              | Yes        |
| POST        | /reservations     | Membuat reservasi baru             | `{ "id_customer": 1, "id_table": 2, "reservation_time": "2025-09-01T19:00:00", "guest_count": 4 }`   | Reservasi berhasil dibuat (JSON)     | No         |
| PUT         | /reservations/{id}| Update reservasi                   | `{ "status": "Confirmed" }`                                                                           | Reservasi berhasil diupdate (JSON)   | Yes        |
| DELETE      | /reservations/{id}| Batalkan reservasi                 | -                                                                                                     | Pesan sukses (JSON)                  | Yes        |

---

## Staff
| HTTP Method | URL Path     | Kegunaan                     | Request Body                                                                 | Expected Response             | Butuh Auth |
|-------------|-------------|------------------------------|------------------------------------------------------------------------------|-------------------------------|------------|
| GET         | /staff      | Mendapatkan daftar staff     | -                                                                            | Daftar staff (JSON)           | Yes        |
| GET         | /staff/{id} | Mendapatkan detail staff     | -                                                                            | Detail staff (JSON)           | Yes        |
| POST        | /staff      | Tambah staff baru            | `{ "name": "Alice", "role": "waiter", "phone": "0812345678" }`               | Staff berhasil dibuat (JSON)  | Yes (Admin)|
| PUT         | /staff/{id} | Update data staff            | `{ "role": "manager" }`                                                      | Staff berhasil diupdate (JSON)| Yes        |
| DELETE      | /staff/{id} | Hapus staff                  | -                                                                            | Pesan sukses (JSON)           | Yes        |

---

## Payment
| HTTP Method | URL Path         | Kegunaan                        | Request Body                                                                 | Expected Response                   | Butuh Auth |
|-------------|-----------------|---------------------------------|------------------------------------------------------------------------------|-------------------------------------|------------|
| GET         | /payments       | Mendapatkan daftar pembayaran   | -                                                                            | Daftar pembayaran (JSON)            | Yes        |
| GET         | /payments/{id}  | Mendapatkan detail pembayaran   | -                                                                            | Detail pembayaran (JSON)            | Yes        |
| POST        | /payments       | Tambah pembayaran baru          | `{ "id_reservation": 1, "amount": 200000, "method": "cash" }`                | Payment berhasil dibuat (JSON)      | Yes        |
| PUT         | /payments/{id}  | Update status pembayaran        | `{ "status": "paid" }`                                                       | Payment berhasil diupdate (JSON)    | Yes        |
| DELETE      | /payments/{id}  | Hapus pembayaran                | -                                                                            | Pesan sukses (JSON)                 | Yes        |

---

## Feedback
| HTTP Method | URL Path       | Kegunaan                     | Request Body                                                                 | Expected Response                  | Butuh Auth |
|-------------|---------------|------------------------------|------------------------------------------------------------------------------|------------------------------------|------------|
| GET         | /feedback     | Mendapatkan daftar feedback  | -                                                                            | Daftar feedback (JSON)             | Yes        |
| GET         | /feedback/{id}| Mendapatkan detail feedback  | -                                                                            | Detail feedback (JSON)             | Yes        |
| POST        | /feedback     | Tambah feedback baru         | `{ "id_customer": 1, "id_reservation": 2, "rating": 5, "comment": "Mantap!" }` | Feedback berhasil dibuat (JSON) | No         |
| PUT         | /feedback/{id}| Update feedback              | `{ "rating": 4, "comment": "Bagus, tapi agak lama." }`                       | Feedback berhasil diupdate (JSON)  | Yes        |
| DELETE      | /feedback/{id}| Hapus feedback               | -                                                                            | Pesan sukses (JSON)                | Yes        |

---

## ReservationStaff (Junction Table)
| HTTP Method | URL Path                 | Kegunaan                            | Request Body                                      | Expected Response                      | Butuh Auth |
|-------------|-------------------------|-------------------------------------|---------------------------------------------------|----------------------------------------|------------|
| GET         | /reservation-staff      | Mendapatkan daftar assignment staff | -                                                 | Daftar relasi reservasi-staff (JSON)   | Yes        |
| POST        | /reservation-staff      | Assign staff ke reservasi           | `{ "id_reservation": 1, "id_staff": 2 }`          | Relasi berhasil dibuat (JSON)          | Yes        |
| DELETE      | /reservation-staff/{id} | Hapus assignment staff              | -                                                 | Relasi berhasil dihapus (JSON)         | Yes        |
