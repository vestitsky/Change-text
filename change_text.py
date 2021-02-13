from tkinter import *

root = Tk()
root.geometry('800x500')
root.title('Преобразователь текста')
root_text = root.clipboard_get()
text_window = Text(root, font='Times, 14')
text_window.pack()


def change_text():
    root.clipboard_clear()
    text_get = text_window.get("1.0", END)
    root.clipboard_append(text_get)  # Сохранение в буфер обмена
    root.update()
def clear_text():
    text_window.delete("1.0", END)


Button(text='Преобразовать', command=change_text).pack()
Button(text='Очистить', command=clear_text).pack()
root.mainloop()
