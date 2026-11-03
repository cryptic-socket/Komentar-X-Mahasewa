from playwright.sync_api import sync_playwright
import pandas as pd
import time

# Target URL sesuai permintaan
TARGET_URL = "https://x.com/txtruangpodcast/status/2115707648137933260"

# Set untuk menyimpan komentar (menghindari duplikasi)
comments_set = set()

def extract_text_from_json(json_data):
    """
    Fungsi rekursif untuk mencari key 'full_text' di dalam JSON GraphQL X 
    yang strukturnya sangat dalam dan sering berubah.
    """
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == "full_text":
                # Filter agar tidak mengambil teks pendek yang bukan komentar
                if len(value) > 5 and value not in comments_set:
                    comments_set.add(value)
                    print(f"[+] Tertangkap: {value[:50]}...")
            else:
                extract_text_from_json(value)
    elif isinstance(json_data, list):
        for item in json_data:
            extract_text_from_json(item)

def handle_response(response):
    """Event listener yang akan terpicu setiap kali ada network response"""
    # Endpoint X untuk memuat komentar biasanya mengandung 'TweetDetail'
    if "TweetDetail" in response.url and response.request.method == "GET":
        try:
            # Ambil body JSON dari paket jaringan
            data = response.json()
            extract_text_from_json(data)
        except Exception:
            pass # Abaikan jika response gagal di-parse

def main():
    with sync_playwright() as p:
        # PERBAIKAN: Gunakan Chrome asli dan sembunyikan status bot
        browser = p.chromium.launch(
            headless=False,
            channel="chrome", 
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        # PERBAIKAN: Tambahkan pengabaian HTTPS error
        context = browser.new_context(
            storage_state="state.json",
            ignore_https_errors=True
        ) 
        page = context.new_page()

        # 1. Daftarkan event listener untuk network interception
        page.on("response", handle_response)

        # 2. Buka postingan target (Otomatis sudah login)
        print("[-] Membuka URL target...")
        
        # Tambahkan timeout panjang agar tidak error saat render awal
        page.goto(TARGET_URL, timeout=60000, wait_until="domcontentloaded")
        page.wait_for_timeout(5000) 

        # 3. Loop Scrolling untuk memicu lazy-loading
        print("[-] Memulai scrolling untuk intercept JSON...")
        for i in range(70):
            page.keyboard.press("End")
            page.wait_for_timeout(2500)
            
            if len(comments_set) >= 1100:
                print("[-] Target 1.1k komentar tercapai!")
                break

        # 4. Simpan dataset
        print(f"[-] Total komentar unik yang didapat: {len(comments_set)}")
        df = pd.DataFrame(list(comments_set), columns=['Komentar'])
        df.to_csv("dataset_komentar_x.csv", index=False, encoding='utf-8')
        print("[-] Dataset berhasil disimpan ke dataset_komentar_x.csv")

        browser.close()

if __name__ == "__main__":
    main()