# SecureTaskApp

SecureTaskApp adalah aplikasi manajemen tugas sederhana berbasis Python yang berjalan melalui terminal (CLI).

## Fitur
- Menambahkan tugas.
- Menampilkan daftar tugas.
- Menandai tugas sebagai selesai.
- Menghapus tugas.
- Memvalidasi judul tugas agar tidak kosong.

## Teknologi
- Python
- pytest untuk unit testing
- Bandit untuk Static Application Security Testing (SAST)
- GitHub Actions untuk otomatisasi CI/CD

## Struktur Proyek
- `app/`: kode sumber aplikasi.
- `tests/`: unit test aplikasi.
- `.github/workflows/devsecops.yml`: konfigurasi pipeline DevSecOps.
- `requirements.txt`: daftar dependensi Python.

## Cara Menjalankan
Pastikan Python sudah terpasang. Jalankan perintah berikut dari direktori proyek:

```bash
python -m pip install -r requirements.txt
python -m app.main
```

## Menjalankan Unit Test
```bash
python -m pytest -v
```

## Menjalankan SAST
```bash
python -m bandit -r app -ll
```

## CI/CD Pipeline
GitHub Actions menjalankan pipeline ketika terjadi push ke branch `main` atau pull request menuju branch `main`.

Pipeline terdiri dari dua job:
1. `build`: memasang dependensi dan menjalankan unit test.
2. `sast-scan`: menjalankan pemindaian keamanan Bandit setelah job `build` berhasil.

Pemindaian menggunakan `bandit -ll` sebagai quality gate untuk temuan dengan tingkat keparahan medium dan high.
