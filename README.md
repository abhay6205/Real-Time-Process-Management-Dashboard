# Real-Time Process Monitoring Dashboard

## Overview

The **Real-Time Process Monitoring Dashboard** is a Python-based graphical tool designed to provide administrators with live insights into system processes. It displays detailed information about process states, CPU usage, and memory consumption in an intuitive interface. The dashboard enables efficient process management by allowing users to monitor system performance, identify resource-intensive processes, and terminate them if necessary.

This project was developed by a team of three—Abhay, Harsh, and Shoaib, leveraging `psutil` for process data, `tkinter` for the GUI, and `matplotlib` for real-time visualizations.

---

## Problem Statement

**Problem:** Real-Time Process Monitoring Dashboard  
**Description:** Create a graphical dashboard that displays real-time information about process states, CPU usage, and memory consumption. The tool should allow administrators to manage processes efficiently and identify potential issues promptly.

---

## Features

- **Real-Time Process Table**: Displays a list of running processes with columns for PID, Name, Status, CPU%, Memory (MB), and User.
- **Visual Alerts**: Highlights processes with high CPU usage (>50%) in light red and high memory usage (>1GB) in light yellow.
- **Top Resource Graphs**: Bar charts showing the top 5 processes by CPU and memory usage, updated in real-time.
- **Process Termination**: Allows users to select and terminate processes with a confirmation prompt.
- **Customizable Refresh Rate**: Adjustable refresh interval (in milliseconds) to control update frequency.
- **Error Handling**: Gracefully handles permission issues, missing processes, and other exceptions.

---

## Prerequisites

- **Python 3**
- **Required Libraries**:
  - `psutil`: For process and system monitoring.
  - `tkinter`: For the GUI (usually included with Python).
  - `matplotlib`: For plotting graphs.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abhay6205/Real-Time-Process-Management-Dashboard.git
   cd Real-Time-Process-Management-Dashboard
   ```

2. **Install Dependencies**:
   Install the required Python libraries using `pip`:
   ```bash
   pip install psutil matplotlib
   ```
   *Note*: `tkinter` is typically included with Python. If not, install it via your package manager (e.g., `sudo apt-get install python3-tk` on Ubuntu).

3. **Run the Application**:
   ```bash
   python process_monitor.py
   ```
   Replace `process_monitor.py` with the actual filename of your script.

---

## Usage

1. **Launch the Dashboard**:
   Run the script to open the GUI window.

2. **Monitor Processes**:
   - The table updates automatically, showing all running processes.
   - High CPU/memory usage processes are highlighted for quick identification.
   - Graphs display the top 5 processes by CPU and memory usage.

3. **Adjust Refresh Rate**:
   - Enter a new value (in milliseconds) in the "Refresh (ms)" field to change how often the data updates (default is 1000 ms).

4. **Terminate a Process**:
   - Select a process in the table.
   - Click "Kill Selected Process".
   - Confirm the action in the pop-up dialog.
   - Note: Some processes may require administrator/root privileges to terminate.

5. **Exit**:
   Close the window to stop the application.

---

## Development Team and Timeline

This project was a collaborative effort by:
- **Abhay Kumar**: Focused on core functionality, process monitoring, and error handling.
- **Harsh**: Worked on GUI design, layout, and integration of visualizations.
- **Shoaib**: Handled graphing features, performance optimization, and testing.

**Timeline**: The team developed this dashboard from March 5, 2025, to March 27, 2025 where the team started maintaining the github portfolio from march 17 onwards. The development process included problem analysis, planning, coding, debugging, and refining the tool to meet the problem statement's requirements.

---

## Code Structure

- **`osproject.py`**: Main script containing the dashboard implementation.
  - **Imports**: Libraries for process monitoring, GUI, and plotting.
  - **GUI Setup**: Frames, table (`Treeview`), graphs, and controls.
  - **Core Functions**:
    - `update_processes()`: Fetches and displays process data, updates graphs.
    - `kill_process()`: Handles process termination with error checking.
  - **Event Loop**: Runs the real-time updates and user interactions.

---

## Limitations

- **Administrator Privileges**: Some processes may require elevated permissions to monitor or terminate.
- **Performance**: High refresh rates with many processes may impact system performance.
- **Total Processes Counter**: The "Total Processes" label is not dynamically updated in the current version.

---

## Future Enhancements

- Add sorting functionality to the process table by clicking column headers.
- Implement a filter to search for specific processes by name or PID.
- Display system-wide CPU and memory usage metrics.
- Update the "Total Processes" label dynamically.
- Add support for saving process logs to a file.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.

---

## Acknowledgments

- Built with [psutil](https://github.com/giampaolo/psutil), [tkinter](https://docs.python.org/3/library/tkinter.html), and [matplotlib](https://matplotlib.org/).
- Special thanks to Abhay, Harsh, and Shoaib for their dedication to bring this project to life.

---

### Notes:
1. **Team Contributions**: Abhay: GUI and process termination, Harsh: Graphing and debugging, Shoaib: Data collection and optimization.
2. **Timeline**: (March 5–27, 2025).
3. **GitHub Setup**: Replace `abhay6205` with your actual GitHub username and ensure the repository name matches your project.

## THANKS!!
