import json #allows u to save and load tasks as json file

import os #to check if file exists

TASKS_FILE = 'tasks.json' #
TASKS = [] #Global list to hold tasks in memory

print("Task file name:", TASKS_FILE)
print("Initial tasks list:", TASKS)

def load_tasks():
    """Load tasks from the JSON file into the TASKS list."""
    global TASKS

    if os.path.exists(TASKS_FILE):
       try:
           with open(TASKS_FILE, 'r') as f: #Open the file, call it "f", and when I am done reading, close it automatically
               TASKS = json.load(f) #Reads the text from the file and converts it from JSON to Python objects
       except json.JSONDecodeError:
            print("Error: Could not decode JSON from the tasks file.")
            TASKS = []
    else:
        TASKS = []
    
    print(f"loaded {len(TASKS)} tasks.")

load_tasks()
   
        