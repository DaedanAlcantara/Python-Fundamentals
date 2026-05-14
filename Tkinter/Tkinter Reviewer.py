"""
COMPREHENSIVE TKINTER REVIEW APPLICATION
Concepts covered:
- Basic widgets (Label, Entry, Button, Checkbutton, Text)
- Themed widgets (ttk: Combobox, Treeview, Notebook, Progressbar, Scale)
- Layout managers (grid, pack, place - demonstrated separately)
- Event handling (command, bind, event object)
- Python 3.10+ match/case for event handling
- Form validation with messagebox
- Multiple windows and dynamic updates
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
from datetime import datetime

# ========== MAIN APPLICATION CLASS ==========

class TkinterReviewApp:
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.title("Tkinter Complete Reviewer - All Concepts")
        self.root.geometry("1080x1920")
        self.root.minsize(800, 600)
        
        # Configure style for ttk
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Modern looking theme
        
        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs for different concept demonstrations
        self.create_widgets_tab()
        self.create_layout_tab()
        self.create_events_tab()
        self.create_contact_manager_tab()  # Main activity
        
        # Set up status bar at bottom
        self.setup_status_bar()
        
        # Start the main event loop
        self.root.mainloop()
    
    # ========== TAB 1: BASIC & THEMED WIDGETS ==========
    
    def create_widgets_tab(self):
        """Demonstrates basic and themed Tkinter widgets"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📦 Widgets Demo")
        
        # Use grid for form-like layout
        main_frame = ttk.Frame(tab, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        tab.columnconfigure(0, weight=1)
        
        # Section title
        ttk.Label(main_frame, text="Basic & Themed Widgets", 
                  font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        # === Basic Widgets Section ===
        ttk.Label(main_frame, text="🟢 Basic Widgets:", 
                  font=('Arial', 11, 'bold')).grid(row=1, column=0, columnspan=2, sticky='w', pady=(10,5))
        
        # Label
        ttk.Label(main_frame, text="Label Widget:").grid(row=2, column=0, sticky='w', padx=5)
        demo_label = tk.Label(main_frame, text="Hello from Label!", bg="lightyellow", relief="ridge")
        demo_label.grid(row=2, column=1, padx=5, pady=2, sticky='w')
        
        # Entry
        ttk.Label(main_frame, text="Entry Widget:").grid(row=3, column=0, sticky='w', padx=5)
        self.demo_entry = ttk.Entry(main_frame, width=30)
        self.demo_entry.grid(row=3, column=1, padx=5, pady=2)
        self.demo_entry.insert(0, "Type something...")
        
        # Button
        ttk.Label(main_frame, text="Button Widget:").grid(row=4, column=0, sticky='w', padx=5)
        ttk.Button(main_frame, text="Click Me", 
                   command=lambda: self.update_demo_label(demo_label)).grid(row=4, column=1, padx=5, pady=2, sticky='w')
        
        # Checkbutton with variable
        ttk.Label(main_frame, text="Checkbutton:").grid(row=5, column=0, sticky='w', padx=5)
        self.check_var = tk.BooleanVar()
        ttk.Checkbutton(main_frame, text="I agree to terms", 
                        variable=self.check_var).grid(row=5, column=1, padx=5, pady=2, sticky='w')
        
        # Text widget (multi-line)
        ttk.Label(main_frame, text="Text Widget:").grid(row=6, column=0, sticky='nw', padx=5)
        text_frame = ttk.Frame(main_frame)
        text_frame.grid(row=6, column=1, padx=5, pady=2)
        self.demo_text = tk.Text(text_frame, height=4, width=30)
        self.demo_text.pack()
        self.demo_text.insert('1.0', "Multi-line\ntext area")
        
        # === Themed Widgets Section (ttk) ===
        ttk.Label(main_frame, text="\n🎨 Themed Widgets (ttk):", 
                  font=('Arial', 11, 'bold')).grid(row=7, column=0, columnspan=2, sticky='w', pady=(15,5))
        
        # Combobox
        ttk.Label(main_frame, text="Combobox:").grid(row=8, column=0, sticky='w', padx=5)
        self.combo = ttk.Combobox(main_frame, values=["Option 1", "Option 2", "Option 3"], state="readonly")
        self.combo.grid(row=8, column=1, padx=5, pady=2, sticky='w')
        self.combo.set("Select an option")
        
        # Progressbar
        ttk.Label(main_frame, text="Progressbar:").grid(row=9, column=0, sticky='w', padx=5)
        self.progress = ttk.Progressbar(main_frame, length=200, mode='determinate')
        self.progress.grid(row=9, column=1, padx=5, pady=2, sticky='w')
        ttk.Button(main_frame, text="Update Progress", 
                   command=self.update_progress).grid(row=9, column=2, padx=5)
        
        # Scale (Slider)
        ttk.Label(main_frame, text="Scale (Slider):").grid(row=10, column=0, sticky='w', padx=5)
        self.scale_var = tk.DoubleVar(value=50)
        self.scale = ttk.Scale(main_frame, from_=0, to=100, variable=self.scale_var,
                               command=self.on_scale_change)
        self.scale.grid(row=10, column=1, padx=5, pady=2, sticky='ew')
        self.scale_label = ttk.Label(main_frame, text="50")
        self.scale_label.grid(row=10, column=2, padx=5)
        
        # Vertical Scale example (optional)
        ttk.Label(main_frame, text="Vertical Scale:").grid(row=11, column=0, sticky='w', padx=5)
        self.vert_scale_var = tk.DoubleVar(value=25)
        self.vert_scale = ttk.Scale(main_frame, from_=0, to=100, variable=self.vert_scale_var, orient='vertical')
        self.vert_scale.grid(row=11, column=1, padx=5, pady=2, sticky='ns')


        # Spinbox (Python 3.9+)
        ttk.Label(main_frame, text="Spinbox:").grid(row=12, column=0, sticky='w', padx=5)
        self.spinbox = ttk.Spinbox(main_frame, from_=0, to=100, width=10)
        self.spinbox.grid(row=12, column=1, padx=5, pady=2, sticky='w')
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)

    
    def update_demo_label(self, label):
        """Update label with entry text"""
        text = self.demo_entry.get()
        if text:
            label.config(text=f"You wrote: {text}", bg="lightgreen")
        else:
            label.config(text="Please enter something!", bg="lightcoral")
    
    def update_progress(self):
        """Simulate progress update"""
        current = self.progress['value']
        if current < 100:
            self.progress['value'] = current + 10
        else:
            self.progress['value'] = 0
            messagebox.showinfo("Progress Complete", "Task finished!")
    
    def on_scale_change(self, value):
        """Handle scale slider movement"""
        self.scale_label.config(text=f"{int(float(value))}")
    
    # ========== TAB 2: LAYOUT MANAGERS DEMO ==========
    
    def create_layout_tab(self):
        """Demonstrates pack(), grid(), and place() layout managers"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📐 Layout Managers")
        
        # Create three frames to demonstrate each layout manager
        # Frame 1: pack() demo
        pack_frame = ttk.LabelFrame(tab, text="pack() - Stacked Layout", padding="10")
        pack_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
     
        ttk.Button(pack_frame, text="Top").pack(side='top', fill='x', pady=2)
        ttk.Button(pack_frame, text="Center").pack(expand=True)
        ttk.Button(pack_frame, text="Bottom2").pack(side='bottom', fill='x', pady=2)
        ttk.Button(pack_frame, text="Bottom").pack(side='bottom', fill='x', pady=2)
        ttk.Button(pack_frame, text="Left").pack(side='left', padx=2)
        ttk.Button(pack_frame, text="Right").pack(side='right', padx=2)
        
        # Frame 2: grid() demo
        grid_frame = ttk.LabelFrame(tab, text="grid() - Table Layout", padding="10")
        grid_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        # Simple login form using grid
        ttk.Label(grid_frame, text="Null Name").grid(row=0, column=0, sticky='w', padx=5, pady=2)
        ttk.Button(grid_frame, text="Null Button").grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(grid_frame, text="Username:").grid(row=1, column=0, sticky='w', padx=5, pady=2)
        ttk.Entry(grid_frame).grid(row=1, column=1, padx=5, pady=2)
        ttk.Label(grid_frame, text="Password:").grid(row=2, column=0, sticky='w', padx=5, pady=2)
        ttk.Entry(grid_frame, show="*").grid(row=2, column=1, padx=5, pady=2)
        ttk.Button(grid_frame, text="Login", 
                   command=lambda: messagebox.showinfo("Login", "Demo login clicked")).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Frame 3: place() demo
        place_frame = ttk.LabelFrame(tab, text="place() - Absolute Positioning", padding="10")
        place_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        
        # Show warning about place() being less common
        warning_label = tk.Label(place_frame, text="⚠️ place() uses exact coordinates\n(less flexible for resizing)", 
                                  bg="yellow", fg="black")
        warning_label.place(x=10, y=10, width=180, height=40) 
        
        demo_button = tk.Button(place_frame, text="I'm placed at (50, 80)")
        demo_button.place(x=50, y=80)
        
        # Configure grid weights
        tab.columnconfigure(0, weight=1)
        tab.columnconfigure(1, weight=1)
        tab.columnconfigure(2, weight=1)
        tab.rowconfigure(0, weight=1)
    
    # ========== TAB 3: EVENT HANDLING DEMO ==========
    
    def create_events_tab(self):
        """Demonstrates event handling with bind() and command"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="⚡ Event Handling")
        
        main_frame = ttk.Frame(tab, padding="10")
        main_frame.pack(fill='both', expand=True)
        
        ttk.Label(main_frame, text="Event Handling Demo", 
                  font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Event type 1: command parameter (button click)
        ttk.Label(main_frame, text="1. Button command event:").pack(anchor='w', pady=(10,5))
        self.event_entry = ttk.Entry(main_frame, width=40)
        self.event_entry.pack(pady=5)
        
        ttk.Button(main_frame, text="Submit (command=)", 
                   command=self.on_button_click).pack(pady=5)
        
        # Event type 2: bind() for keyboard events
        ttk.Label(main_frame, text="\n2. Key press event (type here):").pack(anchor='w', pady=(10,5))
        self.key_entry = ttk.Entry(main_frame, width=40)
        self.key_entry.pack(pady=5)
        self.key_entry.bind('<Key>', self.on_key_press)  # Bind key event
        self.key_entry.bind('<Return>', self.on_enter_key)  # Bind Enter key
        
        self.key_status = ttk.Label(main_frame, text="⌨️ Press any key...", foreground="gray")
        self.key_status.pack(pady=5)
        
        # Event type 3: bind to mouse events
        ttk.Label(main_frame, text="\n3. Mouse event (click/hover on box):").pack(anchor='w', pady=(10,5))
        self.mouse_box = tk.Canvas(main_frame, width=200, height=100, bg="lightblue", relief="ridge")
        self.mouse_box.pack(pady=5)
        self.mouse_box.bind('<Button-1>', self.on_mouse_click)
        self.mouse_box.bind('<Enter>', self.on_mouse_enter)
        self.mouse_box.bind('<Leave>', self.on_mouse_leave)
        
        self.mouse_status = ttk.Label(main_frame, text="🖱️ Click or hover on the blue box", foreground="gray")
        self.mouse_status.pack(pady=5)
        
        # Python 3.10+ match/case example
        ttk.Label(main_frame, text="\n4. Python 3.10+ match/case in event handler:").pack(anchor='w', pady=(10,5))
        self.match_entry = ttk.Entry(main_frame, width=40)
        self.match_entry.pack(pady=5)
        self.match_entry.bind('<KeyRelease>', self.match_case_demo)
        
        self.match_status = ttk.Label(main_frame, text="📝 Type 'hello' or 'quit' or a number...", foreground="gray")
        self.match_status.pack(pady=5)
        
        # Output area
        ttk.Label(main_frame, text="\n📋 Event Log:").pack(anchor='w', pady=(10,5))
        self.event_log = tk.Text(main_frame, height=8, width=70)
        self.event_log.pack(pady=5)
        
        ttk.Button(main_frame, text="Clear Log", command=self.clear_event_log).pack(pady=5)
    
    def on_button_click(self):
        """Handle button click event"""
        text = self.event_entry.get()
        if text:
            self.log_event(f"Button clicked with text: '{text}'")
            messagebox.showinfo("Submitted", f"You entered: {text}")
        else:
            self.log_event("Button clicked but entry was empty")
            messagebox.showwarning("Empty", "Please enter some text")
    
    def on_key_press(self, event):
        """Handle key press events - demonstrates event object"""
        self.key_status.config(text=f"⌨️ Key pressed: '{event.keysym}' (code: {event.keycode})", 
                               foreground="green")
        self.log_event(f"Key pressed: {event.keysym}")
    
    def on_enter_key(self, event):
        """Handle Enter key specifically"""
        text = self.key_entry.get()
        self.key_status.config(text=f"✅ Enter pressed with text: '{text}'", foreground="blue")
        self.log_event(f"Enter key pressed, entry text: '{text}'")
    
    def on_mouse_click(self, event):
        """Handle mouse click on canvas"""
        self.mouse_status.config(text=f"🖱️ Clicked at position: ({event.x}, {event.y})", 
                                 foreground="darkblue")
        self.log_event(f"Mouse click at ({event.x}, {event.y})")
    
    def on_mouse_enter(self, event):
        """Handle mouse entering widget"""
        self.mouse_box.config(bg="lightgreen")
        self.mouse_status.config(text="✨ Mouse entered the box!", foreground="green")
        self.log_event("Mouse entered the blue box")
    
    def on_mouse_leave(self, event):
        """Handle mouse leaving widget"""
        self.mouse_box.config(bg="lightblue")
        self.mouse_status.config(text="👋 Mouse left the box", foreground="gray")
        self.log_event("Mouse left the blue box")
    
    def match_case_demo(self, event):
        """Demonstrate Python 3.10+ match/case syntax"""
        text = self.match_entry.get().lower()
        
        # Using structural pattern matching (Python 3.10+)
        match text:
            case "hello":
                self.match_status.config(text="🎉 Hello there! Welcome!", foreground="purple")
                self.log_event("match/case: matched 'hello'")
            case "quit" | "exit":
                self.match_status.config(text="👋 Typing 'quit' doesn't actually quit 😄", foreground="red")
                self.log_event("match/case: matched 'quit' or 'exit'")
            case _ if text.isdigit():
                self.match_status.config(text=f"🔢 You typed the number {text}", foreground="orange")
                self.log_event(f"match/case: matched number {text}")
            case _ if len(text) > 0:
                self.match_status.config(text=f"📝 You typed: '{text}'", foreground="gray")
                self.log_event(f"match/case: other input '{text}'")
            case _:
                self.match_status.config(text="📝 Type something...", foreground="gray")
    
    def log_event(self, message):
        """Add timestamped message to event log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.event_log.insert('1.0', f"[{timestamp}] {message}\n")
        # Keep log manageable
        if int(self.event_log.index('end-1c').split('.')[0]) > 20:
            self.event_log.delete('end-2l', 'end-1c')
    
    def clear_event_log(self):
        """Clear the event log text widget"""
        self.event_log.delete('1.0', tk.END)
        self.log_event("Event log cleared")
    
    # ========== TAB 4: CONTACT MANAGER (MAIN ACTIVITY) ==========
    
    def create_contact_manager_tab(self):
        """Complete Contact List Manager application - integrates all concepts"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📱 Contact Manager (Main Activity)")
        
        # Main container with padding
        main_container = ttk.Frame(tab, padding="10")
        main_container.pack(fill='both', expand=True)
        
        # Title
        ttk.Label(main_container, text="My Contact List", 
                  font=('Arial', 16, 'bold')).pack(pady=10)
        
        # === Form Frame using grid() ===
        form_frame = ttk.LabelFrame(main_container, text="Contact Information", padding="10")
        form_frame.pack(fill='x', pady=10)
        
        # Grid layout for form
        # Row 0: Name
        ttk.Label(form_frame, text="Name:*").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.contact_name = ttk.Entry(form_frame, width=30)
        self.contact_name.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        
        # Row 1: Phone
        ttk.Label(form_frame, text="Phone:*").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.contact_phone = ttk.Entry(form_frame, width=30)
        self.contact_phone.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
        
        # Row 2: Email
        ttk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.contact_email = ttk.Entry(form_frame, width=30)
        self.contact_email.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
        
        # Row 3: Group (using ttk.Combobox)
        ttk.Label(form_frame, text="Group:").grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.contact_group = ttk.Combobox(form_frame, values=["Family", "Friend", "Classmate", "Workmate", "Other"],
                                          state="readonly", width=27)
        self.contact_group.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        self.contact_group.set("Friend")
        
        # Configure grid weights
        form_frame.columnconfigure(1, weight=1)
        
        # === Buttons Frame ===
        button_frame = ttk.Frame(main_container)
        button_frame.pack(fill='x', pady=10)
        
        ttk.Button(button_frame, text="➕ Add Contact", command=self.add_contact).pack(side='left', padx=5)
        ttk.Button(button_frame, text="🗑️ Delete Selected", command=self.delete_contact).pack(side='left', padx=5)
        ttk.Button(button_frame, text="🧹 Clear Form", command=self.clear_form).pack(side='left', padx=5)
        ttk.Button(button_frame, text="📋 Show All", command=self.refresh_treeview).pack(side='left', padx=5)
        
        # === Treeview for displaying contacts ===
        tree_frame = ttk.LabelFrame(main_container, text="Contact List", padding="10")
        tree_frame.pack(fill='both', expand=True, pady=10)
        
        # Create Treeview with scrollbar
        columns = ("Name", "Phone", "Email", "Group")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)
        
        # Define headings
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Group", text="Group")
        
        # Define column widths
        self.tree.column("Name", width=150)
        self.tree.column("Phone", width=120)
        self.tree.column("Email", width=200)
        self.tree.column("Group", width=100)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_contact_select)
        
        # Bind double-click to populate form (extra feature)
        self.tree.bind('<Double-Button-1>', self.on_double_click)
        
        # Status label
        self.contact_status = ttk.Label(main_container, text="Ready - Add contacts to get started", foreground="gray")
        self.contact_status.pack(pady=5)
        
        # Initialize contact list storage
        self.contacts = []  # Store contacts as dicts
        self.next_id = 1
    
    def validate_contact_input(self):
        """Validate form inputs - demonstrates validation"""
        name = self.contact_name.get().strip()
        phone = self.contact_phone.get().strip()
        
        if not name:
            messagebox.showwarning("Validation Error", "Name is required!")
            self.contact_name.focus()
            return False
        
        if not phone:
            messagebox.showwarning("Validation Error", "Phone number is required!")
            self.contact_phone.focus()
            return False
        
        # Optional: Phone number format validation
        if not phone.replace("-", "").replace("+", "").isdigit():
            if not messagebox.askyesno("Invalid Format", 
                                        "Phone number contains non-digit characters. Continue anyway?"):
                return False
        
        return True
    
    def add_contact(self):
        """Add new contact to the list"""
        if not self.validate_contact_input():
            return
        
        contact = {
            'id': self.next_id,
            'name': self.contact_name.get().strip(),
            'phone': self.contact_phone.get().strip(),
            'email': self.contact_email.get().strip(),
            'group': self.contact_group.get()
        }
        
        self.contacts.append(contact)
        self.next_id += 1
        
        # Add to treeview
        self.tree.insert("", "end", values=(contact['name'], contact['phone'], 
                                            contact['email'], contact['group']),
                         tags=(contact['id'],))
        
        self.clear_form()
        self.contact_status.config(text=f"✅ Contact '{contact['name']}' added successfully!", 
                                   foreground="green")
        
        # Reset status after 3 seconds
        self.root.after(3000, lambda: self.contact_status.config(text="Ready", foreground="gray"))
    
    def delete_contact(self):
        """Delete selected contact from treeview and storage"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a contact to delete.")
            return
        
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?"):
            # Get the item values
            item = self.tree.item(selected[0])
            values = item['values']
            name = values[0] if values else "Unknown"
            
            # Remove from treeview
            self.tree.delete(selected[0])
            
            # Remove from storage by name (simple approach)
            self.contacts = [c for c in self.contacts if c['name'] != name]
            
            self.contact_status.config(text=f"🗑️ Deleted contact '{name}'", foreground="orange")
            self.clear_form()
    
    def clear_form(self):
        """Clear all form fields"""
        self.contact_name.delete(0, tk.END)
        self.contact_phone.delete(0, tk.END)
        self.contact_email.delete(0, tk.END)
        self.contact_group.set("Friend")
        self.contact_name.focus()
        self.contact_status.config(text="Form cleared", foreground="gray")
    
    def refresh_treeview(self):
        """Refresh the treeview with all contacts"""
        # Clear treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Re-add all contacts
        for contact in self.contacts:
            self.tree.insert("", "end", values=(contact['name'], contact['phone'],
                                                contact['email'], contact['group']),
                             tags=(contact['id'],))
        
        self.contact_status.config(text=f"📋 Showing {len(self.contacts)} contacts", foreground="blue")
    
    def on_contact_select(self, event):
        """Populate form when a contact is selected from treeview"""
        selected = self.tree.selection()
        if not selected:
            return
        
        item = self.tree.item(selected[0])
        values = item['values']
        
        if values:
            self.clear_form()
            self.contact_name.insert(0, values[0])
            self.contact_phone.insert(0, values[1])
            self.contact_email.insert(0, values[2])
            self.contact_group.set(values[3])
            self.contact_status.config(text=f"✏️ Editing contact: {values[0]}", foreground="purple")
    
    def on_double_click(self, event):
        """Handle double-click on treeview item"""
        self.on_contact_select(event)
        self.contact_status.config(text="Double-click detected - you can now edit the contact", foreground="green")
    
    # ========== STATUS BAR ==========
    
    def setup_status_bar(self):
        """Create status bar at bottom using place()"""
        self.status_var = tk.StringVar()
        self.status_var.set("✅ Ready | Tkinter Reviewer - All concepts demonstrated")
        
        status_bar = ttk.Label(self.root, textvariable=self.status_var, 
                               relief='sunken', anchor='w', padding=(5, 2))
        status_bar.pack(side='bottom', fill='x')
        
        # Update status with Python version info
        import sys
        self.status_var.set(f"✅ Python {sys.version.split()[0]} | Tkinter Complete Reviewer - Widgets | Layout | Events | Contact Manager")


# ========== RUN THE APPLICATION ==========

if __name__ == "__main__":
    app = TkinterReviewApp()