#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

#Explore California Touring Company
#Desert to Sea Tour

# 1. display logo
# 2. Name, Email Address, Multiline comments
# 3. Submit & Clear buttons

#Submit- 
# Print contents of input fields to the console
# Empty content of input field
# Notify the user that comment were submitted

#Clear-
# Empty the input fields
 



from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):  
        
        # Displsy logo
        self.logo = PhotoImage(file = "/Users/cecilee/PythonProjects/Lynda.com/4_Ex_Files_Python_Tkinter/Exercise Files/Ch08/tour_logo.gif")
        self.label_logo = ttk.Label(master, image = self.logo)
        self.label_logo.grid(row = 0, column = 0, stick = 'nsew', padx = 10, pady = 10)
        
        # Name
        self.label_name = ttk.Label(master, text = "Name: ")
        self.label_name.grid(row = 1, column = 0, stick = 'nsew')
        self.entry_name = ttk.Entry(master, width = 50)
        self.entry_name.grid(row = 1, column = 1, columnspan = 4, stick = 'nsew')
        self.entry_name.insert(0, "Enter your name.")
                    
        # Email
        self.label_email = ttk.Label(master, text = "Email: ")
        self.label_email.grid(row = 2, column = 0, stick = 'nsew')
        self.entry_email = ttk.Entry(master, width = 50)
        self.entry_email.grid(row = 2, column = 1, columnspan = 4, stick = 'nsew')
        self.entry_email.insert(0, "Enter your email.")
        
        # Multiline comments
        self.label_comments = ttk.Label(master, text = "Comments: ")
        self.label_comments.grid(row = 3, column = 0, stick = 'nsew')
        self.text_comments = Text(master, width = 50, height = 10)
        self.text_comments.grid(row = 3, column = 1, columnspan = 4, stick = 'nsew')
        self.text_comments.insert(1.0, "Enter your comments.")

        # Submit button
        self.button_submit = ttk.Button(master, text = "Submit")
        self.button_submit.grid(row = 4, column = 1, columnspan = 2, stick = 'nsew', padx = 40, pady = 10)
        self.button_submit.config(command = self.callback_sumbit)
        
        # Clear submit
        self.button_clear = ttk.Button(master, text = "Clear")
        self.button_clear.grid(row = 4, column = 3, columnspan = 2, stick = 'nsew', padx = 40, pady = 10)
        self.button_clear.config(command = self.callback_clear)
        
    def callback_sumbit(self):
        print(self.entry_name.get())
        print(self.entry_email.get())
        print(self.text_comments.get('1.0', 'end'))        
        messagebox.showinfo(title = None, message = "Thanks for you feedback!")
    
    def callback_clear(self):
        self.entry_name.delete(0, END)
        self.entry_email.delete(0, END)
        self.text_comments.delete('1.0', 'end')
            
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
