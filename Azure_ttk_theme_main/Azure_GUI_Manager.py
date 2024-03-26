import ast
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class Storage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Manager")

        # Set the Azure theme
        self.root.tk.call("source", "azure.tcl")
        self.root.tk.call("set_theme", "dark")

        self.create_widgets()

    def create_widgets(self):
        accent_button = ttk.Button(self.root, text='View All Password', command=self.ViewPassword)
        accent_button.pack()

        self.edit_button = ttk.Button(self.root, text="Edit Password", command=self.EditPassword)
        self.edit_button.pack()

        self.add_button = ttk.Button(self.root, text="Add Password", command=self.AddPassword)
        self.add_button.pack()

        self.delete_button = ttk.Button(self.root, text="Delete Password", command=self.RemovePassword)
        self.delete_button.pack()

        self.exit_button = ttk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

    def ViewPassword(self):
        with open("viewpass.txt", "r") as file:
            read = file.read()
        dictionary = ast.literal_eval(read)

        result = ""
        for key, value in dictionary.items():
            result += f"{key} - {value}\n"

        messagebox.showinfo("View Passwords", result)

    def EditPassword(self):
        with open("viewpass.txt", "r+") as file:
            read = file.readlines()
            file.seek(0)

            dictionary = ast.literal_eval(read[0])
            lists = list(dictionary.keys())

            options = "\n".join(f"{i+1}.{lists[i]}" for i in range(len(lists)))
            key = simpledialog.askstring("Edit Password", f"Enter Account Number:\n{options}")

            found = False
            for j in range(len(lists)):
                if key == lists[j]:
                    value = simpledialog.askstring("Edit Password", f"Enter New Password Of {key}")
                    dictionary[key] = value
                    found = True
                    break

            if found:
                file.write(str(dictionary))
                file.truncate()
                messagebox.showinfo("Edit Password", "Password updated successfully.")
            else:
                messagebox.showinfo("Edit Password", "Incorrect Account Name.")

    def AddPassword(self):
        key = simpledialog.askstring("Add Password", "Enter Account Name")
        value = simpledialog.askstring("Add Password", f"Enter {key} Password")

        with open("viewpass.txt", "r") as file:
            read = file.read()

        dictionary = ast.literal_eval(read)
        dictionary[key] = value

        with open("viewpass.txt", "w") as file:
            file.write(str(dictionary))

        messagebox.showinfo("Add Password", "Password added successfully.")

    def RemovePassword(self):
        try:
            with open("viewpass.txt", "r") as file:
                read = file.read()

            dictionary = ast.literal_eval(read)
            lists = list(dictionary.keys())

            options = "\n".join(f"{i+1}.{lists[i]}" for i in range(len(lists)))
            key = simpledialog.askstring("Remove Password", f"Enter Account Name:\n{options}")

            if key in dictionary:
                del dictionary[key]
                messagebox.showinfo("Remove Password", f"{key} Password is deleted.")
            else:
                messagebox.showinfo("Remove Password", "Incorrect Account Name.")

            with open("viewpass.txt", "w") as file:
                file.write(str(dictionary))

        except Exception as error:
            messagebox.showinfo("Remove Password", "Incorrect Account Name.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    object = Storage()
    object.run()
