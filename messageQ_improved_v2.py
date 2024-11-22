import tkinter as tk
from tkinter import ttk
from multiprocessing import Queue

# Create the message queue
message_queue = Queue(maxsize=5)

# Function to send custom messages to the queue
def send_message():
    custom_message = entry_message.get()
    if custom_message.strip() == "":
        log_message("Message cannot be empty!")
        return
    if not message_queue.full():
        message_queue.put(custom_message)
        update_queue_display()
        log_message(f"Sent: {custom_message}")
        entry_message.delete(0, tk.END)  # Clear the input field
    else:
        log_message("Queue is full!")

# Function to receive messages from the queue
def receive_message():
    if not message_queue.empty():
        message = message_queue.get()
        log_message(f"Received: {message}")
        update_queue_display()
    else:
        log_message("Queue is empty!")

# Function to log activity
def log_message(msg):
    log_area.insert(tk.END, msg + "\n")
    log_area.see(tk.END)

# Update the queue visualization
def update_queue_display():
    queue_list.delete(0, tk.END)
    temp_queue = Queue()
    while not message_queue.empty():
        msg = message_queue.get()
        queue_list.insert(tk.END, msg)
        temp_queue.put(msg)
    while not temp_queue.empty():
        message_queue.put(temp_queue.get())

# GUI Setup
root = tk.Tk()
root.title("Message Queue Visualizer")

# Configure root for resizing
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frame for queue visualization
queue_frame = ttk.LabelFrame(root, text="Message Queue", padding=10)
queue_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Configure the listbox inside queue frame
queue_list = tk.Listbox(queue_frame, height=10, width=30)
queue_list.pack(expand=True, fill=tk.BOTH)

# Frame for controls
control_frame = ttk.Frame(root, padding=10)
control_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Configure control frame
control_frame.grid_columnconfigure(0, weight=1)
control_frame.grid_columnconfigure(1, weight=1)
control_frame.grid_columnconfigure(2, weight=1)

# Control widgets
ttk.Label(control_frame, text="Message:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_message = ttk.Entry(control_frame, width=20)
entry_message.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

send_button = ttk.Button(control_frame, text="Send Message", command=send_message)
send_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

receive_button = ttk.Button(control_frame, text="Receive Message", command=receive_message)
receive_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Log area
log_frame = ttk.LabelFrame(root, text="Activity Log", padding=10)
log_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

log_area = tk.Text(log_frame, height=10, width=50, state=tk.NORMAL)
log_area.pack(expand=True, fill=tk.BOTH)

root.mainloop()
