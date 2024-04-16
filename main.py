class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully.")
        else:
            print("Task not found in the list.")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print("Task updated successfully.")
        else:
            print("Task not found in the list.")

    def view_tasks(self):
        if not self.tasks:
            print("Your To-Do List is empty.")
        else:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

if __name__ == "__main__":
    manager = ToDoListManager()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            task_to_add = input("Enter the task to add: ")
            manager.add_task(task_to_add)
        elif choice == "2":
            task_to_remove = input("Enter the task to remove: ")
            manager.remove_task(task_to_remove)
        elif choice == "3":
            old_task = input("Enter the task to update: ")
            new_task = input("Enter the updated task description: ")
            manager.update_task(old_task, new_task)
        elif choice == "4":
            manager.view_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")
