import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

 
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected!"

    return ''.join(random.choice(characters) for _ in range(length))


def run_gui_mode():
    def on_generate():
        try:
            length = int(length_entry.get())
            use_letters = var_letters.get()
            use_numbers = var_numbers.get()
            use_symbols = var_symbols.get()

            password = generate_password(length, use_letters, use_numbers, use_symbols)
            if password.startswith("Error"):
                messagebox.showerror("Error", password)
            else:
                password_entry.delete(0, tk.END)
                password_entry.insert(0, password)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid length.")

    def copy_password():
        password = password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showwarning("Warning", "No password to copy.")

 
    root = tk.Tk()
    root.title("🎯 Password Generator")
    root.geometry("420x350")
    root.config(bg="#1e1e2f")  # Dark background
    root.resizable(False, False)

    title = tk.Label(root, text="🔐 Secure Password Generator", bg="#1e1e2f", fg="#00d2ff",
                     font=("Helvetica", 16, "bold"))
    title.pack(pady=10)

    tk.Label(root, text="Password Length:", bg="#1e1e2f", fg="white", font=("Helvetica", 12)).pack(pady=5)
    length_entry = tk.Entry(root, width=10, justify='center', font=("Helvetica", 12))
    length_entry.pack()

    global var_letters, var_numbers, var_symbols
    var_letters = tk.BooleanVar(value=True)
    var_numbers = tk.BooleanVar(value=True)
    var_symbols = tk.BooleanVar(value=True)

    tk.Checkbutton(root, text="Include Letters", variable=var_letters, bg="#1e1e2f", fg="white",
                   selectcolor="#1e1e2f", font=("Helvetica", 11)).pack(anchor='w', padx=30)
    tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, bg="#1e1e2f", fg="white",
                   selectcolor="#1e1e2f", font=("Helvetica", 11)).pack(anchor='w', padx=30)
    tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, bg="#1e1e2f", fg="white",
                   selectcolor="#1e1e2f", font=("Helvetica", 11)).pack(anchor='w', padx=30)

    tk.Button(root, text="✨ Generate Password", command=on_generate,
              bg="#00d2ff", fg="black", font=("Helvetica", 12, "bold"), width=20).pack(pady=10)

    global password_entry
    password_entry = tk.Entry(root, width=30, font=("Courier", 13), justify='center')
    password_entry.pack(pady=5)

    tk.Button(root, text="📋 Copy to Clipboard", command=copy_password,
              bg="#57e389", fg="black", font=("Helvetica", 12, "bold"), width=20).pack(pady=10)

    root.mainloop()


def run_cli_mode():
    print("\n--- CLI Password Generator ---")
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        result = generate_password(length, use_letters, use_numbers, use_symbols)
        print("Generated Password:", result)

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    print("Choose mode:\n1. CLI Mode\n2. GUI Mode")
    mode = input("Enter 1 or 2: ").strip()

    if mode == '1':
        run_cli_mode()
    elif mode == '2':
        run_gui_mode()
    else:
        print("Invalid choice. Please enter 1 or 2.")
