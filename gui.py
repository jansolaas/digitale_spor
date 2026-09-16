# gui.py
import tkinter as tk
from tkinter import scrolledtext, messagebox
import main  # Import your processing function

def on_submit():
    input_str = input_text.get("1.0", tk.END).strip()
    try:
        result = main.process_input(input_str)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Input to main.py GUI")

tk.Label(root, text="Input string:").pack(anchor="w")
input_text = scrolledtext.ScrolledText(root, width=70, height=5)
input_text.pack(padx=10, pady=5)

tk.Button(root, text="Submit", command=on_submit).pack(pady=5)

tk.Label(root, text="Output:").pack(anchor="w")
output_text = scrolledtext.ScrolledText(root, width=70, height=15, state=tk.DISABLED)
output_text.pack(padx=10, pady=5)

root.mainloop()