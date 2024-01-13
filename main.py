import tkinter as tk
from tkinter import ttk
from alice_window import AliceWindow
from bob_window import BobWindow
from claus_window import ClausWindow
from work_window import WorkWindow

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Основное окно")
        master.geometry("400x300")

        # Кнопка для открытия окон Alice, Bob, Claus и Work
        self.start_button = ttk.Button(master, text="Start", command=self.open_windows, style="Start.TButton")
        self.start_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # Добавление стилей
        ttk.Style().configure("Start.TButton", background="green", font=("Arial", 14))

    def open_windows(self):
        self.master.withdraw()

        # Создаем и открываем окна Alice, Bob, Claus и Work
        alice_window = AliceWindow(self.master, self)
        alice_window.show()

        bob_window = BobWindow(self.master, self)
        bob_window.show()

        claus_window = ClausWindow(self.master, self)
        claus_window.show()

        self.work_window = WorkWindow(self.master, self)
        self.work_window.show()
 
    def show_hello_message(self, name, message):
        # Метод для отображения сообщения от окна Alice, Bob, Claus или Work
        self.work_window.show_hello_message(name, message)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
