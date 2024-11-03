import os
import sys
import time
from time import sleep
import tkinter as tk
from sys import exit

# Определяем путь к файлу иконки
if getattr(sys, 'frozen', False):
    # Если запущено из исполняемого файла
    ico = os.path.join(sys._MEIPASS, './present_ico-1.png') # замени на путь к файлу png 128*128 который отобразиться на панели задач
else:
    # Если запущено из исходного кода
    ico = './present_ico-1.png' # замени на путь к файлу png 128*128 который отобразиться на панели задач

def show_break_reminder():
    root = tk.Tk()
    root.title("Напоминание")
    root.iconphoto(False, tk.PhotoImage(file=ico))
    root.geometry("310x120")
    root.configure(bg="#800080")

    label = tk.Label(root, text="Пора сделать перерыв!", padx=20, pady=20, bg="#800080", fg="#ffffff", font=("Helvetica", 14, "bold"))
    label.pack()

    def exit_program():
        root.destroy()
        exit()

    button_frame = tk.Frame(root, bg="#800080")
    button_frame.pack(pady=10)

    exit_button = tk.Button(button_frame, text="Прервать программу", command=exit_program, padx=10, pady=5, bg="#DB26FF", fg="#ffffff", font=("Helvetica", 10))
    exit_button.pack(side=tk.LEFT, padx=5)

    close_button = tk.Button(button_frame, text="Перерыв был сделан", command=root.destroy, padx=10, pady=5, bg="#DB26FF", fg="#ffffff", font=("Helvetica", 10))
    close_button.pack(side=tk.LEFT, padx=5)

    root.eval('tk::PlaceWindow . center') 
    root.mainloop()

def get_break_time():
    input_window = tk.Tk()
    input_window.title("Установка времени")
    input_window.iconphoto(False, tk.PhotoImage(file=ico))
    input_window.geometry("300x120")
    input_window.configure(bg="#800080")

    minutes = tk.IntVar(value=30)

    def set_time():
        try:
            value = entry.get().replace(',', '.')
            value = float(value)
            if value >= 1:
                minutes.set(value)
                input_window.destroy()
            else:
                error_label.config(text="Введите число больше единицы!")
        except ValueError:
            error_label.config(text="В это поле надо вводить число!")

    def on_closing():
        input_window.destroy()
        exit()

    input_window.protocol("WM_DELETE_WINDOW", on_closing)

    label = tk.Label(input_window, text="Интервал напоминания в минутах:", bg="#800080", fg="#ffffff", font=("Helvetica", 12))
    label.pack(pady=10)

    entry = tk.Entry(input_window)
    entry.insert(0, "30")
    entry.pack()

    entry.bind("<Return>", lambda event: set_time())

    error_label = tk.Label(input_window, text="", fg="red", bg="#800080")
    error_label.pack()

    submit_button = tk.Button(input_window, text="Установить", command=set_time, bg="#DB26FF", fg="#ffffff", font=("Helvetica", 10))
    submit_button.pack(pady=5)

    input_window.eval('tk::PlaceWindow . center')

    input_window.mainloop()

    return minutes.get()

if __name__ == '__main__':
    break_time = get_break_time()
    while True:
        sleep(break_time * 60)
        show_break_reminder()
