import tkinter as tk
import ast

class CalculatorApp:
    """A simple calculator application using Tkinter."""

    def __init__(self, root):
        """Initialize the calculator application."""
        self.root = root
        self.root.title("Calculator")

        self.display = tk.Entry(root)
        self.display.grid(row=1, columnspan=6)

        self.create_number_buttons()
        self.create_operation_buttons()
        self.create_special_buttons()

    def create_number_buttons(self):
        """Create number buttons (1-9 and 0)."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        counter = 0

        for x in range(3):
            for y in range(3):
                button_text = numbers[counter]
                button = tk.Button(self.root, text=button_text, command=lambda text=button_text: self.get_number(text), width=4, height=4)
                button.grid(row=x+2, column=y)
                counter += 1

        zero_button = tk.Button(self.root, text="0", command=lambda: self.get_number(0), width=4, height=4)
        zero_button.grid(row=5, column=1)

    def create_operation_buttons(self):
        """Create operation buttons."""
        operations = ['+', '-', '*', '/', '%', '*3.14', '(', ')', '**', '**2']
        count = 0

        for x in range(4):
            for y in range(3):
                if count < len(operations):
                    button = tk.Button(self.root, text=operations[count], command=lambda text=operations[count]: self.get_operation(text), width=4, height=4)
                    count += 1
                    button.grid(row=x+2, column=y+3)

    def create_special_buttons(self):
        """Create special buttons (AC, =, <-)."""
        tk.Button(self.root, text="AC", width=4, height=4, command=self.clear_all).grid(row=5, column=0)
        tk.Button(self.root, text="=", width=4, height=4, command=self.calculate).grid(row=5, column=2)
        tk.Button(self.root, text="<-", width=4, height=4, command=self.undo).grid(row=5, column=4)

    def get_number(self, num):
        """Insert numbers to the entry."""
        self.display.insert(tk.END, num)

    def get_operation(self, operator):
        """Insert operations to the entry."""
        length = len(operator)
        self.display.insert(tk.END, operator)

    def clear_all(self):
        """Clear all entry values."""
        self.display.delete(0, tk.END)

    def calculate(self):
        """Calculate results of the entry."""
        entire_string = self.display.get()
        try:
            node = ast.parse(entire_string, mode="eval")
            result = eval(compile(node, '<string>', 'eval'))
            self.clear_all()
            self.display.insert(0, result)
        except Exception:
            self.clear_all()
            self.display.insert(0, "Error")

    def undo(self):
        """Undo and clear unwanted elements in the entry."""
        entire_string = self.display.get()
        if len(entire_string):
            new_string = entire_string[:-1]
            self.clear_all()
            self.display.insert(0, new_string)
        else:
            self.clear_all()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.geometry("300x300")
    root.mainloop()
