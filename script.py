import string
import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class GUI():
    def __init__(self, master):
        self.master = master
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()

        root.title('Password Generator')
        root.geometry('600x300')
        root.configure(bg='#1F1F1F')  # Dark theme
        root.resizable(False, False)

        style = ttk.Style()
        style.configure("TLabel", foreground="#E0E0E0", background="#1F1F1F", font=("Segoe UI", 12))
        style.configure("TEntry", font=("Segoe UI", 12))
        style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=6)
        style.map("TButton", background=[("active", "#2E8B57")])

        # Title
        self.title_label = Label(text="Password Generator", font=("Segoe UI", 18, "bold"), bg="#1F1F1F", fg="#00CED1")
        self.title_label.pack(pady=(20, 10))

        # Password length
        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.pack()
        self.length_entry = ttk.Entry(root, textvariable=self.passwordlen, width=30)
        self.length_entry.pack(pady=5)

        # Generated Password
        self.generated_label = ttk.Label(root, text="Generated Password:")
        self.generated_label.pack()
        self.generated_entry = ttk.Entry(root, textvariable=self.generatedpassword, width=30, foreground="#DC143C")
        self.generated_entry.pack(pady=5)

        # Buttons
        self.button_frame = Frame(root, bg="#1F1F1F")
        self.button_frame.pack(pady=20)

        self.generate_btn = ttk.Button(self.button_frame, text="Generate Password", command=self.generate_pass)
        self.generate_btn.grid(row=0, column=0, padx=5)

        self.reset_btn = ttk.Button(self.button_frame, text="Reset", command=self.reset_fields)
        self.reset_btn.grid(row=0, column=1, padx=5)

    def generate_pass(self):
        upper = list(string.ascii_uppercase)
        lower = list(string.ascii_lowercase)
        chars = list("@#%&()\"?!")
        numbers = list(string.digits)

        try:
            length = int(self.passwordlen.get())
        except ValueError:
            messagebox.showerror("Error", "Password length must be a number.")
            return

        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long.")
            return

        u = random.randint(1, length - 3)
        l = random.randint(1, length - 2 - u)
        c = random.randint(1, length - 1 - u - l)
        n = length - u - l - c

        password = (
            random.sample(upper, u)
            + random.sample(lower, l)
            + random.sample(chars, c)
            + random.sample(numbers, n)
        )
        random.shuffle(password)
        gen_passwd = "".join(password)

        self.generated_entry.delete(0, END)
        self.generated_entry.insert(0, gen_passwd)

    def reset_fields(self):
        self.length_entry.delete(0, END)
        self.generated_entry.delete(0, END)

if __name__ == '__main__':
    root = Tk()
    pass_gen = GUI(root)
    root.mainloop()

