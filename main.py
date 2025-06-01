import tkinter as tk
from tkinter import ttk, messagebox, font
from tkinter.constants import *


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("800x600")
        self.root.minsize(700, 500)

        # Modern color scheme
        self.colors = {
            'background': '#f5f7fa',
            'primary': '#4f46e5',
            'primary_light': '#6366f1',
            'secondary': '#f43f5e',
            'text': '#1e293b',
            'text_light': '#64748b',
            'card': '#ffffff',
            'success': '#10b981'
        }

        # Configure styles
        self.configure_styles()

        # Initialize task list
        self.tasks = []

        # Create UI
        self.create_ui()

    def configure_styles(self):
        """Configure custom styles for the application"""
        style = ttk.Style()

        # General style configurations
        style.theme_use('clam')
        self.root.configure(bg=self.colors['background'])

        # Button styles
        style.configure('TButton',
                        font=('Segoe UI', 10),
                        padding=8,
                        borderwidth=0)

        style.map('Primary.TButton',
                  background=[('active', self.colors['primary_light']),
                              ('!active', self.colors['primary'])],
                  foreground=[('!active', 'white')])

        style.map('Secondary.TButton',
                  background=[('active', '#f54e6e'),
                              ('!active', self.colors['secondary'])],
                  foreground=[('!active', 'white')])

        # Entry style
        style.configure('TEntry',
                        font=('Segoe UI', 11),
                        padding=8,
                        bordercolor=self.colors['text_light'],
                        lightcolor=self.colors['text_light'])

        # Frame style
        style.configure('Card.TFrame',
                        background=self.colors['card'],
                        borderwidth=2,
                        relief=tk.RAISED)

        # Label styles
        style.configure('Title.TLabel',
                        font=('Segoe UI', 18, 'bold'),
                        background=self.colors['background'],
                        foreground=self.colors['text'])

        style.configure('Subtitle.TLabel',
                        font=('Segoe UI', 12),
                        background=self.colors['background'],
                        foreground=self.colors['text_light'])

        # Treeview style (for task list)
        style.configure('Treeview',
                        font=('Segoe UI', 11),
                        rowheight=35,
                        background=self.colors['card'],
                        fieldbackground=self.colors['card'],
                        foreground=self.colors['text'])

        style.configure('Treeview.Heading',
                        font=('Segoe UI', 11, 'bold'),
                        background=self.colors['primary'],
                        foreground='white')

        style.map('Treeview',
                  background=[('selected', self.colors['primary_light'])],
                  foreground=[('selected', 'white')])

    def create_ui(self):
        """Create the main user interface"""
        # Header frame
        header_frame = ttk.Frame(self.root, padding=(20, 10))
        header_frame.pack(fill=X, pady=(0, 10))

        # App title
        title_label = ttk.Label(header_frame,
                                text="To-Do List",
                                style='Title.TLabel')
        title_label.pack(side=LEFT)

        # Add some decorative elements
        ttk.Separator(self.root, orient=HORIZONTAL).pack(fill=X, padx=20)

        # Main content frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Input panel (left side)
        input_frame = ttk.Frame(main_frame, style='Card.TFrame', padding=20)
        input_frame.pack(side=LEFT, fill=Y, padx=(0, 10))

        # Task input form
        ttk.Label(input_frame,
                  text="Add New Task",
                  font=('Segoe UI', 14, 'bold'),
                  foreground=self.colors['primary']).pack(anchor=W, pady=(0, 15))

        # Task title
        ttk.Label(input_frame,
                  text="Task Title:",
                  font=('Segoe UI', 10)).pack(anchor=W)
        self.task_entry = ttk.Entry(input_frame,
                                    font=('Segoe UI', 11),
                                    width=30)
        self.task_entry.pack(fill=X, pady=(0, 10))

        # Task description
        ttk.Label(input_frame,
                  text="Description:",
                  font=('Segoe UI', 10)).pack(anchor=W)
        self.desc_entry = tk.Text(input_frame,
                                  font=('Segoe UI', 11),
                                  height=4,
                                  width=30,
                                  padx=8,
                                  pady=8,
                                  highlightthickness=1,
                                  highlightcolor=self.colors['text_light'],
                                  highlightbackground=self.colors['text_light'])
        self.desc_entry.pack(fill=X, pady=(0, 10))

        # Priority selection
        ttk.Label(input_frame,
                  text="Priority:",
                  font=('Segoe UI', 10)).pack(anchor=W)
        self.priority_var = tk.StringVar(value="Medium")
        priority_menu = ttk.Combobox(input_frame,
                                     textvariable=self.priority_var,
                                     values=["Low", "Medium", "High"],
                                     state='readonly',
                                     font=('Segoe UI', 11))
        priority_menu.pack(fill=X, pady=(0, 20))

        # Action buttons
        button_frame = ttk.Frame(input_frame)
        button_frame.pack(fill=X)

        self.add_button = ttk.Button(button_frame,
                                     text="Add Task",
                                     style='Primary.TButton',
                                     command=self.add_task)
        self.add_button.pack(side=LEFT, fill=X, expand=True, padx=(0, 5))

        self.update_button = ttk.Button(button_frame,
                                        text="Update",
                                        style='Secondary.TButton',
                                        command=self.update_task,
                                        state=DISABLED)
        self.update_button.pack(side=LEFT, fill=X, expand=True)

        # Task list panel (right side)
        list_frame = ttk.Frame(main_frame, style='Card.TFrame', padding=10)
        list_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Task list header
        ttk.Label(list_frame,
                  text="Your Tasks",
                  font=('Segoe UI', 14, 'bold'),
                  foreground=self.colors['primary']).pack(anchor=W, pady=(0, 10))

        # Task list (using Treeview for better appearance)
        self.task_tree = ttk.Treeview(list_frame,
                                      columns=('priority', 'description'),
                                      selectmode='browse',
                                      style='Treeview')

        # Configure columns
        self.task_tree.heading('#0', text='Task', anchor=W)
        self.task_tree.heading('priority', text='Priority', anchor=W)
        self.task_tree.heading('description', text='Description', anchor=W)

        self.task_tree.column('#0', width=200, stretch=NO)
        self.task_tree.column('priority', width=100, stretch=NO)
        self.task_tree.column('description', width=300)

        self.task_tree.pack(fill=BOTH, expand=True)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame,
                                  orient=VERTICAL,
                                  command=self.task_tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.task_tree.configure(yscrollcommand=scrollbar.set)

        # Action buttons for task list
        action_frame = ttk.Frame(list_frame)
        action_frame.pack(fill=X, pady=(10, 0))

        self.delete_button = ttk.Button(action_frame,
                                        text="Delete Task",
                                        style='Secondary.TButton',
                                        command=self.delete_task,
                                        state=DISABLED)
        self.delete_button.pack(side=LEFT, fill=X, expand=True, padx=(0, 5))

        self.complete_button = ttk.Button(action_frame,
                                          text="Mark Complete",
                                          style='Primary.TButton',
                                          command=self.mark_complete,
                                          state=DISABLED)
        self.complete_button.pack(side=LEFT, fill=X, expand=True)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.root,
                               textvariable=self.status_var,
                               font=('Segoe UI', 9),
                               foreground=self.colors['text_light'],
                               padding=(10, 5),
                               relief=tk.SUNKEN,
                               anchor=W)
        status_bar.pack(fill=X, side=BOTTOM)

        # Bind selection event
        self.task_tree.bind('<<TreeviewSelect>>', self.on_task_select)

    def add_task(self):
        """Add a new task to the list"""
        title = self.task_entry.get().strip()
        description = self.desc_entry.get("1.0", END).strip()
        priority = self.priority_var.get()

        if not title:
            messagebox.showwarning("Warning", "Task title cannot be empty!")
            return

        # Add to internal list
        task_id = len(self.tasks) + 1
        task_data = {
            'id': task_id,
            'title': title,
            'description': description,
            'priority': priority,
            'completed': False
        }
        self.tasks.append(task_data)

        # Add to Treeview
        self.task_tree.insert('', END,
                              text=title,
                              values=(priority, description),
                              tags=('pending',))

        # Clear input fields
        self.task_entry.delete(0, END)
        self.desc_entry.delete("1.0", END)
        self.priority_var.set("Medium")

        self.status_var.set(f"Task '{title}' added successfully!")

    def on_task_select(self, event):
        """Handle task selection event"""
        selected_item = self.task_tree.selection()
        if selected_item:
            self.update_button['state'] = NORMAL
            self.delete_button['state'] = NORMAL
            self.complete_button['state'] = NORMAL

            # Load selected task into input fields
            item = self.task_tree.item(selected_item)
            self.task_entry.delete(0, END)
            self.task_entry.insert(0, item['text'])
            self.desc_entry.delete("1.0", END)
            self.desc_entry.insert("1.0", item['values'][1])
            self.priority_var.set(item['values'][0])
        else:
            self.update_button['state'] = DISABLED
            self.delete_button['state'] = DISABLED
            self.complete_button['state'] = DISABLED

    def update_task(self):
        """Update the selected task"""
        selected_item = self.task_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No task selected!")
            return

        title = self.task_entry.get().strip()
        description = self.desc_entry.get("1.0", END).strip()
        priority = self.priority_var.get()

        if not title:
            messagebox.showwarning("Warning", "Task title cannot be empty!")
            return

        # Update Treeview item
        self.task_tree.item(selected_item,
                            text=title,
                            values=(priority, description))

        # Update internal list
        item_id = self.task_tree.index(selected_item)
        if 0 <= item_id < len(self.tasks):
            self.tasks[item_id]['title'] = title
            self.tasks[item_id]['description'] = description
            self.tasks[item_id]['priority'] = priority

        self.status_var.set(f"Task '{title}' updated successfully!")

        # Clear selection
        self.task_tree.selection_remove(selected_item)

    def delete_task(self):
        """Delete the selected task"""
        selected_item = self.task_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No task selected!")
            return

        task_title = self.task_tree.item(selected_item, 'text')

        if messagebox.askyesno("Confirm Delete",
                               f"Are you sure you want to delete '{task_title}'?"):
            # Remove from Treeview
            self.task_tree.delete(selected_item)

            # Remove from internal list
            item_id = self.task_tree.index(selected_item)
            if 0 <= item_id < len(self.tasks):
                self.tasks.pop(item_id)

            self.status_var.set(f"Task '{task_title}' deleted successfully!")

            # Clear input fields
            self.task_entry.delete(0, END)
            self.desc_entry.delete("1.0", END)
            self.priority_var.set("Medium")

    def mark_complete(self):
        """Mark the selected task as completed"""
        selected_item = self.task_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No task selected!")
            return

        task_title = self.task_tree.item(selected_item, 'text')

        # Update Treeview appearance
        self.task_tree.item(selected_item, tags=('completed',))
        self.task_tree.tag_configure('completed',
                                     foreground=self.colors['text_light'])

        # Update internal list
        item_id = self.task_tree.index(selected_item)
        if 0 <= item_id < len(self.tasks):
            self.tasks[item_id]['completed'] = True

        self.status_var.set(f"Task '{task_title}' marked as completed!")

        # Clear selection
        self.task_tree.selection_remove(selected_item)


def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()


