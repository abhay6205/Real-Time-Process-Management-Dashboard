import psutil
import time

# Variables 
refresh_rate = tk.IntVar(value=1000)  # Refresh rate in ms

# Update processes (data collection and process management part)
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
    
    
    
    # Dynamic refresh
    elapsed = (time.time() - start_time) * 1000
    delay = max(100, refresh_rate.get() - int(elapsed))
    root.after(delay, update_processes)

# Kill process (error handling and process termination)
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
