import tkinter as tk
from tkinter import ttk, messagebox

# Function to perform the conversion
def convert():
    try:
        input_value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        # Conversion factor dictionary (base unit: Meters)
        # All units are converted to meters first, then to the target unit
        factor_to_meter = {
            "Millimeter": 0.001,
            "Centimeter": 0.01,
            "Inch": 0.0254,
            "Meter": 1.0,
            "Foot": 0.3048,
            "Yard": 0.9144,
            "Mile": 1609.344,
            "Nautical Mile": 1852.0,
            "Kilometer": 1000.0
        }

        # Validation
        if not from_unit or not to_unit:
            messagebox.showwarning("Warning", "Please select 'From' and 'To' units!")
            return
        
        # Formula: (Value x From_Factor) -> Meters -> ( / To_Factor) -> Result
        value_in_meters = input_value * factor_to_meter[from_unit]
        result = value_in_meters / factor_to_meter[to_unit]

        # Display result (rounded to 6 decimal places)
        label_result.config(text=f"Result: {result:.6f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Function to reset inputs
def reset():
    entry_value.delete(0, tk.END)
    combo_from.set('')
    combo_to.set('')
    label_result.config(text="Result: -")

# Main window setup
root = tk.Tk()
root.title("Length Unit Converter")
root.geometry("400x450")
root.resizable(False, False)

# App Title
label_title = tk.Label(root, text="Length Unit Converter", font=("Arial", 16, "bold"))
label_title.pack(pady=15)

# Input Frame
frame_input = tk.Frame(root)
frame_input.pack(padx=10)

# Label and Entry for Value
tk.Label(frame_input, text="Value:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_value = tk.Entry(frame_input, font=("Arial", 11), width=20)
entry_value.grid(row=0, column=1, padx=5, pady=5)

# Label and Combobox for "From" Unit
tk.Label(frame_input, text="From Unit:", font=("Arial", 11)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
unit_list = [
    "Millimeter", "Centimeter", "Inch", "Meter",
    "Foot", "Yard", "Mile", "Nautical Mile", "Kilometer"
]
combo_from = ttk.Combobox(frame_input, values=unit_list, font=("Arial", 10), width=17, state="readonly")
combo_from.grid(row=1, column=1, padx=5, pady=5)

# Label and Combobox for "To" Unit
tk.Label(frame_input, text="To Unit:", font=("Arial", 11)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
combo_to = ttk.Combobox(frame_input, values=unit_list, font=("Arial", 10), width=17, state="readonly")
combo_to.grid(row=2, column=1, padx=5, pady=5)

# Convert and reset Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=20)

btn_convert = tk.Button(frame_buttons, text="Convert", command=convert, font=("Arial", 11, "bold"), bg="#4cAF50", fg="white", width=10)
btn_convert.grid(row=0, column=0, padx=10)

btn_reset = tk.Button(frame_buttons, text="Reset", command=reset, font=("Arial", 11), bg="#f44336", fg="white", width=10)
btn_reset.grid(row=0, column=1, padx=10)

# Result Label
label_result = tk.Label(root, text="Result: -", font=("Arial", 14, "bold"), fg="#333")
label_result.pack(pady=30)

# Footer
tk.Label(root, text="Created with Python Tkinter", font=("Arial", 8), fg="gray").pack(side=tk.BOTTOM, pady=5)

# Main Application loop
root.mainloop()