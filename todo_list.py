print("This Is Your (** TO DO LIst **) Try To complete it on Time . Have A Good day ..\n")



tasks = []

while True :
    print("Choise 1 --> Add Tasks ")
    print("Choice 2 --> Check Tasks ")
    print("Choice 3 --> Delete Tasks")
    print("Choice 4 --> Exit")

    choice = input("Choose Your Choice (1-4):")

    if choice == "1":
        task = input("Enter Your Tasks:")
        tasks.append(task)
        print("Your Task is added Succesfully.")

    if choice == "2":
        if not tasks:
            print("No Tasks Available ")

    else:
        print("\nYour Tasks Are:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}") 

    if choice == "3":
        if not tasks:
            print("No tasks Availbale to Delete\n")

        else:
            task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Removed task: {removed} ❌")
        else:
            print("Invalid task number.")
    
    
            if choice == "4":
                print("Exiting To-Do List. Goodbye 👋")
                

            else:
                print("Invalid choice! Try again.")












