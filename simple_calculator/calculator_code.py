import tkinter as tk
from math import sqrt


class Calc:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x350")

        # Title shown
        self.title_frame = tk.LabelFrame(self.window, bg='black')
        self.window_title = tk.Label(self.title_frame, text="My Calculator", font="Arial 30 bold italic",
                                     bg='lightblue', fg='darkblue')
        self.window_title.pack()
        self.title_frame.pack()

        # Expression that will be evaluated as Python code
        self.expression = ""
        # Equation is what is shown on the widget
        self.equation = tk.StringVar()  # StringVar objects hold string values linked to widget properties
        # Widget
        self.entryframe = tk.LabelFrame(self.window, bg='lightyellow')
        self.ops = tk.Entry(self.entryframe, textvariable=self.equation, font=('Helvetica', 12), width=20)
        self.ops.grid(row=0, column=0)
        self.del_btn = tk.Button(self.entryframe, text='DEL', command=self.delete, bg='orange')
        self.del_btn.grid(row=0, column=1)
        self.entryframe.pack(pady=15)

        # Widget for buttons
        self.buttonframe = tk.LabelFrame(self.window, fg='lightblue')
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        n_rows = 4
        n_cols = 4
        font = ('Arial', 15)
        # Generate buttons for the 9 digits
        for row in range(1, 4):
            for column in range(3):
                number = 3 * (3 - row) + column + 1
                self.btn = tk.Button(self.buttonframe, text=str(number), command=lambda number=number: self.press(number), font=font)
                self.btn.grid(row=row, column=column, sticky=tk.E+tk.W)

        # Operations
        operations = {'/': '/', 'x': '*', '-': '-', '+': '+'}
        for index, (k, v) in enumerate(operations.items()):
            self.btn = tk.Button(self.buttonframe, text=k, command=lambda v=v: self.press(v), font=font)
            self.btn.grid(row=index, column=3, sticky=tk.E+tk.W)

        # Zero
        self.btn_zero = tk.Button(self.buttonframe, text='0', command=lambda: self.press('0'), font=font)
        self.btn_zero.grid(row=4, column=0)

        # Decimals
        self.btn_dec = tk.Button(self.buttonframe, text='.', command=lambda: self.press('.'), font=font)
        self.btn_dec.grid(row=4, column=1, sticky=tk.E + tk.W)

        # Clear
        self.btn_clear = tk.Button(self.buttonframe, text="AC", command=self.clear, font=('Arial', 10))
        self.btn_clear.grid(row=4, column=2, sticky=tk.E + tk.W + tk.S + tk.N)

        # Equal
        self.btn_equal = tk.Button(self.buttonframe, text="=", command=self.press_equal, font=font)
        self.btn_equal.grid(row=4, column=3, sticky=tk.E + tk.W)

        # Square root
        self.btn_sqrt = tk.Button(self.buttonframe, text='√', command=self.press_sqrt, font=font)
        self.btn_sqrt.grid(row=0, column=0, sticky=tk.E + tk.W)

        # Parentheses
        self.btn_l = tk.Button(self.buttonframe, text='(', command=lambda: self.press('('), font=font)
        self.btn_r = tk.Button(self.buttonframe, text=')', command=lambda: self.press(')'), font=font)
        self.btn_l.grid(row=0, column=1, sticky=tk.E + tk.W)
        self.btn_r.grid(row=0, column=2, sticky=tk.E + tk.W)

        self.buttonframe.pack()

        self.window.mainloop()

    def press(self, num):
        self.expression += str(num)
        self.equation.set(self.expression)

    def press_sqrt(self):
        self.expression += 'sqrt'
        self.equation.set(self.expression)

    def clear(self):
        self.expression = ""
        self.equation.set("")

    def delete(self):
        self.expression = self.expression[:-1]
        self.equation.set(self.expression)

    def press_equal(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = total
        except ZeroDivisionError:
            self.equation.set('Cannot divide by zero')
            self.expression = ''
        except:
            self.equation.set('Error')
            self.expression = ''


calcu = Calc()
