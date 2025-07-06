import os
print(f"Current working directory: {os.getcwd()}")
new_directory_path ="/Users/minakahipandey/PycharmProjects/todo_app/work-file"
todos = []
os.chdir(new_directory_path)
print(f"new working directory:{os.getcwd()}")
while True:
    user_action = input("Type add, show, edit, complete, clear or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter todo: ") + "\n"
            todos.append(todo)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)
                file.close()

        case 'show':
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
                file.close()

            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip()}")

        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ") + "\n"
            todos[number - 1] = new_todo

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Enter the number of the todo to complete: "))
            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            removed = todos.pop(number - 1)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

            print(f"Removed: {removed.strip()}")
        case 'clear':
            with open("todos.txt",'r') as file:
                todos=file.readlines()
                removed=todos.clear()
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
            print("file cleared")


        case 'exit':
            break

        case _:
            print("Invalid command.")




