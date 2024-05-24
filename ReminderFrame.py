from customtkinter import *
import datetime
from Page import Page
from tkinter import messagebox, END

class ReminderFrame(Page):
    def __init__(self, app):
        super().__init__(app.root, app)

        CTkLabel(self.frame, text="Deskripsi").grid(row=0, column=0, padx=5, pady=5)
        CTkLabel(self.frame, text="Tanggal (YYYY-MM-DD)").grid(row=0, column=1, padx=5, pady=5)

        self.desc_entry = CTkEntry(self.frame, placeholder_text="Deskripsi")
        self.desc_entry.grid(row=1, column=0, padx=5, pady=5)

        self.date_entry = CTkEntry(self.frame, placeholder_text="YYYY-MM-DD")
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        add_reminder_button = CTkButton(self.frame, text="Tambah Pengingat", command=self.add_reminder)
        add_reminder_button.grid(row=1, column=2, padx=5, pady=5)

        self.reminder_listbox = CTkTextbox(self.frame, width=500, height=300)
        self.reminder_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        back_button = CTkButton(self.frame, text="Kembali ke Menu Utama", command=self.app.show_main_frame)
        back_button.grid(row=3, column=0, columnspan=3, pady=10)

    def update_reminder_listbox(self):
        self.reminder_listbox.delete("1.0", END)
        for desc, date in self.app.reminders:
            self.reminder_listbox.insert(END, f"{desc} - {date.strftime('%Y-%m-%d')}\n")

    def add_reminder(self):
        self.app.add_reminder(self.desc_entry.get(), self.date_entry.get())
