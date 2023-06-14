import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import winsound

# Create a graphical interface
root = tk.Tk()
root.title('Adoc&&MD Split Converter')
root.iconbitmap('./_icons/icon.ico')

# Disable window scaling
root.resizable(width=False, height=False)

window_width = 450
window_height = 250

# Define the application screen position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Creating the "Select File" button
button_file = tk.Button(root, text="Выбрать файл")
button_file.pack(anchor="nw", padx=20, pady=20, ipadx=10, ipady=10, side='left', expand=False)

# Create a drop-down menu with parameter selection
options = ["adoc", "md"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Sets the default value

# Define the maximum width of the drop-down menu
max_option_width = max(len(option) for option in options)
option_menu = tk.OptionMenu(root, selected_option, *options)
option_menu.config(width=max_option_width)  # Set the button width
option_menu.pack(anchor="ne", padx=20, pady=20, ipadx=10, ipady=10, side='right')

# Create the "Start Program" button
button_start = tk.Button(root, text="Start Program", state=tk.DISABLED)
button_start.pack(anchor="n", padx=10, pady=20, ipadx=10, ipady=10, side='top', expand=True)

# Create the "Warning" message
warning_label = tk.Label(root, text="Select your file first", fg="red", font=("Arial", 14))
option_menu.config(width=max_option_width)
warning_label.pack(anchor="center", expand=True)

# Create the "Quit program" button
button_quit = tk.Button(root, text="Exit Program", command=root.quit)
button_quit.pack(anchor="s", padx=10, pady=30, ipadx=20, ipady=10, side='bottom', expand=True)

# The variable that will contain the path to the selected file
selected_file = ''

# Runtime icon
icon_image = tk.PhotoImage(file="./_icons/thumb.png")
icon_label = tk.Label(root, image=icon_image, compound="none")
icon_label.place(anchor="sw")
icon_label.pack_forget()


# Create a function to open a file
def open_file():
    global selected_file
    script_dir = os.path.dirname(__file__)
    selected_file = filedialog.askopenfilename(initialdir=script_dir, title="Select a File",
                                               filetypes=(("adoc files", "*.adoc"),
                                                          ("md files", "*.md")))
    # Check if a file is selected and enable/disable buttons
    if selected_file:
        button_start.configure(state=tk.NORMAL)
        hide_warning_label()
    else:
        button_start.configure(state=tk.DISABLED)
        show_warning_label()


# Create a function to execute the script.py file
def start_program():
    file_format = selected_option.get()
    subprocess.call(["python", "script.py", selected_file, "--format", file_format])
    play_sound("./_sound/pig.wav")  # Audio playback
    button_start.configure(state=tk.DISABLED)  # Make the "Start Program" button inactive after successful execution
    hide_warning_label()  # Hide the "Warning" message
    icon_label.pack()  # Display the execution icon
    root.after(1000, hide_icon)  # Start the function to hide the execution icon after 1 second
    root.after(1102, show_warning_label)  # Display warning_label after 1001 milliseconds


# Function for audio playback
def play_sound(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_FILENAME)


# Function for hide the execution icon
def hide_icon():
    icon_label.pack_forget()


# Function for the display "Warning" message
def show_warning_label():
    warning_label.pack()


# Function for hide the "Warning" message
def hide_warning_label():
    warning_label.pack_forget()


# Bind the functions to the buttons
button_file.configure(command=open_file)
button_start.configure(command=start_program)

# Start the main event loop
root.mainloop()
