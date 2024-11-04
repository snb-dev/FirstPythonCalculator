import tkinter as tk

values = []

window = tk.Tk()
window.title("Calculator")
window.geometry("600x400")

expression = tk.StringVar()

top_frame = tk.Frame(window, bg = "lightblue", width= 400, height = 200 )
top_frame.pack(fill="x")

add_value = tk.Entry(top_frame, textvariable=expression, width= 300, font= ("Arial", 16))
values = tk.Entry(window)
add_value.pack(pady=10, padx= 10)

def button_click(value):
    current = expression.get()
    expression.set(current + str(value))

def clear_display():
    expression.set("")

def calculate():
    try:
        result = eval(expression.get())
        expression.set(result)
    except Exception as e:
        expression.set("Error")

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

buttonOne = tk.Button(button_frame, text="1", width=5, command=lambda t="1": button_click(t) )
buttonOne.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

buttonTwo = tk.Button(button_frame, text="2", width=5, command=lambda t="2": button_click(t) )
buttonTwo.grid(row=0, column=10, columnspan= 10, pady=10, padx=10)

buttonThree = tk.Button(button_frame, text="3", width=5, command=lambda t="3": button_click(t) )
buttonThree.grid(row=0, column=20, columnspan= 10, pady=10, padx=10)

buttonFour = tk.Button(button_frame, text="4", width=5, command=lambda t="4": button_click(t) )
buttonFour.grid(row=2, column=0, columnspan= 10, pady=10, padx=10)

buttonFive = tk.Button(button_frame, text="5", width=5, command=lambda t="5": button_click(t) )
buttonFive.grid(row=2, column=10, columnspan= 10, pady=10, padx=10)

buttonSix = tk.Button(button_frame, text="6", width=5, command=lambda t="6": button_click(t) )
buttonSix.grid(row=2, column=20, columnspan= 10, pady=10, padx=10)

buttonSeven = tk.Button(button_frame, text="7", width=5, command=lambda t="7": button_click(t) )
buttonSeven.grid(row=4, column=0, columnspan= 10, pady=10, padx=10)

buttonEight = tk.Button(button_frame, text="8", width=5, command=lambda t="8": button_click(t) )
buttonEight.grid(row=4, column=10, columnspan= 10, pady=10, padx=10)

buttonNine = tk.Button(button_frame, text="9", width=5, command=lambda t="9": button_click(t) )
buttonNine.grid(row=4, column=20, columnspan= 10, pady=10, padx=10)

buttonZero = tk.Button(button_frame, text="0", width=5, command=lambda t="0": button_click(t) )
buttonZero.grid(row=6, column=10, columnspan= 10, pady=10, padx=10)

buttonPlus = tk.Button(button_frame, text="+", width=5, command=lambda t="+": button_click(t) )
buttonPlus.grid(row=4, column=50, columnspan= 10, pady=10, padx=10)


buttonSub = tk.Button(button_frame, text="-", width=5, command=lambda t="-": button_click(t) )
buttonSub.grid(row=4, column=60, columnspan= 10, pady=10, padx=10)

buttonDiv = tk.Button(button_frame, text="/", width=5, command=lambda t="/": button_click(t) )
buttonDiv.grid(row=2, column=50, columnspan= 10, pady=10, padx=10)

buttonMul = tk.Button(button_frame, text="X", width=5, command=lambda t="*": button_click(t) )
buttonMul.grid(row=2, column=60, columnspan= 10, pady=10, padx=10)

buttonC = tk.Button(button_frame, text="C", width=5, command=clear_display)
buttonC.grid(row=0, column=50, columnspan= 10, pady=10, padx=10)

buttonMod = tk.Button(button_frame, text="%", width=5, command=lambda t="%": button_click(t) )
buttonMod.grid(row=0, column=60, columnspan= 10, pady=10, padx=10)

buttonEuq = tk.Button(button_frame, text="=", width=5, command=calculate)
buttonEuq.grid(row=6, column=55, columnspan= 10, pady=10, padx=10)




window.mainloop()
