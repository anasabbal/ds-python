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

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

if __name__ == '__main__':
    lst = DoublyLinkedList()
    lst.insertAtBegin(3)
    lst.insertAtBegin(2)
    lst.insertAtBegin(1)
    lst.display()