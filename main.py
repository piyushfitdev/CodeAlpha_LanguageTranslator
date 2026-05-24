import tkinter as tk
from tkinter import ttk, messagebox

from translator import translate_text
from speech import speak_text

# -------------------- MAIN WINDOW -------------------- #

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x500")
root.config(bg="#f2f2f2")

# -------------------- LANGUAGES -------------------- #

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-cn",
    "Russian": "ru",
    "Arabic": "ar"
}

# -------------------- FUNCTIONS -------------------- #

def perform_translation():
    input_data = input_text.get("1.0", tk.END).strip()

    if input_data == "":
        messagebox.showerror("Error", "Please enter some text")
        return

    source = languages[source_language.get()]
    target = languages[target_language.get()]

    translated = translate_text(input_data, source, target)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated)


def copy_text():
    translated = output_text.get("1.0", tk.END).strip()

    root.clipboard_clear()
    root.clipboard_append(translated)

    messagebox.showinfo("Copied", "Text copied!")

# -------------------- TITLE -------------------- #

title_label = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 20, "bold"),
    bg="#f2f2f2"
)

title_label.pack(pady=10)

# -------------------- INPUT -------------------- #

input_label = tk.Label(
    root,
    text="Enter Text:",
    font=("Arial", 12),
    bg="#f2f2f2"
)

input_label.pack()

input_text = tk.Text(root, height=6, width=70)
input_text.pack(pady=5)

# -------------------- LANGUAGE SELECTION -------------------- #

lang_frame = tk.Frame(root, bg="#f2f2f2")
lang_frame.pack(pady=10)

source_language = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    state="readonly"
)

source_language.grid(row=0, column=0, padx=20)
source_language.set("English")

target_language = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    state="readonly"
)

target_language.grid(row=0, column=1, padx=20)
target_language.set("Hindi")

# -------------------- BUTTON -------------------- #

translate_button = tk.Button(
    root,
    text="Translate",
    command=perform_translation
)

translate_button.pack(pady=10)

# -------------------- OUTPUT -------------------- #

output_text = tk.Text(root, height=6, width=70)
output_text.pack(pady=10)

# -------------------- EXTRA BUTTONS -------------------- #

button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack()

copy_button = tk.Button(
    button_frame,
    text="Copy",
    command=copy_text
)

copy_button.grid(row=0, column=0, padx=10)

speak_button = tk.Button(
    button_frame,
    text="Speak",
    command=lambda: speak_text(
        output_text.get("1.0", tk.END)
    )
)

speak_button.grid(row=0, column=1, padx=10)

# -------------------- RUN -------------------- #

root.mainloop()