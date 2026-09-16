# CTF AES-CBC Decryptor – Digitale Spor

Et verktøy for å løse CTF/krypteringsoppgaver med AES-CBC, spesielt egnet for digitale spor-oppgaver som PST bruker i sine rekrutteringsprosesser.

## 🚀 Installering
bash git clone <your-repo-url> cd digitale_spor
# (valgfritt anbefalt) Opprett virtuelt miljø
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
pip install -r requirements.txt``` 

## ✨ Bruk

### 🖥️ Start GUI
```
- Lim inn en base64+gzip-kodet streng i tekstfeltet og klikk "Submit".
- Dekryptert output vises nederst.

### ⚡ Kommandolinje
bash python main.py --input "<din_base64_gzip_input>"``` 
eller
bash python main.py # bruker innebygget eksempel-input
```
``` 
### 📋 Eksempel-input (kan brukes i GUI eller CLI)
```
H4sIGDWKLmkA/2RhdGAuZW5jAGVnZ3tmb3J0c2V0dH0AFY5BagYxCIXvknUXGhNn0tsYn0IppZtS+Cm9+5jFAx98+vnXYD/W3lunrZFBHGJdUmiJ94G19vSYFkbKc/CF21MtbsXAqVNWv5J40kKn2IARzgnI7jY6bNYaj/bWvr4RZfLtVT7jVbMlXFxZr+4GScgszb0WJRm4uI/fwhCBkx2WJ/XFxWrKJb1tof0/ADsDrMgAAAA=

## 🛠️ Avhengigheter

Alle pakkene (bl.a. `cryptography`) installeres med:

pip install -r requirements.txt.

Dersom du får feilmeldinger på cryptography under Windows, kan det hende du trenger [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

**Krav:** Python 3.9+

## ℹ️ Om prosjektet

Dette repoet er laget for bruk i forbindelse med rekruttering og kompetansetesting i digitale spor. Fritt til intern bruk og testing! Ta gjerne kontakt for spørsmål og videreutvikling.

---
*Kontakt: jansolaas@pm.me*
```
