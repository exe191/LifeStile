import tkinter as tk


def bmiwin():
    bmi_window = tk.Toplevel()
    bmi_window.title("BMI - Индекс массы тела")
    bmi_window.geometry("600x300")
    bmi_window.resizable(False, False)
    
    fields = [
    ("name",   "Введите имя", str),
    ("height", "Введите рост (см)", float),
    ("weight", "Введите вес (кг)", float),
    ("age",    "Введите возраст", int),
]

    entries = {}
    types = {}
    for row, (key, text, t) in enumerate(fields):
        tk.Label(bmi_window, text=text).grid(row=row, column=0, sticky="w", padx=5, pady=5)
        e = tk.Entry(bmi_window)
        e.grid(row=row, column=1, padx=5, pady=5)
        entries[key] = e
        types[key] = t
    result = tk.Label(bmi_window, text="Тут появиться ответ", background="#FFCDD2")
    result.place(relx=1.0, rely=0.0, anchor="ne")

    def press():
        try:
            name = str(entries["name"].get())
            height = float(entries["height"].get()) / 100
            weight = float(entries["weight"].get())
            age = int(entries["age"].get())
            bmi = round(weight / (height ** 2), 2)
            result.config(text=f"Имя: {name} \nРост: {weight} \nВозраст: {age} \nBMI: {bmi}")
        except ValueError:
            result.config(text="Ошибка")

    bth = tk.Button(bmi_window, text="Посчитать", command=press)
    bth.place(relx=0.5, rely=0.5, anchor="center")
    return bmi_window, result