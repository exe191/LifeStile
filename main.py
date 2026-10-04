import tkinter as tk
import bmi_menu
import calc_menu


def mainwin():
    window = tk.Tk()
    window.title("LIFESTATS")
    window.geometry("600x300")
    window.resizable(False, False)
    return window

window = mainwin()

def button():
    bth_bmi = tk.Button(window, text="BMI", command=lambda: bmi_menu.bmiwin())
    bth_bmi.place(x = 1, y = 1)
    bth_calc = tk.Button(window, text="Калькулятор", command=lambda: calc_menu.calcwin())
    bth_calc.place(x=55, y=1)

button()
window.mainloop()