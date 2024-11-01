from tkinter import *
from Initial_encryption import encrypt, decrypt
from Improved_encryption import encrypt_with_substitution, decrypt_with_substitution

func_encrypt = encrypt_with_substitution
func_decrypt = decrypt_with_substitution

def encrypt_text():
    text = input_text.get("1.0", END).strip()
    key = key_enc.get("1.0", END).strip()
    encrypted_text = func_encrypt(text, key)
    output_text.delete("1.0", END)
    output_text.insert(END, encrypted_text)

def decrypt_text():
    text = input_text_decrypt.get("1.0", END).strip()
    key = key_dec.get("1.0", END).strip()
    decrypted_text = func_decrypt(text, key)
    output_text_decrypt.delete("1.0", END)
    output_text_decrypt.insert(END, decrypted_text)


# Настройка окна
window = Tk()
window.iconbitmap("icon.ico")
window.title("Шифрование и дешифрование методом вертикальной перестановки")
window.geometry('800x400')
BG = "lightgray"
BGG = "white"

# Фрейм для шифрования
frame_encr = LabelFrame(window, text="Шифрование", bg=BG)
frame_encr.pack(side=LEFT, padx=10, pady=10, fill="both", expand=True)

# Поле для ввода текста для шифрования
label_text_encrypt = Label(frame_encr, text="Введите текст для шифрования", bg=BG)
label_text_encrypt.grid(row=0, column=0, padx=10, pady=5, sticky="w")

input_text = Text(frame_encr, height=5, width=40, wrap=WORD)
input_text.grid(row=1, column=0, padx=10, pady=5)

# Поле для ввода ключа для шифрования
label_key_enc = Label(frame_encr, text="Введите ключ", bg=BG)
label_key_enc.grid(row=2, column=0, padx=10, pady=5, sticky="w")

key_enc = Text(frame_encr, height=1, width=40, wrap=WORD)
key_enc.grid(row=3, column=0, padx=10, pady=5)

# Кнопка для шифрования
encrypt_button = Button(frame_encr, text="Зашифровать текст", bg=BGG, command=encrypt_text)
encrypt_button.grid(row=4, column=0, padx=10, pady=10)

# Поле для вывода результата шифрования
output_text = Text(frame_encr, height=5, width=40, wrap=WORD)
output_text.grid(row=6, column=0, padx=10, pady=5)

# Фрейм для дешифрования
frame_decr = LabelFrame(window, text="Дешифрование", bg=BG)
frame_decr.pack(side=LEFT, padx=10, pady=10, fill="both", expand=True)

label_text_decrypt = Label(frame_decr, text="Введите текст для дешифрования", bg=BG)
label_text_decrypt.grid(row=0, column=0, padx=10, pady=5, sticky="w")

input_text_decrypt = Text(frame_decr, height=5, width=40, wrap=WORD)
input_text_decrypt.grid(row=1, column=0, padx=10, pady=5)

# Поле для ввода ключа для дешифрования
label_key_dec = Label(frame_decr, text="Введите ключ", bg=BG)
label_key_dec.grid(row=2, column=0, padx=10, pady=5, sticky="w")

key_dec = Text(frame_decr, height=1, width=40, wrap=WORD)
key_dec.grid(row=3, column=0, padx=10, pady=5)

# Кнопка для дешифрования
decrypt_button = Button(frame_decr, text="Расшифровать текст", bg=BGG, command=decrypt_text)
decrypt_button.grid(row=4, column=0, padx=10, pady=10)

# Поле для вывода результата дешифрования
output_text_decrypt = Text(frame_decr, height=5, width=40, wrap=WORD)
output_text_decrypt.grid(row=6, column=0, padx=10, pady=5)


# Запуск основного цикла
window.mainloop()
