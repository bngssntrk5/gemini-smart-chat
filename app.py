import os
import time
from dotenv import load_dotenv
from google import genai
from google.api_core import exceptions

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def solve_and_run():
    try:
        print("Sistemdeki aktif modeller taranıyor...")
        # Mevcut modelleri listele
        available_models = [m.name for m in client.models.list()]
        
        if not available_models:
            print("Hata: Hiç model bulunamadı. API anahtarını kontrol et!")
            return

        # Listede 'gemini-1.5-flash' içeren ilk modeli seç
        # Eğer yoksa listenin en başındaki modeli seç
        selected_model = next((m for m in available_models if "gemini-1.5-flash" in m), available_models[0])
        
        print(f"Uygun model bulundu: {selected_model}")
        print("İstek gönderiliyor...")

        response = client.models.generate_content(
            model=selected_model, 
            contents="Merhaba Bengisu! Teknik engelleri aştık, ilk mesajımız ulaştı."
        )
        
        print("\n--- BAŞARILI! ---")
        print(response.text)

    except exceptions.ResourceExhausted:
        print("\n[Hata] Kota doldu, 45 saniye bekleniyor...")
        time.sleep(45)
        solve_and_run()
    except Exception as e:
        print(f"\n[Kesin Hata]: {e}")

if __name__ == "__main__":
    if not api_key:
        print("Hata: .env dosyasında GEMINI_API_KEY bulunamadı!")
    else:
        solve_and_run()