import tkinter as tk

values  = ""

# function here
def enter_values(value):
    global values
    global result

    values += value
    result.config(text = values)

def evaluate():
    global values
    try:
        result.config(text = eval(values))
    except ZeroDivisionError:
        result.config(text = "0")
    except:
        result.config(text = "invalid syntax")
    values = ""
    
    
def reset():
    global values
    values = ""
    

def erase():
    global values

    aval = list(values)
    
    values = ""
    try:
        aval.pop()
        for i in aval:
            values += i
        result.config(text = values)
    except:
        values = ""
        result.config(text = values)
# GUI here
window = tk.Tk()
window.title("Calulator")
window.maxsize(250,150)
window.minsize(250,150)
#snippet here

# operators
add_button = tk.Button(text = "+",  width = 8,command = lambda: enter_values("+"))
add_button.grid(row=1,column= 3)

sub_button = tk.Button(text = "-",  width = 8,command = lambda: enter_values("-"))
sub_button.grid(row= 2,column= 3)

multiply_button = tk.Button(text = "*",width = 8 ,command = lambda: enter_values("*"))
multiply_button.grid(row = 3,column = 3)

divide_button = tk.Button(text = "/",width = 8,command = lambda: enter_values("/"))
divide_button.grid(row = 4,column = 1)

evaluate = tk.Button(text = "=",width = 8,command = evaluate)
evaluate.grid(row = 4 , column = 3)

reset = tk.Button(text = "C", width = 7,command = reset)
reset.grid(row = 4,column = 2)

erase = tk.Button(text = "Erase",width = 10,command = erase)
erase.grid(row = 5,columnspan = 4)

result = tk.Label(font = (16),text = "")
result.grid(row = 0,columnspan = 3)

# first row
button1 = tk.Button(text = "1",width = 7, command  = lambda: enter_values("1"))
button1.grid(row=1,column=0)

button2 = tk.Button(text = "2",width = 7, command  = lambda: enter_values("2"))
button2.grid(row=1,column=1)

button3 = tk.Button(text = "3",width = 7, command  = lambda: enter_values("3"))
button3.grid(row=1,column=2)

# second row
button4 = tk.Button(text = "4",width = 7, command  = lambda: enter_values("4"))
button4.grid(row=2,column=0)

button5 = tk.Button(text = "5",width = 7, command  = lambda: enter_values("5"))
button5.grid(row=2,column=1)

button6 = tk.Button(text = "6",width = 7, command  = lambda: enter_values("6"))
button6.grid(row=2,column=2)

# third row
button7 = tk.Button(text = "7",width = 7, command  = lambda: enter_values("7"))
button7.grid(row=3,column=0)

button8 = tk.Button(text = "8",width = 7, command  = lambda: enter_values("8"))
button8.grid(row=3,column=1)

button9 = tk.Button(text = "9",width = 7, command  = lambda: enter_values("9"))
button9.grid(row=3,column=2)

# forth row
button0 =tk.Button(text = "0", width = 7,command = lambda: enter_values("0"))
button0.grid(row= 4,column = 0)

window.mainloop()

# bug
# geometry is not in a perfect place
# whenever there is more values in a label it make the button wider from each other
