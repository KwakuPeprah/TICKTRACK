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



def save_tasks():
    """Save the TASKS list to the JSON file."""
    with open(TASKS_FILE, 'w') as f:             #Open the file for writing
        json.dump(TASKS, f, indent=4)             #Convert Python objects to JSON and write to the file
    print(f"saved {len(TASKS)} tasks.")          #display how many tasks were saved    
   


def add_task(description):
    new_task = {
        'id': len(TASKS) + 1,
        'description': description,
        'completed': False
    }
    TASKS.append(new_task)
    save_tasks()
    print(f"\nTask added: '{description}'\n")

def view_tasks():
    if not TASKS:
        print("\n✅ Your task list is empty!")
        return

    print("\n--- Current Tasks ---")
    for task in TASKS:
        status = "✅" if task['completed'] else "☐"
        print(f"[{task['id']}] {status} {task['description']}")
    print("---------------------\n")

def complete_task(task_id):
    try:
        task_id = int(task_id)
    except ValueError:
        print("\n❌ Invalid ID. Please enter a number.")
        return

    found = False
    for task in TASKS:
        if task['id'] == task_id:
            task['completed'] = True
            found = True
            print(f"\nTask ID {task_id} ('{task['description']}') marked as complete.")
            break
        save_tasks()
    
    if not found:
        print(f"\n❌ Task with ID {task_id} not found.")
    
    
def main():
        load_tasks()

        while True:
            print("\n--- Task Tracker CLI ---")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Complete Task")
            print("4. Exit")
        
            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                view_tasks()
            elif choice == '2':
                desc = input("Enter task description: ").strip()
                if desc:
                    add_task(desc)
                else:
                    print("Task description cannot be empty.")
            elif choice == '3':
                    task_id_str = input("Enter the ID of the task to complete: ").strip()
                    if task_id_str:
                        complete_task(task_id_str)
            elif choice == '4':
                 print("👋 Exiting Task Tracker. Goodbye!")
                 break
            else:
                 print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
        