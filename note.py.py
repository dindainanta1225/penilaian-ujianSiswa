import tkinter as tk
from tkinter import filedialog, messagebox
import os

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Pink Aesthetic Notepad ♡")
        self.root.geometry("700x500")
        self.file_path = None

        # Colors
        self.bg_color = "#ffd6e7"   # soft pink
        self.menu_color = "#ffb6d5" # brighter pink
        self.text_bg = "#fff0f7"    # pastel pink
        self.text_fg = "#333333"    # dark gray for readability
        self.highlight_color = "#ff80b3"  # highlight bar

        root.configure(bg=self.bg_color)

        # Text Area (Aesthetic)
        self.text_area = tk.Text(
            root,
            undo=True,
            bg=self.text_bg,
            fg=self.text_fg,
            font=("Helvetica", 12),
            insertbackground="black",
            relief="flat",
            bd=5
        )
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)

        # Menu Bar
        menu_bar = tk.Menu(root, bg=self.menu_color, fg="black", activebackground=self.highlight_color)
        root.config(menu=menu_bar)

        # FILE MENU
        file_menu = tk.Menu(menu_bar, tearoff=0, bg=self.menu_color, activebackground=self.highlight_color)
        menu_bar.add_cascade(label="File ♡", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Delete", command=self.delete_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # EDIT MENU
        edit_menu = tk.Menu(menu_bar, tearoff=0, bg=self.menu_color, activebackground=self.highlight_color)
        menu_bar.add_cascade(label="Edit ✎", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))
        edit_menu.add_command(label="Select All", command=lambda: self.text_area.tag_add("sel", "1.0", "end"))
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)

        # HELP MENU
        help_menu = tk.Menu(menu_bar, tearoff=0, bg=self.menu_color, activebackground=self.highlight_color)
        menu_bar.add_cascade(label="Help ❀", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)

    # ========================
    # FILE FUNCTIONS (CRUD)
    # ========================

    def new_file(self):
        self.file_path = None
        self.text_area.delete(1.0, "end")

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not path:
            return

        self.file_path = path
        with open(path, "r") as file:
            content = file.read()
            self.text_area.delete(1.0, "end")
            self.text_area.insert(1.0, content)

    def save_file(self):
        if not self.file_path:
            path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if not path:
                return
            self.file_path = path

        content = self.text_area.get(1.0, "end-1c")
        with open(self.file_path, "w") as file:
            file.write(content)
        messagebox.showinfo("Saved", "Your cute pink note has been saved ♡")

    def delete_file(self):
        if not self.file_path:
            messagebox.showwarning("Warning", "No note to delete!")
            return

        answer = messagebox.askyesno("Delete", "Are you sure you want to delete this note?")
        if answer:
            try:
                os.remove(self.file_path)
                self.text_area.delete(1.0, "end")
                self.file_path = None
                messagebox.showinfo("Deleted", "Your note has been deleted ♡")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete note:\n{e}")

    def about(self):
        messagebox.showinfo("About", "Pink Aesthetic Notepad by (Nama Kamu) ♡")

# Run Program
if __name__ == "__main__":
    root = tk.Tk()
    Notepad(root)
    root.mainloop()