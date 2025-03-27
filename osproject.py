import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize window
root = tk.Tk()
root.title("Real-Time Process Monitoring Dashboard")
root.geometry("1200x800")

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

# CPU graph integration
fig_cpu = plt.Figure(figsize=(6, 4), dpi=100)
canvas_cpu = FigureCanvasTkAgg(fig_cpu, master=graph_frame)
canvas_cpu.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Memory graph integration
fig_mem = plt.Figure(figsize=(6, 4), dpi=100)
canvas_mem = FigureCanvasTkAgg(fig_mem, master=graph_frame)
canvas_mem.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Selection handling
def on_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])["values"]
        print(f"Selected: {item}")

tree.bind("<<TreeviewSelect>>", on_select)
tree.focus_set()

# Control panel
tk.Button(control_frame, text="Kill Selected Process", command=kill_process).pack(side=tk.LEFT, padx=5)
tk.Label(control_frame, text="Refresh (ms):").pack(side=tk.LEFT, padx=5)
tk.Entry(control_frame, textvariable=refresh_rate, width=6).pack(side=tk.LEFT)
tk.Label(control_frame, text=" | ").pack(side=tk.LEFT)
tk.Label(control_frame, text="Total Processes: ").pack(side=tk.LEFT)
total_procs_label = tk.Label(control_frame, text="0")
total_procs_label.pack(side=tk.LEFT)

# Start and run (GUI event loop)
root.mainloop()
