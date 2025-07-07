import tkinter as tk
from tkinter import scrolledtext
import ServerManager as SM
import os
import CryptoTools as CT

def SendMessage(ChatDisplay, MessageEntry):
    Msg = MessageEntry.get()
    if Msg.strip():
        ChatDisplay.config(state='normal')
        ChatDisplay.insert(tk.END, f"You: {Msg}\n")
        ChatDisplay.config(state='disabled')
        ChatDisplay.yview(tk.END)
        MessageEntry.delete(0, tk.END)

def UpdateText(TextField, Text):
    TextField.set(Text)

def SwitchChat(ChatLabelTextField, Name):
    print("Switched to " + Name)
    UpdateText(ChatLabelTextField, Name)

def AddFriend(ScrollableFrame):
    AddFreindPopup = tk.Tk()
    AddFreindPopup.title("Add Friend")
    AddFreindPopup.geometry("640x480")

    tk.Button(ScrollableFrame, text="Name", bg="#f0f0f0", height=1, width=17, command=lambda n="Name": SwitchChat("Name"), anchor="w", justify="left").pack(padx=10)
    print("Added Friend")

def StartServerConection(ID):
    print("Getting a connection from the person with ID : " + ID)

def GetLatestVersion():
    return "1.1.1"

def UpdateToLatestVersion():
    print("Updating version")
    DataUnencrypted = [
        GetLatestVersion(),
        "A24SDFD134AR34Gksjgnk432j3agnjk",
        "[Dana, 7/6/2025, 15:15] : Hello, this is Dana from the CDC."
    ]
    EncryptedData = []
    for Line in DataUnencrypted:
        EncryptedData.append(CT.EncryptText(Line, CT.GetUniqueComputerCodeForFileEncryption()) + "\n")
    return EncryptedData

def CheckVersion(Lines, Name):
    print("Checking version")
    print("Versions are " + Lines[0] + " vs " + GetLatestVersion() + " (Current : Latest)")
    if Lines[0] != GetLatestVersion():
        Lines = UpdateToLatestVersion()
        with open("SafeChat/People/" + Name, "w") as File:
            File.writelines(Lines)
    return Lines

def LoadChat(Name, ChatDisplay):
    print(Name + " is being loaded")
    with open("SafeChat/People/" + Name) as File:
        Encrypted = File.readlines()
        Decrypted = []
        for Line in Encrypted:
            Decrypted.append(CT.DecryptText(Line, CT.GetUniqueComputerCodeForFileEncryption()).replace("\n", ""))
        Lines = Decrypted
        if not Decrypted:
            print("Could not decrypt file: " + str(Name))
            return
        print(Lines)
        Lines = CheckVersion(Lines, Name)
        if not Lines or len(Lines) < 2:
            print("File " + str(Name) + " missing required lines.")
            return
    StartServerConection(Lines[1])
    i = 2
    while i < len(Lines):
        Message = tk.StringVar()
        Message.set(Lines[i])
        TKEntry = tk.Entry(textvariable=Message)
        SendMessage(ChatDisplay, TKEntry)
        print(Lines[i])
        i += 1

def GetFriendsList(ChatDisplay):
    print("Friend List")
    Directory = 'SafeChat/People/'
    TxtFiles = [file for file in os.listdir(Directory) if file.endswith('.txt')]
    ParsedTxtFilesNames = []
    print("------------------------------------------------------------")
    for File in TxtFiles:
        LoadChat(File, ChatDisplay)
        ParsedTxtFilesNames += [File.replace(".txt", "").replace("_", " ")]
        print("------------------------------------------------------------")
    return ParsedTxtFilesNames