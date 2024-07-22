import customtkinter as ctk
from tkinter.filedialog import askopenfilename

def button_function():
    # print(askopenfilename())
    quit()

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

m = ctk.CTk()  # create CTk window like     you do with the Tk window
m.geometry("400x300")
m.title("Expensive Statements Summary")

# Frame
frame = ctk.CTkFrame(master=m, width=380, height=280, border_color='red')
frame.place(x=10, y=10)
frame.pack_propagate(0)  # Prevent frame from resizing

# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=frame, text="End Process", command=button_function)
button.pack(side='bottom', pady=10)

# Window Packing
m.minsize(400, 300)
m.maxsize(400, 300)

m.mainloop()