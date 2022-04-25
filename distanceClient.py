# Importing necessary Python packages:
import sys
from tkinter import *
import socket
import pickle

# Defining server constants:
SERVER = "localhost"
PORT = 5000
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
HEADER = 8192

# Creating functions (commands) for clear, exit and table buttons created for the GUI:
def clear():
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    textarea.config(state = NORMAL)
    textarea.delete('1.0', END)
    textarea.config(state = DISABLED)

def exit():
    sys.exit()

def table():
    textarea.config(state = NORMAL)
    textarea.delete('1.0', END)

    s = txt1.get()
    e = txt2.get()
    i = txt3.get()
    
    # Checking if no values are entered in the boxes:
    if (s == "" or e == "" or i == ""):
        textarea.insert(END, "Start' - 'End' - 'Increment' must not be empty.\n")
    # Checking if boxes contain only positive numerical values:
    elif s.isdigit() == False or e.isdigit() == False or i.isdigit() == False:
        textarea.insert(END, "'Start' - 'End' - 'Increment' must contain only positive integers.\n")
    # Checking if increment value is equal to zero:
    elif i == "0":
        textarea.insert(END, "'Increment' must not be zero.\n")
    # Checking stat value is greater that end value:
    elif int(s) > int(e):
        textarea.insert(END, "'Start' must not be greater than 'End'.\n")
    else:
        # Creating client socket:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Connecting to server:
            client.connect(ADDR)

            # Sending data to client:
            client.send((s + " " + e + " " + i).encode(FORMAT))

            # Receiving lists for distances from server:
            recv_tab = client.recv(HEADER)
            table = pickle.loads(recv_tab)

            # Printing table:
            textarea.insert(END, table)
            textarea.config(state = DISABLED)
        except socket.error:
                textarea.config(state = NORMAL)
                textarea.insert(END, "Server not available.")
                textarea.config(state = DISABLED)
        finally:
            client.close()

    #textarea.config(state = DISABLED)

# Creating root instance and defining properties:
root = Tk()
root.title("Assignment 3 - Question 1")
root.geometry("300x500")
root.resizable(False, False)

# Creating label incstances, defining properties and placing them at the right position:
lbl1 = Label(text = "Stopping Distances", bg = "salmon",
             font = ("Normal", 12), bd = 1, relief = "raised")
lbl1.place(x = 0, y = 0, 
           width = 300, height = 50)

lbl2 = Label(text = "Start", bg = "gold",
             font = ("Normal", 12), anchor = "w", padx = 15,
             bd =1, relief = "raised")
lbl2.place(x = 0, y = 50, 
           width = 150, height = 50)

lbl3 = Label(text = "End", bg = "gold",
             font = ("Normal", 12), anchor = "w", padx = 15,
             bd =1, relief = "raised")
lbl3.place(x = 0, y = 100, 
           width = 150, height = 50)

lbl4 = Label(text = "Increment", bg = "gold",
             font = ("Normal", 12), anchor = "w", padx = 15,
             bd =1, relief = "raised")
lbl4.place(x = 0, y = 150, 
           width = 150, height = 50)

lbl5 = Label(bg = "forestgreen",          
             bd = 1, relief = "solid")
lbl5.place(x = 150, y = 250, 
           width = 150, height = 50)

# Creating button incstances, defining properties and placing them at the right position.
btn1 = Button(text = "Clear", bg = "forestgreen",  
              font = ("Normal", 12), anchor = "w", padx = 15,
              bd = 1, relief = "solid",
              command = clear)
btn1.place(x = 0, y = 200, 
           width = 150, height = 50)

btn2 = Button(text = "Exit", bg = "forestgreen",  
              font = ("Normal", 12), anchor = "w", padx = 15,
              bd = 1, relief = "solid",
              command = exit)
btn2.place(x = 0, y = 250, 
           width = 150, height = 50)

btn3 = Button(text = "Table", bg = "forestgreen",  
              font = ("Normal", 12), anchor = "w", padx = 15,
              bd = 1, relief = "solid",
              command = table)
btn3.place(x = 150, y = 200, 
           width = 150, height = 50)

# Creating entry instances, defining properties and placing them at the right position.
txt1 = Entry(bd = 0.5, relief = "solid",
             font = ("Normal", 12), justify = "center")
txt1.place(x =150, y = 50, 
           width = 150, height = 50)

txt2 = Entry(bd = 0.5, relief = "solid",
             font = ("Normal", 12), justify = "center")
txt2.place(x =150, y = 100, 
           width = 150, height = 50)

txt3 = Entry(bd = 0.5, relief = "solid",
             font = ("Normal", 12), justify = "center")
txt3.place(x =150, y = 150, 
           width = 150, height = 50)

# Creating test instace, defining properties and placing it at the right position.
textarea = Text(root, bg = "white", padx = 15) 
vscroll = Scrollbar(orient = VERTICAL) 
vscroll.config(command = textarea.yview) 
textarea.config(yscrollcommand = vscroll.set) 
textarea.config(state = DISABLED) 
textarea.place(x = 0,y = 300, 
               width = 300, height = 200) 
vscroll.place(x = 280, y = 300, 
              width = 20, height = 200) 

root.mainloop()