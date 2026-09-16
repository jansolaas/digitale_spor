"""
main.py – CTF AES-CBC Decryptor, for Digitale Spor
--------------------------------------------------
Kan brukes både som importert modul og direkte fra CLI.
Dekrypterer base64+gzip+AES-CBC fra input-streng (eks. fra GUI eller CLI).
"""
import base64
import gzip
import json
import string
import sys
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

EXAMPLE_INPUT = (
    "H4sIGDWKLmkA/2RhdGAuZW5jAGVnZ3tmb3J0c2V0dH0AFY5BagYxCIXvknUXGhNn0tsYn0I"
    "ppZtS+Cm9+5jFAx98+vnXYD/W3lunrZFBHGJdUmiJ94G19vSYFkbKc/CF21MtbsXAqVNWv5J"
    "40kKn2IARzgnI7jY6bNYaj/bWvr4RZfLtVT7jVbMlXFxZr+4GScgszb0WJRm4uI/fwhCBkx2"
    "WJ/XFxWrKJb1tof0/ADsDrMgAAAA="
)

def process_input(input_data):
    """
    Prøver å dekryptere base64/gzip/AES-CBC-data.
    Returnerer resultatstreng, eller feilmelding.
    """
    result_lines = []
    try:
        try:
            decoded = base64.b64decode(input_data.strip())
        except Exception:
            return (
                "❌ Kunne ikke dekode base64.\n"
                "Kontroller at input er riktig kopiert (uten linjeskift/mellomrom).\n"
            )
        try:
            decompressed = gzip.decompress(decoded)
        except Exception:
            return "❌ Kunne ikke pakke ut gzip – er input base64+gzip?\n"
        try:
            data = json.loads(decompressed)
        except Exception:
            return "❌ Kunne ikke trekke ut JSON fra gzip-dataen.\n"
        if not all(k in data for k in ("key", "iv", "data")):
            return "❌ Klarte å lese JSON, men mangler en eller flere nøkler ('key', 'iv', 'data').\n"
        result_lines.append("Dekryptert input data (base64/gzip) lastet som JSON:")
        result_lines.append(json.dumps(data, indent=2))
        result_lines.append("-" * 60)
        cipher_iv = bytes.fromhex(data["iv"])
        encrypted_text = bytes.fromhex(data["data"])
        HEX_CHARS = "0123456789abcdef"
        key_hex = data["key"]

        def try_decrypt(key_bytes):
            try:
                cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(cipher_iv),
                                backend=default_backend())
                decryptor = cipher.decryptor()
                decrypted = decryptor.update(encrypted_text) + decryptor.finalize()
            except Exception:
                return None
            pad_len = decrypted[-1]
            if not (1 <= pad_len <= 16):
                return None
            if decrypted[-pad_len:] != bytes([pad_len]) * pad_len:
                return None
            candidate = decrypted[:-pad_len]
            try:
                text = candidate.decode("utf-8")
            except UnicodeDecodeError:
                return None
            printable = sum(c in string.printable for c in text)
            if printable / max(len(text), 1) < 0.5:
                return None
            return text

        found = []
        for pos in range(len(key_hex) + 1):
            for ch in HEX_CHARS:
                candidate_hex = key_hex[:pos] + ch + key_hex[pos:]
                try:
                    key_bytes = bytes.fromhex(candidate_hex)
                except ValueError:
                    continue
                result = try_decrypt(key_bytes)
                if result:
                    found.append((candidate_hex, pos, ch, result))

        if found:
            for key, pos, ch, text in found:
                result_lines.append(f"Gyldig treff med enkelt-innsetting:'{ch}' på posisjon {pos}")
                result_lines.append(f"    Fullstendig nøkkel: {key}")
                result_lines.append(f"    Dekryptert melding:\n\n   {text}\n")
        else:
            result_lines.append("Ingen treff med enkelt-innsetting. "
                  "Nøkkelen kan mangle mer enn ett tegn, "
                  "eller være skadet på en annen måte.")
    except Exception as e:
        result_lines.append(f"❌ Uventet feil: {e}\n")
    return "\n".join(result_lines)

def main():
    parser = argparse.ArgumentParser(description="AES-CBC base64/gzip brute-force-dekryptering.")
    parser.add_argument(
        "--input", "-i", type=str, default=None,
        help="Base64+gzip-streng (helst på én linje)."
    )
    args = parser.parse_args()
    if args.input:
        inp = args.input
    else:
        print("Ingen input oppgitt – bruker eksempelinput.")
        inp = EXAMPLE_INPUT
    result = process_input(inp)
    print(result)

if __name__ == "__main__":
    main()