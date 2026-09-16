"""
gui.py – Enkel Tkinter GUI for digitale spor CTF-dekryptering
-------------------------------------------------------------
Lar deg lime inn en base64+gzip-streng og kjøre process_input fra main.py.
"""
import tkinter as tk
from tkinter import scrolledtext, messagebox
import main

EXAMPLE_INPUT = (
    "H4sIGDWKLmkA/2RhdGAuZW5jAGVnZ3tmb3J0c2V0dH0AFY5BagYxCIXvknUXGhNn0tsYn0I"
    "ppZtS+Cm9+5jFAx98+vnXYD/W3lunrZFBHGJdUmiJ94G19vSYFkbKc/CF21MtbsXAqVNWv5J"
    "40kKn2IARzgnI7jY6bNYaj/bWvr4RZfLtVT7jVbMlXFxZr+4GScgszb0WJRm4uI/fwhCBkx2"
    "WJ/XFxWrKJb1tof0/ADsDrMgAAAA="
)

def paste_example():
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, EXAMPLE_INPUT)

def on_submit():
    input_str = input_text.get("1.0", tk.END).strip()
    if not input_str:
        messagebox.showwarning("Tomt felt!", "Lim inn base64+gzip-streng i feltet.")
        return
    try:
        result = main.process_input(input_str)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state=tk.DISABLED)
    except Exception as e:
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f'Feil: {e}')
        output_text.config(state=tk.DISABLED)
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Digitale Spor – CTF AES-CBC Decryptor")
root.geometry("770x500")

tk.Label(root, text="Base64+gzip-streng (lim inn eller bruk eksempel):", font=("Segoe UI", 10)).pack(anchor="w")
input_text = scrolledtext.ScrolledText(root, width=90, height=5, font=("Consolas", 10))
input_text.pack(padx=10, pady=2)

btn_frame = tk.Frame(root)
btn_frame.pack()
tk.Button(btn_frame, text="Submit", command=on_submit, width=18, bg="#6d4aff", fg="white").pack(side=tk.LEFT, padx=4, pady=4)
tk.Button(btn_frame, text="Lim inn eksempel", command=paste_example, width=15).pack(side=tk.LEFT, padx=4)

tk.Label(root, text="Output:", font=("Segoe UI", 10)).pack(anchor="w")
output_text = scrolledtext.ScrolledText(root, width=90, height=18, font=("Consolas", 10), state=tk.DISABLED)
output_text.pack(padx=10, pady=2)

root.mainloop()