todo_list = []
def show_list():
    for i in range(len(todo_list)):
        print(i+1, end=". ")
        print(todo_list[i])

def enlist(item):
    todo_list.append(item)
    show_list()
def done(queue_number):
    todo_list[queue_number-1] += "FINISHED"
    show_list()
def remove(queue_number):
    todo_list.pop(queue_number-1)
    show_list()
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

def funcshun():
    print("Your TODO List")
    print("type 'exit' at any moment to quit the program")
    print("if you want to restart where you left, call funcshun()")

    while True:
        print()
        print("enlist item -- enlist(item)")
        print("check item -- done(queue_number)")
        print("remove item -- remove(queue_number)")
        print("move item up/down on the list -- move(queue_number, target_queue_number)")

        d = input()
        if d.lower() == "exit":
            file = open("TodoList.csv", 'w')
            for i in todo_list:
                file.write(i+"\n")
            file.close()
            print("TODO List exported. ")
            print("Thank You. GoodBye.")
            break
        else:
            eval(d)

funcshun()

