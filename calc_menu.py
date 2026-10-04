import tkinter as tk
# доделать калькулятор
def calcwin():
    calc_window = tk.Toplevel()
    calc_window.title("Калькулятор")
    calc_window.geometry("600x300")
    calc_window.resizable(False, False)

    chars = [
        ("seven", "7"), ("eight", "8"), ("nine", "9"), ("divide", "/"),
        ("four",  "4"), ("five",  "5"), ("six",  "6"), ("multiply", "*"),
        ("one",   "1"), ("two",   "2"), ("three","3"), ("minus", "-"),
        ("zero",  "0"), ("equals","="), ("clear","C"), ("plus", "+"),
    ]
    
    char_new = {}
    COLUMNS = 4

    result = tk.Label(calc_window, text="Тут появиться ответ", background="#FFCDD2")
    result.place(relx=1.0, rely=0.0, anchor="ne")
    for i, (key, text) in enumerate(chars):
        row = i // COLUMNS
        column = i % COLUMNS
        b = tk.Button(calc_window, text=text)
        b.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
        char_new[key] = b

    return calc_window