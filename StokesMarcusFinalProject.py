"""
Project Name: StokesMarcusFinalProject
Author: Marcus Stokes
Date: [12/11/2024]
Description:
This Python program uses tkinter to create a GUI application with three main features:
1. A main window for user input and navigation.
2. A functional calculator for basic arithmetic operations.
3. A second window for additional interaction.
The program demonstrates modular programming, input validation, and secure coding practices.
"""


import tkinter as tk
from tkinter import messagebox

# Function to validate input
def validate_input(entry):
    if not entry.strip():
        messagebox.showerror("Error", "Input cannot be empty!")
        return False
    return True

# Callback functions
def open_second_window():
    if validate_input(entry.get()):
        second_window = tk.Toplevel(root)
        second_window.title("Second Window")
        tk.Label(second_window, text="This is the second window!").pack(pady=20)
        tk.Button(second_window, text="Close", command=second_window.destroy).pack()

def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

def open_calculator():
    # Create a new window for the calculator
    calculator_window = tk.Toplevel(root)
    calculator_window.title("Calculator")
    
    # Variables
    equation = tk.StringVar()

    # Entry widget to display the current equation
    tk.Entry(calculator_window, textvariable=equation, font=("Arial", 20), justify="right").grid(row=0, column=0, columnspan=4)

    # Calculator button click handler
    def on_button_click(symbol):
        if symbol == "=":
            try:
                result = eval(equation.get())
                equation.set(result)
            except Exception as e:
                equation.set("Error")
        elif symbol == "C":
            equation.set("")
        else:
            equation.set(equation.get() + str(symbol))

    # Buttons for the calculator
    buttons = [
        "7", "8", "9", "/", 
        "4", "5", "6", "*", 
        "1", "2", "3", "-", 
        "C", "0", "=", "+"
    ]

    # Add buttons to the window
    row, col = 1, 0
    for button in buttons:
        tk.Button(
            calculator_window, text=button, width=5, height=2, font=("Arial", 14),
            command=lambda b=button: on_button_click(b)
        ).grid(row=row, column=col)
        col += 1
        if col > 3:  # Move to next row after 4 buttons
            col = 0
            row += 1

# Main window setup
root = tk.Tk()
root.title("Final Project GUI")

# GUI Widgets
tk.Label(root, text="Enter your name:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Open Calculator", command=open_calculator).pack(pady=10)
tk.Button(root, text="Open Second Window", command=open_second_window).pack(pady=10)
tk.Button(root, text="Exit", command=exit_app).pack(pady=10)

root.mainloop()
