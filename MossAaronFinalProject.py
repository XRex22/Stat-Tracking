"""
Program: MossAaronFinalProject.py
Author: Hunter Moss
Last date Modified: 5/7/2024
The purpose of this program is to allow a user to track, save, and load characters and their stats in a .txt file.
"""

import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class Player:
    def __init__(self, name, currency, health, experience, details):
        self.name = name
        self.currency = currency
        self.health = health
        self.experience = experience
        self.details = details

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Player Stat Tracker")

        self.current_view = None
        self.players = []

        self.home_view()

    def save_data(self):
        def save_file():
            file_name = file_entry.get()
            if not file_name.endswith(".txt"):
                file_name += ".txt"
            if file_name:
                try:

                    # Get the directory of the script
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    # Join the directory with the file name
                    file_path = os.path.join(script_dir, file_name)

                    with open(file_path, "w") as file:
                        num_players = len(self.players)
                        for i, player in enumerate(self.players):
                            # Write each player's data to the file
                            file.write(f"{player.name},{player.currency},{player.health},{player.experience},{player.details}")
                           # if i != num_players - 1:
                              #  file.write("\n")

                    messagebox.showinfo("Save", f"Data saved to {file_name} successfully!")
                    new_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Error saving data: {str(e)}")
            else:
                messagebox.showerror("Error", "Please enter a file name!")

        def browse_file(file_entry):
            file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if file_name:
                file_entry.delete(0, tk.END)
                file_entry.insert(0, file_name)
                
                with open(file_name, "w") as file:
                    num_players = len(self.players)
                    for i, player in enumerate(self.players):
                        # Remove new lines
                        player_details = player.details.replace("\n", " | ")
                        player_details = player_details.replace(",", ".")
                        # Write each player's data to the file
                        file.write(f"{player.name},{player.currency},{player.health},{player.experience},{player_details}")
                        if i != num_players - 1:
                            file.write("\n")

                messagebox.showinfo("Save", f"Data saved to {file_name} successfully!")
                new_window.destroy()


        new_window = tk.Toplevel(self)
        new_window.title("Save File")

        file_label = tk.Label(new_window, text="Enter file name:")
        file_label.pack()

        file_entry = tk.Entry(new_window)
        file_entry.pack()

        file_dialog_button = tk.Button(new_window, text="Browse", command=lambda: browse_file(file_entry))
        file_dialog_button.pack()

        save_button = tk.Button(new_window, text="Save", command=save_file)
        save_button.pack()

    def load_data(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, "r") as file:
                    # Read data from the file and process it
                    lines = file.readlines()
                    for line_num, line in enumerate(lines, start=1):
                        player_data = line.strip().split(",")  # Split line by commas
                        if len(player_data) == 5:  # Check if the line has the expected number of elements
                            # Create a Player object from the data and add it to the list of players
                            player = Player(player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])
                            self.players.append(player)
                        else:
                            messagebox.showerror("Error", f"Invalid data format in line {line_num}: {line.strip()}")
                            return  # Stop loading data if an error occurs
                messagebox.showinfo("Load", "Data loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error loading data: {str(e)}")
        else:
            messagebox.showinfo("Load", "No file selected!")
            
    def add_player_view(self):
        def add_player():
            # Get player details from entry widgets
            player_name = name_entry.get()
            player_currency = currency_entry.get()
            player_health = health_entry.get()
            player_experience = experience_entry.get()
            player_details = details_entry.get("1.0", tk.END)

            # Create a new Player object with the provided details
            new_player = Player(player_name, player_currency, player_health, player_experience, player_details)

            # Add the new player to the list of players
            self.players.append(new_player)

            messagebox.showinfo("Add Player", f"Player '{player_name}' added successfully! \nDon't forget to Save with the Save File button!")
            new_window.destroy()

        new_window = tk.Toplevel(self)
        new_window.title("Add Player")

        # Labels and entry widgets for player details
        name_label = tk.Label(new_window, text="Player Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(new_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        currency_label = tk.Label(new_window, text="Currency:")
        currency_label.grid(row=1, column=0, padx=5, pady=5)
        currency_entry = tk.Entry(new_window)
        currency_entry.grid(row=1, column=1, padx=5, pady=5)

        health_label = tk.Label(new_window, text="Health:")
        health_label.grid(row=2, column=0, padx=5, pady=5)
        health_entry = tk.Entry(new_window)
        health_entry.grid(row=2, column=1, padx=5, pady=5)

        experience_label = tk.Label(new_window, text="Experience:")
        experience_label.grid(row=3, column=0, padx=5, pady=5)
        experience_entry = tk.Entry(new_window)
        experience_entry.grid(row=3, column=1, padx=5, pady=5)

        details_label = tk.Label(new_window, text="Details:")
        details_label.grid(row=4, column=0, padx=5, pady=5)
        details_entry = tk.Text(new_window, height=4, width=30)
        details_entry.grid(row=4, column=1, padx=5, pady=5)

        # Save button to add the player
        save_button = tk.Button(new_window, text="Save", command=add_player)
        save_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Back button to return to the previous view
        
        back_button = tk.Button(new_window, text="Back", command=self.home_view)
        back_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def edit_player_view(self):
        def update_player():
            # Get updated player details from entry widgets
            player_name = name_entry.get()
            player_currency = currency_entry.get()
            player_health = health_entry.get()
            player_experience = experience_entry.get()
            player_details = details_entry.get("1.0", tk.END)


            # Update the selected player's details
            selected_player.name = player_name
            selected_player.currency = player_currency
            selected_player.health = player_health
            selected_player.experience = player_experience
            selected_player.details = player_details

            messagebox.showinfo("Edit Player", f"Player '{player_name}' updated successfully! \nDon't forget to Save with the Save File button!")
            new_window.destroy()

        def select_player():
            # Get the index of the selected player from the listbox
            index = player_listbox.curselection()
            if index:
                # Retrieve the selected player from the list of players
                global selected_player
                selected_player = self.players[index[0]]

                # Update the entry widgets with the selected player's details
                name_entry.delete(0, tk.END)
                name_entry.insert(0, selected_player.name)
                currency_entry.delete(0, tk.END)
                currency_entry.insert(0, selected_player.currency)
                health_entry.delete(0, tk.END)
                health_entry.insert(0, selected_player.health)
                experience_entry.delete(0, tk.END)
                experience_entry.insert(0, selected_player.experience)
                details_entry.delete("1.0", tk.END)
                details_entry.insert("1.0", selected_player.details)
                
            else:
                messagebox.showerror("Error", "Please select a player to edit!")

        new_window = tk.Toplevel(self)
        new_window.title("Edit Player")



        # Listbox to display the list of players
        player_listbox = tk.Listbox(new_window)
        for player in self.players:
            player_listbox.insert(tk.END, player.name)
        player_listbox.pack()

        # Button to select a player to edit
        select_button = tk.Button(new_window, text="Select Player", command=select_player)
        select_button.pack()

        # Entry labels for player details
        name_label = tk.Label(new_window, text="Player Name:")
        name_label.pack()
        name_entry = tk.Entry(new_window)
        name_entry.pack()

        currency_label = tk.Label(new_window, text="Currency:")
        currency_label.pack()
        currency_entry = tk.Entry(new_window)
        currency_entry.pack()

        health_label = tk.Label(new_window, text="Health:")
        health_label.pack()
        health_entry = tk.Entry(new_window)
        health_entry.pack()

        experience_label = tk.Label(new_window, text="Experience:")
        experience_label.pack()
        experience_entry = tk.Entry(new_window)
        experience_entry.pack()

        details_label = tk.Label(new_window, text="Details:")
        details_label.pack()
        details_entry = tk.Text(new_window, height=4, width=30)
        details_entry.pack()

        # Save button to update the player
        save_button = tk.Button(new_window, text="Save", command=update_player)
        save_button.pack()

        # Back button to return to the previous view
        back_button = tk.Button(new_window, text="Back", command=self.home_view)
        back_button.pack()

    def home_view(self):
        self.current_view = "home"
        self.title("Player Stat Tracker")
        
        # Destroy existing widgets
        for widget in self.winfo_children():
            widget.destroy()
        
        self.banner()
        self.save_button()
        self.load_button()
        self.add_player_button()
        self.edit_player_button()
        self.exit_button()

    def clear_view(self):
        if self.current_view != "home":
            for widget in self.winfo_children():
                widget.destroy()
        self.current_view = "home"
        self.home_view()

    def banner(self):
        # Create a label widget for the banner
        banner_label = tk.Label(self, text="  Player Stat Tracker  ", font=("Century Schoolbook", 24), bg="grey", fg="gold")
        banner_label.pack(fill=tk.X)  # Pack the label to fill the horizontal space

    def save_button(self):
        save_button = tk.Button(self, text="Save File", command=self.save_data)
        save_button.pack()

    def load_button(self):
        load_button = tk.Button(self, text="Load File", command=self.load_data)
        load_button.pack()

    def add_player_button(self):
        add_player_button = tk.Button(self, text="Add Player", command=self.add_player_view)
        add_player_button.pack()

    def edit_player_button(self):
        edit_player_button = tk.Button(self, text="Edit Player", command=self.edit_player_view)
        edit_player_button.pack()

    def exit_button(self):
        exit_button = tk.Button(self, text="Exit", command=self.exit)
        exit_button.pack(side=tk.BOTTOM)

    def back_button(self):
        back_button = tk.Button(self, text="Back", command=self.home_view)
        back_button.pack(side=tk.TOP)

    def exit(self):
        result = messagebox.askquestion("Exit", "Any unsaved changes will be lost. \nAre you sure you wish to Exit?")
        if result.lower() == 'yes':
            self.destroy()
        if result.lower() == 'no':
            return

def browse_file(file_entry):
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_name:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_name)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
