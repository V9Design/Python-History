import tkinter as tk
from tkinter import font

class CalculatorModern:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Modern")
        self.root.geometry("320x480")
        self.root.resizable(False, False)

        # Color Configuration
        self.bg_color = "#212121"
        self.btn_color = "#333333"
        self.btn_active = "#4a4a4a"
        self.op_color = "#ff9500"
        self.op_active = "#ffb340"
        self.text_color = "#ffffff"
        self.eq_color = "#4cd964"

        self.root.configure(bg=self.bg_color)

        # Variable to store expressions
        self.expression = ""
        self.display_var = tk.StringVar()

        # Custom font
        self.font_large = font.Font(family='Segoe UI', size=32, weight='bold')
        self.font_medium = font.Font(family='Segoe UI', size=14, weight='bold')

        self.create_widgets()

    def create_widgets(self):
        # Display
        display_frame = tk.Frame(self.root, bg=self.bg_color)
        display_frame.pack(expand=True, fill='both', padx=10, pady=10)

        display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=self.font_large,
            bg=self.bg_color,
            fg=self.text_color,
            anchor="e",
            justify="right"
        )
        display_label.pack(expand=True, fill='both')

        # Buttons
        buttons_frame = tk.Frame(self.root, bg=self.bg_color)
        buttons_frame.pack(expand=True, fill='both', padx=10, pady=10)

        # Grid Configuration
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        
        # First to third row button layout
        # Format: (text, row, column)
        layout_simple = [
            ('C', 0, 0), ('√', 0, 1), ('%', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('2', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
        ]

        for (text, row, col) in layout_simple:
            self.create_button(buttons_frame, text, row, col)

        # Last row layout (special)
        # Button 0 (2 columns wide)
        self.create_button(buttons_frame, '0', 4, 0, span=2)
            
        # Button ( . )
        self.create_button(buttons_frame, '.', 4, 2)
            
        # Button ( = )
        self.create_button(buttons_frame, '=', 4, 3, is_equal=True)

        # Configure rows to be proportional
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
    
    def create_button(self, parent, text, row, col, span=1, is_equal=False):
        # Color determination logic
        if text in ['/', '*', '-', '+']:
            bg = self.op_color
            fg = self.text_color
            active_bg = self.op_active
            hover_bg = "#e08900"
        elif text == '=' or is_equal:
            bg = self.eq_color
            fg = self.text_color
            active_bg = "#5ae077"
            hover_bg = "#3cb054"
        elif text == 'C':
            bg = "#a5a5a5"
            fg = "#000000"
            active_bg = "#cfcfcf"
            hover_bg = "#dcdcdc"
        else:
            bg = self.btn_color
            fg = self.text_color
            active_bg = self.btn_active
            hover_bg = "#555555"

        btn = tk.Button(
            parent,
            text=text,
            font=self.font_medium,
            bg=bg,
            fg=fg,
            activebackground=active_bg,
            activeforeground=fg,
            borderwidth=0,
            cursor="hand2",
            command=lambda: self.on_button_click(text)
        )

        # Grid Placement
        btn.grid(row=row, column=col, columnspan=span, sticky="nsew", padx=2, pady=2)

        # Hover Effect
        btn.bind("<Enter>", lambda e, b=btn, h=hover_bg: b.config(bg=h))
        btn.bind("<Leave>", lambda e, b=btn, h=bg: b.config(bg=h))
    
    def on_button_click(self, char):
        if char == 'C':
            self.clear_display()
        elif char == '=':
            self.calculate()
        elif char == '√':
            try:
                result = float(eval(self.expression)) ** 0.5
                self.expression = str(result)
                self.display_var.set(self.expression)
            except:
                self.display_var.set("Error")
                self.expression = ""
        elif char == '%':
            try:
                result = float(eval(self.expression)) / 100
                self.expression = str(result)
                self.display_var.set(self.expression)
            except:
                self.display_var.set("Error")
                self.expression = ""
        else:
            self.append_to_expression(char)
    
    def append_to_expression(self, char):
        self.expression += str(char)
        self.display_var.set(self.expression)
    
    def clear_display(self):
        self.expression = ""
        self.display_var.set("")
    
    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.display_var.set("Error")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = CalculatorModern(root)
    root.mainloop()