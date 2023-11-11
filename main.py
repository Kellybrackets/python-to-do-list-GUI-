import tkinter as tk
from tkinter import ttk, messagebox
import turtle

def draw_koch_snowflake():
    try:
        screen = turtle.Screen()
        screen.bgcolor("white")

        fractal_turtle = turtle.Turtle()
        fractal_turtle.speed(0)

        fractal_turtle.penup()
        fractal_turtle.goto(-150, 90)
        fractal_turtle.pendown()

        koch_snowflake(fractal_turtle, 4, 300)

        screen.protocol("WM_DELETE_WINDOW", lambda: on_closing(screen, app))
        screen.mainloop()
    except turtle.Terminator:
        pass

def on_closing(screen, app):
    screen.bye()
    app.destroy()

def exit_app():
    result = messagebox.askyesno("Exit", "Are you sure you want to exit?\nThank you for using the GRIT Labs To-Do List.")
    if result:
        app.destroy()

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)

def add_task():
    try:
        task = entry.get()
        duration = duration_entry.get()
        if task:
            task_with_duration = f"{task} (Duration: {duration} mins)"
            listbox.insert(tk.END, task_with_duration)
            entry.delete(0, tk.END)
            duration_entry.delete(0, tk.END)
            add_check_button(task_with_duration)
        else:
            messagebox.showwarning("Warning", "You must enter a task!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        task_item = listbox.get(selected_task)
        listbox.delete(selected_task)
        remove_check_button(task_item)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def add_check_button(task_item):
    try:
        check_var = tk.BooleanVar()
        check_button = ttk.Checkbutton(listbox, variable=check_var, text=task_item, style="Custom.TCheckbutton", command=lambda: draw_koch_snowflake_and_message())
        check_button.pack(anchor="w")
        check_buttons[task_item] = check_var
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def remove_check_button(task_item):
    try:
        check_var = check_buttons.get(task_item)
        if check_var:
            check_buttons.pop(task_item)
            for widget in listbox.winfo_children():
                if isinstance(widget, ttk.Checkbutton):
                    if widget["text"] == task_item:
                        widget.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_task():
    try:
        selected_task = listbox.curselection()[0]
        new_task = entry.get()
        new_duration = duration_entry.get()
        if new_task:
            task_item = listbox.get(selected_task)
            listbox.delete(selected_task)
            task_with_duration = f"{new_task} (Duration: {new_duration} mins)"
            listbox.insert(tk.END, task_with_duration)
            entry.delete(0, tk.END)
            duration_entry.delete(0, tk.END)
            update_check_button(task_item, task_with_duration)
        else:
            messagebox.showwarning("Warning", "You must enter a task!")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_check_button(old_task, new_task):
    try:
        check_var = check_buttons.get(old_task)
        if check_var:
            check_buttons.pop(old_task)
            for widget in listbox.winfo_children():
                if isinstance(widget, ttk.Checkbutton):
                    if widget["text"] == old_task:
                        widget.config(text=new_task)
                        check_buttons[new_task] = check_var
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def draw_koch_snowflake_and_message():
    app.after(100, draw_koch_snowflake)
    messagebox.showinfo("Good Job", "Good job for completing!")

app = tk.Tk()
app.title("GRIT Labs To-Do List")

app.style = ttk.Style()
app.configure(bg="gray")

welcome_label = tk.Label(app, text="Welcome to the GRIT Labs To-Do List", font=("Helvetica", 16), bg="gray", fg="black")
welcome_label.pack(pady=20)

entry_label = tk.Label(app, text="Task:", font=("Helvetica", 14), bg="gray", fg="black")
entry = tk.Entry(app, font=("Helvetica", 14), background="white", foreground="black")
duration_label = tk.Label(app, text="Duration (mins):", font=("Helvetica", 14), bg="gray", fg="black")
duration_entry = tk.Entry(app, font=("Helvetica", 14), background="white", foreground="black")
add_button = ttk.Button(app, text="Add Task", command=add_task, style="Custom.TButton")
update_button = ttk.Button(app, text="Update Task", command=update_task, style="Custom.TButton")
delete_button = ttk.Button(app, text="Delete Task", command=delete_task, style="Custom.TButton")
exit_button = ttk.Button(app, text="Exit", command=exit_app, style="Custom.TButton")

listbox = tk.Listbox(app, font=("Helvetica", 14), bg="white", selectbackground="gray", selectforeground="black", height=5)

check_buttons = {}

entry_label.pack(pady=5, anchor="w")
entry.pack(pady=5, padx=10, fill=tk.X)
duration_label.pack(pady=5, anchor="w")
duration_entry.pack(pady=5, padx=10, fill=tk.X)
add_button.pack(pady=5)
update_button.pack(pady=5)
delete_button.pack(pady=5)
exit_button.pack(pady=5)
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

app.geometry("400x400")
app.mainloop()


