import pandas as pd

print("[-] Membaca dataset_siap_AI_konteks.csv...")
df = pd.read_csv("dataset_siap_AI_konteks.csv")

# Kamus Lexicon Diperluas (Berdasarkan konteks komentar X yang di-scrape)
kata_positif = [
    'bagus', 'keren', 'mantap', 'dukung', 'bela', 'setuju', 'semangat', 
    'hebat', 'pintar', 'cerdas', 'maju', 'pro', 'baik', 'bener', 'hidup',
    'wangi', 'bersih', 'asli', 'murni', 'pinter', 'sukses', 'jujur', 
    'membanggakan', 'harum', 'lancar','memajukan',""
]

kata_negatif = [
    'sewa', 'bayar', 'buzzer', 'tolol', 'bodoh', 'jelek', 'kampungan', 
    'dungu', 'goblok', 'anjing', 'jamet', 'miskin', 'hancur', 'palsu', 
    'bohong', 'gadungan', 'malu', 'aneh', 'sampah', 'gembel', 'kontol', 
    'bayaran', 'rusak', 'bego', 'miris', 'najis', 'dekil',
    'maharental', 'kumuh', 'plenger', 'jigong', 'boti', 'ngarang', 
    'pengkhianat', 'dongo', 'ajg', 'kntl', 'bajingan', 'penjilat', 
    'korup', 'bloon', 'preman', 'ngamen', 'pengamen', 'warkop', 
    'rental', 'pansos', 'kusam', 'burik', 'bau', 'buladig', 'zolim', 
    'cosplay', 'sandiwara', 'bodong', 'cepe', 'receh', 'nasi', 
    'mabok', 'miras', 'judol', 'beler', 'komuk', 'tua', 'bikin malu',
    'abal', 'abal-abal', 'pulu-pulu', 'dongo', 'sindikat', 'lucu', 'kocak','bayaran','gembel','sewaan',
    'taikk','anj','bngst','hell nawhh', 'biadapp','jamet','dekil','aneh', 'biadab','bahlul','pecandu judol dan miras',
    'taek','zolim','palsu','ngarang', 'penjahat','gak berpendidikan',''
]

def hitung_sentimen(text):
    text = str(text).lower()
    words = text.split()
    
    skor = 0
    for word in words:
        if word in kata_positif:
            skor += 1
        elif word in kata_negatif:
            skor -= 1
            
    # Penentuan label berdasarkan skor akhir
    if skor > 0:
        return 'Positif'
    elif skor < 0:
        return 'Negatif'
    else:
        return 'Netral'

# Eksekusi Pelabelan Otomatis
print("[-] Melakukan pelabelan otomatis (Lexicon-based)...")
df['Label'] = df['Komentar_Final_AI'].apply(hitung_sentimen)

# Tampilkan statistik hasil pelabelan
print("\n[+] Hasil Distribusi Label:")
print(df['Label'].value_counts())

# Simpan ke dataset baru yang siap masuk model ML
df.to_csv("dataset_berlabel.csv", index=False, encoding='utf-8')
print("\n[-] Selesai! Data berlabel disimpan ke dataset_berlabel.csv")