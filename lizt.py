import list

#Stress Testing Remaining 

def main():
    lst = list.List("To-do List")
    
    lst.add_item("Laundry", 2, True)
    lst.add_item("Dishes", 2, False)
    lst.add_item("Grocery", 1, True)
    lst.add_item("Workout", 0, False)
    lst.show()

    lst.check_item(1)
    lst.show()

    lst.update_item_name(4, "Workout 1")
    lst.update_item_urgency(4, True)
    lst.add_item("Workout 2", 3, False)
    lst.update_item_priority(5, 1)
    lst.update_item_urgency(5, False)
    lst.show()

    lst.check_item(3)
    lst.uncheck_item(1)
    lst.check_item(2)

    lst.remove_item(1)
    lst.remo

    lst.show()


if __name__ == '__main__':
    main()