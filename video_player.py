import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import video_library as lib  
from check_videos import CheckVideos
from tkinter import messagebox
from tkinter import filedialog
import csv

class LibraryItem:
    def __init__(self, name, director, rating):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0
    
    def info(self):
        return f"{self.name} directed by {self.director}, rated {self.rating}, played {self.play_count} times"

library = {}

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        
        self.library_items = []

        self.create_widgets()

    def create_widgets(self):
        self.check_videos_button = tk.Button(self.root, text="Check Videos", command=self.check_videos)
        self.check_videos_button.pack()

        self.create_video_list_button = tk.Button(self.root, text="Create Video List", command=self.create_video_list)
        self.create_video_list_button.pack()

        self.update_videos_button = tk.Button(self.root, text="Update Videos", command=self.update_videos)
        self.update_videos_button.pack()

        self.load_library_button = tk.Button(self.root, text="Load Library", command=self.load_library)
        self.load_library_button.pack()

        self.library_listbox = tk.Listbox(self.root)
        self.library_listbox.pack(fill=tk.BOTH, expand=True)

    def check_videos(self):
        pass

    def create_video_list(self):
        pass

    def update_videos(self):
        pass

    def load_library(self):
        file_path = "video_library.csv"  
        self.library_items = LibraryItem.read_library(file_path)
        self.update_library_listbox()

    def update_library_listbox(self):
        self.library_listbox.delete(0, tk.END)
        for item in self.library_items:
            self.library_listbox.insert(tk.END, item.info())

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return

def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return

class CheckVideos:
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Check Videos")

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def check_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            lib.increment_play_count(key)  
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(window))

def create_video_list_clicked():
    video_list = lib.list_all()
    messagebox.showinfo("Video List", video_list)
    status_lbl.configure(text="Create Video List button was clicked!")

def update_videos_clicked():
    update_window = tk.Toplevel(window)
    update_window.geometry("300x200")
    update_window.title("Update Video Rating")
    
    tk.Label(update_window, text="Video Key:").pack(pady=5)
    entry_key = tk.Entry(update_window)
    entry_key.pack(pady=5)
    
    tk.Label(update_window, text="New Rating:").pack(pady=5)
    entry_rating = tk.Entry(update_window)
    entry_rating.pack(pady=5)
    status_lbl.configure(text="Update Videos button was clicked!")
    
    def update_rating():
        key = entry_key.get()
        new_rating = entry_rating.get()
        try:
            new_rating = int(new_rating)
            lib.set_rating(key, new_rating)
            messagebox.showinfo("Success", f"Updated rating for {key} to {new_rating}")
        except ValueError:
            messagebox.showerror("Error", "Invalid rating value")
        update_window.destroy()

    tk.Button(update_window, text="Update", command=update_rating).pack(pady=10)

def import_video_list():
    status_lbl.configure(text="Import Video List button was clicked!")
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            video_list = list(reader)
            listbox_videos.delete(0, tk.END)  
            for video in video_list:
                listbox_videos.insert(tk.END, video)

def export_video_list():
    status_lbl.configure(text="Export Video List button was clicked!")
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Key", "Name", "Director", "Rating", "Play Count"])
            for key, video in lib.library.items():
                writer.writerow([key, video.name, video.director, video.rating, video.play_count])
        status_lbl.configure(text="Video list exported successfully")
    else:
        status_lbl.configure(text="Export cancelled")

def edit_videos_clicked():
    edit_window = tk.Toplevel(window)
    edit_window.geometry("400x300")
    edit_window.title("Edit Video Details")
    
    tk.Label(edit_window, text="Video Key:").pack(pady=5)
    entry_key = tk.Entry(edit_window)
    entry_key.pack(pady=5)
    
    tk.Label(edit_window, text="New Name:").pack(pady=5)
    entry_name = tk.Entry(edit_window)
    entry_name.pack(pady=5)
    
    tk.Label(edit_window, text="New Director:").pack(pady=5)
    entry_director = tk.Entry(edit_window)
    entry_director.pack(pady=5)
    
    tk.Label(edit_window, text="New Rating:").pack(pady=5)
    entry_rating = tk.Entry(edit_window)
    entry_rating.pack(pady=5)

    def update_details():
        key = entry_key.get()
        new_name = entry_name.get()
        new_director = entry_director.get()
        new_rating = entry_rating.get()
        try:
            new_rating = int(new_rating)
            video = library.get(key)
            if video:
                video.name = new_name
                video.director = new_director
                video.rating = new_rating
                messagebox.showinfo("Success", f"Updated details for video {key}")
                edit_window.destroy()
            else:
                messagebox.showerror("Error", f"Video {key} not found")
        except ValueError:
            messagebox.showerror("Error", "Invalid rating value")
    
    tk.Button(edit_window, text="Update", command=update_details).pack(pady=10)

window = tk.Tk()
window.geometry("520x400")
window.title("Video Player")

fonts.configure()

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_video_list_btn = tk.Button(window, text="Create Video List", command=create_video_list_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_videos_btn = tk.Button(window, text="Update Videos", command=update_videos_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

btn_import_video_list = tk.Button(window, text="Import Video List", command=import_video_list)
btn_import_video_list.grid(row=2, column=0, padx=10, pady=10)

btn_export_video_list = tk.Button(window, text="Export Video List", command=export_video_list)
btn_export_video_list.grid(row=2, column=1, padx=10, pady=10)

edit_videos_btn = tk.Button(window, text="Edit Videos", command=edit_videos_clicked)
edit_videos_btn.grid(row=2, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

listbox_videos = tk.Listbox(window, width=50, height=15)
listbox_videos.grid(row=4, column=0, columnspan=4, pady=10)

window.mainloop()
