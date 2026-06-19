import tkinter as tk
from tkinter import messagebox

contacts = []
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        clear_fields()
        refresh_list()
        messagebox.showinfo("Success", "Contact Added Successfully!")
    else:
        messagebox.showwarning("Warning", "Name and Phone are required!")

def refresh_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(
            tk.END,
            f"{contact['name']} - {contact['phone']}"
        )

def search_contact():
    keyword = search_entry.get().lower()

    contact_listbox.delete(0, tk.END)

    for contact in contacts:
        if (keyword in contact["name"].lower() or
                keyword in contact["phone"]):
            contact_listbox.insert(
                tk.END,
                f"{contact['name']} - {contact['phone']}"
            )

def update_contact():
    try:
        index = contact_listbox.curselection()[0]

        contacts[index]["name"] = name_entry.get()
        contacts[index]["phone"] = phone_entry.get()
        contacts[index]["email"] = email_entry.get()
        contacts[index]["address"] = address_entry.get()

        refresh_list()
        messagebox.showinfo("Success", "Contact Updated!")
    except:
        messagebox.showwarning("Warning", "Select a contact first!")

def delete_contact():
    try:
        index = contact_listbox.curselection()[0]
        contacts.pop(index)
        refresh_list()
        clear_fields()
        messagebox.showinfo("Success", "Contact Deleted!")
    except:
        messagebox.showwarning("Warning", "Select a contact first!")

def show_details(event):
    try:
        index = contact_listbox.curselection()[0]
        contact = contacts[index]

        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact["name"])

        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["phone"])

        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact["email"])

        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact["address"])
    except:
        pass

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Management System")
root.geometry("600x550")

# Labels and Entries
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

tk.Label(root, text="Search by Name or Phone").pack(pady=5)
search_entry = tk.Entry(root, width=40)
search_entry.pack()

tk.Button(root, text="Search", command=search_contact).pack(pady=5)

contact_listbox = tk.Listbox(root, width=60, height=15)
contact_listbox.pack(pady=10)

contact_listbox.bind("<<ListboxSelect>>", show_details)

root.mainloop()
