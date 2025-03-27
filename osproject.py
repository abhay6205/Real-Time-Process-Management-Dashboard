import matplotlib.pyplot as plt

# Graph frame (Shoaib defines axes and graphing logic)
ax_cpu = fig_cpu.add_subplot(111)
ax_mem = fig_mem.add_subplot(111)

# Update processes (graphing and optimization part)
def update_processes():
    # (Data collection by Abhay)
    # Treeview update (shared with Harsh for display)
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
    
    # Graphing logic
    top_cpu = sorted(processes, key=lambda x: x[3], reverse=True)[:5]
    top_mem = sorted(processes, key=lambda x: x[4], reverse=True)[:5]
    
    ax_cpu.clear()
    cpu_names = [x[1][:15] + "..." if len(x[1]) > 15 else x[1] for x in top_cpu]
    ax_cpu.bar(range(5), [x[3] for x in top_cpu], color="salmon")
    ax_cpu.set_xticks(range(5))
    ax_cpu.set_xticklabels(cpu_names, rotation=45, ha='right')
    ax_cpu.set_title("Top 5 CPU Usage")
    ax_cpu.set_ylabel("CPU %")
    fig_cpu.tight_layout()
    canvas_cpu.draw()
    
    ax_mem.clear()
    mem_names = [x[1][:15] + "..." if len(x[1]) > 15 else x[1] for x in top_mem]
    ax_mem.bar(range(5), [x[4] for x in top_mem], color="lightblue")
    ax_mem.set_xticks(range(5))
    ax_mem.set_xticklabels(mem_names, rotation=45, ha='right')
    ax_mem.set_title("Top 5 Memory Usage")
    ax_mem.set_ylabel("Memory MB")
    fig_mem.tight_layout()
    canvas_mem.draw()
