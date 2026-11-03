from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        # Menggunakan Chrome asli agar aman dari deteksi bot
        browser = p.chromium.launch(
            headless=False, 
            channel="chrome", 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()

        print("[-] Membuka halaman login X...")
        page.goto("https://x.com/i/flow/login", timeout=60000, wait_until="domcontentloaded")
        
        # SCRIPT BERHENTI DI SINI DAN MENUNGGU
        print("[-] SILAKAN LOGIN MANUAL DI BROWSER YANG TERBUKA.")
        print("[-] Script akan menunggu sampai kamu berhasil masuk ke beranda X (waktu 2 menit)...")
        
        try:
            # Begitu URL berubah jadi beranda, script lanjut jalan
            page.wait_for_url("https://x.com/home", timeout=120000)
            print("[-] Beranda terdeteksi! Mengekstrak cookies...")
            
            # Simpan kondisi login ke file
            context.storage_state(path="state.json")
            print("[-] SUKSES! Sesi berhasil disimpan ke state.json.")
        
        except Exception as e:
            print("[-] Waktu habis (2 menit) atau kamu belum selesai login. Silakan ulangi.")

        browser.close()

if __name__ == "__main__":
    main()