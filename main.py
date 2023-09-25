import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from ttkthemes import ThemedStyle
from tkcalendar import Calendar, DateEntry


def change_theme(theme_name):
    style.set_theme(theme_name)
    root.update()


def on_theme_select():
    selected_theme = theme_var.get()
    change_theme(selected_theme)


def save_form(name_label, name_input, date_label, date_input, desc_label, desc_input, price_label, price_input):
    form_data = {name_label.cget("text"): name_input.get(), date_label.cget("text"): date_input.get(),
                 desc_label.cget("text"): desc_input.get("1.0", "end-1c"), price_label.cget("text"): price_input.get()}

    print("Wartości z formularza:", form_data)

    pass


def show_form():
    form_window = tk.Toplevel(root)
    form_window.title("Formularz")
    form_window.geometry("400x800")
    name_label = ttk.Label(form_window, text="NAZWA")
    name_input = ttk.Entry(form_window)
    date_label = ttk.Label(form_window, text="DATA")
    date_input = DateEntry(form_window, background=style, bd=2)
    desc_label = ttk.Label(form_window, text="OPIS")
    desc_input = tk.Text(form_window)
    price_label = ttk.Label(form_window, text='SUMA')
    price_input = ttk.Entry(form_window)

    name_label.pack(fill=tk.BOTH, pady=10)
    name_input.pack(fill=tk.BOTH, padx=10)

    date_label.pack(fill=tk.BOTH, pady=10)
    date_input.pack(fill=tk.BOTH, padx=10)

    desc_label.pack(fill=tk.BOTH, padx=10)
    desc_input.pack(fill=tk.BOTH, padx=10)

    price_label.pack(fill=tk.BOTH, padx=10)
    price_input.pack(fill=tk.BOTH, padx=10)
    save_button = ttk.Button(form_window, text="Zapisz", command=lambda: save_form(name_label, name_input, date_label,
                                                                                   date_input, desc_label, desc_input,
                                                                                   price_label, price_input))
    save_button.pack(fill=tk.BOTH, padx=12, pady=5)


def change_theme_screen():
    change_theme_window = tk.Toplevel(root)
    change_theme_window.title("Zmień motyw")
    change_theme_window.geometry("400x800")
    theme_frame = ttk.LabelFrame(change_theme_window, text="Wybierz motyw")
    theme_frame.pack(padx=10, pady=10, fill="both")
    canvas = tk.Canvas(theme_frame, height=6)
    canvas.pack(side="top", fill="both", expand=True)
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


def exit_app():
    root.destroy()


root = tk.Tk()
style = ThemedStyle(root)
theme_var = tk.StringVar()

style.set_theme("arc")
available_themes = style.theme_names()

theme_var.set(available_themes[0])  # Domyślny motyw
menu = tk.Frame(root)
menu.pack(pady=10)

root.title("Moje rachunki")
root.geometry("700x100")
show_button = ttk.Button(menu, text="Dashboard")
add_button = ttk.Button(menu, text="Dodaj rachunek", command=lambda: show_form())
other_add_button = ttk.Button(menu, text="Inne wydatki")
change_theme_button = ttk.Button(menu, text="Zmień motyw", command=lambda: change_theme_screen())
exit_button = ttk.Button(menu, text="Zamknij aplikację", command=lambda: exit_app())
show_button.pack(side=tk.LEFT, padx=5)
add_button.pack(side=tk.LEFT, padx=5)
other_add_button.pack(side=tk.LEFT, padx=5)
change_theme_button.pack(side=tk.LEFT, padx=5)
exit_button.pack(side=tk.LEFT, padx=5)
root.mainloop()
