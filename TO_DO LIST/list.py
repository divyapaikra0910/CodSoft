# To-Do List Application

class ToDoList:
    def __init__(self):
        self.tasks = []  # List to store tasks

    def show_tasks(self):
        if not self.tasks:
            print("\nYour to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "✅" if task['completed'] else "❌"
                print(f"{i}. {task['task']} [{status}]")

    def add_task(self, task_name):
        self.tasks.append({"task": task_name, "completed": False})
        print(f"Task '{task_name}' has been added to your list.")

    def update_task(self, task_index, new_task_name):
        try:
            self.tasks[task_index - 1]['task'] = new_task_name
            print(f"Task {task_index} has been updated to '{new_task_name}'.")
        except IndexError:
            print("Invalid task number. Please try again.")

    def mark_task_done(self, task_index):
        try:
            self.tasks[task_index - 1]['completed'] = True
            print(f"Task {task_index} has been marked as done.")
        except IndexError:
            print("Invalid task number. Please try again.")

    def delete_task(self, task_index):
        try:
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task['task']}' has been deleted.")
        except IndexError:
            print("Invalid task number. Please try again.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks have been cleared!")


def main():
    todo = ToDoList()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark task as done")
        print("5. Delete task")
        print("6. Clear all tasks")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            todo.show_tasks()
        elif choice == "2":
            task_name = input("Enter the task to add: ")
            todo.add_task(task_name)
        elif choice == "3":
            todo.show_tasks()
            try:
                task_index = int(input("Enter the task number to update: "))
                new_task_name = input("Enter the new task name: ")
                todo.update_task(task_index, new_task_name)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            todo.show_tasks()
            try:
                task_index = int(input("Enter the task number to mark as done: "))
                todo.mark_task_done(task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            todo.show_tasks()
            try:
                task_index = int(input("Enter the task number to delete: "))
                todo.delete_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "6":
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ").lower()
            if confirm == "yes":
                todo.clear_tasks()
        elif choice == "7":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
