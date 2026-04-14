import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Labels and Buttons")

# Create a label
label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=10)

# Create a button
button = tk.Button(window, text="Click Me!")
button.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()
