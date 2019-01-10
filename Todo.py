todo_list = []

def show_list():
    if bool(todo_list):
        print("==========TODO LIST==========")
        for i in range(len(todo_list)):
            print(i+1, end=". ")
            print(todo_list[i])
    print("==========TODO LIST==========")

def welcome_note():
    print("Your TODO List")
    print("type 'exit' at any moment to quit the program")
    print("if you want to restart where you left, call todo()")

def instructions():
    print()
    print("enlist item -- enlist(item)")
    print("check item -- done(queue_number)")
    print("remove item -- remove(queue_number)")
    print("move item up/down on the list -- move(queue_number, target_queue_number)")
    print()

def enlist(item):
    if item != "":
        todo_list.append(item)

def done(queue_number):
    finished_tag = "\t \t [x]"
    if finished_tag not in todo_list[queue_number-1]:
        todo_list[queue_number-1] +=  finished_tag
    else:
        print("\nTask already Complete. \n")

def remove(queue_number):
    if 0 < queue_number < len(todo_list):
        todo_list.pop(queue_number-1)
    else:
        if queue_number < 0:
            print("\nInvalid queue number\n")
        else:
            print("The list doesn't have that many items.")

def move(queue_number, list_number):
    if list_number > queue_number:
        item = todo_list.pop(queue_number-1)
        if list_number >= len(todo_list):
            todo_list.append(item)
        else:
            todo_list.insert(list_number-1, item)
        show_list()
    elif list_number == queue_number:
        show_list()
    else:
        item = todo_list.pop(queue_number-1)
        todo_list.insert(list_number-1, item)
        show_list()

def restore(file_name="TodoList.csv"):
    listed = open(file_name)
    for i in listed:
        if i.strip() != '':
            todo_list.append(i.strip())
    listed.close()

    print("All your old items have been added")

def todo():

    adding_tasks = True 

    welcome_note()
    restore()

    while adding_tasks:
        instructions()

        show_list()
        
        task = input()

        if "exit" in task:
            if bool(todo_list):
                listed = open("TodoList.csv", 'w')            
                for i in todo_list:
                    listed.write(i+"\n")
                    listed.close()
                print("TODO List exported. \nThank You. GoodBye.")
                adding_tasks = False
        else:
            eval(task.strip())

todo()
input("Exit now...")
