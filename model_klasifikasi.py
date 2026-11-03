import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Data
print("[-] Membaca dataset yang sudah dilabeli...")
# Pastikan kamu sudah menambahkan kolom 'Label' di file ini
df = pd.read_csv("dataset_berlabel.csv") 

# Hapus baris yang kosong (jaga-jaga ada error saat pelabelan)
df = df.dropna(subset=['Komentar_Final_AI', 'Label'])

# 2. Pisahkan Fitur (X) dan Target/Label (y)
X = df['Komentar_Final_AI']
y = df['Label']

# 3. Split Data Training & Testing (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"[-] Data dibagi: {len(X_train)} training, {len(X_test)} testing.")

# 4. Ekstraksi Fitur TF-IDF (Mengubah teks jadi matriks angka)
print("[-] Melakukan vektorisasi TF-IDF...")
tfidf = TfidfVectorizer()
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test) # Gunakan transform agar konsisten dengan data latih

# 5. Pelatihan Model (Training)
print("[-] Melatih model Naive Bayes...")
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# 6. Evaluasi dan Pengujian Model
print("[-] Melakukan prediksi pada data testing...")
y_pred = model.predict(X_test_tfidf)

akurasi = accuracy_score(y_test, y_pred)
print(f"\n[+] Akurasi Model: {akurasi * 100:.2f}%")
print("\n[+] Laporan Klasifikasi Lengkap:")
print(classification_report(y_test, y_pred))