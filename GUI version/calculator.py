import tkinter as tk
from operations import add, subtract, multiply, divide

# Function to handle button clicks
def on_click(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(operator))

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        expression = entry.get()
        # Split simple expressions like "5+3"
        if "+" in expression:
            a, b = expression.split("+")
            result = add(float(a), float(b))
        elif "-" in expression:
            a, b = expression.split("-")
            result = subtract(float(a), float(b))
        elif "*" in expression:
            a, b = expression.split("*")
            result = multiply(float(a), float(b))
        elif "/" in expression:
            a, b = expression.split("/")
            result = divide(float(a), float(b))
        else:
            result = "Error"

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for input
entry = tk.Entry(root, width=20, font=("Arial", 16), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear
    else:
        action = lambda x=text: on_click(x)

    tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=action).grid(row=row, column=col)

# Run the Tkinter loop
root.mainloop()
