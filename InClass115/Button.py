#importing the tkinter class librairy
import tkinter as tk

#defining a bitton clcik and the outcome when a button click happens
def button_click():
    print("Button clicked")
#created a root window named "Button Example" 
root = tk.Tk()
root.title("Button Example")

#creatingn the button to be within window reads clcik me and follows the button click command
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

#create loop to link button to window
root.mainloop()



