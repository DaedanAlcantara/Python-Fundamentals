"""
=============================================================
  CHAPTER 6 REVIEWER: GUI Programming with Tkinter
  Batangas State University — ACP Final Exam Reviewer
=============================================================
  TOPICS COVERED:
    1. Tkinter Basics — creating a window
    2. Common Widgets — Label, Button, Entry, Text,
                        Listbox, Checkbutton
    3. Themed Widgets (ttk) — Combobox, Treeview,
                               Notebook, Progressbar
    4. Layout Managers — pack(), grid(), place()
    5. Event Handling — command=, .bind(), StringVar + .trace()
    6. Common Event Bindings reference

  HOW TO USE THIS REVIEWER:
    Run this file in IDLE or VS Code.
    Each section is wrapped in its own demo window.
    Close each window to move to the next demo.
=============================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox


# ─────────────────────────────────────────────
# SECTION 1: TKINTER BASICS — Hello World
# Key ideas:
#   tk.Tk()        → creates the main window
#   .title()       → sets the title bar text
#   .geometry()    → sets window size 'WxH'
#   tk.Label()     → displays text
#   .pack()        → adds widget to window
#   .mainloop()    → starts the event loop (ALWAYS LAST)
# ─────────────────────────────────────────────
def demo1_basics():
    root = tk.Tk()
    root.title("DEMO 1 — Tkinter Basics")
    root.geometry("420x200")

    tk.Label(root, text="✅ SECTION 1: Tkinter Basics",
             font=("Arial", 13, "bold"), fg="darkred").pack(pady=10)

    tk.Label(root, text="tk.Tk()       → Creates the main window").pack(anchor="w", padx=20)
    tk.Label(root, text=".title()      → Sets window title").pack(anchor="w", padx=20)
    tk.Label(root, text=".geometry()   → Sets window size e.g. '420x200'").pack(anchor="w", padx=20)
    tk.Label(root, text=".mainloop()   → Starts the event loop (always last!)").pack(anchor="w", padx=20)

    tk.Button(root, text="Close → Next Demo", command=root.destroy).pack(pady=10)
    root.mainloop()


# ─────────────────────────────────────────────
# SECTION 2: COMMON WIDGETS
# Key ideas:
#   Label       → displays text or images
#   Button      → clickable action trigger
#   Entry       → single-line text input
#   Text        → multi-line text area
#   Listbox     → scrollable list of items
#   Checkbutton → on/off toggle checkbox
# ─────────────────────────────────────────────
def demo2_widgets():
    root = tk.Tk()
    root.title("DEMO 2 — Common Widgets")
    root.geometry("420x380")

    tk.Label(root, text="✅ SECTION 2: Common Widgets",
             font=("Arial", 13, "bold"), fg="darkred").pack(pady=8)

    # Label
    tk.Label(root, text="Label → Displays text or images",
             bg="#f0f0f0", relief="groove", width=40).pack(pady=3)

    # Entry
    tk.Label(root, text="Entry → Single-line text input:").pack()
    entry = tk.Entry(root, width=30)
    entry.insert(0, "Type something here...")
    entry.pack(pady=2)

    # Text
    tk.Label(root, text="Text → Multi-line text area:").pack()
    text_widget = tk.Text(root, height=3, width=40)
    text_widget.insert("1.0", "This is a multi-line\ntext area widget.")
    text_widget.pack(pady=2)

    # Checkbutton
    chk_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Checkbutton → On/Off toggle",
                   variable=chk_var).pack()

    # Listbox
    tk.Label(root, text="Listbox → Scrollable list:").pack()
    listbox = tk.Listbox(root, height=3, width=30)
    for item in ["Item A", "Item B", "Item C"]:
        listbox.insert(tk.END, item)
    listbox.pack(pady=2)

    # Button
    tk.Button(root, text="Button → Click Me! (closes this demo)",
              command=root.destroy, bg="#b22222", fg="white").pack(pady=8)

    root.mainloop()


# ─────────────────────────────────────────────
# SECTION 3: THEMED WIDGETS (ttk)
# Key ideas:
#   Always import:  from tkinter import ttk
#   ttk.Button      → OS-native styled button
#   ttk.Entry       → cleaner focus ring and border
#   ttk.Combobox    → dropdown selector widget
#   ttk.Treeview    → table / hierarchical list
#   ttk.Notebook    → tabbed navigation panel
#   ttk.Progressbar → loading/progress indicator
#   RULE: Always prefer ttk over plain tk where available
# ─────────────────────────────────────────────
def demo3_ttk():
    root = tk.Tk()
    root.title("DEMO 3 — ttk Themed Widgets")
    root.geometry("440x360")

    tk.Label(root, text="✅ SECTION 3: Themed Widgets (ttk)",
             font=("Arial", 13, "bold"), fg="darkred").pack(pady=8)

    # ttk.Combobox
    tk.Label(root, text="ttk.Combobox → Dropdown selector:").pack()
    combo = ttk.Combobox(root, values=["Family", "Friend", "Classmate", "Workmate"])
    combo.set("Select group...")
    combo.pack(pady=3)

    # ttk.Progressbar
    tk.Label(root, text="ttk.Progressbar → Progress indicator:").pack()
    progress = ttk.Progressbar(root, length=300, value=65)
    progress.pack(pady=3)
    tk.Label(root, text="  (value=65 means 65% progress)").pack()

    # ttk.Notebook (tabs)
    tk.Label(root, text="ttk.Notebook → Tabbed panel:").pack(pady=(8, 0))
    notebook = ttk.Notebook(root, width=380, height=80)
    tab1 = tk.Frame(notebook)
    tab2 = tk.Frame(notebook)
    tk.Label(tab1, text="Content of Tab 1").pack(pady=10)
    tk.Label(tab2, text="Content of Tab 2").pack(pady=10)
    notebook.add(tab1, text="Tab 1")
    notebook.add(tab2, text="Tab 2")
    notebook.pack(pady=5)

    # ttk.Treeview (table)
    tk.Label(root, text="ttk.Treeview → Table view:").pack()
    tree = ttk.Treeview(root, columns=("Name", "Grade"), show="headings", height=3)
    tree.heading("Name", text="Name")
    tree.heading("Grade", text="Grade")
    tree.insert("", tk.END, values=("Juan dela Cruz", "90"))
    tree.insert("", tk.END, values=("Maria Santos", "95"))
    tree.pack(pady=3)

    ttk.Button(root, text="Close → Next Demo", command=root.destroy).pack(pady=8)
    root.mainloop()


# ─────────────────────────────────────────────
# SECTION 4: LAYOUT MANAGERS
# Key ideas:
#   pack()  → stacks widgets in one direction
#             side='left'/'right'/'top'/'bottom'
#   grid()  → arranges in row-column table
#             row=, column=, columnspan=, sticky=
#   place() → exact pixel coordinates
#             x=, y=, relx=, rely=
#   ⚠️  NEVER mix pack() and grid() in the same parent!
# ─────────────────────────────────────────────
def demo4_layout():
    root = tk.Tk()
    root.title("DEMO 4 — Layout Managers")
    root.geometry("480x420")

    tk.Label(root, text="✅ SECTION 4: Layout Managers",
             font=("Arial", 13, "bold"), fg="darkred").pack(pady=8)

    # --- pack() demo ---
    tk.Label(root, text="── pack() → stacks widgets ──",
             fg="navy", font=("Arial", 10, "bold")).pack()
    frame_pack = tk.Frame(root, relief="groove", bd=2)
    frame_pack.pack(padx=10, pady=4, fill="x")
    tk.Button(frame_pack, text="LEFT",  bg="#ffcccc").pack(side="left",  padx=4, pady=4)
    tk.Button(frame_pack, text="RIGHT", bg="#ccffcc").pack(side="right", padx=4, pady=4)
    tk.Button(frame_pack, text="TOP (default)", bg="#ccccff").pack()

    # --- grid() demo ---
    tk.Label(root, text="── grid() → row/column form ──",
             fg="navy", font=("Arial", 10, "bold")).pack(pady=(8, 0))
    frame_grid = tk.Frame(root, relief="groove", bd=2)
    frame_grid.pack(padx=10, pady=4, fill="x")

    fields = ["Username", "Password"]
    for i, field in enumerate(fields):
        tk.Label(frame_grid, text=f"{field}:").grid(
            row=i, column=0, sticky="W", padx=8, pady=3)
        tk.Entry(frame_grid, width=20).grid(
            row=i, column=1, padx=5, pady=3)
    tk.Button(frame_grid, text="Login",
              bg="#b22222", fg="white").grid(
        row=2, column=0, columnspan=2, pady=5)

    # --- place() demo ---
    tk.Label(root, text="── place() → exact pixel position ──",
             fg="navy", font=("Arial", 10, "bold")).pack(pady=(8, 0))
    frame_place = tk.Frame(root, relief="groove", bd=2, height=70)
    frame_place.pack(padx=10, pady=4, fill="x")
    frame_place.pack_propagate(False)
    tk.Label(frame_place, text="x=10, y=10",
             bg="#ffffcc", relief="raised").place(x=10, y=10)
    tk.Label(frame_place, text="x=200, y=30",
             bg="#ccffff", relief="raised").place(x=200, y=30)

    tk.Label(root, text="⚠️  NEVER mix pack() and grid() in the same parent!",
             fg="red", font=("Arial", 9, "bold")).pack()

    tk.Button(root, text="Close → Next Demo", command=root.destroy).pack(pady=6)
    root.mainloop()


# ─────────────────────────────────────────────
# SECTION 5: EVENT HANDLING
# Key ideas:
#   command=         → simplest: pass function ref to Button
#   .bind(event, fn) → attach event to any widget
#   StringVar+.trace → react to variable changes in real time
#   .config()        → update a widget's property live
#   event.keysym     → name of the key pressed
#
#   Common event strings:
#     <Button-1>        → left mouse click
#     <Button-3>        → right mouse click
#     <Double-Button-1> → double left click
#     <Return>          → Enter key
#     <Key>             → any key pressed
#     <Enter>           → mouse enters widget
#     <Leave>           → mouse leaves widget
# ─────────────────────────────────────────────
def demo5_events():
    root = tk.Tk()
    root.title("DEMO 5 — Event Handling")
    root.geometry("440x380")

    tk.Label(root, text="✅ SECTION 5: Event Handling",
             font=("Arial", 13, "bold"), fg="darkred").pack(pady=8)

    # --- command= ---
    tk.Label(root, text="── command= (Button click) ──",
             fg="navy", font=("Arial", 10, "bold")).pack()
    result_lbl = tk.Label(root, text="(click the button)", bg="#f9f9f9", width=35)
    result_lbl.pack(pady=3)

    name_entry = tk.Entry(root, width=25)
    name_entry.insert(0, "Enter your name")
    name_entry.pack(pady=2)

    def on_greet():
        name = name_entry.get()
        result_lbl.config(text=f"Hello, {name}! 👋")

    ttk.Button(root, text="Greet Me (command=)", command=on_greet).pack(pady=4)

    # --- .bind() ---
    tk.Label(root, text="── .bind() — key press events ──",
             fg="navy", font=("Arial", 10, "bold")).pack(pady=(8, 0))
    key_lbl = tk.Label(root, text="Last key pressed: (none)", bg="#f0f0ff", width=35)
    key_lbl.pack(pady=3)

    bind_entry = tk.Entry(root, width=25)
    bind_entry.pack(pady=2)

    def on_key(event):
        key_lbl.config(text=f"Last key pressed: {event.keysym}")

    bind_entry.bind("<Key>", on_key)

    # --- StringVar + .trace() ---
    tk.Label(root, text="── StringVar + .trace() — live search ──",
             fg="navy", font=("Arial", 10, "bold")).pack(pady=(8, 0))
    search_var = tk.StringVar()
    trace_lbl = tk.Label(root, text="You typed: (nothing yet)", bg="#f0fff0", width=35)
    trace_lbl.pack(pady=3)

    search_entry = tk.Entry(root, textvariable=search_var, width=25)
    search_entry.pack(pady=2)

    def on_search_change(*args):
        trace_lbl.config(text=f"You typed: '{search_var.get()}'")

    search_var.trace("w", on_search_change)

    ttk.Button(root, text="Close → Done!", command=root.destroy).pack(pady=10)
    root.mainloop()


# ─────────────────────────────────────────────
# QUICK REFERENCE CHEAT SHEET (printed to console)
# ─────────────────────────────────────────────
def print_cheatsheet():
    print("""
