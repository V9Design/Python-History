from tkinter import *

# initialize the main window
root = Tk()
root.title("Temperature Converter")
root.resizable(width=False, height=False)

# window dimensions
HEIGHT = 150
WIDTH = 450

canvas = Canvas(root, bg="#2c3e50", height=HEIGHT, width=WIDTH)
canvas.pack()

def convert_temperature():
    try:
        # Get user input and selected units
        user_value = float(num_input.get())
        from_unit = input_unit_selector.get()
        to_unit = output_unit_selector.get()

        # 1. Convert any input unit to Celsius (Base Unit)
        if from_unit == "Celsius":
            celsius = user_value
        elif from_unit == "Reamur":
            celsius = user_value * 1.25
        elif from_unit == "Fahrenheit":
            celsius = (user_value - 32) / 1.8
        elif from_unit == "Kelvin":
            celsius = user_value + 273.15
        elif from_unit == "Rankine":
            celsius = (user_value - 491.67) * 1.8
        
        # 2. Convert from Celsius to the target output unit
        if to_unit == "Celsius":
            result = celsius
        elif to_unit == "Reamur":
            result = celsius * 0.8
        elif to_unit == "Fahrenheit":
            result = (celsius * 1.8) + 32
        elif to_unit == "Kelvin":
            result = celsius + 273.15
        elif to_unit == "Rankine":
            result = (celsius + 273.15) * 1.8
        
        # 3. Update the output field
        num_output.config(state="normal") # Ensure field is editable
        num_output.delete(0, END)
        num_output.insert(0, f"{result:.2f}") # Format to 2 decimal places

    except ValueError:
        num_output.delete(0, END)
        num_output.insert(0, "Error")

# --- UI Setup ---
# Bbackground Frame
input_frame = Frame(root, bg="#34495e", bd=5)
input_frame.place(relx=0.5, rely=0.4, relwidth=0.9, relheight=0.4, anchor="center")

temp_units = ("Celsius", "Reamur", "Fahrenheit", "Kelvin", "Rankine")

# Input side
input_unit_selector = Spinbox(input_frame, values=temp_units, wrap=True)
input_unit_selector.place(relx=0.02, rely=0.5, relwidth=0.3, relheight=0.8, anchor="w")

num_input = Entry(input_frame)
num_input.place(relx=0.35, rely=0.5, relwidth=0.15, relheight=0.8, anchor="w")
num_input.insert(0, "0")

# Center Label
to_label = Label(input_frame, text="to", fg="white", bg="#34495e", font=("Arial", 10, "bold"))
to_label.place(relx=0.53, rely=0.5, anchor="center")

# Output Side
output_unit_selector = Spinbox(input_frame, values=temp_units, wrap=True)
output_unit_selector.place(relx=0.8, rely=0.5, relwidth=0.3, relheight=0.8, anchor="e")

num_output = Entry(input_frame)
num_output.place(relx=0.98, rely=0.5, relwidth=0.15, relheight=0.8, anchor="e")

# Action Button
convert_button = Button(root, text="CONVERT", font=("Arial", 10, "bold"), command=convert_temperature)
convert_button.place(relx=0.5, rely=0.8, relwidth=0.4, relheight=0.15, anchor="center")

root.mainloop()