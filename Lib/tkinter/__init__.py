import tkinter as tk
from tkinter import ttk, messagebox

def calculate_bmr(gender, weight, height, age):
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict Equation.
    """
    if gender == 'Male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'Female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Invalid gender. Choose 'Male' or 'Female'.")
    return bmr

def calculate_tdee(bmr, activity_level):
    """
    Calculate TDEE based on BMR and activity level.
    """
    activity_multipliers = {
        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725,
        "Very Active": 1.9
    }

    if activity_level not in activity_multipliers:
        raise ValueError("Invalid activity level.")

    return bmr * activity_multipliers[activity_level]

def calculate():
    try:
        gender = gender_var.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        activity_level = activity_var.get()

        bmr = calculate_bmr(gender, weight, height, age)
        tdee = calculate_tdee(bmr, activity_level)

        result_label.config(text=f"BMR: {bmr:.2f} kcal/day\nTDEE: {tdee:.2f} kcal/day")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def clear():
    gender_var.set("Male")
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    activity_var.set("Sedentary")
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("TDEE Calculator")

# Gender
gender_label = ttk.Label(root, text="Gender:")
gender_label.grid(row=0, column=0, padx=10, pady=5)
gender_var = tk.StringVar(value="Male")
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"], state="readonly")
gender_combobox.grid(row=0, column=1, padx=10, pady=5)

# Weight
weight_label = ttk.Label(root, text="Weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=5)
weight_entry = ttk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

# Height
height_label = ttk.Label(root, text="Height (cm):")
height_label.grid(row=2, column=0, padx=10, pady=5)
height_entry = ttk.Entry(root)
height_entry.grid(row=2, column=1, padx=10, pady=5)

# Age
age_label = ttk.Label(root, text="Age (years):")
age_label.grid(row=3, column=0, padx=10, pady=5)
age_entry = ttk.Entry(root)
age_entry.grid(row=3, column=1, padx=10, pady=5)

# Activity Level
activity_label = ttk.Label(root, text="Activity Level:")
activity_label.grid(row=4, column=0, padx=10, pady=5)
activity_var = tk.StringVar(value="Sedentary")
activity_combobox = ttk.Combobox(root, textvariable=activity_var, values=["Sedentary", "Light", "Moderate", "Active", "Very Active"], state="readonly")
activity_combobox.grid(row=4, column=1, padx=10, pady=5)

# Buttons
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, padx=10, pady=10)

clear_button = ttk.Button(root, text="Clear", command=clear)
clear_button.grid(row=5, column=1, padx=10, pady=10)

# Result Label
result_label = ttk.Label(root, text="", anchor="center")
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
