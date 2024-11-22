import tkinter as tk
from tkinter import ttk

# Semaphore value (initially set to 3 for demonstration purposes)
semaphore_value = 3
max_semaphore_value = 3

# List of active processes holding the semaphore
active_processes = []

def acquire_semaphore():
    global semaphore_value
    if semaphore_value > 0:
        semaphore_value -= 1
        process_name = f"Process {len(active_processes) + 1}"
        active_processes.append(process_name)
        log_message(f"{process_name} acquired the semaphore.")
    else:
        log_message("Semaphore is at 0! No resource available.")
    update_display()

def release_semaphore():
    global semaphore_value
    if active_processes:
        process_name = active_processes.pop(0)
        semaphore_value += 1
        log_message(f"{process_name} released the semaphore.")
    else:
        log_message("No process is holding the semaphore.")
    update_display()

def update_display():
    semaphore_label.config(text=f"Semaphore Value: {semaphore_value}")
    process_list.delete(0, tk.END)
    for process in active_processes:
        process_list.insert(tk.END, process)

def log_message(msg):
    log_area.insert(tk.END, msg + "\n")
    log_area.see(tk.END)

# GUI Setup
root = tk.Tk()
root.title("Semaphore Simulation")

# Semaphore Value Display
semaphore_frame = ttk.LabelFrame(root, text="Semaphore State", padding=10)
semaphore_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

semaphore_label = ttk.Label(semaphore_frame, text=f"Semaphore Value: {semaphore_value}", font=("Arial", 14))
semaphore_label.pack()

# Active Processes
process_frame = ttk.LabelFrame(root, text="Active Processes", padding=10)
process_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

process_list = tk.Listbox(process_frame, height=5, width=30)
process_list.pack(expand=True, fill=tk.BOTH)

# Control Buttons
control_frame = ttk.Frame(root, padding=10)
control_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

acquire_button = ttk.Button(control_frame, text="Acquire Resource", command=acquire_semaphore)
acquire_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

release_button = ttk.Button(control_frame, text="Release Resource", command=release_semaphore)
release_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Log Area
log_frame = ttk.LabelFrame(root, text="Activity Log", padding=10)
log_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

log_area = tk.Text(log_frame, height=10, width=50, state=tk.NORMAL)
log_area.pack(expand=True, fill=tk.BOTH)

# Resizable Configuration
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