╔══════════════════════════════════════════════════════════════╗
║     CHAPTER 6 CHEAT SHEET — GUI Programming with Tkinter    ║
╠══════════════════════════════════════════════════════════════╣
║  BASICS                                                      ║
║   import tkinter as tk                                       ║
║   from tkinter import ttk                                    ║
║   root = tk.Tk()          # create window                    ║
║   root.title("Title")     # set title bar                    ║
║   root.geometry("WxH")    # set window size                  ║
║   root.mainloop()         # start event loop (ALWAYS LAST)   ║
╠══════════════════════════════════════════════════════════════╣
║  WIDGETS             USAGE                                   ║
║   tk.Label()         display text/images                     ║
║   tk.Button()        clickable trigger                       ║
║   tk.Entry()         single-line text input                  ║
║   tk.Text()          multi-line text area                    ║
║   tk.Checkbutton()   on/off toggle                           ║
║   tk.Listbox()       scrollable list                         ║
║   ttk.Combobox()     dropdown selector                       ║
║   ttk.Treeview()     table / hierarchical list               ║
║   ttk.Notebook()     tabbed panel                            ║
║   ttk.Progressbar()  progress indicator                      ║
╠══════════════════════════════════════════════════════════════╣
║  LAYOUT MANAGERS                                             ║
║   .pack()   side='left/right/top/bottom'                     ║
║   .grid()   row=, column=, columnspan=, sticky=, padx/pady=  ║
║   .place()  x=, y=, relx=, rely=, anchor=                    ║
║   ⚠️  NEVER mix pack() and grid() in same parent!            ║
╠══════════════════════════════════════════════════════════════╣
║  EVENT HANDLING                                              ║
║   command=my_func          button click (no event obj)       ║
║   widget.bind("<Evt>", fn) any widget, fn receives event obj ║
║   StringVar + .trace("w")  watch variable changes live       ║
║   widget.config(text="x")  update widget property live       ║
╠══════════════════════════════════════════════════════════════╣
║  COMMON EVENT STRINGS                                        ║
║   <Button-1>        left mouse click                         ║
║   <Button-3>        right mouse click                        ║
║   <Double-Button-1> double left click                        ║
║   <Return>          Enter key                                ║
║   <Key>             any key pressed                          ║
║   <Enter>           mouse enters widget                      ║
║   <Leave>           mouse leaves widget                      ║
╚══════════════════════════════════════════════════════════════╝
    """)


# ─────────────────────────────────────────────
# MAIN RUNNER — launches all demos in sequence
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print_cheatsheet()
    print(">>> Starting Chapter 6 Reviewer Demos...")
    print(">>> Close each window to proceed to the next demo.\n")

    demo1_basics()
    demo2_widgets()
    demo3_ttk()
    demo4_layout()
    demo5_events()

    print("\n✅ Chapter 6 Reviewer Complete! Good luck on your exam!")