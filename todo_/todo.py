# A simple command-line TODO application
tasks = []
print('======Welcome to TODO app======\n')

def view_task():
    # Display all tasks with their status
    if not tasks:
        print('\nNothing to do, add a task!\n')
    else:
        print('\n--- Current Tasks ---')
        for index, task in enumerate(tasks, start=1):
            status = '✔️ Done' if task['completed'] else 'Pending'
            print(f"{index}. {task['title']} - {status}")
            print('---------------------\n')


def add_task():
    # Add a new task to the list
    new_task = input('Add a new task: ').strip()

    # Check for duplicates (case-insensitive)
    exists = any(task['title'].lower() == new_task.lower() for task in tasks)
    if new_task:
        if exists:
            print('Task already exists, please try again')
            return
        else:
            task = {'title': new_task , 'completed' : False}
            tasks.append(task)
            print(f'Task "{new_task}" added successfully')
    else:
        print('Task cannot be empty, please try again')


def task_status_update():
    # Update the status of a task to completed
    view_task()
    if not tasks:
        return
    try:
        task_status = int(input('Which task did you just complete: (select the number) '))
        tasks[task_status - 1]['completed'] = True
        print(f'Task {task_status} marked as completed')
    except (ValueError, IndexError):
        print('Invalid task number, please try again')


def delete_task():
    view_task()
    if not tasks:
        return              
    try:
        task_num = int(input('Which task do you want to delete: (select the number) '))
        deleted = tasks.pop(task_num - 1)
        
        print(f'Task {task_num} deleted successfully')
    except (ValueError, IndexError):
        print('Invalid task number, please try again')


def exit_app():
    print('\n Exiting program... Goodbye')
    return True
    


def main():
    while True:
        choices = '''   ---What would you like to do--- \n
                        1. Show existing tasks  📋
                        2. Add a tasks  ➕
                        3. Update task status ✔️
                        4. Delete task ❌
                        5. Exit 🚪
                '''
        print(choices)
        try:
            choice = int(input('Choose one: '))

        except ValueError:
            print("⚠️ Invalid choice. Please enter a number from the menu.")
            continue
# Using match-case to iterate through user choices
        match choice:
            case 1:
                view_task()
            case 2:
                add_task()
            case 3:
                task_status_update()
            case 4:
                delete_task()
            case 5:
                if exit_app():
                    break
            case _ :
                print("⚠️ Invalid choice. Please enter a number from the menu.")

        

if __name__ == '__main__':
    main()