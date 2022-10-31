from node import *


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def create_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
    
    def insert_at_first(self, data):
        current = self.head
        node = self.create_node(data)


