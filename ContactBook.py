import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Missing Info", "Name and phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    clear_entries()
    show_contacts()
    messagebox.showinfo("Success", "Contact added successfully!")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def show_contacts():
    contact_list.delete(0, tk.END)
    for i, c in enumerate(contacts):
        contact_list.insert(tk.END, f"{i+1}. {c['name']}    -    {c['phone']}   -   {c['email']}    -   {c['address']}")

def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone:")
    contact_list.delete(0, tk.END)
    found = False
    for i, c in enumerate(contacts):
        if query.lower() in c['name'].lower() or query in c['phone']:
            contact_list.insert(tk.END, f"{i+1}. {c['name']}    -    {c['phone']}       -      {c['email']}     -      {c['address']}")
            found = True
    if not found:
        messagebox.showinfo("Not Found", "No contact matches the search.")

def get_selected_contact_index():
    selected = contact_list.curselection()
    if not selected:
        return None
    return int(selected[0])

def update_contact():
    index = get_selected_contact_index()
    if index is None:
        messagebox.showwarning("Select Contact", "Select a contact to update.")
        return

    contact = contacts[index]
    name = simpledialog.askstring("Update", "Enter new name:", initialvalue=contact["name"])
    phone = simpledialog.askstring("Update", "Enter new phone:", initialvalue=contact["phone"])
    email = simpledialog.askstring("Update", "Enter new email:", initialvalue=contact["email"])
    address = simpledialog.askstring("Update", "Enter new address:", initialvalue=contact["address"])

    contacts[index] = {
        "name": name or contact["name"],
        "phone": phone or contact["phone"],
        "email": email or contact["email"],
        "address": address or contact["address"]
    }
    show_contacts()
    messagebox.showinfo("Updated", "Contact updated.")

def delete_contact():
    index = get_selected_contact_index()
    if index is None:
        messagebox.showwarning("Select Contact", "Select a contact to delete.")
        return
    confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this contact?")
    if confirm:
        del contacts[index]
        show_contacts()
        messagebox.showinfo("Deleted", "Contact deleted.")

# GUI setup
root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x700")
root.config(bg= "#f29215")

tk.Label(root, text="CONTACT BOOK",font = ("Algerian",40,"bold"),bg="#d2f95e",fg="#710f95").grid(row=0, column=2)
tk.Label(root, text="Name:",font = ("Cascadia Code SemiBold",20),bg="#f4a37a").grid(row=1, column=1, pady=10)
tk.Label(root, text="Phone:",font = ("Cascadia Code SemiBold",20),bg="#f4a37a").grid(row=2, column=1,pady=10)
tk.Label(root, text="Email:",font = ("Cascadia Code SemiBold",20),bg="#f4a37a").grid(row=3, column=1,pady=10)
tk.Label(root, text="Address:",font = ("Cascadia Code SemiBold",20),bg="#f4a37a").grid(row=4, column=1,pady=10)


name_entry = tk.Entry(root,font=(20))
phone_entry = tk.Entry(root,font=(20))
email_entry = tk.Entry(root,font=(20))
address_entry = tk.Entry(root,font=(20))

name_entry.grid(row=1, column=2, padx=10, pady=10)
phone_entry.grid(row=2, column=2, padx=10, pady=10)
email_entry.grid(row=3, column=2, padx=10, pady=10)
address_entry.grid(row=4, column=2, padx=10, pady=10)

tk.Button(root, text="Add Contact", font = ("Cascadia Code SemiLight",14),bg="#a1eef4",command=add_contact).grid(row=7, column=1, pady=10)
tk.Button(root, text="Search Contact",font = ("Cascadia Code SemiLight",14),bg="#a1eef4", command=search_contact).grid(row=7, column=2)
tk.Button(root, text="Update Contact",font = ("Cascadia Code SemiLight",14),bg="#a1eef4", command=update_contact).grid(row=8, column=1)
tk.Button(root, text="Delete Contact",font = ("Cascadia Code SemiLight",14),bg="#a1eef4", command=delete_contact).grid(row=8, column=2)

contact_list = tk.Listbox(root, font = (12),bg= "#a3f650", width=80)
contact_list.grid(row=10, column=1, columnspan=2, pady=10)

show_contacts()

root.mainloop()
