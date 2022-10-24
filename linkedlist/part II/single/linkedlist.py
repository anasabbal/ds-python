from node import *

class Linkedlist:

    def __init__(self):
        self.head = None


    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node

    def insert_at_end(self, data):
        start = self.head
        new_node = Node(data)

        while start.getNextNode():
            start = start.getNextNode()

        start.setNext(new_node)

    def remove(self, item):
        start = self.head
        previous = None
        get = False

        # search
        while not get:
            if start.getData() == item:
                get = True
            else:
                previous = start
                start = start.getNextNode()

        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setNext(start.getNextNode())
        return get

        
    def clear_linked_list(self):
        self.head = None
        return True
    
    def display(self):
        start = self.head
        if start is None:
            print("Empty Linked list")
            return False

        while start:
            print(str(start.data), end=" ")
            start = start.next
            if start:
                print("-->", end=" ")
        print()
    
    def size(self):
        start = self.head
        size = 0

        while start:
            size += 1
            start = start.getNextNode()
        return size

# creating LinkedList
list_arr = Linkedlist()

# adding to start
list_arr.insert_at_begin(5)
list_arr.insert_at_begin(4)
list_arr.insert_at_begin(1)

# add to end
list_arr.insert_at_end(10)

# adding to start
list_arr.insert_at_begin(3)
list_arr.insert_at_begin(2)

# Display Linked list
list_arr.display()
print(list_arr.size())

print(list_arr.remove(5))
list_arr.display()

# Size linkedlist
print(list_arr.size())