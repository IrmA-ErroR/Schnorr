import tkinter as tk
from tkinter import ttk, messagebox
import time

class WorkWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window

        self.work_window = tk.Toplevel(master)
        self.work_window.title("Work Window")
        self.work_window.geometry("800x300")

        # Имена и поля для каждого окна (Alice, Bob, Claus)
        self.names = ["Alice", "Bob", "Claus"]
        self.name_entries = {}

        # Заголовок Простые числа
        primes_label = tk.Label(self.work_window, text="Простые числа:", font=("Arial", 14, "bold"))
        primes_label.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.W)

        # Поле для p
        p_label = tk.Label(self.work_window, text="p:", font=("Arial", 14))
        p_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.p_entry = tk.Entry(self.work_window, font=("Arial", 14))
        self.p_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Поле для q
        q_label = tk.Label(self.work_window, text="q:", font=("Arial", 14))
        q_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.q_entry = tk.Entry(self.work_window, font=("Arial", 14))
        self.q_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # Разделитель
        ttk.Separator(self.work_window, orient=tk.HORIZONTAL).grid(row=3, columnspan=2, sticky="ew", pady=10)

        # Заголовок Открытые ключи
        keys_label = tk.Label(self.work_window, text="Открытые ключи:", font=("Arial", 14, "bold"))
        keys_label.grid(row=4, column=0, columnspan=2, pady=5, sticky=tk.W)

        for i, name in enumerate(self.names):
            # Метка с именем
            name_label = tk.Label(self.work_window, text=f"{name}:", font=("Arial", 14))
            name_label.grid(row=5+i, column=0, padx=10, pady=5, sticky=tk.W)

            # Поле для отображения приветствия
            self.name_entries[name] = tk.Entry(self.work_window, state=tk.DISABLED, font=("Arial", 14))
            self.name_entries[name].grid(row=5+i, column=1, padx=10, pady=5, sticky=tk.W)

        # Флаг для отслеживания заполненных полей
        self.all_fields_filled = False

        
        # Кнопка для генерации P и Q
        generate_button = ttk.Button(self.work_window, text="Генерация P и Q", command=self.generate_p_and_q, style="Blue.TButton")
        generate_button.place(relx=0.8, rely=0.2, anchor=tk.CENTER)

        # Кнопка Finish
        self.finish_button = ttk.Button(self.work_window, text="Finish", command=self.finish, style="Red.TButton")
        self.finish_button.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

        # Добавление стилей
        ttk.Style().configure("Blue.TButton", background="blue", font=("Arial", 14))
        ttk.Style().configure("Red.TButton", background="red", font=("Arial", 14))

    def generate_p_and_q(self):
        # Путь к файлам
        file_p_path = "p.txt"
        file_q_path = "q.txt"

        # Загрузка значений P и Q из файлов
        p_values = self.load_numbers_from_file(file_p_path)
        q_values = self.load_numbers_from_file(file_q_path)

        if not p_values and not q_values:
            return

        # Генерация случайного индекса
        num_index = self.generate_random_index(len(p_values))

        # Установка значений P и Q на экран
        self.q_entry.config(state=tk.NORMAL)
        self.q_entry.delete(0, tk.END)
        self.q_entry.insert(0, q_values[num_index])
        self.q_entry.config(state=tk.DISABLED)
        
        self.p_entry.config(state=tk.NORMAL)
        self.p_entry.delete(0, tk.END)
        self.p_entry.insert(0, p_values[num_index])
        self.p_entry.config(state=tk.DISABLED)

        # Запоминаем текущие значения p и q
        self.current_p = p_values[num_index]
        with open("temp.txt", "a") as file:
            file.write(f"{p_values[num_index]}:{q_values[num_index]}\n")

    def generate_random_index(self, max_value):
        seed = int(time.time())
        i = (seed % max_value)
        return i

    def load_numbers_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                numbers = [line.strip() for line in lines if line.strip().isdigit()]
                if not numbers:
                    messagebox.showerror("Ошибка", f"Файл {filename} не содержит корректных числовых значений")
                    return None
                return numbers
        except FileNotFoundError:
            messagebox.showerror("Ошибка", f"Файл {filename} не найден")
            return None

    def show_hello_message(self, name, message):
        # Метод для отображения сообщения от окна Alice, Bob или Claus
        self.name_entries[name].config(state=tk.NORMAL)
        self.name_entries[name].delete(0, tk.END)
        self.name_entries[name].insert(0, message)
        self.name_entries[name].config(state=tk.DISABLED)


    def show(self):
        self.work_window.deiconify()

    def finish(self):
        import os
        try:
            os.remove("temp.txt")
        except FileNotFoundError:
            pass
        # Метод для завершения работы программы
        self.work_window.destroy()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkWindow(root, None)  # Для тестирования отдельно окна Work Window
    root.mainloop()