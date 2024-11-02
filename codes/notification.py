# import time
from time import sleep
import tkinter as tk
from sys import exit
# import sys

def show_break_reminder():
    # Создаем главное окно
    root = tk.Tk()
    root.title("Напоминание")
    
    # Устанавливаем иконку
    root.iconbitmap("./../icons/present_ico.ico")  # Укажи путь к своему файлу .ico

    # Устанавливаем размер окна 310x120 пикселей
    root.geometry("310x120")
    
    # Основной цвет фона
    root.configure(bg="#800080")  # Фиолетовый

    # Создаем метку с текстом
    label = tk.Label(root, text="Пора сделать перерыв!", padx=20, pady=20, bg="#800080", fg="#ffffff", font=("Helvetica", 14, "bold"))
    label.pack()

    # Функция для выхода из программы
    def exit_program():
        root.destroy()  # Закрываем окно
        exit()      # Выходим из программы

    # Создаем фрейм для кнопок
    button_frame = tk.Frame(root, bg="#800080")
    button_frame.pack(pady=10)  # Отступ сверху и снизу

    # Создаем кнопку для выхода из программы
    exit_button = tk.Button(button_frame, text="Прервать программу", command=exit_program, padx=10, pady=5, bg="#DB26FF", fg="#ffffff", font=("Helvetica", 10))
    exit_button.pack(side=tk.LEFT, padx=5)  # Отступ слева

    # Создаем кнопку для закрытия окна
    close_button = tk.Button(button_frame, text="Перерыв был сделан", command=root.destroy, padx=10, pady=5, bg="#DB26FF", fg="#ffffff", font=("Helvetica", 10))
    close_button.pack(side=tk.LEFT, padx=5)  # Отступ справа

    # Центруем окно на экране
    root.eval('tk::PlaceWindow . center') 
    
    # Запускаем главный цикл
    root.mainloop()

def get_break_time():
    # Создаем окно для ввода времени
    input_window = tk.Tk()
    input_window.title("Установка времени")

    # Устанавливаем размер окна
    input_window.geometry("300x120")
    input_window.configure(bg="#800080")  # Фиолетовый фон

    # Переменная для хранения времени
    minutes = tk.IntVar(value=30)  # Устанавливаем значение по умолчанию на 30 минут

    def set_time():
        try:
            value = entry.get().replace(',', '.')
            value = float(value)
            if value >= 1:
                minutes.set(value)  # Устанавливаем значение
                input_window.destroy()  # Закрываем окно ввода
            else:
                error_label.config(text="Введите число больше единицы!")
        except ValueError:
            error_label.config(text="В это поле надо вводить число!")

    def on_closing():
        # Обработка закрытия окна
        input_window.destroy()
        exit()  # Выходим из программы

    def on_enter(event):
        set_time()  # Вызываем функцию установки времени при нажатии Enter

    # Привязываем обработчик к событию закрытия окна
    input_window.protocol("WM_DELETE_WINDOW", on_closing)

    # Создаем метку и поле ввода
    label = tk.Label(input_window, text="Интервал напоминания в минутах:", bg="#800080", fg="#ffffff", font=("Helvetica", 12))
    label.pack(pady=10)

    entry = tk.Entry(input_window)
    entry.insert(0, "30")  # Устанавливаем значение по умолчанию
    entry.pack()

    # Привязываем обработчик к событию нажатия клавиши
    entry.bind("<Return>", on_enter)  # Нажатие Enter

    error_label = tk.Label(input_window, text="", fg="red", bg="#800080")
    error_label.pack()

    # Создаем кнопку для подтверждения ввода
    submit_button = tk.Button(input_window, text="Установить", command=set_time, bg="#DB26FF", fg="#ffffff", font=("Helvetica", 10))
    submit_button.pack(pady=5)

    input_window.eval('tk::PlaceWindow . center')  # Центруем окно на экране

    input_window.mainloop()

    return minutes.get()  # Возвращаем введенное значение

if __name__ == '__main__':
    break_time = get_break_time()  # Запрашиваем время у пользователя
    while True:
        sleep(break_time * 60)  # Переводим минуты в секунды
        show_break_reminder()
