import tkinter as tk
from tkinter import ttk, messagebox

video_list = []

def add_to_list(title):
    if title :
        video_list.append(title)
        messagebox.showinfo("Success", "Video added to the list!")
    else:
        messagebox.showerror("Error", "Please enter both title .")

def save_list():
    if video_list:
        with open('video_list.txt', 'w') as file:
            for title, url in video_list:
                file.write(f"{title}\n")
        messagebox.showinfo("Success", "Video list saved!")
    else:
        messagebox.showerror("error","No video to save")

def main():
    root = tk.Tk()
    root.title("Create Video List")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

   
    ttk.Label(frame, text="Video Title:").grid(row=0, column=0, sticky=tk.W)
    title_entry = ttk.Entry(frame)
    title_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Video URL:").grid(row=1, column=0, sticky=tk.W)
    url_entry = ttk.Entry(frame)
    url_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

 
    ttk.Button(frame, text="Add to List", command=lambda: add_to_list(title_entry.get(), url_entry.get())).grid(row=2, column=0, columnspan=2)
    ttk.Button(frame, text="Save List", command=save_list).grid(row=3, column=0, columnspan=2)


    root.mainloop()

if __name__ == "__main__":
    main()