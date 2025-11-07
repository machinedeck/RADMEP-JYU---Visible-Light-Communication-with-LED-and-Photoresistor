# From https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/?ref=lbp

from tkinter import *
from tkinter import messagebox
from pyarduino_comm import info_transfer
# Initiate window
interface = Tk()
interface.configure(background = "gray")

interface.title("LiFi 8-bit Transmitter Protocol - Alpha Version")

# Window size
interface.geometry('480x70')

port = 'COM4'

def entered_value():
    text_value = text.get()
    if text_value.isdigit() == True:
        if int(text_value) >=0 and int(text_value) < 256 and len(text_value) <= 3 and int(text_value[0]) != 0:
            print("True")
            print(text_value)
            text.delete(0, END)
            text.insert(0, "SENDING.......")
            messagebox.showinfo(" ", "Data will be sent now, click \"OK\". Please wait until transmission is done, ありがとう!")
            number = int(text_value)
            intr = info_transfer(port, number)
            intr.run()
            text.delete(0, END)
            text.insert(0, "ニース, 進め!!!!")
            messagebox.showinfo(" ", "Done!")
            text.delete(0, END)
            
        else:
            print("False")
            text.delete(0, END)
            text.insert(0, "ERRORRRR!!!!")
            messagebox.showerror("Incorrect Input", "Data should be a non-negative integer less than 256, having at most three digits and not starting with 0.")
            text.delete(0, END)

        
    else:
        print("False")
        text.delete(0, END)
        text.insert(0, "ERRORRRR!!!!")
        messagebox.showerror("Incorrect Input", "Data should be a non-negative integer less than 256, having at most three digits and not starting with 0.")
        text.delete(0, END)

def delete_value():
    text.delete(0, END)

# # Add text
text = Entry(interface, width = 15, 
             borderwidth = 2, 
             font = "Arial_Baltic 30",
             background = "black",
             fg = "green",
             justify = RIGHT)

text.place(x = 10, y = 10)

enterbtn = Button(interface,
                  text = "OK!",
                  fg = "black",
                  font = "Arial_Baltic 11",
                  height = 2,
                  width = 5,
                  command = entered_value)
enterbtn.place(x = 355, y = 11)

escbtn = Button(interface,
                  text = "C",
                  fg = "white",
                  bg = "red",
                  font = "Arial_Baltic 11",
                  height = 2,
                  width = 5,
                  command = delete_value)
escbtn.place(x = 414, y = 11)

interface.mainloop()