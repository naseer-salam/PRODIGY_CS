import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def encrypt_text():
    text = text_entry.get()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(text, shift, mode='encrypt')
    result_label.config(text=f"Encrypted Message: {encrypted_text}")

def decrypt_text():
    text = text_entry.get()
    shift = int(shift_entry.get())
    decrypted_text = caesar_cipher(text, shift, mode='decrypt')
    result_label.config(text=f"Decrypted Message: {decrypted_text}")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text").replace("Encrypted Message: ", "").replace("Decrypted Message: ", ""))
    messagebox.showinfo("Copied", "The result has been copied to the clipboard.")

def on_quit():
    root.quit()

# Setting up the GUI window
root = tk.Tk()
root.title("Caesar Cipher GUI")

# Adding a label for the text input
text_label = tk.Label(root, text="Enter text:")
text_label.pack()

# Adding an entry widget for the user to enter the text
text_entry = tk.Entry(root, width=50)
text_entry.pack()

# Adding a label for the shift input
shift_label = tk.Label(root, text="Enter shift value:")
shift_label.pack()

# Adding an entry widget for the user to enter the shift value
shift_entry = tk.Entry(root, width=10)
shift_entry.pack()

# Adding a button to trigger encryption
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

# Adding a button to trigger decryption
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

# Adding a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Adding a button to copy the result to the clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

# Adding a button to quit the application
quit_button = tk.Button(root, text="Quit", command=on_quit)
quit_button.pack()

# Running the main loop of the GUI
root.mainloop()

