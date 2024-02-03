
from googletrans import Translator
from tkinter import *
from tkinter import messagebox

def translate_function():
    if len(src_entry.get("1.0", "end-1c")) > 1:
        src_v = src_entry.get("1.0", "end-1c").lower()
        src_v = src_v.replace(" ", "")
    else:
        src_v = 'auto'  # Use 'auto' for automatic language detection

    if len(dest_entry.get("1.0", "end-1c")) > 1:
        dest_v = dest_entry.get("1.0", "end-1c").lower()
        dest_v = dest_v.replace(" ", "")
    else:
        dest_v = 'en'  # Use 'en' for English as the default target language

    if len(text_entry.get("1.0", "end-1c")) <= 1:
        messagebox.showerror(message="Enter valid text")
    else:
        text_v = text_entry.get("1.0", "end-1c")
        translated_text = translator_object.translate(text_v, src=src_v, dest=dest_v)
        messagebox.showinfo(message="TRANSLATED TEXT: " + translated_text.text)

def clear():
    dest_entry.delete("1.0", "end-1c")
    src_entry.delete("1.0", "end-1c")
    text_entry.delete("1.0", "end-1c")

window = Tk()
window.geometry("500x300")
window.title("Language Translator")

translator_object = Translator()

title_label = Label(window, text="Language Translator Using Python", font=("Gayathri", 12)).pack()

text_label = Label(window, text="Text to translate:").place(x=10, y=20)
text_entry = Text(window, width=40, height=5, font=("Ubuntu Mono", 12))
text_entry.place(x=130, y=20)

src_label = Label(window, text="Source language (empty: auto-detect):").place(x=10, y=120)
src_entry = Text(window, width=20, height=1, font=("Ubuntu Mono", 12))
src_entry.place(x=275, y=120)

dest_label = Label(window, text="Target language (empty: english-default):").place(x=10, y=150)
dest_entry = Text(window, width=20, height=1, font=("Ubuntu Mono", 12))
dest_entry.place(x=300, y=150)

button1 = Button(window, text='Translate', bg='Turquoise', command=translate_function).place(x=160, y=190)
button2 = Button(window, text='Clear', bg='Turquoise', command=clear).place(x=270, y=190)

window.mainloop()
