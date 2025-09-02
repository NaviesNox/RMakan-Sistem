# API Endpoint Documentation
## Customer
| HTTP Method | URL Path          | Kegunaan                          | Request Body                                                                 | Expected Response                     | Butuh Auth |
|-------------|------------------|-----------------------------------|------------------------------------------------------------------------------|---------------------------------------|------------|
| GET         | /customers       | Mendapatkan daftar customer       | -                                                                            | `[{"id_customer": 1,"name": "John Doe","phone": "08123456789","email": "john@example.com","created_at": "2025-09-01T12:30:00Z"}`, `{"id_customer": 2,"name": "John Jones","phone": "08123456788","email": "johnj@example.com","created_at": "2025-09-01T12:31:00Z"}]`     | Yes        |
| GET         | /customers/{id}  | Mendapatkan detail customer       | -                                                                            | `[{"id_customer": 2,"name": "John Jones","phone": "08123456788","email": "johnj@example.com","created_at": "2025-09-01T12:31:00Z"}]`     | Yes        |
| POST        | /customers       | Menambahkan customer baru         | `[{ "name": "John Maine", "phone": "0812222113111", "email": "johnD@mail.com" }]`        | ```[{"id_customer": 3,"name": "John Maine","phone": "0812222113111","email": "johnM@example.com","created_at": "2025-09-01T12:32:00Z"}]```       | No         |
| PUT         | /customers/{id}  | Update data customer              | `[{ "nasme": "John Smith", "phone": "081298765432", "email": "john@mail.com" }]`        | `[{"id_customer": 1,"name": "John Smith","phone": "081298765432","email": "johnsmith@example.com","created_at": "2025-09-01T12:30:00Z"}]`    | Yes        |
| DELETE      | /customers/{id}  | Hapus customer                    | -                                                                            | `{"message": "Customer dengan id 1 berhasil"}`                  | Yes        |

---

## Meja
| HTTP Method | URL Path     | Kegunaan                     | Request Body                                                                 | Expected Response               | Butuh Auth |
|-------------|-------------|------------------------------|------------------------------------------------------------------------------|---------------------------------|------------|
| GET         | /meja       | Mendapatkan daftar meja      | -                                                                            | `[{"id": 1,"table_number": 1,"capacity": 4,"location": "indoor","status": "available"}, {"id": 2,"table_number": 2,"capacity": 4,"location": "indoor","status": "available"}, "id": 3,"table_number": 3, "capacity": 4,"location": "indoor","status": "available"]`       | Yes        |
| GET         | /meja/{id}  | Mendapatkan detail meja      | -                                                                            | `[{"id":1,"table_number": 1,"capacity": 4,"location": "indoor","status": "available"}]`             | Yes        |
| POST        | /meja       | Tambah meja baru             | `{ "table_number": 4, "capacity": 4, "location": "indoor", "status": "tersedia` | `[{"id": 4,"table_number": 5,"capacity": 4,"location": "indoor","status": "available"}]`   | Yes        |
| PUT         | /meja/{id}  | Update data meja             | `{"table_number": 1,"capacity": 4,"location": "vip","status": "tersedia"}`                              | ``{"id": 1,"table_number": 1,"capacity": 4,"location": "vip","status": "tersedia"}``  | Yes        |
| DELETE      | /meja/{id}  | Hapus meja                   | -                                                                            | `{"message": "Meja dengan id 1 berhasil dihapus"}`             | Yes        |

---

