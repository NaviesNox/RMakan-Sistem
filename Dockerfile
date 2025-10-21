# Gunakan image dasar Python versi 3.11 yang ringan (slim)
FROM python:3.11-slim

# Atur direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt .

# Update package list, install dependency sistem yang dibutuhkan untuk build (misalnya libpq-dev untuk PostgreSQL)
# lalu hapus cache apt agar image lebih kecil
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Install semua package Python dari requirements.txt tanpa menyimpan cache pip
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode proyek ke dalam container
COPY . .

# Jalankan aplikasi FastAPI menggunakan Uvicorn pada port 8000 dan host 0.0.0.0
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
