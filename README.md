<div align="center">

# KOMENTAR-X-MAHASEWA
**Data Mining, Text Preprocessing, Lexicon-Based Labeling, and Naive Bayes Classification Pipeline**

</div>

---

## 1. Tentang Proyek
Repositori ini mendokumentasikan rangkaian proses *Data Mining* dan *Natural Language Processing* (NLP) untuk melakukan ekstraksi, pembersihan data, pelabelan otomatis berbasis kamus (*lexicon*), hingga pemodelan klasifikasi *Machine Learning* pada komentar platform X (Twitter) terkait isu mahasiswa. Proyek ini dirancang secara modular menggunakan Python.

---

## 2. Arsitektur & Alur Kerja Pipeline
Alur kerja pengolahan data dalam proyek ini terbagi menjadi lima tahapan sistematis:

1. **Scraping Data**: Mengambil data komentar mentah dari respons jaringan (*network interception* GraphQL) menggunakan Playwright.
2. **Data Cleaning (Preprocessing)**: Membersihkan teks dari tautan web, tag akun, tanda baca berlebih, dan baris kosong.
3. **NLP Stopword Removal**: Membuang kata hubung menggunakan pustaka Sastrawi tanpa menerapkan *stemming*, guna mempertahankan konteks imbuhan asli kata.
4. **Lexicon-Based Labeling**: Memberikan label sentimen (Positif, Negatif, Netral) secara otomatis berdasarkan pencocokan kamus kata kunci spesifik media sosial.
5. **Machine Learning Classification**: Mengubah teks menjadi representasi vektor numerik menggunakan TF-IDF Vectorizer dan melatih model dengan algoritma *Multinomial Naive Bayes*.

---

## 3. Struktur Direktori Repositori

| Berkas / Direktori | Deskripsi Fungsi |
| :--- | :--- |
| `buat_sesi.py` | Otomasi browser awal untuk menyimpan sesi *login* ke `state.json`. |
| `x_network_scraper.py` | Skrip utama penyadap jaringan untuk menarik komentar dari tautan X. |
| `preprocessing.py` | Skrip pembersihan awal teks dari *noise* dan karakter khusus. |
| `tahap2_nlp.py` | Skrip penghapusan *stopword* Sastrawi tanpa merusak morfem kata. |
| `pelabelan_lexicon.py` | Skrip pelabelan sentimen otomatis berdasarkan kamus leksikon. |
| `model_klasifikasi.py` | Pelatihan model *Naive Bayes*, pengujian data, dan pencetakan metrik. |
| `state.json` | Berkas autentikasi sesi peramban untuk mencegah *login* berulang. |
| `dataset_komentar_x.csv` | Berkas keluaran data mentah hasil *scraping*. |
| `dataset_bersih.csv` | Berkas keluaran setelah melalui pembersihan teks awal. |
| `dataset_siap_AI_konteks.csv` | Berkas keluaran setelah pemrosesan *stopword* NLP. |
| `dataset_berlabel.csv` | Dataset akhir yang telah memiliki kolom label sentimen. |

---

## 4. Persiapan Lingkungan (Prerequisites)
Pastikan Python telah terpasang di perangkat Anda. Jalankan perintah berikut di terminal untuk menginstal pustaka yang dibutuhkan:

```bash
pip install playwright pandas scikit-learn Sastrawi
playwright install
```

---

## 5. Tata Cara Eksekusi Program (Step-by-Step)
Jalankan urutan skrip di bawah ini secara berurutan melalui terminal pada direktori proyek:

### Langkah 1: Inisialisasi Sesi Login
```bash
python buat_sesi.py
```

### Langkah 2: Pengumpulan Data Komentar
```bash
python x_network_scraper.py
```
*Menghasilkan berkas `dataset_komentar_x.csv`*

### Langkah 3: Pembersihan Data Awal
```bash
python preprocessing.py
```
*Menghasilkan berkas `dataset_bersih.csv`*

### Langkah 4: Pemrosesan NLP Tanpa Stemming
```bash
python tahap2_nlp.py
```
*Menghasilkan berkas `dataset_siap_AI_konteks.csv`*

### Langkah 5: Pelabelan Sentimen Otomatis
```bash
python pelabelan_lexicon.py
```
*Menghasilkan berkas `dataset_berlabel.csv`*

### Langkah 6: Pelatihan dan Evaluasi Model
```bash
python model_klasifikasi.py
```

---

## 6. Metodologi dan Pemodelan
* **Train-Test Split**: Pembagian data menggunakan rasio 80% untuk pelatihan (*training*) dan 20% untuk pengujian (*testing*).
* **Ekstraksi Fitur**: Menggunakan pembobotan kata *Term Frequency-Inverse Document Frequency* (TF-IDF).
* **Algoritma Klasifikasi**: Menggunakan *Multinomial Naive Bayes* yang handal untuk klasifikasi teks berdimensi tinggi.

---

## 7. Hasil Evaluasi dan Performa Model
* **Jumlah Dataset**: Memproses sekitar 401 baris data komentar bersih setelah filter duplikasi.
* **Distribusi Label**: Sebaran data didominasi oleh kategori Netral dan Negatif, mencerminkan respons diskusi yang kritis.
* **Akurasi Model**: Model mencapai tingkat akurasi sebesar **65.43%** pada data uji.

---

## 8. Analisis dan Insight Data
1. **Dominasi Sentimen Kritis**: Komentar di sekitar topik tersebut memuat ungkapan protes atau sinis yang berhasil diidentifikasi oleh model melalui kamus leksikon negatif.
2. **Keterbatasan Leksikon**: Pendekatan berbasis kamus harfiah memiliki tantangan dalam mengenali kalimat sarkasme implisit, yang menjadi bahan evaluasi untuk riset lanjutan.
