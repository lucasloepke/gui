import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()

    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.01)  
        progress['value'] = i
        # Update the GUI
        m.update_idletasks()
    time.sleep(0.2)
    progress.stop()

m = tk.Tk(screenName=None,  baseName=None,  className='Tk',  useTk=1)
m.title('Internal Tool')

# Create a progressbar widget
progress = ttk.Progressbar(m, orient="horizontal", length=300, mode="determinate")

# Button to start progress
start_button = tk.Button(m, text="Start Progress", command=start_progress, background='springgreen')

label = tk.Label(m, text='SAC-Tools')

button = tk.Button(m, text='End Process', width=25, command=m.destroy, background='lightgray')

m.minsize(400, 300)
m.maxsize(400, 300)
label.pack(anchor='n')
start_button.pack(pady=10)
progress.pack(pady=20)
button.pack(side='bottom', pady=10)
m.mainloop()