import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# =========================================================
# FILE HANDLING REVIEWER APP
# Chapter 6 - File Handling
# =========================================================

root = tk.Tk()
root.title("File Handling Reviewer")
root.geometry("850x600")
root.config(bg="#eef5fb")

FILE_NAME = "student_file.txt"

# =========================================================
# TITLE
# =========================================================

title = tk.Label(
    root,
    text="Python File Handling Reviewer",
    font=("Arial", 24, "bold"),
    bg="#eef5fb",
    fg="#154360"
)
title.pack(pady=15)

# =========================================================
# OUTPUT BOX
# =========================================================

output_box = tk.Text(
    root,
    width=90,
    height=20,
    font=("Consolas", 11),
    relief="solid",
    bd=2
)
output_box.pack(pady=10)

# =========================================================
# DISPLAY FUNCTION
# =========================================================

def display(text):
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, text)

# =========================================================
# CREATE FILE (x MODE)
# =========================================================

def create_file():

    try:
        file = open(FILE_NAME, "x")
        file.close()

        display(
            'CREATE MODE ("x")\n\n'
            f'File "{FILE_NAME}" created successfully.'
        )

    except FileExistsError:

        display(
            'CREATE MODE ("x")\n\n'
            "Error: File already exists."
        )

# =========================================================
# WRITE FILE (w MODE)
# =========================================================

def write_file():

    text = simpledialog.askstring(
        "Write File",
        "Enter text to write:"
    )

    if text:

        file = open(FILE_NAME, "w")

        file.write(text)

        file.close()

        display(
            'WRITE MODE ("w")\n\n'
            "File written successfully.\n\n"
            f"Written Content:\n{text}"
        )

# =========================================================
# READ FILE (r MODE)
# =========================================================

def read_file():

    try:

        file = open(FILE_NAME, "r")

        content = file.read()

        file.close()

        display(
            'READ MODE ("r")\n\n'
            f"File Content:\n\n{content}"
        )

    except FileNotFoundError:

        display(
            'READ MODE ("r")\n\n'
            "Error: File does not exist."
        )

# =========================================================
# APPEND FILE (a MODE)
# =========================================================

def append_file():

    text = simpledialog.askstring(
        "Append File",
        "Enter text to append:"
    )

    if text:

        file = open(FILE_NAME, "a")

        file.write("\n" + text)

        file.close()

        display(
            'APPEND MODE ("a")\n\n'
            "Text appended successfully.\n\n"
            f"Appended Text:\n{text}"
        )

# =========================================================
# WRITE + READ (w+ MODE)
# =========================================================

def write_read_file():

    text = simpledialog.askstring(
        "Write + Read",
        "Enter text:"
    )

    if text:

        file = open(FILE_NAME, "w+")

        file.write(text)

        file.seek(0)

        content = file.read()

        file.close()

        display(
            'WRITE + READ MODE ("w+")\n\n'
            f"Stored Content:\n\n{content}"
        )

# =========================================================
# APPEND + READ (a+ MODE)
# =========================================================

def append_read_file():

    text = simpledialog.askstring(
        "Append + Read",
        "Enter text:"
    )

    if text:

        file = open(FILE_NAME, "a+")

        file.write(text + "\n")

        file.seek(0)

        content = file.read()

        file.close()

        display(
            'APPEND + READ MODE ("a+")\n\n'
            f"Complete File Content:\n\n{content}"
        )

# =========================================================
# READ + WRITE (r+ MODE)
# =========================================================

def read_write_file():

    try:

        file = open(FILE_NAME, "r+")

        old_content = file.read()

        file.write("\nAdditional text using r+ mode.")

        file.seek(0)

        new_content = file.read()

        file.close()

        display(
            'READ + WRITE MODE ("r+")\n\n'
            "Original Content:\n"
            f"{old_content}\n\n"
            "Updated Content:\n"
            f"{new_content}"
        )

    except FileNotFoundError:

        display(
            'READ + WRITE MODE ("r+")\n\n'
            "Error: File does not exist."
        )

