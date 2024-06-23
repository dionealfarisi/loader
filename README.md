# Loader Script

## Deskripsi
Loader Script adalah sebuah skrip Python yang menyediakan berbagai metode untuk menampilkan loading progress saat menjalankan suatu proses. Skrip ini berguna untuk memberikan feedback visual kepada pengguna saat proses yang memerlukan waktu sedang berlangsung, seperti saat membaca atau menulis data, pengolahan file, atau komputasi yang kompleks.

## Fitur
- Menyediakan berbagai metode loading progress, termasuk TQDM, ProgressBar2, Alive Progress, Rich, Halo, Progress, Click, dan Yaspin.
- Memungkinkan pengguna untuk memilih metode loading yang sesuai dengan preferensi atau kebutuhan mereka.
- Mudah digunakan dan diintegrasikan dalam skrip Python lainnya.
- Cocok untuk digunakan dalam berbagai jenis proyek, mulai dari proyek sederhana hingga proyek yang lebih kompleks.

## Cara Penggunaan
1. Pastikan Python sudah terinstal di sistem kamu.
2. Instal modul-modul yang diperlukan dengan menjalankan perintah berikut di terminal:
   ```bash
   chmod +x setup.sh
   ```
  Skrip setup.sh di rancang untuk melakukan penginstalan juga agar dapat di gunakan sepeti module pada umumnya.
   ```bash
   bash setup.sh
   ```
3. Jalankan skrip example dengan menjalankan perintah berikut di terminal:
   ```bash
   python example.py
   ```
4. Pilih metode loading yang ingin kamu gunakan dari daftar yang disediakan.
5. Amati progress loading yang ditampilkan sesuai dengan metode yang kamu pilih.

## Penggunaan Loader

Berikut adalah contoh penggunaan Loader dalam skrip Python:

```python
from Loader.load import Loader

loader_methods = ["tqdm", "progressbar2", "alive_progress", "rich", "halo", "progress", "click", "yaspin"]

for method in loader_methods:
    print(f"Running loader with method: {method}")
    loader = Loader(method=method, duration=0.05)
    loader.start()
    print()
```

1. **Impor Kelas Loader**: Pertama, kita mengimpor kelas `Loader` dari modul `Loader.load`. Kelas ini digunakan untuk menampilkan loading progress dengan berbagai metode.

2. **Definisikan Metode Loader**: Kemudian, kita mendefinisikan daftar `loader_methods` yang berisi berbagai metode loading progress yang ingin diuji. Metode yang dimasukkan ke dalam daftar ini adalah `tqdm`, `progressbar2`, `alive_progress`, `rich`, `halo`, `progress`, `click`, dan `yaspin`.

3. **Loop Melalui Metode Loader**: Selanjutnya, kita melakukan iterasi melalui daftar `loader_methods` dan menjalankan Loader dengan setiap metode. Pada setiap iterasi, kita mencetak pesan yang menunjukkan metode loader yang sedang dijalankan, membuat instance Loader dengan metode tersebut, dan memulai loader dengan menggunakan metode `start()`.

4. **Menambahkan Durasi Loader**: Ada juga parameter opsional `duration` yang diberikan pada setiap instance Loader. Parameter ini menentukan durasi (dalam detik) untuk menampilkan setiap iterasi loading. Dalam contoh tersebut, durasi ditetapkan sebagai `0.05` detik.

Dengan cara ini, skrip tersebut akan menjalankan Loader dengan berbagai metode yang disediakan oleh kelas `Loader` dan menampilkan loading progress untuk setiap metode tersebut. Ini memungkinkan untuk membandingkan berbagai metode dan memilih yang sesuai dengan kebutuhan spesifik kamu dalam proyek kamu.

## Kontribusi
Kontribusi dalam bentuk laporan bug, saran fitur, atau pull request sangat disambut. Untuk mengajukan kontribusi, silakan buka sebuah issue atau kirimkan pull request ke repositori ini.

## Lisensi
Skrip ini dilisensikan di bawah lisensi MIT. Silakan lihat [LICENSE](LICENSE) untuk informasi lebih lanjut.

---

Dalam contoh README di atas, kamu dapat menyesuaikan deskripsi, fitur, cara penggunaan, dan informasi lainnya sesuai dengan kebutuhan dan fitur yang ada dalam skrip loader kamu. Pastikan untuk menyertakan informasi lisensi yang sesuai jika kamu berencana untuk melepas skrip ini ke domain publik.
