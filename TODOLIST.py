
class Task:
    def __init__(self, title, description, deadline=None,status=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status=status

    def __str__(self):
        return f"Задача: {self.title}\nОписание: {self.description}\nДедлайн: {self.deadline}\nСтатус задачи: {self.status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self, index, title, description, deadline):
        if 0 < len(self.tasks):
            task = self.tasks[index - 1]
            task.title = title
            task.description = description
            task.deadline=deadline
            task.status=status
        else:
            print("Недопустимый номер задачи.")

    def remove_task(self, index):
        if 0 < len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Задача '{removed_task.title}' удалена.")
        else:
            print("Недопустимый номер задачи.")


    def view_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}\n")
        else:
            print("У вас нет задач.")

    def save_tasks(self, name):
        with open(f"{name}.txt","a",encoding='utf-8') as file:
            for tasks in self.tasks:
             file.write(tasks.__str__())
        print("Задачи сохранены.")


    def filter_by_status(self,status):
        def search(task):
            if "Выполнен" in task.__str__():
                return True
            return False

        search_lst = list(filter(search,self.tasks))
        if len(search_lst)==0:
            print(f"Нет задач с статусом")
        for i in search_lst :
            print(i) 


    def search_tasks(self,key):
        def search(task):
            if key in task.__str__():
                return True
            return False

        search_lst = list(filter(search,self.tasks))
        if len(search_lst)==0:
            print(f"Нет задач содержащих ключевое слово '{key}'.")
        for i in search_lst :
            print(i)       
        
todolist = ToDoList()

while True:
        print("Выберите действие:")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Редактировать задачу")
        print("4. Удалить задачу")
        print("5. Сохранить задачи")
        print("6. Показать задачу по статусу")
        print("7. Поиск задач по ключевым словам")
        print("8. Выход")
        

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            deadline = input("Введите дедлайн(дд.мм.гггг): ")
            status=input("Введите статус задачи: ")
            task = Task(title, description, deadline,status)
            todolist.add_task(task)
            print("Задача добавлена.")
        elif choice == "2":
            todolist.view_tasks()
        elif choice == "3":
            todolist.view_tasks()
            index = int(input("Введите номер задачи для редактирования: "))
            title = input("Введите новое название задачи: ")
            description = input("Введите новое описание задачи: ")
            deadline = input("Введите новый дедлайн(дд.мм.гггг): ")
            status = input("Введите новый статус: ")
            todolist.edit_task(index, title, description, deadline)
        elif choice == "4":
            todolist.view_tasks()
            index = int(input("Введите номер задачи для удаления: "))
            todolist.remove_task(index)
        elif choice == "5":
            name = input("Введите имя файла для сохранения задач: ")
            todolist.save_tasks(name)
        elif choice == "6":
            status = input("Введите статус задачи (Выполнен/Не выполнен): ")
            if status in ["Выполнен", "Не выполнен"]:
             todolist.filter_by_status(status)
            else:
                print("Недопустимый статус. Введите 'Выполнен' или 'Не выполнен'.")
        elif choice == "7":
            key= input("Введите ключевое слово для поиска: ")
            todolist.search_tasks(key)
        elif choice == "8":
            print("Спасибо за использование программы. До свидания!")
            break

