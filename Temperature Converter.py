import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("900x510")
root.resizable(False, False)

# Color Palette
PRIMARY_COLOR ="#212121"
SECONDARY_COLOR = "#00FFFF"
PRIM_SHADE1 = "#303030"
SCNDY_SHADE1 = "#228B22"

def get_font(size=9, bold=False):
    return ("TkDefaultFont", size, "bold" if bold else "normal")

def validate_input(P):
    # Allows empty string (deletion), a single minus sign, or valid floats
    if P == "" or P == "-":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False

# Conversion Logic
calc_func = {
    "cf": lambda x: x * 9/5 + 32,
    "ck": lambda x: x + 273.15,
    "fc": lambda x: (x - 32) * 5/9,
    "kc": lambda x: x - 273.15
}

calc_func["fk"] = lambda x: calc_func["ck"](calc_func["fc"](x))
calc_func["kf"] = lambda x: calc_func["cf"](calc_func["kc"](x))

def convert(from_inpt, from_unit_var, to_unit_var, res_var):
    from_u = from_unit_var.get().lower()
    # Extract first letter (C, F, or K) from strings like "Fahrenheit"
    to_u = to_unit_var.get()[0].lower()

    try:
        val = float(from_inpt.get())
    except ValueError:
        res_var.set("Error")
        return
    
    # Calculate result
    if from_u == to_u:
        res = val
    else:
        key = from_u + to_u
        res = calc_func[key](val)
    
    # Formatting output
    unit_symbol = f" °{to_u.upper()}" if to_u != "k" else f" {to_u.upper()}"
    res_var.set(f"{res:.2f}{unit_symbol}")

# Register validation
reg = root.register(validate_input)

# --- UI element ---

# Background & Container
border_frame = tk.Frame(root, bg=SECONDARY_COLOR, width=450, height=510)
border_frame.place(x=0, y=0)

left_frame = tk.Frame(border_frame, bg=PRIMARY_COLOR, width=440, height=500)
left_frame.place(x=5, y=5)

# Input Section
enter_label = tk.Label(left_frame, text="Enter Temperature", bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, font=get_font(16, True))
enter_label.place(x=30, y=50)

deg_label = tk.Entry(left_frame, text="Degree", bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, font=get_font(9))
deg_label.place(x=30, y=120)

inpt_entry = tk.Entry(left_frame, bg=PRIM_SHADE1, fg="#ffffff", insertbackground="#ffffff", borderwidth=5, relief="flat", validatecommand=(reg, "%P"), validate="key")
inpt_entry.place(x=30, y=160, width=265, height=42)

# Variables
unit_var = tk.StringVar(value="C")
convert_var = tk.StringVar(value="Fahrenheit")
result_var = tk.StringVar(value="")

# Style configuration
style = ttk.Style()
style.configure("unit.TMenubutton", background=SECONDARY_COLOR)
style.configure("convertTo.TMenubutton", background=PRIM_SHADE1)

# Dropdowns
unit_menu = ttk.OptionMenu(left_frame, unit_var, "C", "C", "F", "K", style="unit.TMenubutton")
unit_menu.place(x=300, y=160, width=50, height=42)

convert_label = tk.Label(left_frame, text="Convert To", bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, font=get_font(9))
convert_label.place(x=30, y=280)

convert_menu = ttk.OptionMenu(left_frame, convert_var, "Fahrenheit", "Celsius", "Fahrenheit", "Kelvin", style="convertTo.TMenubutton")
convert_menu.place(x=30, y=320, width=320, height=42)

# Button - Fixed command with all 4 arguments
convert_btn = tk.Button(left_frame, text="CONVERT", bg=SECONDARY_COLOR, fg=PRIMARY_COLOR, font=get_font(12, True), relief="flat", activebackground=SCNDY_SHADE1, bd=0, 
                        command=lambda: convert(inpt_entry, unit_var, convert_var, result_var))
convert_btn.place(x=150, y=420, width=140, height=40)

# Result Side
right_frame = tk.Frame (root, bg=SECONDARY_COLOR, width=450, height=510)
right_frame.place(x=450, y=0)

result_label = tk.Label(right_frame, textvariable=result_var, bg=SECONDARY_COLOR, fg=PRIMARY_COLOR, font=get_font(52, True))
result_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


root.mainloop()