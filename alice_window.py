import tkinter as tk
from tkinter import ttk, messagebox
import my_math

class AliceWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window

        self.alice_window = tk.Toplevel(master)
        self.alice_window.title("Окно Alice")
        self.alice_window.geometry("800x300")  # Увеличил ширину окна

        # Заголовок Алиса
        alice_label = tk.Label(self.alice_window, text="Алиса", font=("Arial", 16, "bold"))
        alice_label.grid(row=0, column=0, columnspan=3, pady=10)


        # Поле для открытого ключа
        open_key_label = tk.Label(self.alice_window, text="Открытый ключ:", font=("Arial", 14))
        open_key_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.open_key_entry = tk.Entry(self.alice_window, state=tk.DISABLED, font=("Arial", 14))
        self.open_key_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Поле для закрытого ключа
        private_key_label = tk.Label(self.alice_window, text="Закрытый ключ:", font=("Arial", 14))
        private_key_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.private_key_entry = tk.Entry(self.alice_window, state=tk.DISABLED, font=("Arial", 14))
        self.private_key_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # Кнопка в окне Alice
        self.hello_button = ttk.Button(self.alice_window, text="Генерация ключей", command=self.generate_keys, style="Blue.TButton")
        self.hello_button.grid(row=1, column=3, rowspan=2, padx=10, pady=5)

        # Добавление стилей
        ttk.Style().configure("Blue.TButton", background="blue", font=("Arial", 14))

    def generate_keys(self):
        try:
            with open("temp.txt", "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    p, q = map(int, last_line.split(":"))
                else:
                    raise ValueError("Файл temp.txt пуст")
        except (FileNotFoundError, ValueError) as e:
            messagebox.showerror("Ошибка", f"Значения p и q не сформированы")
            return

        # Здесь вызываем функции для генерации открытого и закрытого ключей
        
        private_key = self.generate_private_key(q)
        g, open_key = self.generate_open_key(private_key, p, q)

        # Заполняем соответствующие поля
        self.open_key_entry.config(state=tk.NORMAL)
        self.open_key_entry.delete(0, tk.END)
        self.open_key_entry.insert(0, open_key)
        self.open_key_entry.config(state=tk.DISABLED)

        self.private_key_entry.config(state=tk.NORMAL)
        self.private_key_entry.delete(0, tk.END)
        self.private_key_entry.insert(0, private_key)
        self.private_key_entry.config(state=tk.DISABLED)

        # Вывод информационного сообщения
        info_message = f"Ключи сгенерированы\np = {p}\nq = {q}\nx = {private_key}\ng = {g}\ny = {open_key}"
        messagebox.showinfo("Генерация ключей", info_message)

        # Отправка сообщения в основное окно
        self.main_window.show_hello_message("Alice", open_key)


    def generate_open_key(self, x, p, q):
        g = my_math.generate_g(p, q)
        while x == g:
            g = my_math.generate_g(p, q)
            # print(g, x)
        y = my_math.mod_inverse(pow(g, x, p), p)
        while y == g or y == x:
            y = my_math.mod_inverse(pow(g, x, p), p)
            # print(y, x, g)
        return g, y

    def generate_private_key(self, q):
        x = my_math.my_random(q)
        return x

    def show(self):
        self.alice_window.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    app = AliceWindow(root, None)  # Для тестирования отдельно окна Alice
    root.mainloop()
