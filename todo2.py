tasks = []

def add_task():
    name_task = input("Type the new task: ")
    date_task = input("Add a date: ")
    hour_task = input("Add a hour: ")
    task = {
        "name": name_task,
        "date": date_task,
        "hour": hour_task,
        "done": False
    }

    tasks.append(task)

def remove_task():
    name = input("Enter the name of the task you want to remove: ")
    for task in tasks:
        if task["name"] == name:
            remove_it = input(f"Are you sure you want to remove the task '{name}'? y = yes, n = no:\n")
            if remove_it == 'y':
                tasks.remove(task)
            else:
                continue
        else:
            continue
    

def list_tasks():
    for i, task in enumerate(tasks):
        print(f'{i + 1}. {task["name"]}. Done: {task["done"]}')
        

def mark_as_done():
    name = input('Enter the name of the task to make as done: ')
    for task in tasks:
        if task['name'] == name:
            remove_it = input(f'Are you sure you want to make the task "{name}" as done? y = yes, n = no: ')
            if remove_it == 'y':
                task['done'] = True
                print(f'The task {name} was marked as done.')
            else: 
                continue
        else: 
            continue


while True:
    print("===Enter a number:===")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List tasks.")
    print("4. Mark task as done.")
    print("0. Quit")

    number = int(input())

    if number == 1:
        add_task()
    
    elif number == 2:
        remove_task()

    elif number == 3:
        list_tasks()

    elif number == 4:
        mark_as_done()

    elif number == 0:
        exit()
    
    else:
        print("Not a valid number!")