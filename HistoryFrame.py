from customtkinter import *
from Page import Page
from tkinter import END

class HistoryFrame(Page):
    def __init__(self, app):
        super().__init__(app.root, app)

        self.filter_var = StringVar()
        self.filter_var.set("Semua Kategori")
        self.filter_menu = CTkComboBox(self.frame, values=["Semua Kategori", "Gaji", "Bonus", "Investasi", "Hiburan", "Makan", "Transportasi"], variable=self.filter_var, command=self.filter_history)
        self.filter_menu.pack(pady=10)

        self.history_listbox = CTkTextbox(self.frame, width=500, height=300)
        self.history_listbox.pack(padx=10, pady=10)

        back_button = CTkButton(self.frame, text="Kembali ke Menu Utama", command=self.app.show_main_frame)
        back_button.pack(pady=10)

    def update_history_listbox(self):
        self.history_listbox.delete("1.0", END)
        selected_category = self.filter_var.get()
        for desc, amount, category, type_ in self.app.history:
            if selected_category == "Semua Kategori" or category == selected_category:
                self.history_listbox.insert(END, f"{type_}: {desc} - Rp {amount:,} (Kategori: {category})\n")

    def filter_history(self, _=None):
        self.update_history_listbox()
