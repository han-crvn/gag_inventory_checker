# Import libraries.
import tkinter as tk
from tkinter import ttk, messagebox
from back_end import Inventory

# Create class for the GUI of the app.
class MainApp:

    # Set the size, font, font size, and color of the app.
    def __init__(self, root):
        self.root = root
        self.root.title("GAG Inventory Checker")
        self.root.geometry("400x400")
        self.root.minsize(400, 400)
        self.root.maxsize(400, 400)
        self.center_window(400, 400)

        # Format the color of main background.
        self.root.configure(bg = "#A7DDE9")
        
        # Format the font, font size, and color of the buttons.
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Main.TFrame", background = "#A7DDE9")
        style.configure("Title.TLabel", font = ("Poppins", 30), foreground = "#2C3E50", background = "#A7DDE9")
        style.configure("Custom.TButton", font = ("Poppins", 10), background = "#66B2D6", foreground = "#2C3E50")
        
        # Format the frame of app.
        self.main_frame = ttk.Frame(self.root, style = "Main.TFrame")
        self.main_frame.place(relx = 0.5, rely = 0.5, anchor = "center")

        # Run the app.
        self.inventory = Inventory()
        self.main_menu()

    # Center the window on the screen.
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_axis = (screen_width // 2) - (width // 2)
        y_axis = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x_axis}+{y_axis}")
    
    # Clear widgets from the main frame.
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # Display the main menu options.
    def main_menu(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text = "MAIN MENU", style = "Title.TLabel").pack(pady = 10)

        # List of options.
        options = [
            ("Check Inventory", self.check_inventory),
            ("Add Goods/Pets", self.not_implemented),
            ("Edit Inventory", self.not_implemented),
            ("Exit", self.root.quit)
        ]
        # List down the options.
        for text, command in options:
             ttk.Button(self.main_frame, text = text, command = command, style = "Custom.TButton").pack(pady = 5)

    # Display options to choose between goods or pets.
    def check_inventory(self): 
        self.clear_frame()
        
        # Format the label.
        ttk.Label(self.main_frame, text = "Check Inventory", style = "Title.TLabel").pack(pady = 10)
        
        # Format the buttons.
        ttk.Button(self.main_frame, text = "View Goods", command = self.view_goods, style = "Custom.TButton").pack(pady = 5)
        ttk.Button(self.main_frame, text = "View Pets", command = self.view_pets, style = "Custom.TButton").pack(pady = 5)
        ttk.Button(self.main_frame, text = "Back", command = self.main_menu, style = "Custom.TButton").pack(pady = 5)

    # List down all goods and allow users to view more details.
    def view_goods(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text = "Goods List", style = "Title.TLabel").pack(pady=10)
        goods = self.inventory.get_goods()

        # List down the goods.
        for list_good, good in enumerate(goods):
            ttk.Button(self.main_frame, text = good.get_details(), command = lambda list_num = list_good: self.show_good_detail(list_num)).pack(pady = 2)
        
        # Format the button.
        ttk.Button(self.main_frame, text = "Back", command = self.check_inventory, style = "Custom.TButton").pack(pady = 10)

    # Show detailed information of the goods.
    def show_good_detail(self, index):
        self.clear_frame()
        good = self.inventory.get_goods()[index]
        detail = f"Name: {good.get_name()}\nPrice: ${good.get_price()}\nMutation: {good.get_mutation()}\nStatus: {good.get_status()}"
        ttk.Label(self.main_frame, text = detail, style = "Title.TLabel").pack(pady = 10)
        ttk.Button(self.main_frame, text = "Back", command = self.view_goods, style = "Custom.TButton").pack()
    
    # List down all the pets and show details.

    # Display options to add goods or pets.

    # Create form to add new goods.

    # Create form to add new pets.

    # Display options to choose whether to edit goods or pets.

    # List of goods for editing or removing.

    # OptionS to remove or mark a good a sold.

    # Remove good from inventory.

    # List of pets for editing or removing.

    # OptionS to remove or mark a pet as sold.

    # Remove a pet from inventory.

    # Mark a pet as sold.


    # (TEMPORARY) Test run checker.
    def not_implemented(self):
        messagebox.showinfo("Not Ready", "This feature is not yet implemented.")