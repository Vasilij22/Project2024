import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class MusicInfoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Information App")

        # First window widgets
        self.add_info_button = tk.Button(master, text="Add Info", command=self.open_add_info_window)
        self.add_info_button.pack(pady=10)

        self.apskatit_button = tk.Button(master, text="Apskatit", command=self.open_apskatit_window)
        self.apskatit_button.pack(pady=10)

        self.close_button = tk.Button(master, text="Close", command=master.destroy)
        self.close_button.pack(pady=10)

        # Data structure to hold music information
        self.music_info_list = []

    def open_add_info_window(self):
        add_info_window = tk.Toplevel(self.master)
        add_info_window.title("Add Music Info")

        # Entry widgets
        self.song_name_entry = tk.Entry(add_info_window, width=30)
        self.song_name_entry.grid(row=0, column=1, pady=10)
        self.singer_entry = tk.Entry(add_info_window, width=30)
        self.singer_entry.grid(row=1, column=1, pady=10)
        self.genre_entry = tk.Entry(add_info_window, width=30)
        self.genre_entry.grid(row=2, column=1, pady=10)
        self.year_entry = tk.Entry(add_info_window, width=30)
        self.year_entry.grid(row=3, column=1, pady=10)

        # Labels
        tk.Label(add_info_window, text="Song Name:").grid(row=0, column=0, pady=10)
        tk.Label(add_info_window, text="Singer:").grid(row=1, column=0, pady=10)
        tk.Label(add_info_window, text="Genre:").grid(row=2, column=0, pady=10)
        tk.Label(add_info_window, text="Year:").grid(row=3, column=0, pady=10)

        # Buttons
        self.save_button = tk.Button(add_info_window, text="Save", command=self.save_info)
        self.save_button.grid(row=4, column=0, pady=10)
        self.add_button = tk.Button(add_info_window, text="Add", command=self.add_info)
        self.add_button.grid(row=4, column=1, pady=10)

        # Table
        self.table = ttk.Treeview(add_info_window, columns=("Song Name", "Singer", "Genre", "Year"), show="headings")
        self.table.heading("Song Name", text="Song Name")
        self.table.heading("Singer", text="Singer")
        self.table.heading("Genre", text="Genre")
        self.table.heading("Year", text="Year")
        self.table.grid(row=5, column=0, columnspan=2, pady=10)

    def save_info(self):
        song_name = self.song_name_entry.get()
        singer = self.singer_entry.get()
        genre = self.genre_entry.get()
        year = self.year_entry.get()

        if song_name and singer and genre and year:
            # Choose a file to save information
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

            if file_path:
                # Update data structure
                self.music_info_list.append((song_name, singer, genre, year))

                # Save information to chosen file
                with open(file_path, "a") as file:
                    file.write(f"{song_name}, {singer}, {genre}, {year}\n")

                # Update table
                self.update_table()

                messagebox.showinfo("Success", "Information saved successfully!")
            else:
                messagebox.showinfo("Information", "Operation canceled.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def add_info(self):
        song_name = self.song_name_entry.get()
        singer = self.singer_entry.get()
        genre = self.genre_entry.get()
        year = self.year_entry.get()

        if song_name and singer and genre and year:
            # Choose a file to add information
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

            if file_path:
                # Update data structure
                self.music_info_list.append((song_name, singer, genre, year))

                # Add information to chosen file
                with open(file_path, "a") as file:
                    file.write(f"{song_name}, {singer}, {genre}, {year}\n")

                # Update table
                self.update_table()

                messagebox.showinfo("Success", "Information added successfully!")
            else:
                messagebox.showinfo("Information", "Operation canceled.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def update_table(self):
        # Clear existing data
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert updated data
        for info in self.music_info_list:
            self.table.insert("", "end", values=info)

    def open_apskatit_window(self):
        apskatit_window = tk.Toplevel(self.master)
        apskatit_window.title("Apskatit Music Info")

        # Choose a file to view information
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if file_path:
            try:
                with open(file_path, "r") as file:
                    lines = [line.strip().split(", ") for line in file.readlines()]
                # Table for displaying information
                table = ttk.Treeview(apskatit_window, columns=("Song Name", "Singer", "Genre", "Year"), show="headings")
                table.heading("Song Name", text="Song Name")
                table.heading("Singer", text="Singer")
                table.heading("Genre", text="Genre")
                table.heading("Year", text="Year")

                # Insert data into table
                for line in lines:
                    table.insert("", "end", values=line)

                table.pack(padx=10, pady=10)
            except FileNotFoundError:
                tk.Label(apskatit_window, text="No information available.").pack(pady=10)
        else:
            tk.Label(apskatit_window, text="Operation canceled.").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicInfoApp(root)
    root.mainloop()

# make first window where is 3 button Add info ,Apskatit,Close then when click button add info there will be a  second window where will be table button save and add also there can write a songs name, singer name,genre, year when click save button save information in  chosen .txt in the map when click add button you add information to chosen file  then when click button apskatit will be a window where you can check information in table  from chosen file where was saved songs info


