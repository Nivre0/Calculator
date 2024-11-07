import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

# Display widget
display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def click_button(item):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + str(item))

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Keyboard bindings
def key_event(event):
    key = event.char
    if key in '0123456789+-*/.':
        click_button(key)
    elif key == '\r':  # Enter key
        calculate()
    elif key == '\x08':  # Backspace key
        current_text = display.get()
        display.delete(0, tk.END)
        display.insert(0, current_text[:-1])

# Bind the key_event function to all keypresses
root.bind("<Key>", key_event)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_value = 1
col_value = 0
for button_text in buttons:
    if button_text == "=":
        btn = tk.Button(root, text=button_text, font=("Arial", 18), command=calculate, width=5, height=2)
    else:
        btn = tk.Button(root, text=button_text, font=("Arial", 18),
                        command=lambda bt=button_text: click_button(bt), width=5, height=2)

    btn.grid(row=row_value, column=col_value, padx=5, pady=5)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Clear button
clear_button = tk.Button(root, text="C", font=("Arial", 18), command=clear_display, width=5, height=2)
clear_button.grid(row=row_value, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Run the application
root.mainloop()
