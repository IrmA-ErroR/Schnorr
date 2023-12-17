import tkinter as tk
from get_primes import PrimeGenerator
from get_secret import find_g, get_x, find_y

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Главное окно")
        self.master.geometry("500x450")  # Задаем размеры главного окна
        self.prime_generator = None  # Здесь будет объект PrimeGenerator
        self.p = None
        self.q = None
        self.used_gs = set()
        self.used_xs = set()
        self.prime_difference = 11

        tk.Button(self.master, text="Старт", font=("Arial", 16), command=self.generate_primes).pack(side=tk.TOP, pady=10)

    def generate_primes(self):
        num_digits = 5
        shift = 100

        self.prime_generator = PrimeGenerator(num_digits, shift)
        self.p, self.q = self.prime_generator.generate_prime(shift)

        self.display_primes()
        self.create_windows()

    def display_primes(self):
        # Очистка предыдущих значений
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Toplevel):
                self.update_window_content(widget)
            else:
                widget.destroy()

        # Отображение новых значений
        self.p_label = tk.Label(self.master, text=f"p = {self.p}", font=("Arial", 14))
        self.p_label.pack(anchor="nw", padx=20)

        self.q_label = tk.Label(self.master, text=f"q = {self.q}", font=("Arial", 14))
        self.q_label.pack(anchor="nw", padx=20)


    def create_windows(self):
        alice_window = self.create_window("Алиса", 101)
        bob_window = self.create_window("Боб", 202)
        claus_window = self.create_window("Клаус", 303)

        self.master.update()

    def create_window(self, title, prime_difference):
        window = tk.Toplevel(self.master)
        window.title(title)

        x = get_x(self.q, self.used_xs, id=prime_difference)
        g = find_g(self.q, self.p, prime_difference, self.used_gs)
        y = find_y(self.q, self.p, g)

        title_label = tk.Label(window, text=title, font=("Arial", 18, "bold"))
        title_label.pack()

        x_label_text = f"Закрытый ключ (x) = {x}"
        x_label = tk.Label(window, text=x_label_text, font=("Arial", 14))
        x_label.pack(anchor="nw", padx=20)

        g_label_text = f"g = {g}"
        g_label = tk.Label(window, text=g_label_text, font=("Arial", 14))
        g_label.pack(anchor="nw", padx=20)

        y_label_text = f"Открытый ключ (y) = {y}"
        y_label = tk.Label(window, text=y_label_text, font=("Arial", 14))
        y_label.pack(anchor="nw", padx=20)

        # Установка размеров окна
        window.geometry("500x400")

        tk.Button(window, text="Отправить открытый ключ", font=("Arial", 16), command=lambda: self.send_signature(window, title, y)).pack(side=tk.BOTTOM, pady=10)
        
        return window
    
    def send_signature(self, window, sender, signature):
        self.display_primes()

        sender_label = tk.Label(self.master, text=f"Отправитель: {sender}", font=("Arial", 14))
        sender_label.pack(anchor="nw", padx=20)

        signature_label_text = f"Открытый ключ отправителя (y) = {signature}"
        signature_label = tk.Label(self.master, text=signature_label_text, font=("Arial", 14))
        signature_label.pack(anchor="nw", padx=20)

        window.withdraw()

    def update_window_content(self, window):
        for widget in window.winfo_children():
            widget.destroy()

        title = window.title()
        prime_difference = 11  # Ваш код для получения prime_difference из title

        x = get_x(self.q, self.used_xs, id=prime_difference)
        g = find_g(self.q, self.p, prime_difference, self.used_gs)
        y = find_y(self.q, self.p, g)

        title_label = tk.Label(window, text=title, font=("Arial", 18, "bold"))
        title_label.pack()

        x_label_text = f"Закрытый ключ (x) = {x}"
        x_label = tk.Label(window, text=x_label_text, font=("Arial", 14))
        x_label.pack(anchor="nw", padx=20)

        g_label_text = f"g = {g}"
        g_label = tk.Label(window, text=g_label_text, font=("Arial", 14))
        g_label.pack(anchor="nw", padx=20)

        y_label_text = f"Открытый ключ (y) = {y}"
        y_label = tk.Label(window, text=y_label_text, font=("Arial", 14))
        y_label.pack(anchor="nw", padx=20)

        tk.Button(window, text="Отправить подпись", font=("Arial", 16), command=lambda: self.send_signature(window, title, y)).pack(side=tk.BOTTOM, pady=10)

    def send_signature(self, window, sender, signature):
        self.display_primes()

        info_label_text = f"Отправитель: {sender}, Открытый ключ (y): {signature}"
        info_label = tk.Label(self.master, text=info_label_text, font=("Arial", 14))
        info_label.pack(anchor="nw", padx=20)

        window.withdraw()  # Скрыть окно, но не закрывать

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
