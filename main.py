import os
import tkinter as tk
from tkinter import filedialog
from threading import Thread


def analyze_directory():
    directory_path = directory_entry.get()
    if not os.path.isdir(directory_path):
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "Invalid directory path.")
        return

    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "Analyzing directory... Please wait.")

    # Start the file analysis process in a separate thread
    t = Thread(target=analyze_files, args=(directory_path,))
    t.start()


def analyze_files(directory_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for file_name in filenames:
            file_path = os.path.join(dirpath, file_name)
            file_size = os.path.getsize(file_path)
            total_size += file_size
            result_text.insert(tk.END, f"{file_path} - {file_size} bytes\n")

    result_text.insert(tk.END, f"\nTotal Size: {total_size} bytes")


def select_directory():
    directory_path = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(tk.END, directory_path)


root = tk.Tk()
root.title("Directory Analyzer")

select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack()

directory_entry = tk.Entry(root, width=50)
directory_entry.pack()

analyze_button = tk.Button(root, text="Analyze", command=analyze_directory)
analyze_button.pack()

result_text = tk.Text(root, height=20, width=50)
result_text.pack()

root.mainloop()
