import tkinter
import customtkinter
from pytube import YouTube
from tkinter import messagebox, filedialog
import webbrowser

def clear():
	finishLabelone.configure(text="")
	finishLabeltwo.configure(text="")
	progressBar.set(float(0))
	pPercentage.configure(text='0%')
	link.delete(0, "end")
	destination.delete(0, "end")

def open_browser():
	webbrowser.open_new('https://www.youtube.com')

def Browse():
    download_File = filedialog.asksaveasfile(
        initialdir="YOUR DIRECTORY PATH", title="Save Video", filetypes=(("MP4", ".mp4"), ("All Files", "*.*")), defaultextension=(".mp4"))
    if download_File is not None:
        download_Directory = download_File.name
        download_File.close()
        save_var.set(download_Directory)

def startHighResDownload():
	try:
		ytLink = link.get() # Gets input of the link to be downloaded
		path = destination.get() #getting the location where the video needs to be downloaded
		ytObject = YouTube(ytLink, on_progress_callback=on_progress)
		video = ytObject.streams.get_highest_resolution()
		video.download(path)
		finishLabelone.configure(text="Download Complete", text_color="Green")
		finishLabeltwo.configure(text="High Resolution Video: " + ytObject.title, text_color="White")
	except:
		finishLabelone.configure(text="Download Failed", text_color="Red")
		finishLabeltwo.configure(text="")

def startLowResDownload():
	try:
		ytLink = link.get()
		path = destination.get() #getting the location where the video needs to be downloaded
		ytObject = YouTube(ytLink, on_progress_callback=on_progress)
		video = ytObject.streams.get_lowest_resolution()
		video.download(path)
		finishLabelone.configure(text="Download Complete", text_color="Green")
		finishLabeltwo.configure(text="Last Video Downloaded (Low Res): " + ytObject.title, text_color="White")
	except:
		finishLabelone.configure(text="Download Failed", text_color="Red")
		finishLabeltwo.configure(text="")

def startAudioDownload():
	try:
		ytLink = link.get()
		path = destination.get() #getting the location where the video needs to be downloaded
		ytObject = YouTube(ytLink, on_progress_callback=on_progress)
		video = ytObject.streams.get_audio_only()
		video.download(path)
		finishLabelone.configure(text="Download Complete", text_color="Green")
		finishLabeltwo.configure(text="Last Audio Downloaded: " + ytObject.title, text_color="White")
	except:
		finishLabelone.configure(text="Download Failed", text_color="Red")
		finishLabeltwo.configure(text="")

def on_progress(stream, chunk, bytes_remaining):
	total_size = stream.filesize
	bytes_downloaded = total_size - bytes_remaining
	percentage_of_completion = bytes_downloaded / total_size * 100
	per =str(int(percentage_of_completion))
	pPercentage.configure(text=per + '%')
	pPercentage.update()

	# Update progress bar
	progressBar.set(float(percentage_of_completion) / 100)


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("860x300")
app.title("Altimit Youtube Video Downloader | Version: Alpha 0.3")

# Make the window non-resizable

app.resizable(False, False)


headerLabel = customtkinter.CTkLabel(app, text="ALTIMIT YOUTUBE VIDEO DOWNLOADER", font=("ariel", 32))
headerLabel.grid(row=0, columnspan=4, padx=0, pady=10)

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert YouTube URL")
title.grid(row=1, column=0, padx=10, pady=10, sticky="E")

# Link Input
url_var=tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.grid(row=1, column=1, padx=10, pady=10)

# Get Youtube Link Button
getyoutubelink = customtkinter.CTkButton(app, text="YouTube.com", command=open_browser)
getyoutubelink.grid(row=1, column=2, padx=10, pady=10)

savefiletitle = customtkinter.CTkLabel(app, text="Save File Location")
savefiletitle.grid(row=2, column=0, padx=10, pady=10, sticky="E")

save_var=tkinter.StringVar()
destination = customtkinter.CTkEntry(app, width=350, height=40, textvariable=save_var)
destination.grid(row=2, column=1, padx=10, pady=10)

# Browse Button
savelocation = customtkinter.CTkButton(app, text="Browse", command=Browse)
savelocation.grid(row=2, column=2, padx=10, pady=10)

# Finished Downloading
finishLabelone = customtkinter.CTkLabel(app, text="")
finishLabelone.grid(row=3, column=0, padx=10, pady=10,sticky="E")
finishLabeltwo = customtkinter.CTkLabel(app, text="")
finishLabeltwo.grid(row=7, column=1, padx=10, pady=10)

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.grid(row=3, column=1, sticky="E")

progressBar = customtkinter.CTkProgressBar(app, width=325)
progressBar.set(0)
progressBar.grid(row=3, column=1)

# Download High Resolution Button
highdownload = customtkinter.CTkButton(app, text="Download Video", command=startHighResDownload)
highdownload.grid(row=4, column=0, padx=30, pady=10, sticky="E")

# Clear Button
clearbutton = customtkinter.CTkButton(app, text="Reset", command=clear)
clearbutton.grid(row=4, column=1, padx=10, pady=20)

# Download Audio Button
audiodownload = customtkinter.CTkButton(app, text="Download Audio", command=startAudioDownload)
audiodownload.grid(row=4, column=2, padx=0, pady=10)

# Clear Button
clearbutton = customtkinter.CTkButton(app, text="Reset", command=clear)
clearbutton.grid(row=4, column=1, padx=10, pady=20)

# Run app
app.mainloop()
