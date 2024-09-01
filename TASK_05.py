import json
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importing ttk for Notebook widget

FILENAME = "contacts.json"

class ContactManagementSystem:
    def __init__(self, root):
        self.root = root
        self.contacts = self.load_contacts()
        self.create_widgets()

    def load_contacts(self):
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        with open(FILENAME, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)  # Changed to ttk.Notebook
        self.notebook.pack(pady=10, expand=True)

        self.add_contact_frame = tk.Frame(self.notebook)
        self.view_contacts_frame = tk.Frame(self.notebook)
        self.search_contact_frame = tk.Frame(self.notebook)
        self.update_contact_frame = tk.Frame(self.notebook)
        self.delete_contact_frame = tk.Frame(self.notebook)

        self.notebook.add(self.add_contact_frame, text="Add Contact")
        self.notebook.add(self.view_contacts_frame, text="View Contacts")
        self.notebook.add(self.search_contact_frame, text="Search Contact")
        self.notebook.add(self.update_contact_frame, text="Update Contact")
        self.notebook.add(self.delete_contact_frame, text="Delete Contact")

        self.add_contact_widgets()
        self.view_contacts_widgets()
        self.search_contact_widgets()
        self.update_contact_widgets()
        self.delete_contact_widgets()

    def add_contact_widgets(self):
        tk.Label(self.add_contact_frame, text="Name:").grid(row=0, column=0)
        tk.Label(self.add_contact_frame, text="Phone:").grid(row=1, column=0)
        tk.Label(self.add_contact_frame, text="Email:").grid(row=2, column=0)
        tk.Label(self.add_contact_frame, text="Address:").grid(row=3, column=0)

        self.add_name_entry = tk.Entry(self.add_contact_frame)
        self.add_phone_entry = tk.Entry(self.add_contact_frame)
        self.add_email_entry = tk.Entry(self.add_contact_frame)
        self.add_address_entry = tk.Entry(self.add_contact_frame)

        self.add_name_entry.grid(row=0, column=1)
        self.add_phone_entry.grid(row=1, column=1)
        self.add_email_entry.grid(row=2, column=1)
        self.add_address_entry.grid(row=3, column=1)

        tk.Button(self.add_contact_frame, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2)

    def view_contacts_widgets(self):
        self.view_contacts_text = tk.Text(self.view_contacts_frame)
        self.view_contacts_text.pack(fill="both", expand=True)
        tk.Button(self.view_contacts_frame, text="Refresh", command=self.view_contacts).pack()

    def search_contact_widgets(self):
        tk.Label(self.search_contact_frame, text="Search Term:").grid(row=0, column=0)
        self.search_term_entry = tk.Entry(self.search_contact_frame)
        self.search_term_entry.grid(row=0, column=1)
        tk.Button(self.search_contact_frame, text="Search", command=self.search_contact).grid(row=1, column=0, columnspan=2)
        self.search_contact_text = tk.Text(self.search_contact_frame)
        self.search_contact_text.grid(row=2, column=0, columnspan=2)

    def update_contact_widgets(self):
        tk.Label(self.update_contact_frame, text="Name:").grid(row=0, column=0)
        self.update_name_entry = tk.Entry(self.update_contact_frame)
        self.update_name_entry.grid(row=0, column=1)
        tk.Label(self.update_contact_frame, text="New Phone:").grid(row=1, column=0)
        self.update_phone_entry = tk.Entry(self.update_contact_frame)
        self.update_phone_entry.grid(row=1, column=1)
        tk.Label(self.update_contact_frame, text="New Email:").grid(row=2, column=0)
        self.update_email_entry = tk.Entry(self.update_contact_frame)
        self.update_email_entry.grid(row=2, column=1)
        tk.Label(self.update_contact_frame, text="New Address:").grid(row=3, column=0)
        self.update_address_entry = tk.Entry(self.update_contact_frame)
        self.update_address_entry.grid(row=3, column=1)
        tk.Button(self.update_contact_frame, text="Update Contact", command=self.update_contact).grid(row=4, column=0, columnspan=2)

    def delete_contact_widgets(self):
        tk.Label(self.delete_contact_frame, text="Name:").grid(row=0, column=0)
        self.delete_name_entry = tk.Entry(self.delete_contact_frame)
        self.delete_name_entry.grid(row=0, column=1)
        tk.Button(self.delete_contact_frame, text="Delete Contact", command=self.delete_contact).grid(row=1, column=0, columnspan=2)

    def add_contact(self):
        name = self.add_name_entry.get().strip()
        if name in self.contacts:
            messagebox.showwarning("Duplicate Entry", "Contact with this name already exists.")
            return
        phone = self.add_phone_entry.get().strip()
        email = self.add_email_entry.get().strip()
        address = self.add_address_entry.get().strip()

        if name and phone:
            self.contacts[name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            self.save_contacts()
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries(self.add_name_entry, self.add_phone_entry, self.add_email_entry, self.add_address_entry)
        else:
            messagebox.showerror("Error", "Name and Phone are required.")

    def view_contacts(self):
        self.view_contacts_text.delete(1.0, tk.END)
        if not self.contacts:
            self.view_contacts_text.insert(tk.END, "No contacts found.")
        else:
            for name, details in self.contacts.items():
                self.view_contacts_text.insert(tk.END, f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}\n\n")

    def search_contact(self):
        search_term = self.search_term_entry.get().strip().lower()
        self.search_contact_text.delete(1.0, tk.END)
        if not search_term:
            messagebox.showerror("Error", "Please enter a search term.")
            return
        found = False
        for name, details in self.contacts.items():
            if search_term in name.lower():
                self.search_contact_text.insert(tk.END, f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}\n\n")
                found = True
        if not found:
            self.search_contact_text.insert(tk.END, "No contact found with that name.")

    def update_contact(self):
        name = self.update_name_entry.get().strip()
        if name not in self.contacts:
            messagebox.showerror("Error", "Contact not found.")
            return

        phone = self.update_phone_entry.get().strip()
        email = self.update_email_entry.get().strip()
        address = self.update_address_entry.get().strip()

        if phone or email or address:
            if phone:
                self.contacts[name]['Phone'] = phone
            if email:
                self.contacts[name]['Email'] = email
            if address:
                self.contacts[name]['Address'] = address

            self.save_contacts()
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries(self.update_name_entry, self.update_phone_entry, self.update_email_entry, self.update_address_entry)
        else:
            messagebox.showwarning("No Changes", "No new information provided.")

    def delete_contact(self):
        name = self.delete_name_entry.get().strip()
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_entries(self.delete_name_entry)
        else:
            messagebox.showerror("Error", "Contact not found.")

    def clear_entries(self, *entries):
        for entry in entries:
            entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Management System")
    root.geometry("400x400")
    app = ContactManagementSystem(root)
    root.mainloop()