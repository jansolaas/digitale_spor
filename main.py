import base64, gzip, json, string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


# print("--- Crypto-steg ---")

# --- Steg 1: Pakk ut JSON-en fra gzip/base64 ---
# input_data = "H4sIGDWKLmkA/2RhdGAuZW5jAGVnZ3tmb3J0c2V0dH0AFY5BagYxCIXvknUXGhNn0tsYn0IppZtS+Cm9+5jFAx98+vnXYD/W3lunrZFBHGJdUmiJ94G19vSYFkbKc/CF21MtbsXAqVNWv5J40kKn2IARzgnI7jY6bNYaj/bWvr4RZfLtVT7jVbMlXFxZr+4GScgszb0WJRm4uI/fwhCBkx2WJ/XFxWrKJb1tof0/ADsDrMgAAAA="


# ... existing code ...

def process_input(input_data):
    # Copy-paste everything from main.py that processes input_data
    # Collect result in a string, return it instead of printing

    decoded = base64.b64decode(input_data)
    decompressed = gzip.decompress(decoded)
    data = json.loads(decompressed)
    result_lines = []
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
    return "\n".join(result_lines)

# For command line operation:
if __name__ == "__main__":
    print("--- Crypto-steg ---")
    input_data = "H4sIGDWKLmkA/2RhdGAuZW5jAGVnZ3tmb3J0c2V0dH0AFY5BagYxCIXvknUXGhNn0tsYn0IppZtS+Cm9+5jFAx98+vnXYD/W3lunrZFBHGJdUmiJ94G19vSYFkbKc/CF21MtbsXAqVNWv5J40kKn2IARzgnI7jY6bNYaj/bWvr4RZfLtVT7jVbMlXFxZr+4GScgszb0WJRm4uI/fwhCBkx2WJ/XFxWrKJb1tof0/ADsDrMgAAAA="
    print(process_input(input_data))