# =========================================================
# CREATE + READ + WRITE (x+ MODE)
# =========================================================

def create_read_write():

    filename = "new_file.txt"

    try:

        file = open(filename, "x+")

        file.write("This file uses x+ mode.")

        file.seek(0)

        content = file.read()

        file.close()

        display(
            'CREATE + READ + WRITE MODE ("x+")\n\n'
            f"Created File: {filename}\n\n"
            f"Content:\n{content}"
        )

    except FileExistsError:

        display(
            'CREATE + READ + WRITE MODE ("x+")\n\n'
            "Error: File already exists."
        )

# =========================================================
# DELETE FILE
# =========================================================

def delete_file():

    if os.path.exists(FILE_NAME):

        os.remove(FILE_NAME)

        display(
            "DELETE FILE\n\n"
            f'"{FILE_NAME}" deleted successfully.'
        )

    else:

        display(
            "DELETE FILE\n\n"
            "Error: File does not exist."
        )

# =========================================================
# GROCERY LIST TRACKER
# =========================================================

def grocery_tracker():

    item = simpledialog.askstring(
        "Grocery List",
        "Enter grocery item:"
    )

    if item:

        file = open("grocery.txt", "a")

        file.write(item + "\n")

        file.close()

        file = open("grocery.txt", "r")

        groceries = file.read()

        file.close()

        display(
            "GROCERY LIST TRACKER\n\n"
            f"Current Grocery List:\n\n{groceries}"
        )

# =========================================================
# LOGIN LOGGER
# =========================================================

def login_logger():

    username = simpledialog.askstring(
        "Login",
        "Enter username:"
    )

    if username:

        file = open("login_log.txt", "a")

        file.write(f"User Logged In: {username}\n")

        file.close()

        file = open("login_log.txt", "r")

        logs = file.read()

        file.close()

        display(
            "LOGIN LOGGER\n\n"
            f"Login Records:\n\n{logs}"
        )

# =========================================================
# GRADE EVALUATOR
# =========================================================

def grade_evaluator():

    try:

        grade = int(simpledialog.askstring(
            "Grade Evaluator",
            "Enter grade:"
        ))

        if grade >= 75:
            result = "PASSED"
        else:
            result = "FAILED"

        file = open("grades.txt", "a")

        file.write(f"Grade: {grade} - {result}\n")

        file.close()

        display(
            "GRADE EVALUATOR\n\n"
            f"Grade: {grade}\n"
            f"Result: {result}"
        )

    except:

        messagebox.showerror(
            "Error",
            "Please enter a valid number."
        )

# =========================================================
# BUTTON FRAME
# =========================================================

button_frame = tk.Frame(root, bg="#eef5fb")
button_frame.pack(pady=10)

buttons = [

    ("Create File (x)", create_file),
    ("Write File (w)", write_file),
    ("Read File (r)", read_file),
    ("Append File (a)", append_file),

    ("Write + Read (w+)", write_read_file),
    ("Append + Read (a+)", append_read_file),
    ("Read + Write (r+)", read_write_file),
    ("Create + Read + Write (x+)", create_read_write),

    ("Delete File", delete_file),
    ("Grocery Tracker", grocery_tracker),
    ("Login Logger", login_logger),
    ("Grade Evaluator", grade_evaluator)

]

row = 0
column = 0

for text, command in buttons:

    btn = tk.Button(
        button_frame,
        text=text,
        width=25,
        height=2,
        bg="#2e86c1",
        fg="white",
        font=("Arial", 10, "bold"),
        command=command
    )

    btn.grid(row=row, column=column, padx=5, pady=5)

    column += 1

    if column > 2:
        column = 0
        row += 1

# =========================================================
# MAIN LOOP
# =========================================================

root.mainloop()
