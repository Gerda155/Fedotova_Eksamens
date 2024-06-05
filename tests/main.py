import tkinter as tk

class StartScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python tests")
        self.geometry("500x250")

        self.start_button = tk.Button(self, text="Sākt", command=self.open_name_screen)
        self.start_button.place(relx=0.5, rely=0.4, anchor="center")

    def open_name_screen(self):
        self.withdraw()  # Скрыть окно
        name_screen = NameScreen(self)
        name_screen.deiconify()  # Показать окно


class NameScreen(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Python tests")
        self.geometry("500x250")

        self.name_label = tk.Label(self, text="Ievadi vārdu:")
        self.name_label.place(relx=0.3, rely=0.3)

        self.name_entry = tk.Entry(self)
        self.name_entry.place(relx=0.5, rely=0.3)

        self.submit_button = tk.Button(self, text="Sākt testu", command=self.open_question_screen)
        self.submit_button.place(relx=0.5, rely=0.6, anchor="center")

    def open_question_screen(self):
        name = self.name_entry.get()
        self.withdraw()
        question_screen = jautajums1(self.master, name)
        question_screen.deiconify()


class jautajums1(tk.Toplevel):
    def __init__(self, master, name):
        super().__init__(master)
        self.title("1. jautājums")
        self.geometry("500x250")

        self.name = name

        self.jautajums1 = tk.Label(self, text=f"Izvēlieties sadalīšanas operācijas.")
        self.atbilde1 = tk.Label(self, text=f"a) /      b) ||\n c) or       d) //")
        self.close_button = tk.Button(self, text="Close", command=self.close)
        self.atb1_entry = tk.Entry(self)

        self.jautajums1.place(relx=0.5, rely=0.5, anchor="center")
        self.atbilde1.place(relx=0.5, rely=0.5, anchor="center")
        self.close_button.place(relx=0.5, rely=0.5, anchor="center")
        self.atb1_entry.place(relx=0.5, rely=0.3)


if __name__ == "__main__":
    app = StartScreen()
    app.mainloop()