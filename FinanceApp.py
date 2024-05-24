from customtkinter import *
from tkinter import messagebox, filedialog, END
import matplotlib.pyplot as plt
import csv
import datetime
from MainFrame import MainFrame
from HistoryFrame import HistoryFrame
from ReminderFrame import ReminderFrame

class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Catatan Finansial Pribadi")

        self.balance = 0
        self.history = []
        self.reminders = []

        self.main_frame = MainFrame(self)
        self.history_frame = HistoryFrame(self)
        self.reminder_frame = ReminderFrame(self)

        self.show_main_frame()

    def show_main_frame(self):
        self.history_frame.frame.pack_forget()
        self.reminder_frame.frame.pack_forget()
        self.main_frame.frame.pack(fill="both", expand=True)
        self.main_frame.update_balance_label()

    def show_history_frame(self):
        self.main_frame.frame.pack_forget()
        self.reminder_frame.frame.pack_forget()
        self.history_frame.frame.pack(fill="both", expand=True)
        self.history_frame.update_history_listbox()

    def show_reminder_frame(self):
        self.main_frame.frame.pack_forget()
        self.history_frame.frame.pack_forget()
        self.reminder_frame.frame.pack(fill="both", expand=True)
        self.reminder_frame.update_reminder_listbox()

    def add_transaction(self, desc, amount, category, type_):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Jumlah harus lebih dari nol.")
            if category == "Pilih Kategori":
                raise ValueError("Pilih kategori yang valid.")
            if type_ == "Pemasukan":
                self.balance += amount
                self.history.append((desc, amount, category, type_))
            else:
                if amount > self.balance:
                    raise ValueError("Saldo tidak mencukupi.")
                self.balance -= amount
                self.history.append((desc, amount, category, type_))
            self.main_frame.update_balance_label()
            self.main_frame.clear_entries()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def add_reminder(self, desc, date):
        try:
            reminder_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            if reminder_date < datetime.datetime.now():
                raise ValueError("Tanggal harus di masa depan.")
            self.reminders.append((desc, reminder_date))
            self.reminder_frame.update_reminder_listbox()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def check_reminders(self):
        now = datetime.datetime.now()
        for desc, reminder_date in self.reminders:
            if reminder_date.date() == now.date():
                messagebox.showinfo("Pengingat", f"Hari ini adalah tanggal pengingat untuk: {desc}")

    def show_graph(self):
        categories = {}
        for desc, amount, category, type_ in self.history:
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

        fig, ax = plt.subplots()
        ax.bar(categories.keys(), categories.values())
        ax.set_xlabel('Kategori')
        ax.set_ylabel('Jumlah (Rp)')
        ax.set_title('Pemasukan dan Pengeluaran Berdasarkan Kategori')
        plt.show()

    def export_to_csv(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if filepath:
            with open(filepath, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Deskripsi", "Jumlah", "Kategori", "Tipe"])
                for desc, amount, category, type_ in self.history:
                    writer.writerow([desc, amount, category, type_])

# Entry point
if __name__ == "__main__":
    root = CTk()
    app = FinanceApp(root)
    root.mainloop()
