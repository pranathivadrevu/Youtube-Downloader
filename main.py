import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        Video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        Video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download Error!", text_color = "red")
    





#ssystem settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our App frame

app = customtkinter.CTk() #Initilaize it for
app.geometry("720x480") #resolution
app.title("Youtube Downloader")

# Adding UI elements

title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx= 10, pady=10)

#Linkl Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width= 350, height=40, textvariable=url_var)
link.pack()


# Finished Downlaoding

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()


# Download Button

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# run as a Look or run app
app.mainloop()
