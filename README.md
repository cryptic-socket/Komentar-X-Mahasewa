Komentar-X-Mahasewa

Repositori ini mendokumentasikan proyek Data Mining dan Natural Language Processing (NLP) untuk melakukan ekstraksi, pembersihan data, pelabelan otomatis berbasis kamus, hingga pemodelan klasifikasi Machine Learning pada komentar platform X (Twitter) terkait isu mahasiswa.

Daftar Isi

Tentang Proyek

Arsitektur & Alur Kerja Pipeline

Struktur Direktori Repositori

Persiapan Lingkungan (Prerequisites)

Tata Cara Eksekusi Program (Step-by-Step)

Metodologi dan Pemodelan

Hasil Evaluasi dan Performa Model

Analisis dan Insight Data

Pengembangan Lanjutan

Tentang Proyek

Proyek ini dikembangkan untuk memenuhi tugas mata kuliah Data Mining. Fokus utamanya adalah menganalisis opini publik secara otomatis dari kolom komentar sebuah utas atau kiriman di X. Seluruh proses dari awal pengambilan data hingga evaluasi model klasifikasi dibangun menggunakan bahasa pemrograman Python dengan pendekatan modular.

Arsitektur & Alur Kerja Pipeline

Alur kerja pengolahan data dalam proyek ini terbagi menjadi lima tahapan utama:

Scraping Data: Mengambil data komentar mentah dari respons jaringan (GraphQL) menggunakan Playwright.

Data Cleaning (Preprocessing): Membersihkan teks dari tautan web, tag akun, tanda baca berlebih, dan baris kosong.

NLP Stopword Removal: Membuang kata hubung dan kata tidak penting menggunakan pustaka Sastrawi tanpa menerapkan stemming, guna mempertahankan konteks imbuhan asli kata (seperti kata dibayar).

Lexicon-Based Labeling: Memberikan label sentimen (Positif, Negatif, Netral) secara otomatis berdasarkan pencocokan kamus kata kunci yang disesuaikan dengan konteks sosial media.

Machine Learning Classification: Mengubah teks menjadi representasi vektor numerik menggunakan TF-IDF Vectorizer dan melatih model dengan algoritma Multinomial Naive Bayes.

Struktur Direktori Repositori

Berikut adalah penjelasan dari setiap berkas yang ada di dalam direktori proyek:

buat_sesi.py: Berkas utilitas untuk melakukan autentikasi awal dan menyimpan sesi login browser ke dalam state.json.

x_network_scraper.py: Skrip utama untuk melakukan ekstraksi komentar secara otomatis dari target tautan X.

preprocessing.py: Skrip untuk membersihkan teks mentah dari noise seperti URL dan karakter non-alfanumerik.

tahap2_nlp.py: Skrip pemrosesan lanjutan untuk penghapusan stopword tanpa merusak morfem kata.

pelabelan_lexicon.py: Skrip untuk memberikan label sentimen otomatis berdasarkan kamus leksikon yang diperluas.

model_klasifikasi.py: Skrip pelatihan model Naive Bayes, pengujian data, serta pencetakan laporan evaluasi.

state.json: Berkas penyimpanan token sesi login browser untuk menghindari login berulang.

dataset_komentar_x.csv: Hasil keluaran data mentah dari proses scraping.

dataset_bersih.csv: Hasil keluaran setelah melalui tahap pembersihan teks awal.

dataset_siap_AI_konteks.csv: Hasil keluaran setelah pemrosesan stopword NLP.

dataset_berlabel.csv: Dataset akhir yang telah memiliki kolom label sentimen.

Persiapan Lingkungan (Prerequisites)

Sebelum menjalankan program, pastikan komputer telah terpasang Python versi terbaru dan pustaka pendukung yang diperlukan. Jalankan perintah berikut di terminal:

pip install playwright pandas scikit-learn Sastrawi
playwright install


Tata Cara Eksekusi Program (Step-by-Step)

Ikuti urutan eksekusi skrip di bawah ini secara berurutan agar alur data berjalan dengan baik:

1. Inisialisasi Sesi Login

Jika berkas state.json belum tersedia di direktori, jalankan skrip berikut untuk masuk ke akun X secara manual:

python buat_sesi.py


2. Pengumpulan Data Komentar

Jalankan skrip penyadap jaringan untuk mengumpulkan komentar dari target kiriman:

python x_network_scraper.py


Berkas keluaran: dataset_komentar_x.csv

3. Pembersihan Data Awal

Bersihkan data mentah dari gangguan format teks:

python preprocessing.py


Berkas keluaran: dataset_bersih.csv

4. Pemrosesan NLP Tanpa Stemming

Lakukan penyaringan kata hubung dan kata gaul tanpa mengubah bentuk dasar kata:

python tahap2_nlp.py


Berkas keluaran: dataset_siap_AI_konteks.csv

5. Pelabelan Sentimen Otomatis

Terapkan pendekatan leksikon untuk mengkategorikan sentimen teks secara otomatis:

python pelabelan_lexicon.py


Berkas keluaran: dataset_berlabel.csv

6. Pelatihan dan Evaluasi Model Machine Learning

Latih model klasifikasi teks dan tampilkan matriks evaluasi performa:

python model_klasifikasi.py


Metodologi dan Pemodelan

Pembagian Data (Train-Test Split): Dataset dibagi dengan rasio 80% untuk pelatihan model (training set) dan 20% untuk pengujian model (testing set).

Ekstraksi Fitur: Menggunakan metode Term Frequency-Inverse Document Frequency (TF-IDF) untuk membobotkan kata-kata penting di dalam korpus teks.

Algoritma Klasifikasi: Menggunakan Multinomial Naive Bayes yang terbukti efektif dan efisien untuk pemodelan teks berdimensi tinggi.

Hasil Evaluasi dan Performa Model

Berdasarkan pengujian eksekusi program pada dataset komentar X:

Jumlah Data: Memproses sekitar 401 baris data komentar bersih.

Distribusi Label: Sebaran data didominasi oleh kategori Netral dan Negatif, mencerminkan karakteristik diskusi publik yang kritis.

Akurasi Model: Mencapai tingkat akurasi sebesar 65.43% pada data uji.

Metrik Performa: Berdasarkan laporan klasifikasi, kelas Netral memiliki recall yang sangat tinggi, sementara kelas Negatif memiliki tingkat precision yang handal dalam mendeteksi ujaran protes.

Analisis dan Insight Data

Dominasi Sentimen Kritis: Komentar di sekitar topik tersebut cenderung memuat ungkapan sinis atau protes terhadap isu yang dibahas, yang berhasil ditangkap dengan baik oleh model melalui kamus leksikon negatif.

Tantangan Sarkasme: Pendekatan berbasis leksikon harfiah memiliki keterbatasan dalam mengenali kalimat sindiran atau sarkasme implisit yang menggunakan kosa kata formal atau positif. Hal ini menjadi bahan evaluasi penting untuk pengembangan riset teks mining berikutnya.

Pengembangan Lanjutan

Beberapa poin pengembangan yang dapat dilakukan di masa mendatang meliputi:

Menambahkan teknik Deep Learning seperti LSTM atau Fine-tuning model bahasa pre-trained (BERT) untuk menangkap konteks semantik yang lebih dalam.

Memperluas kamus leksikon dengan slang lokal yang lebih komprehensif guna meningkatkan recall pada kelas negatif dan positif.
