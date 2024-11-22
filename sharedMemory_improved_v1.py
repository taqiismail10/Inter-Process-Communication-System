import tkinter as tk
from tkinter import ttk
from multiprocessing import shared_memory, Lock

# Shared memory and lock
shared_mem_size = 10  # Number of "memory cells"
shared_mem = shared_memory.SharedMemory(create=True, size=shared_mem_size)
lock = Lock()

# Initialize shared memory with zeros
for i in range(shared_mem_size):
    shared_mem.buf[i] = 0

# Generate contiguous memory addresses
base_address = 0x1000  # Example base address
addresses = [hex(base_address + i) for i in range(shared_mem_size)]

# GUI Functions
def manual_write():
    """Manually write to a selected memory cell."""
    try:
        index = int(entry_index.get())
        value = entry_value.get()
        if len(value) > 1:
            log_message("Only one character allowed as a value.")
            return
        if 0 <= index < shared_mem_size:
            with lock:
                shared_mem.buf[index] = ord(value) if value else 0
            update_memory_display()
            log_message(f"Wrote '{value}' to cell {index} (Address: {addresses[index]})")
        else:
            log_message("Index out of range.")
    except ValueError:
        log_message("Invalid input for index.")

def manual_read():
    """Manually read from a selected memory cell."""
    try:
        index = int(entry_index.get())
        if 0 <= index < shared_mem_size:
            with lock:
                value = chr(shared_mem.buf[index]) if shared_mem.buf[index] != 0 else " "
            log_message(f"Read '{value}' from cell {index} (Address: {addresses[index]})")
        else:
            log_message("Index out of range.")
    except ValueError:
        log_message("Invalid input for index.")

def update_memory_display():
    """Update the memory visualization in the GUI."""
    for i in range(shared_mem_size):
        value = chr(shared_mem.buf[i]) if shared_mem.buf[i] != 0 else " "
        memory_cells[i].config(text=f"{value}\n{addresses[i]}")

def log_message(msg):
    """Log activity in the GUI log area."""
    log_area.insert(tk.END, msg + "\n")
    log_area.see(tk.END)

# GUI Setup
root = tk.Tk()
root.title("Shared Memory Visualizer with Addresses")

# Configure root for resizing
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frame for shared memory visualization
memory_frame = ttk.LabelFrame(root, text="Shared Memory", padding=10)
memory_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Configure memory frame for resizing
memory_frame.grid_columnconfigure(0, weight=1)

memory_cells = []
for i in range(shared_mem_size):
    cell = ttk.Label(memory_frame, text=" ", relief="solid", padding=10, width=10, anchor="center")
    cell.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
    memory_frame.grid_columnconfigure(i, weight=1)  # Make columns resizable
    memory_cells.append(cell)

# Frame for manual controls
control_frame = ttk.LabelFrame(root, text="Manual Operations", padding=10)
control_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Configure control frame for resizing
control_frame.grid_columnconfigure(0, weight=1)
control_frame.grid_columnconfigure(1, weight=1)
control_frame.grid_columnconfigure(2, weight=1)

ttk.Label(control_frame, text="Index:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_index = ttk.Entry(control_frame, width=5)
entry_index.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(control_frame, text="Value:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_value = ttk.Entry(control_frame, width=5)
entry_value.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

write_button = ttk.Button(control_frame, text="Write", command=manual_write)
write_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

read_button = ttk.Button(control_frame, text="Read", command=manual_read)
read_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

# Log area
log_frame = ttk.LabelFrame(root, text="Activity Log", padding=10)
log_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

log_area = tk.Text(log_frame, height=10, width=60, state=tk.NORMAL)
log_area.pack(expand=True, fill=tk.BOTH)

# Initial update
update_memory_display()

# Start GUI event loop
root.mainloop()

# Clean up shared memory on exit
shared_mem.close()
shared_mem.unlink()
