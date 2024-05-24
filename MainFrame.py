from customtkinter import *
from Page import Page
from tkinter import END

class MainFrame(Page):
    def __init__(self, app):
        super().__init__(app.root, app)

        self.balance_label = CTkLabel(self.frame, text=f"Saldo Saat Ini: Rp {self.app.balance:,}", font=("Helvetica", 32))
        self.balance_label.pack(pady=40, padx=40)

        form_frame = CTkFrame(self.frame)
        form_frame.pack(pady=10)

        CTkLabel(form_frame, text="Deskripsi").grid(row=0, column=0, padx=5, pady=5)
        CTkLabel(form_frame, text="Jumlah").grid(row=0, column=1, padx=5, pady=5)
        CTkLabel(form_frame, text="Kategori").grid(row=0, column=2, padx=5, pady=5)

        self.desc_entry = CTkEntry(form_frame, placeholder_text="Deskripsi")
        self.desc_entry.grid(row=1, column=0, padx=5, pady=5)

        self.amount_entry = CTkEntry(form_frame, placeholder_text="Jumlah")
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.category_var = StringVar()
        self.category_var.set("Pilih Kategori")
        self.category_menu = CTkComboBox(form_frame, values=["Gaji", "Bonus", "Investasi", "Hiburan", "Makan", "Transportasi"], variable=self.category_var)
        self.category_menu.grid(row=1, column=2, padx=5, pady=5)

        button_frame2 = CTkFrame(self.frame)
        button_frame2.pack(pady=10)

        self.add_income_button = CTkButton(button_frame2, text="Tambah Pemasukan", command=self.add_income)
        self.add_income_button.grid(row=0, column=0, padx=5, pady=5)

        self.add_expense_button = CTkButton(button_frame2, text="Tambah Pengeluaran", command=self.add_expense)
        self.add_expense_button.grid(row=0, column=1, padx=5, pady=5)

        button_frame = CTkFrame(self.frame)
        button_frame.pack(pady=10)

        self.history_button = CTkButton(button_frame, text="Lihat Riwayat", command=self.app.show_history_frame)
        self.history_button.grid(row=0, column=2, padx=5, pady=5)

        self.reminder_button = CTkButton(button_frame, text="Pengingat Pembayaran", command=self.app.show_reminder_frame)
        self.reminder_button.grid(row=0, column=3, padx=5, pady=5)

        self.export_button = CTkButton(button_frame, text="Ekspor CSV", command=self.app.export_to_csv)
        self.export_button.grid(row=0, column=4, padx=5, pady=5)

        self.show_graph_button = CTkButton(button_frame, text="Tampilkan Grafik", command=self.app.show_graph)
        self.show_graph_button.grid(row=0, column=5, padx=5, pady=5)

    def update_balance_label(self):
        self.balance_label.configure(text=f"Saldo Saat Ini: Rp {self.app.balance:,}")

    def add_income(self):
        self.app.add_transaction(self.desc_entry.get(), self.amount_entry.get(), self.category_var.get(), "Pemasukan")

    def add_expense(self):
        self.app.add_transaction(self.desc_entry.get(), self.amount_entry.get(), self.category_var.get(), "Pengeluaran")

    def clear_entries(self):
        self.desc_entry.delete(0, END)
        self.amount_entry.delete(0, END)
        self.category_var.set("Pilih Kategori")
