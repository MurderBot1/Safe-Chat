import tkinter as tk
from tkinter import scrolledtext
import MessageManager
from PIL import Image, ImageTk

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Chat.SafeChat")

# Create the main window
Root = tk.Tk()
Root.title("SafeChat")
Root.geometry("1280x720")
Logo = Image.open("Logo.png")
Logo = ImageTk.PhotoImage(Logo)
Root.iconphoto(True, Logo)

# Left sidebar for people
PeopleFrame = tk.Frame(Root, width=150, bg="#f0f0f0")
PeopleFrame.pack(side=tk.LEFT, fill=tk.Y)
AddPeopleFrame = tk.Frame(PeopleFrame, height=50, bg="#f0f0f0")
AddPeopleFrame.pack(side=tk.BOTTOM, fill=tk.X)

PeopleLabel = tk.Label(PeopleFrame, text="People", bg="#f0f0f0", font=("Arial", 12, "bold"))
PeopleLabel.pack(pady=10)

# Create a canvas and a vertical scrollbar for scrolling it
Canvas = tk.Canvas(PeopleFrame, width=150)
Scrollbar = tk.Scrollbar(PeopleFrame, orient="vertical", command=Canvas.yview)
ScrollableFrame = tk.Frame(Canvas)

AddPeopleButton = tk.Button(AddPeopleFrame, text="Add people", command=lambda: MessageManager.AddFriend(ScrollableFrame)).pack(padx=5, pady=5)

# Configure the scrollable region
ScrollableFrame.bind(
    "<Configure>",
    lambda e: Canvas.configure(
        scrollregion=Canvas.bbox("all")
    )
)

# Embed the frame in the Canvas
Canvas.create_window((0, 0), window=ScrollableFrame, anchor="nw")
Canvas.configure(yscrollcommand=Scrollbar.set)

def _on_mousewheel(event):
    Canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Pack Scrollbar
Canvas.pack(side="left", fill="both", expand=True)
Scrollbar.pack(side="right", fill="y")

Names = MessageManager.GetFriendsList()  # Get the list of friends from the server

# Add dummy people
for Name in Names:
    tk.Button(ScrollableFrame, text=Name, bg="#f0f0f0", height=1, width=17, command=lambda n=Name: MessageManager.SwitchChat(n), anchor="w", justify="left").pack(padx=10)

# Main chat area
ChatFrame = tk.Frame(Root)
ChatFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Scrollable text area
ChatDisplay = scrolledtext.ScrolledText(ChatFrame, wrap=tk.WORD, state='disabled')
ChatDisplay.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Message entry and send button
EntryFrame = tk.Frame(ChatFrame)
EntryFrame.pack(fill=tk.X, padx=10, pady=5)

MessageEntry = tk.Entry(EntryFrame)
MessageEntry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

SendButton = tk.Button(EntryFrame, text="Send", command=lambda: MessageManager.SendMessage(ChatDisplay, MessageEntry))
SendButton.pack(side=tk.RIGHT)

EntryFrame.bind('<Return>', lambda event: MessageManager.SendMessage(ChatDisplay, MessageEntry))

# Run the app
Root.mainloop()