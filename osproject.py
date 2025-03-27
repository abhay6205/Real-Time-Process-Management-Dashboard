import psutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# Initialize window
root = tk.Tk()
root.title("Real-Time Process Monitoring Dashboard")
root.geometry("1200x800")

# Variables
refresh_rate = tk.IntVar(value=1000)  # Refresh rate in ms

# Main layout
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Control frame
control_frame = tk.Frame(main_frame)
control_frame.pack(fill=tk.X)

# Content pane
content_pane = ttk.PanedWindow(main_frame, orient=tk.VERTICAL)
content_pane.pack(fill=tk.BOTH, expand=True)

# Table frame
table_frame = tk.Frame(content_pane)
content_pane.add(table_frame, weight=1)

# Treeview setup
tree = ttk.Treeview(table_frame, 
                    columns=("PID", "Name", "Status", "CPU%", "Memory MB", "User"),
                    show="headings",
                    height=15,
                    selectmode="browse")
tree.heading("PID", text="PID")
tree.heading("Name", text="Name")
tree.heading("Status", text="Status")
tree.heading("CPU%", text="CPU%")
tree.heading("Memory MB", text="Memory MB")
tree.heading("User", text="User")
for col in tree["columns"]:
    tree.column(col, width=120, anchor="center")
tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(fill=tk.Y, side=tk.RIGHT)

# Graph frame
graph_frame = tk.Frame(content_pane)
content_pane.add(graph_frame, weight=1)

# CPU graph
fig_cpu = plt.Figure(figsize=(6, 4), dpi=100)
ax_cpu = fig_cpu.add_subplot(111)
canvas_cpu = FigureCanvasTkAgg(fig_cpu, master=graph_frame)
canvas_cpu.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Memory graph
fig_mem = plt.Figure(figsize=(6, 4), dpi=100)
ax_mem = fig_mem.add_subplot(111)
canvas_mem = FigureCanvasTkAgg(fig_mem, master=graph_frame)
canvas_mem.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Selection debugging
def on_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])["values"]
        print(f"Selected: {item}")

tree.bind("<<TreeviewSelect>>", on_select)
tree.focus_set()

# Update processes
def update_processes():
    start_time = time.time()
    processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'status', 'username']):
        try:
            with proc.oneshot():
                pid = proc.pid
                name = proc.name()
                status = proc.status()
                cpu = proc.cpu_percent(interval=None)
                memory = proc.memory_info().rss / (1024 * 1024)
                user = proc.username().split('\\')[-1]
                processes.append((pid, name, status, cpu, memory, user))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    # Update Treeview
    tree.delete(*tree.get_children())
    for p in processes:
        tags = []
        if p[3] > 50:
            tags.append("high_cpu")
        if p[4] > 1000:
            tags.append("high_mem")
        tree.insert('', 'end', values=(p[0], p[1], p[2], f"{p[3]:.1f}", f"{p[4]:.1f}", p[5]), tags=tags)
    
    tree.tag_configure("high_cpu", background="#ffcccc")
    tree.tag_configure("high_mem", background="#ffffcc")
    
    # Update graphs
    top_cpu = sorted(processes, key=lambda x: x[3], reverse=True)[:5]
    top_mem = sorted(processes, key=lambda x: x[4], reverse=True)[:5]
    
    ax_cpu.clear()
    cpu_names = [x[1][:15] + "..." if len(x[1]) > 15 else x[1] for x in top_cpu]
    ax_cpu.bar(range(5), [x[3] for x in top_cpu], color="salmon")
    ax_cpu.set_xticks(range(5))  # Explicitly set the number of ticks
    ax_cpu.set_xticklabels(cpu_names, rotation=45, ha='right')
    ax_cpu.set_title("Top 5 CPU Usage")
    ax_cpu.set_ylabel("CPU %")
    fig_cpu.tight_layout()
    canvas_cpu.draw()
    
    ax_mem.clear()
    mem_names = [x[1][:15] + "..." if len(x[1]) > 15 else x[1] for x in top_mem]
    ax_mem.bar(range(5), [x[4] for x in top_mem], color="lightblue")
    ax_mem.set_xticks(range(5))  # Explicitly set the number of ticks
    ax_mem.set_xticklabels(mem_names, rotation=45, ha='right')
    ax_mem.set_title("Top 5 Memory Usage")
    ax_mem.set_ylabel("Memory MB")
    fig_mem.tight_layout()
    canvas_mem.draw()
    
    # Dynamic refresh
    elapsed = (time.time() - start_time) * 1000
    delay = max(100, refresh_rate.get() - int(elapsed))
    root.after(delay, update_processes)

# Kill process
def kill_process():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a process first")
        return
    item = tree.item(selected[0])["values"]
    pid, name = int(item[0]), item[1]
    if messagebox.askyesno("Confirm", f"Kill {name} (PID: {pid})?"):
        try:
            process = psutil.Process(pid)
            process.terminate()
            time.sleep(0.1)
            if process.is_running():
                process.kill()
            messagebox.showinfo("Success", f"Process {name} terminated")
        except psutil.NoSuchProcess:
            messagebox.showinfo("Info", "Process already terminated")
        except psutil.AccessDenied:
            messagebox.showerror("Error", "Permission denied - Run as Administrator")
        except Exception as e:
            messagebox.showerror("Error", f"Failed: {str(e)}")

# Control panel
tk.Button(control_frame, text="Kill Selected Process", command=kill_process).pack(side=tk.LEFT, padx=5)
tk.Label(control_frame, text="Refresh (ms):").pack(side=tk.LEFT, padx=5)
tk.Entry(control_frame, textvariable=refresh_rate, width=6).pack(side=tk.LEFT)
tk.Label(control_frame, text=" | ").pack(side=tk.LEFT)
tk.Label(control_frame, text="Total Processes: ").pack(side=tk.LEFT)
total_procs_label = tk.Label(control_frame, text="0")
total_procs_label.pack(side=tk.LEFT)

# Start and run
update_processes()
root.mainloop()
