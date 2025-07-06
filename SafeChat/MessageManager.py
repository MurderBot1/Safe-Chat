import tkinter as tk
from tkinter import scrolledtext
import ServerManager as SM
import os

def SendMessage(ChatDisplay, MessageEntry):
    Msg = MessageEntry.get()
    if Msg.strip():
        ChatDisplay.config(state='normal')
        ChatDisplay.insert(tk.END, f"You: {Msg}\n")
        ChatDisplay.config(state='disabled')
        ChatDisplay.yview(tk.END)
        MessageEntry.delete(0, tk.END)

def SwitchChat(Name):
    print("Switched to " + Name)

def AddFriend(ScrollableFrame):
    AddFreindPopup = tk.Tk()
    AddFreindPopup.title("Add Friend")
    AddFreindPopup.geometry("640x480")

    tk.Button(ScrollableFrame, text="Name", bg="#f0f0f0", height=1, width=17, command=lambda n="Name": SwitchChat("Name"), anchor="w", justify="left").pack(padx=10)
    print("Added Friend")

def GetFriendsList():
    print("Friend List")
    
    return ["Dana Avan","Charlie Vince","Alice Prince","Bob Devani"]