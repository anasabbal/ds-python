from node import *


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def createNode(self, data):
        new_node = Node(data)
        return new_node

    def insertAtBegin(self, data):
        if self.head is None:
            new_node = self.createNode(data)
            self.head = new_node
            return new_node
        
        new_node = self.createNode(data)
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node

        return new_node

    def insertAtEnd(self, data):
        if self.head is None:
            new_node = self.createNode(data)
            self.head = new_node
            return new_node
        new_node = self.createNode(data)
        current_node = self.head
        # search last node with next null
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.previous = current_node

        return new_node

    def size(self):
        current = self.head
        sum = 0
        while current:
            sum += 1
            current = current.next
        return sum

    def findLastNode(self):
        if self.head is None:
            return None
        current = self.head
        while current.next != None:
            current = current.next
        return current

    def searchByIndex(self, index):
        if index > self.size() and index == 0:
            print("Index Out of range list")
            return
        if index == self.size():
            return self.findLastNode().data
        if index == 0:
            return self.head.data

        position = 1
        current = self.head
        while position < index:
            current = current.next
            position += 1
        node = current
        return node


    def insertAtPosition(self, index, data):
        if self.head is None:
            new_node = self.createNode(data)
            self.head = new_node
            return new_node

        if index > self.size() and index == 0:
            print("Index Out of range list")
            return
        
        new_node = self.createNode(data)
        current = self.head

        for i in range(index - 2):
            current = self.head.next

        new_node.previous = current 
        new_node.next = current.next 
        current.next = new_node 
        new_node.next.previous = new_node
        
        return new_node

    def removeByIndex(self, index):
        if index > self.size():
            print("Index Out of range list")
            return
        if index == self.size():
            last_node = self.findLastNode()
            last_node = None
            return 
        if index == 0:
            first_node = self.head
            next_node = first_node.next
            first_node = None
            self.head = next_node
            return
        
        current = self.head

        for i in range(index):
            current = current.next
            prev = current.previous
            nex = current.next

            if(i == index):
                nex.previous = prev
                prev.next = nex
                current = None
                return
    
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='')
            temp = temp.next
        print()

if __name__ == '__main__':
    lst = DoublyLinkedList()
    # add
    lst.insertAtBegin(3)
    lst.insertAtBegin(2)
    lst.insertAtBegin(1)
    lst.insertAtPosition(2, 8)
    # size
    
    # display
    lst.display()
    # find last node
    print(lst.findLastNode().data, end='\n')

    print(lst.searchByIndex(2).data, end='\n')

    lst.removeByIndex(2)
    

    print(lst.size(), end='\n')

    lst.display()

