import tkinter as tk
import time
from main import *

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
    start_animation()

    # Loading screen (stop after 2 seconds)
    root.after(2000, finish_ingredients)

def start_animation():
    global shaking
    shaking = True
    shaker_frame = tk.Label(root, text="🍸", font=("FixedSys", 100), fg="white", bg="VioletRed4")  # Larger size
    shaker_frame.pack(pady=20)
    
    # Function to change emojis in sequence
    def shake_animation_once():
        if shaking:
            # Sequence of emojis to simulate shaking
            shaker_frame.config(text="🍸")  # Cocktail glass emoji
            shaker_frame.after(500, shaker_frame.config, {"text": "🥂"}) 
            shaker_frame.after(1000, shaker_frame.config, {"text": "🍸"})
            shaker_frame.after(1500, shaker_frame.config, {"text": "🍹"}) 
            # Stop after this round of changes
            shaker_frame.after(2000, stop_animation)

    # Function to stop the animation
    def stop_animation():
        global shaking
        shaking = False
        shaker_frame.pack_forget()  # Remove the shaker once animation is done

    shake_animation_once()


# Function to handle finishing the list of ingredients and showing the results
def finish_ingredients():
    # Stop animation immediately when the finish screen is triggered
    global shaking
    shaking = False

    # Retrieve the ingredients list from the listbox
    ingredients = list(ingredient_listbox.get(0, tk.END))

    # Split the response into a name and an ingredient list
    response = generate_drink(ingredients).split('@')
    
    # Check if there's only one ingredient
    if len(ingredients) <= 1:
        label.config(text="Whoops! Looks like that just won’t cut it for a cocktail! \n How about a glass of water instead? 💦")  # Display warning message
        retry_button.pack(pady=30)  # Show the button to allow retrying the ingredient input
    else:
        label.config(text=f"Finished! Ingredients: \n{response[1]}")  # Show the ingredients if more than one
        cocktail_label = tk.Label(root, text="!", font=("FixedSys", 17), fg="goldenrod", bg="VioletRed4")
        cocktail_label.pack(pady=30)
        cocktail_label.config(text=f"Here is a cocktail you can make: \n{response[0]}")
        retry_button.pack(pady=30)

    # Clear screens
    ingredient_listbox.delete(0, tk.END)
    entry.delete(0, tk.END)
    making_cocktail_label.pack_forget()
    label.pack(pady=20)
    ingredient_listbox.pack_forget()
    entry.pack_forget()
    label_ingredient.pack_forget()

# Function to allow the user to enter more ingredients
def retry_ingredients():
    # Hide the retry button
    retry_button.pack_forget()

    # Reset the ingredient list and show the input fields again
    label.config(text="What ingredients do you have?")
    entry.pack(pady=10)
    label_ingredient.pack(pady=5)
    finish_button.pack(pady=20)

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

# Retry button (for entering more ingredients)
retry_button = tk.Button(root, text="Retry and Enter More Ingredients", command=retry_ingredients, font=("FixedSys", 12), bg="old lace")

# Loading screen
making_cocktail_label = tk.Label(root, text="Making Your Personalized Cocktails...", font=("FixedSys", 20), fg="white", bg="VioletRed4")

# Run the application
root.mainloop()
