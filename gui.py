import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import time

def start_progress():
    progress.start()

    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.005)  
        progress['value'] = i
        # Update the GUI
        m.update_idletasks()
    time.sleep(0.2)
    complete = True
    if complete:
        text.pack(side='bottom', pady=10)
        m.update_idletasks()
        m.after(2000, text.config(text='Program Ending...'))
        m.title('Goodbye!')
        button.config(text='Goodbye!')
        m.update_idletasks()
        time.sleep(1)
        quit()
    progress.stop()

def selact():
    actions = askopenfilename()
    if actions:
        actbut.config(bg='spring green', text='Actions Selected ✅')

def selsta():
    statements = askopenfilename()
    if statements:
        stabut.config(bg='spring green', text='Statements Selected ✅')

m = tk.Tk(screenName=None,  baseName=None,  className='Tk',  useTk=1)
m.title('Internal Tool')
complete = False

# Select files button widgets
actbut = tk.Button(m, text="Select Actions", command=selact)
stabut = tk.Button(m, text="Select Statements", command=selsta, activebackground='white')

# Create a progressbar widget
progress = ttk.Progressbar(m, style='success.Striped.Horizontal.TProgressbar', length=300, mode="determinate")

# Button to start progress
start_button = tk.Button(m, text="Create Summary", command=start_progress, bg='turquoise', activebackground='dark turquoise')

label = tk.Label(m, text='SAC-Tools')
text = tk.Label(m, text='Summary Created!')
button = tk.Button(m, text='End Process', width=25, command=m.destroy, background='lightgray')

m.minsize(400, 300)
m.maxsize(400, 300)
label.pack(anchor='n')
actbut.place(x=50,y=25)
stabut.place(x=50,y=60)
start_button.place(x=150,y=150)
progress.place(x=50, y=190)
button.pack(side='bottom', pady=10)
m.mainloop()