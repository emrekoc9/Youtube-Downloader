from tkinter import *
import customtkinter
import pytube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Youtube Downloader")
root.minsize(width=450, height=350)
root.maxsize(width=450, height=350)

url_text = customtkinter.CTkLabel(root, text="Enter Your Youtube URL:")
url_text.pack()

user_input = customtkinter.CTkEntry(root, width=400)
user_input.pack()

path = ""

def clear():
    user_input.delete(0,1000)
def download():
    url = user_input.get()
    resolution = quality.get()
    if videoformat.get() == 2:
        try:
            yt = pytube.YouTube(url, on_progress_callback=on_progress)
            stream = yt.streams.filter(progressive=True, res=resolution).first()
            stream.download()
            progress_status.configure(text="Downloaded.")
        except:
            progress_status.configure(text="Something went wrong.")

    elif videoformat.get() == 1:
        yt = pytube.YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.get_audio_only()
        stream.download(filename=f"{yt.title}.mp3")
        progress_status.configure(text="Downloaded.")
        #except:
        #    progress_status.configure(text="Something went wrong.")
    else:
        progress_status.configure(text="Please choose mp3 or mp4")
def on_progress(stream, chunk, remaining):
    total_size = stream.filesize
    downloaded = total_size - remaining
    percentage_completed = downloaded / total_size * 100

    progress_label.configure(text="%" + str(int(percentage_completed)))
    progress_label.update()

    progress_bar.set(float(percentage_completed/100))

clear_button = customtkinter.CTkButton(root,text="Clear", command=clear)
download_button =customtkinter.CTkButton(root,text="Download",command=download)
clear_button.pack(pady=10)
download_button.pack()

def formatselected():
    global quality_exist
    if videoformat.get() == 2:
            if quality_exist == False:
                quality.place(x=300,y=260)
                quality_exist = True
    else:
        if quality_exist == True:
            quality.place_forget()
            quality_exist = False

videoformat = customtkinter.IntVar()
mp3radio = customtkinter.CTkRadioButton(root, text="mp3",value=1,variable=videoformat,command=formatselected)
mp4radio = customtkinter.CTkRadioButton(root, text="mp4",value=2,variable=videoformat,command=formatselected)
mp4radio.place(x=385,y=297)
mp3radio.place(x=385,y=325)

progress_label = customtkinter.CTkLabel(root, text="%0")
progress_label.pack(pady=10)

progress_bar = customtkinter.CTkProgressBar(root, width=300)
progress_bar.set(0)
progress_bar.pack()

progress_status = customtkinter.CTkLabel(root, text="")
progress_status.pack(pady=10)

quality_exist = False
resolutions = ["720p","360p"]
quality = customtkinter.CTkComboBox(root, values=resolutions,state="readonly")
quality.set("720p")


root.mainloop()