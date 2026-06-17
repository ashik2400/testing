import time

def auto_save(func):
    def wrapper(self, *args, **kwargs):

        result = func(self, *args, **kwargs)

        self.save_tasks()

        print("Tasks auto-saved")

        return result

    return wrapper

# ---------------- DECORATOR ----------------
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"\n{func.__name__} took {end - start:.5f}s")

        return result

    return wrapper


# ---------------- OOP ----------------
class Task:
    def __init__(self, title, completed=False, **kwargs):
        self.title = title
        self.completed = completed
        self.extra = kwargs

    def __str__(self):
        status = "✓" if self.completed else " "

        return f"[{status}] {self.title}"


class TodoApp:
    def __init__(self):
        self.tasks = []

    # ---------- *args ----------
    @auto_save
    def add_tasks(self, *titles):
        for title in titles:
            self.tasks.append(Task(title))

    # ---------- **kwargs ----------
    def create_task(self, **kwargs):
        title = kwargs.pop("title")
        self.tasks.append(Task(title, **kwargs))

    @timer
    def view_tasks(self):

        if not self.tasks:
            print("No tasks found")
            return

        # ---------- GENERATOR ----------
        for index, task in enumerate(self.get_tasks(), start=1):
            print(f"{index}. {task}")

    @auto_save
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
    @auto_save
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    # ---------- GENERATOR ----------
    def get_tasks(self):
        for task in self.tasks:
            yield task

    # ---------- COMPREHENSION ----------
    def completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    # ---------- CONTEXT MANAGER ----------
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(
                    f"{task.title}|{task.completed}\n"
                )

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks.clear()

                for line in file:
                    title, completed = line.strip().split("|")

                    self.tasks.append(
                        Task(
                            title,
                            completed == "True"
                        )
                    )
        except FileNotFoundError:
            pass


# ---------------- MAIN ----------------
app = TodoApp()

app.load_tasks()

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Show Completed")
    print("6. Save")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        app.add_tasks(task)

    elif choice == "2":
        app.view_tasks()

    elif choice == "3":
        app.view_tasks()
        num = int(input("Task number: "))
        app.complete_task(num - 1)

    elif choice == "4":
        app.view_tasks()
        num = int(input("Task number: "))
        app.delete_task(num - 1)

    elif choice == "5":
        completed = app.completed_tasks()

        for task in completed:
            print(task)

    elif choice == "6":
        app.save_tasks()
        print("Saved")

    elif choice == "7":
        app.save_tasks()
        print("Bye")
        break

    else:
        print("Invalid option")

