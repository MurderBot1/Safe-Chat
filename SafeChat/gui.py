import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Hello, Tkinter!")

# Set the window size
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Add a button
def on_button_click():
    label.config(text="Button Clicked!")
def send_message():
    label.config(text="Message Sent!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)
button2 = tk.Button(root, text="Send", command=send_message)
button2.pack(pady=10)

# Run the application
root.mainloop()