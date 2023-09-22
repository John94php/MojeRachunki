import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from ttkthemes import ThemedStyle


def change_theme(theme_name):
    style.set_theme(theme_name)
    root.update()


def on_theme_select():
    selected_theme = theme_var.get()
    change_theme(selected_theme)


def show_form():
    form_window = tk.Toplevel(root)
    form_window.title("Formularz")
    form_window.geometry("400x800")
    name_label = ttk.Label(form_window, text="Nazwa rachunku")
    name_input = ttk.Entry(form_window)
    name_label.pack(fill=tk.BOTH, pady=10)
    name_input.pack(fill=tk.BOTH,padx=10)


root = tk.Tk()
style = ThemedStyle(root)
theme_var = tk.StringVar()

style.set_theme("arc")
available_themes = style.theme_names()
theme_frame = ttk.LabelFrame(root, text="Wybierz motyw")
theme_frame.pack(padx=10, pady=10, fill="both")
canvas = tk.Canvas(theme_frame, height=6)
canvas.pack(side="left", fill="both", expand=True)
scrollbar = ttk.Scrollbar(theme_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")
for theme in available_themes:
    ttk.Radiobutton(
        theme_frame,
        text=theme,
        variable=theme_var,
        value=theme,
        command=on_theme_select,
    ).pack(anchor="w")
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

theme_var.set(available_themes[0])  # Domyślny motyw
menu = tk.Frame(root)
menu.pack(pady=10)

root.geometry("900x300")
root.title("Moje rachunki")
show_button = ttk.Button(menu, text="Dashboard")
add_button = ttk.Button(menu, text="Dodaj rachunek", command=lambda: show_form())
other_add_button = ttk.Button(menu, text="Inne wydatki")
show_button.pack(side=tk.LEFT, padx=5)
add_button.pack(side=tk.LEFT, padx=5)
other_add_button.pack(side=tk.LEFT, padx=5)
root.mainloop()

