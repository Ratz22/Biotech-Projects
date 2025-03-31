import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# ------------------------- DNA to RNA Conversion Functions ------------------------- #
def dna_to_rna():
    """ Converts DNA to RNA by replacing 'T' with 'U'. """
    dna_seq = dna_entry.get("1.0", tk.END).strip().upper()
    rna_seq = dna_seq.replace("T", "U")
    rna_entry.delete("1.0", tk.END)
    rna_entry.insert("1.0", rna_seq)

def rna_to_dna():
    """ Converts RNA back to DNA by replacing 'U' with 'T'. """
    rna_seq = rna_entry.get("1.0", tk.END).strip().upper()
    dna_seq = rna_seq.replace("U", "T")
    dna_entry.delete("1.0", tk.END)
    dna_entry.insert("1.0", dna_seq)

def complementary_strand():
    """ Generates complementary DNA strand. """
    dna_seq = dna_entry.get("1.0", tk.END).strip().upper()
    comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
    comp_seq = "".join(comp.get(base, base) for base in dna_seq)
    comp_entry.delete("1.0", tk.END)
    comp_entry.insert("1.0", comp_seq)

def save_sequence():
    """ Saves DNA sequence to a file. """
    seq = dna_entry.get("1.0", tk.END).strip()
    if not seq:
        messagebox.showerror("Error", "No sequence to save!")
        return
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "w") as f:
            f.write(seq)
        messagebox.showinfo("Success", "Sequence saved successfully!")

def load_sequence():
    """ Loads a DNA sequence from a file. """
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "r") as f:
            dna_entry.delete("1.0", tk.END)
            dna_entry.insert("1.0", f.read())

# ------------------------- GUI DESIGN ------------------------- #
root = tk.Tk()
root.title("DNA to RNA Converter")
root.geometry("700x600")
root.config(bg="#1A1A2E")  # Futuristic Dark Mode Background

# ------------------------- Styling ------------------------- #
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=10, background="#00FFFF", foreground="black")

# Header Label
title_label = tk.Label(root, text="DNA to RNA Converter", font=("Orbitron", 24, "bold"), fg="#00FFFF", bg="#1A1A2E")
title_label.pack(pady=10)

# DNA Input
tk.Label(root, text="Enter DNA Sequence:", font=("Arial", 12, "bold"), fg="#39FF14", bg="#1A1A2E").pack()
dna_entry = tk.Text(root, height=3, width=60, font=("Consolas", 12), bg="#0D1B2A", fg="#00FFFF", insertbackground="#00FFFF")
dna_entry.pack(pady=5)

# RNA Output
tk.Label(root, text="Converted RNA Sequence:", font=("Arial", 12, "bold"), fg="#39FF14", bg="#1A1A2E").pack()
rna_entry = tk.Text(root, height=3, width=60, font=("Consolas", 12), bg="#0D1B2A", fg="#FF00FF", insertbackground="#FF00FF")
rna_entry.pack(pady=5)

# Complementary DNA
tk.Label(root, text="Complementary DNA Strand:", font=("Arial", 12, "bold"), fg="#39FF14", bg="#1A1A2E").pack()
comp_entry = tk.Text(root, height=3, width=60, font=("Consolas", 12), bg="#0D1B2A", fg="#FFAA00", insertbackground="#FFAA00")
comp_entry.pack(pady=5)

# Button Frame
button_frame = tk.Frame(root, bg="#1A1A2E")
button_frame.pack(pady=10)

# Stylish Buttons
btn_convert = ttk.Button(button_frame, text="Convert to RNA", command=dna_to_rna)
btn_convert.grid(row=0, column=0, padx=10)

btn_reverse = ttk.Button(button_frame, text="Reverse Transcription", command=rna_to_dna)
btn_reverse.grid(row=0, column=1, padx=10)

btn_complementary = ttk.Button(button_frame, text="Find Complement", command=complementary_strand)
btn_complementary.grid(row=0, column=2, padx=10)

btn_save = ttk.Button(button_frame, text="Save Sequence", command=save_sequence)
btn_save.grid(row=1, column=0, padx=10, pady=5)

btn_load = ttk.Button(button_frame, text="Load Sequence", command=load_sequence)
btn_load.grid(row=1, column=1, padx=10, pady=5)

# ------------------------- Hover Effect ------------------------- #
def on_enter(e):
    e.widget.config(background="#00FFFF", foreground="black")

def on_leave(e):
    e.widget.config(background="#1A1A2E", foreground="#00FFFF")

for btn in button_frame.winfo_children():
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Run the Tkinter app
root.mainloop()
