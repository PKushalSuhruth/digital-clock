import tkinter as tk
import time

def time_update():
    current_time = time.strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, time_update)  # Update the time every 1 second

# Set up the main application window
root = tk.Tk()
root.title("Digital Clock")

# Create and configure the label to display the clock
clock_label = tk.Label(root, font=('Arial', 48), bg='black', fg='white')
clock_label.pack(anchor='center')

# Start the time update function
time_update()

# Run the main loop to display the window
root.mainloop()
