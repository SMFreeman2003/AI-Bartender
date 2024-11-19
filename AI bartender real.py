import tkinter as tk
from main import generate_drink, generate_drink_name

# Function to handle button click (start the input process)
def start_button():
    label.config(text="What ingredients do you have?")
    button.pack_forget()
    entry.pack(pady=10)
    label_ingredient.pack(pady=5)
    finish_button.pack(pady=20)

# Function to handle ingredient input when "Enter" is pressed
def enter_ingredient(event=None):
    ingredient = entry.get()  # Get the input from the Entry widget
    if ingredient:
        if ingredient_listbox.winfo_ismapped() == False:
            ingredient_listbox.pack(pady=20)
        ingredient_listbox.insert(tk.END, ingredient)
        
        # Clear screen
        entry.delete(0, tk.END)
    else:
        label.config(text="Please enter an ingredient!")

# Function to show the "Making Your Personalized Cocktails..." screen
def show_loading_screen():
    # Clear screen
    label.pack_forget()
    entry.pack_forget()
    ingredient_listbox.pack_forget()
    label_ingredient.pack_forget()
    finish_button.pack_forget()

    making_cocktail_label.pack(pady=20)

    # loading screen
    root.after(2000, finish_ingredients)

# Function to handle finishing the list of ingredients and showing the results
def finish_ingredients():
    ingredients = list(ingredient_listbox.get(0, tk.END))
    label.config(text=f"Finished! Ingredients: {', '.join(ingredients)}")
    
    # Clear screens
    ingredient_listbox.delete(0, tk.END)
    entry.delete(0, tk.END)
    making_cocktail_label.pack_forget()
    label.pack(pady=20)
    ingredient_listbox.pack_forget()
    entry.pack_forget()
    label_ingredient.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("1600x1200")  # Width x Height
root.configure(bg="VioletRed4")

# Welcome screen
label = tk.Label(root, text="Welcome to AI Bartender!", font=("FixedSys", 17), fg="goldenrod", bg="VioletRed4")
label.pack(pady=20)
button = tk.Button(root, text="Start your personalized cocktail experience", command=start_button, font=("FixedSys", 12), bg="old lace")
button.pack()

# Ingredient input stuff
entry = tk.Entry(root, font=("FixedSys", 12), bg="light yellow", width=30)
label_ingredient = tk.Label(root, text="Press Enter after each ingredient", font=("FixedSys", 12), fg="white", bg="VioletRed4")
ingredient_listbox = tk.Listbox(root, font=("FixedSys", 12), width=30, height=8, bg="light yellow", fg="black", selectmode=tk.SINGLE)
entry.bind("<Return>", enter_ingredient)

# Finish button
finish_button = tk.Button(root, text="Finish Ingredients", command=show_loading_screen, font=("FixedSys", 12), bg="old lace")

# Loading screen
making_cocktail_label = tk.Label(root, text="Making Your Personalized Cocktails...", font=("FixedSys", 20), fg="white", bg="VioletRed4")

# Run the application
root.mainloop()
