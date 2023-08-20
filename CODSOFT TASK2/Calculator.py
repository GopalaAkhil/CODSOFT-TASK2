import tkinter as tk

def on_button_click(key):
    current = entry.get()
    if key == "C":
        entry.delete(0, tk.END)
    elif key == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, key)

root = tk.Tk()
root.title("Attractive Calculator")
#root.iconbitmap("calculator.ico")
root.geometry("300x400")
root.config(bg="#f7dc6f")  # Background color for the main window

entry = tk.Entry(root, font=("Helvetica", 20), bd=5, bg="#ffffff")  # White background
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

buttons_frame = tk.Frame(root, bg="#f7dc6f")
buttons_frame.pack()

button_list = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C",)
]

for row_index, row in enumerate(button_list):
    for col_index, key in enumerate(row):
        btn = tk.Button(buttons_frame, text=key, font=("Helvetica", 16, "bold"), bd=3, bg="#3498db", fg="#ffffff", padx=20, pady=20,
                        command=lambda key=key: on_button_click(key))
        btn.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")

# Configure grid to expand buttons equally
buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)
buttons_frame.grid_columnconfigure(2, weight=1)
buttons_frame.grid_columnconfigure(3, weight=1)

buttons_frame.grid_rowconfigure(0, weight=1)
buttons_frame.grid_rowconfigure(1, weight=1)
buttons_frame.grid_rowconfigure(2, weight=1)
buttons_frame.grid_rowconfigure(3, weight=1)
buttons_frame.grid_rowconfigure(4, weight=1)

root.mainloop()
