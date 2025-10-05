# 🧩 OS Lab Assignment 2 — System Startup Simulation (Python)

**Author:** Yuv Raj Singh Yadav  
**Course:** ENCS351 — Operating Systems Lab  
**Topic:** System Startup, Process Creation & Termination Simulation  



Theory for Each Sub-Task
🔹 Sub-Task 1 — Logging Configuration

Theory:
Logging captures real-time system activity. Using logging.basicConfig(), we record timestamps, process names, and messages into a log file to simulate a real OS boot log.

🔹 Sub-Task 2 — Simulating a Process

Theory:
Each process represents a small unit of work. The dummy task (time.sleep(2)) simulates CPU/IO operations, while logging shows when it starts and ends — similar to how daemons start during system boot.

🔹 Sub-Task 3 — Creating Processes

Theory:
The multiprocessing module spawns independent processes that run in parallel, mimicking concurrent services during system startup. Each process executes the same function with different arguments.

🔹 Sub-Task 4 — Joining and Termination

Theory:
join() ensures that the main process waits for all child processes to finish before shutting down — preventing premature system termination and ensuring clean process completion.
---

## 📖 Overview
This project simulates how an operating system starts, creates processes, tracks their activity, and shuts down gracefully.  
Using Python’s `multiprocessing` and `logging` modules, it demonstrates:
- Parallel process creation
- Logging system events with timestamps
- Proper synchronization and termination

---

## 🧠 Learning Objectives
- Understand system booting and process creation  
- Implement multiprocessing in Python  
- Log process lifecycle to simulate OS behavior  

---

## 🧮 How to Run
```bash
# Run on any system with Python 3.x
python3 system_startup_simulation.py