## Reservasi
| HTTP Method | URL Path           | Kegunaan                           | Request Body                                                                                          | Expected Response                    | Butuh Auth |
|-------------|-------------------|------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------|------------|
| GET         | /reservations     | Mendapatkan daftar reservasi       | -                                                                                                     | `[{"id": 1,"id_customer": 1,"id_table": 2,"reservation_time": "2025-09-05T19:00:00","guest_count": 4,"notes": "Ulang tahun, tolong siapkan kue","status": "Pending"}, {"id": 2,"id_customer": 2,"id_table": 3,"reservation_time": "2025-09-10T12:30:00","guest_count": 2,"notes": "Butuh meja dekat jendela","status": "Confirmed"}]`             | Yes        |
| GET         | /reservations/{id}| Mendapatkan detail reservasi       | -                                                                                                     | `{"id": 1,"id_customer": 1,"id_table": 2,"reservation_time": "2025-09-05T19:00:00","guest_count": 4,"notes": "Ulang tahun, tolong siapkan kue","status": "Pending"}`            | Yes        |
| POST        | /reservations     | Membuat reservasi baru             | `{"id_customer": 1, "id_table": 2, "reservation_time": "2025-09-05T19:00:00", "guest_count": 4,"notes": "Ulang tahun, tolong siapkan kue","status": "Pending"}`   | `{ "id": 1, "id_customer": 1, "id_table": 2, "reservation_time": "2025-09-05T19:00:00",  "guest_count": 4, "notes": "Ulang tahun, tolong siapkan kue","status": "Pending"}`    | No         |
| PUT         | /reservations/{id}| Update reservasi                   |  `{"id_customer": 1,"id_table": 2,"reservation_time": "2025-09-05T20:00:00","guest_count": 5,"notes": "Ulang tahun, tambahan 1 orang","status": "Confirmed"}`                                                                       | `{"id": 1, "id_customer": 1, "id_table": 2, "reservation_time": "2025-09-05T20:00:00","guest_count": 5, "notes": "Ulang tahun, tambahan 1 orang","status": "Confirmed"}`  | Yes        |
| DELETE      | /reservations/{id}| Batalkan reservasi                 | -                                 | ``{ "message": "Reservasi dengan id 1 berhasil dihapus}``               | Yes        |

---

## Staff
| HTTP Method | URL Path     | Kegunaan                     | Request Body                                                                 | Expected Response             | Butuh Auth |
|-------------|-------------|------------------------------|------------------------------------------------------------------------------|-------------------------------|------------|
| GET         | /staff      | Mendapatkan daftar staff     | -                                                                            | `[{"id": 1,"name": "Budi","role": "admin","phone": "08121234567"},{"id": 2, "name": "Siti","role": "manager","phone": "0822333444"},{"id": 3,"name": "Andi","role": "waiter","phone": "08123456789"}]` | Yes        |
| GET         | /staff/{id} | Mendapatkan detail staff     | -                                                    | `{ "id": 3, "name": "Andi", "role": "waiter", "phone": "08123456789}`        | Yes        |
| POST        | /staff      | Tambah staff baru            | `{ "name": "Andi", "role": "waiter","phone": "08123456789"}`               | `{ "id": 3, "name": "Andi", "role": "waiter", "phone": "08123456789"}`  | Yes (Admin)|
| PUT         | /staff/{id} | Update data staff            | `{ "name": "Andi Saputra", "role": "manager","phone": "08123456789"}` | `{"id": 3,"name": "Andi Saputra","role": "manager","phone": "08123456789"}`| Yes        |
| DELETE      | /staff/{id} | Hapus staff                  | -                                                                            | `{"message": "Staff dengan id 3 berhasil dihapus"}`
          | Yes        |

---

## Payment
| HTTP Method | URL Path         | Kegunaan                        | Request Body                                                                 | Expected Response                   | Butuh Auth |
|-------------|-----------------|---------------------------------|------------------------------------------------------------------------------|-------------------------------------|------------|
| GET         | /payments       | Mendapatkan daftar pembayaran   | -                                                                            | `[ { "id": 5, "id_reservation": 10, "amount": 250000, "method": "e-wallet", "status": "unpaid", "transaction_time": "2025-09-02T18:30:00"}, {"id": 6,"id_reservation": 11,"amount": 400000,"method": "cash","status": "paid","transaction_time": "2025-09-03T20:15:00"}]`            | Yes        |
| GET         | /payments/{id}  | Mendapatkan detail pembayaran   | -                     | `{"id": 5, "id_reservation": 10,"amount": 250000,"method": "e-wallet","status": "unpaid","transaction_time": "2025-09-02T18:30:00"}`          | Yes        |
| POST        | /payments       | Tambah pembayaran baru          | `{"id_reservation": 10,"amount": 250000,"method": "e-wallet","status": "unpaid","transaction_time": "2025-09-02T18:30:00"}`                | `{"id": 5, "id_reservation": 10, "amount": 250000,"method": "e-wallet", "status": "unpaid","transaction_time": "2025-09-02T18:30:00}`    | Yes        |
| PUT         | /payments/{id}  | Update status pembayaran        | `{"id_reservation": 10,"amount": 250000,"method": "e-wallet","status": "paid","transaction_time": "2025-09-02T18:35:00"}`                                                      | `{ "id": 5, "id_reservation": 10, "amount": 250000, "method": "e-wallet", "status": "paid", "transaction_time": "2025-09-02T18:35:00"}`    | Yes        |
| DELETE      | /payments/{id}  | Hapus pembayaran                | -                                                              | `{"message": "Payment dengan id 5 berhasil dihapus"}`              | Yes        |

---

## Feedback
| HTTP Method | URL Path       | Kegunaan                     | Request Body                                                                 | Expected Response                  | Butuh Auth |
|-------------|---------------|------------------------------|------------------------------------------------------------------------------|------------------------------------|------------|
| GET         | /feedback     | Mendapatkan daftar feedback  | -                                                                            | `[ { "id": 1, "id_customer": 3, "id_reservation": 8, "rating": 4,  "comment": "Makanannya enak tapi agak lama.", "created_at": "2025-09-01T19:20:00" }, { "id": 2, "id_customer": 5, "id_reservation": 10, "rating": 5, "comment": "Sangat puas dengan pelayanannya!", "created_at": "2025-09-02T12:00:00" }, { "id": 4, "id_customer": 7, "id_reservation": 12, "rating": 5, "comment": "Pelayanan sangat baik, makanan cepat keluar dan enak banget asli terutama nasgornya hehe.", "created_at": "2025-09-02T20:30:00" }]`   | Yes        |
| GET         | /feedback/{id}| Mendapatkan detail feedback  | -                                                                            | `{ "id": 4, "id_customer": 7, "id_reservation": 12, "rating": 5, "comment": "Pelayanan sangat baik, makanan cepat keluar dan enak banget asli terutama nasgornya hehe.", "created_at": "2025-09-02T20:30:00"}`            | Yes        |
| POST        | /feedback     | Tambah feedback baru         | `{ "id_customer": 7, "id_reservation": 12, "rating": 5, "comment": "Pelayanan sangat baik, makanan cepat keluar dan enak banget asli terutama nasgornya hehe.", "created_at": "2025-09-02T20:30:00}` | `{ "id": 4, "id_customer": 7, "id_reservation": 12, "rating": 5, "comment": "Pelayanan sangat baik, makanan cepat keluar dan enak banget asli terutama nasgornya hehe.", "created_at": "2025-09-02T20:30:00"}` | No         |
| PUT         | /feedback/{id}| Update feedback              | `{ "id_customer": 7, "id_reservation": 12, "rating": 4, "comment": "Pelayanan baik, tapi tempat agak ramai.","created_at": "2025-09-02T20:40:00"}` | `{"id": 4, "id_customer": 7, "id_reservation": 12,"rating": 4, "comment": "Pelayanan baik, tapi tempat agak ramai.", "created_at": "2025-09-02T20:40:00"}` | Yes        |
| DELETE      | /feedback/{id}| Hapus feedback               | -                                                                            | Pesan sukses (JSON)                | Yes        |

---

## ReservationStaff (Junction Table)
| HTTP Method | URL Path                 | Kegunaan                            | Request Body                     | Expected Response                      | Butuh Auth |
|-------------|-------------------------|-------------------------------------|-----------------------------------|----------------------------------------|------------|
| GET         | /reservation-staff/{id_reservation}      | Lihat semua staff di reservasi tertentu | -               | `{  "id_reservation": 12, "staff": [ {  "id_staff": 3,  "name": "Budi", "role": "waiter" }, { "id_staff": 5, "name": "Ani", "role": "manager" } ] }`  | Yes        |
| POST        | /reservation-staff      | Assign staff ke reservasi           | `{ "id_reservation": 12,"id_staff": 3}`        | `{ "message": "Staff assigned to reservation successfully", "reservation_staff": { "id_reservation": 12, "id_staff": 3}}`          | Yes        |
| DELETE      | /reservation-staff/{id} | Hapus staff dari reservasi             | `{ "id_reservation": 12, "id_staff": 3}`                     |`{ "message": "Staff removed from reservation", "id_reservation": 12, "id_staff": 3}`      | Yes        |

*styling/formating json dimarkdownd gimana dah (bertanya dengan nada kebingungan)