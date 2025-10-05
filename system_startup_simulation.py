#!/usr/bin/env python3
"""
System Startup, Process Creation, and Termination Simulation
Course Code: ENCS351 - Operating Systems Lab
Author: Yuv Raj Singh Yadav
Description:
Simulates a basic system startup using multiprocessing and logging modules.
Each process represents a system service performing a dummy task.
"""

import multiprocessing
import time
import logging

# ---------------------------
# Sub-Task 1: Logging setup
# ---------------------------
logging.basicConfig(
    filename='process_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

# ---------------------------
# Sub-Task 2: Dummy process function
# ---------------------------
def system_process(task_name):
    """Simulate a process performing work."""
    logging.info(f"{task_name} started")
    print(f"{task_name} is running...")
    time.sleep(2)  # Simulate time-consuming work
    logging.info(f"{task_name} ended")
    print(f"{task_name} completed.")

# ---------------------------
# Sub-Task 3 & 4: Main control
# ---------------------------
if __name__ == '__main__':
    print("System Starting...\n")
    start_time = time.time()

    # Create processes (you can add more for demonstration)
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    # System shutdown message
    end_time = time.time()
    print("\nSystem Shutdown.")
    logging.info(f"System startup and shutdown completed in {end_time - start_time:.2f} seconds.")
