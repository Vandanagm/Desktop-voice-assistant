from tkinter import *

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#7F8FAF")

# Configure the grid to have three columns
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=1)

frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#90EE90")
frame.grid(row=0, column=1, padx=55, pady=10)

text_label = Label(frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#90EE90")
text_label.grid(row=0, column=0, padx=20, pady=20)

root.mainloop()
