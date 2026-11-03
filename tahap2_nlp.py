import pandas as pd
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# 1. Load data yang sudah bersih dari script sebelumnya
print("[-] Membaca dataset_bersih.csv...")
df = pd.read_csv("dataset_bersih.csv")

# 2. Inisialisasi Sastrawi
print("[-] Menyiapkan modul Stopword dan Stemming Sastrawi...")
stopword_factory = StopWordRemoverFactory()
stopword_remover = stopword_factory.create_stop_word_remover()

stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

# Daftar kata gaul/slang Twitter yang tidak berguna untuk AI tapi sering muncul
custom_stopwords = ['yg', 'aja', 'kalo', 'klo', 'udah', 'udh', 'sih', 'nih', 'tuh', 'nya', 'bgt', 'banget', 'sama', 'pas', 'dah', 'kan']

def proses_nlp(text):
    text = str(text)
    
    # A. Stopword Removal (Bawaan bahasa Indonesia baku)
    text = stopword_remover.remove(text)
    
    # B. Tokenisasi & Hapus Stopword Gaul
    tokens = text.split()
    tokens = [word for word in tokens if word not in custom_stopwords]
    
    # C. Stemming (Mengembalikan kata berimbuhan jadi kata dasar)
    text_gabung = " ".join(tokens)
    text_stemmed = stemmer.stem(text_gabung)
    
    return text_stemmed

# 3. Eksekusi NLP
# Catatan: Stemming Sastrawi memproses kata satu per satu dengan algoritma kompleks. 
# Untuk 400 data, proses ini mungkin akan memakan waktu 1 hingga 2 menit.
print("[-] Memulai proses NLP (Pemecahan kata & Stemming). Mohon tunggu sekitar 1-2 menit...")
df['Komentar_Final_AI'] = df['Komentar_Bersih'].apply(proses_nlp)

# Hapus baris yang mungkin jadi kosong setelah semua kata tidak pentingnya dibuang
df = df[df['Komentar_Final_AI'].str.strip() != ""]

# 4. Simpan hasil akhir
df.to_csv("dataset_siap_AI.csv", index=False, encoding='utf-8')
print(f"[-] SUKSES! {len(df)} data telah di-stemming dan disimpan ke dataset_siap_AI.csv")