import pandas as pd
import re

# 1. Load dataset mentah
print("[-] Membaca dataset_komentar_x.csv...")
df = pd.read_csv("dataset_komentar_x.csv")

# 2. Filter Iklan (Data Mining Trick)
# Hanya ambil baris yang mengandung mention ke akun target
df = df[df['Komentar'].str.contains('@txtruangpodcast', case=False, na=False)]
print(f"[-] Setelah iklan dibuang, tersisa {len(df)} komentar organik.")

# 3. Fungsi Text Cleaning NLP
def clean_text(text):
    text = str(text)
    # Hapus URL/Link
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Hapus mention @username (termasuk @txtruangpodcast agar teks bersih)
    text = re.sub(r'@\w+', '', text)
    # Hapus hashtag
    text = re.sub(r'#\w+', '', text)
    # Case folding (ubah semua jadi huruf kecil)
    text = text.lower()
    # Hapus karakter non-alfanumerik (tanda baca, emoji, simbol aneh)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Hapus enter/newline dan spasi ganda
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# 4. Eksekusi Pembersihan
print("[-] Membersihkan karakter kotor, link, dan emoji...")
df['Komentar_Bersih'] = df['Komentar'].apply(clean_text)

# Hapus baris yang mungkin jadi kosong setelah dibersihkan
df = df[df['Komentar_Bersih'] != ""]

# 5. Simpan ke CSV baru
# Kita simpan kolom 'Komentar_Bersih' saja agar rapi
df_final = df[['Komentar_Bersih']]
df_final.to_csv("dataset_bersih.csv", index=False, encoding='utf-8')
print(f"[-] Selesai! Data bersih siap pakai berjumlah {len(df_final)} baris disimpan ke dataset_bersih.csv")