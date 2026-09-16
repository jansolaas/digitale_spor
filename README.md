# CTF AES-CBC Decryptor – Digitale Spor

> ⚠️ **Merknad**: Dette prosjektet er utviklet av forfatteren under en søknadsprosess. Det er ikke offisielt knyttet til noen organisasjon og er kun ment for personlig bruk og verifisering av egne svar.

Et verktøy for å løse CTF/krypteringsoppgaver med AES-CBC

## 🚀 Installering

```bash
git clone <your-repo-url>
cd digitale_spor

# (valgfritt anbefalt) Opprett virtuelt miljø
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
pip install -r requirements.txt
```

## ✨ Bruk

### 🖥️ Start GUI

```bash
python gui.py
```
- Lim inn en base64+gzip-kodet streng i tekstfeltet og klikk "Submit".
- Dekryptert output vises nederst.

### ⚡ Kommandolinje

```bash
python main.py --input "<din_base64_gzip_input>"
```
eller
```bash
python main.py
```
(Bruker innebygget eksempel-input dersom du ikke oppgir --input)

### 📋 Eksempel-input (kan brukes i GUI eller CLI)
```
H4sIGDWKLmkA/2RhdGAuZW5jAGVnZ3tmb3J0c2V0dH0AFY5BagYxCIXvknUXGhNn0tsYn0IppZtS+Cm9+5jFAx98+vnXYD/W3lunrZFBHGJdUmiJ94G19vSYFkbKc/CF21MtbsXAqVNWv5J40kKn2IARzgnI7jY6bNYaj/bWvr4RZfLtVT7jVbMlXFxZr+4GScgszb0WJRm4uI/fwhCBkx2WJ/XFxWrKJb1tof0/ADsDrMgAAAA=
```

## 🛠️ Avhengigheter

Alle pakkene (bl.a. `cryptography`) installeres med:
```bash
pip install -r requirements.txt
```

Dersom du får feilmeldinger på cryptography under Windows, kan det hende du trenger [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

**Krav:** Python 3.8+

## 📮 Rekruttering og verifisering

Dette verktøyet er laget som en del av en søknadsprosess. 
Dersom rekrutteringsmiljøer ønsker å verifisere løsninger basert på oppgavedata, 
kan dette repoet tjene som dokumentasjon.

Spørsmål? Ta kontakt: jansolaas@pm.me

---

*Forfatter: Jan Solås – Pipeline Developer*
*Se flere prosjekter: https://github.com/jansolaas*
