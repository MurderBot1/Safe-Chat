import tkinter as tk
from tkinter import scrolledtext
import MessageManager

# Create the main window
Root = tk.Tk()
Root.title("SafeChat")
Root.geometry("1920x1080")

# Left sidebar for people
PeopleFrame = tk.Frame(Root, width=150, bg="#f0f0f0")
PeopleFrame.pack(side=tk.LEFT, fill=tk.Y)

PeopleLabel = tk.Label(PeopleFrame, text="People", bg="#f0f0f0", font=("Arial", 12, "bold"))
PeopleLabel.pack(pady=10)

# Add dummy people
for Name in ["Alice", "Bob", "Charlie", "Dana"]:
    tk.Label(PeopleFrame, text=Name, bg="#f0f0f0").pack(anchor="w", padx=10)

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

# Run the app
Root.mainloop()