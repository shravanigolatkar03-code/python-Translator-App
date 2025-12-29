from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

translator = Translator()

language_names = {v.title(): k for k, v in LANGUAGES.items()}

def translate_text():
    try:
        src_lang = language_names[source_lang.get()]
        dest_lang = language_names[target_lang.get()]
        translated = translator.translate(
            input_text.get("1.0", END),
            src=src_lang,
            dest=dest_lang
        )
        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)
    except:
        output_text.delete("1.0", END)
        output_text.insert(END, "❌ Translation Failed")

def swap_languages():
    s = source_lang.get()
    t = target_lang.get()
    source_lang.set(t)
    target_lang.set(s)

BG_COLOR = "#dff5f5"
CARD_COLOR = "#f0fafa"
TEXT_COLOR = "#3a4f4f"
BUTTON_COLOR = "#5fb3b3"
INPUT_BG = "#ffffff"

root = Tk()
root.title("🌍 Universal Translator")
root.geometry("700x550")
root.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use("default")
style.configure(
    "TCombobox",
    fieldbackground=INPUT_BG,
    background=INPUT_BG,
    foreground=TEXT_COLOR
)

card = Frame(root, bg=CARD_COLOR)
card.place(relx=0.5, rely=0.5, anchor=CENTER, width=620, height=480)

Label(
    card,
    text="🌍 Universal Language Translator",
    font=("Segoe UI", 20, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(pady=20)

Label(
    card,
    text="Type Text",
    font=("Segoe UI", 12),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(anchor="w", padx=40)

input_text = Text(
    card,
    height=5,
    font=("Segoe UI", 12),
    wrap=WORD,
    bg=INPUT_BG,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    bd=1,
    relief=SOLID
)
input_text.pack(padx=40, pady=5, fill=X)

lang_frame = Frame(card, bg=CARD_COLOR)
lang_frame.pack(pady=15)

source_lang = StringVar(value="English")
target_lang = StringVar(value="Hindi")

ttk.Combobox(
    lang_frame,
    textvariable=source_lang,
    values=sorted(language_names.keys()),
    width=20,
    state="readonly"
).grid(row=0, column=0, padx=15)

Button(
    lang_frame,
    text="🔁",
    font=("Segoe UI", 14),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    bd=0,
    command=swap_languages,
    cursor="hand2"
).grid(row=0, column=1)

ttk.Combobox(
    lang_frame,
    textvariable=target_lang,
    values=sorted(language_names.keys()),
    width=20,
    state="readonly"
).grid(row=0, column=2, padx=15)

Button(
    card,
    text="🚀 TRANSLATE",
    font=("Segoe UI", 14, "bold"),
    bg=BUTTON_COLOR,
    fg="white",
    activebackground="#7ccfcf",
    bd=0,
    padx=40,
    pady=12,
    cursor="hand2",
    command=translate_text
).pack(pady=20)

Label(
    card,
    text="Translated Text",
    font=("Segoe UI", 12),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(anchor="w", padx=40)

output_text = Text(
    card,
    height=5,
    font=("Segoe UI", 12),
    wrap=WORD,
    bg=INPUT_BG,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    bd=1,
    relief=SOLID
)
output_text.pack(padx=40, pady=5, fill=X)

root.mainloop()
