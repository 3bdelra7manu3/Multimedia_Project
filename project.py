from tkinter import Tk, Entry, Button, Label, messagebox , Frame
import yt_dlp
import webbrowser as wb

def start_vid(res):
    url = link_entry.get()
    if not url:
        messagebox.showerror("Error", "That's Not A Valid Link.")
        return
    try:
        ydl_opts = {}
        if res == "highest":
            ydl_opts = {'format': 'bestvideo'}
        elif res == "lowest":
            ydl_opts = {'format': 'bestvideo'}
        elif res == "audio_only":
            ydl_opts = {'format': 'bestaudio'}
        else:
            messagebox.showerror("Error", "Please Select An Valid Resolution Opt.")
            return
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url', None)
            if not video_url:
                messagebox.showerror("Error", f"No streams available for {res} resolution.")
            else:
                wb.open(video_url)
    except yt_dlp.utils.DownloadError as err:
        messagebox.showerror("Download Error", f"Could not process the video: {err}")
    except Exception as err:
        messagebox.showerror("Error", f"An unexpected error occurred: {err}")



root = Tk()


root.title("Multimedia Downloader Script.")
Label(root, text="Paste Your Link Here:-").pack(pady=5)
link_entry = Entry(root, width=50)
link_entry.pack(pady=5)
btn_frame = Frame(root)
btn_frame.pack(pady=5)
highest_res_btn = Button(btn_frame, text="High Resolution", command=lambda: start_vid("highest"))
highest_res_btn.pack(side="left", padx=5)
lowest_res_btn = Button(btn_frame, text="Low Resolution", command=lambda: start_vid("lowest"))
lowest_res_btn.pack(side="left", padx=5)
audio_btn = Button(root, text="Audio Only", command=lambda: start_vid("audio_only"))
audio_btn.pack(pady=5)



root.mainloop()