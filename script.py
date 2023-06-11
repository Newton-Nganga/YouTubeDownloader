# #pip3 install pytube
# import pytube

# link = input("Enter or Paste the youtube video url")
# yt = pytube.YouTube(link)
# yt.streams.first().download()
# print("Video download complete",link)

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube

def download_video():
    url = url_entry.get()

    try:
        # Create a YouTube object with the provided URL
        youtube = YouTube(url)

        # Get the highest resolution video
        video = youtube.streams.get_highest_resolution()

        # Ask the user to select the download location
        output_dir = filedialog.askdirectory(title="Select Output Directory")

        # Download the video
        video.download(output_dir)

        messagebox.showinfo("Download Complete", "Video downloaded successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create and position the URL entry field
url_entry = tk.Entry(window, width=40)
url_entry.pack(pady=10)

# Create the download button
download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack(pady=5)

# Start the main event loop
window.mainloop()
