from node import *

class Linkedlist:

    def __init__(self):
        self.head = None

    # add node at beginig linked list
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node

    # add node at ending linked list
    def insert_at_end(self, data):
        start = self.head
        new_node = Node(data)

        while start.getNextNode():
            start = start.getNextNode()

        start.setNext(new_node)

    # remove node from linked list
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

    # get node from linked list by index
    def get_item_from_index(self, index):
        start = self.head
        position = int(index)
        pos = 1
        while pos != position:
            start = start.getNextNode()
            pos += 1
        data = start.getData()
        return data
    
    # clean linked list
    def clear_linked_list(self):
        self.head = None
        return True
    
    # Display Linked list
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

    # find min value in node 
    def find_min_value_from_linked_list(self):
        start = self.head
        min = start.getData()

        while start:
            if min > start.getData():
                min = start.getData()
            start = start.getNextNode()
        return min
    
    # find max value in node 
    def find_max_value_from_linked_list(self):
        start = self.head
        max = start.getData()

        while start:
            if max < start.getData():
                max = start.getData()
            start = start.getNextNode()
        return max

    # search node in linked list by data
    def search(self, data):
        start = self.head
        index = 1
        while start:
            if start.getData() == data:
                return index
            index += 1
            start = start.getNextNode()
        return index

    # build List of python from linked list
    def toList(self):
        start = self.head
        nodeList = []
        while start:
            item = start.getData()
            nodeList.append(item)
            start = start.getNextNode()
        return nodeList

    # sort linked list
    # def sort


    # return size linked list
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
list_arr.insert_at_begin(1)
list_arr.insert_at_begin(4)
list_arr.insert_at_begin(7)


list_arr.display()
print("index by search : ")
print(list_arr.search(1))
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

# print data by index
print(list_arr.get_item_from_index(3))
print(list_arr.get_item_from_index(2))