# 📝 Python To-Do List GUI  
*A simple yet powerful command-line task manager with GUI elements, persistent storage, due dates, and priority tracking.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
![To-Do App Demo](todo_logo.png)  

---

## 🚀 Features  

✅ **Task Management**  
- Add, view, update, delete, and complete tasks with simple commands  

💾 **Persistent Storage**  
- Saves tasks in a local JSON file, retaining data between sessions  

📅 **Due Date Tracking**  
- Add deadlines to tasks using Python’s `datetime` module  

📊 **Progress Summary**  
- Displays how many tasks are pending vs completed  

⚡ **Priority Levels**  
- Tag tasks as Low, Medium, or High priority to stay organized  

🖼️ **Optional GUI Support** (Planned)  
- The project is expandable to include a Tkinter-based GUI interface  

---

## ⚙️ Setup & Installation  

### ✅ Method 1: Git Clone  
```bash
git clone https://github.com/Kellybrackets/Python-to-do-list-GUI-.git
cd Python-to-do-list-GUI-
python main.py
```

### 📁 Method 2: Manual Download
	1.	Download the ZIP from GitHub
	2.	Extract the files
	3.	Navigate to the folder
	4.	Run the app:
 ```
pip install -r requirements.txt  # Only if dependencies exist
python main.py
 ```

### 🛠️ Technical Stack

Language:
	•	Python 3.8+

### Key Python Modules Used:
 ```
import datetime  # For managing task deadlines
import json      # For storing and loading tasks
import os        # For file system operations
 ```

### Planned Modules for GUI:
 ```
import tkinter   # For building a future GUI (not yet implemented)
 ```

### 📌 Future Enhancements
	•	GUI using Tkinter or PyQt
	•	Email reminders for due dates
	•	Cloud sync with Google Drive or Firebase
	•	CLI flags and argument parser (e.g., argparse)
	•	Improved validation and error handling
