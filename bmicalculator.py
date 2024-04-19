import tkinter as tk
from tkinter import messagebox, simpledialog

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    root.geometry("1000x500")  # Set the size of the dialog window

    weight = simpledialog.askfloat("BMI Calculator",
                                   "Enter your weight in kilograms:")
    height = simpledialog.askfloat("BMI Calculator",
                                   "Enter your height in meters:")

    if weight is None or height is None:
        return  # Exit if user cancels input

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    message = f"Your BMI is: {bmi:.2f}\nCategory: {category}"
    messagebox.showinfo("BMI Calculator Result", message)

if __name__ == "__main__":
    main()
