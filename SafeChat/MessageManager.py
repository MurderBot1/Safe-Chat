import tkinter as tk
from tkinter import scrolledtext
import ServerManager as SM

def SendMessage(ChatDisplay, MessageEntry):
    Msg = MessageEntry.get()
    if Msg.strip():
        ChatDisplay.config(state='normal')
        ChatDisplay.insert(tk.END, f"You: {Msg}\n")
        ChatDisplay.config(state='disabled')
        ChatDisplay.yview(tk.END)
        MessageEntry.delete(0, tk.END)
    