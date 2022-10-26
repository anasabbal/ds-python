class Node:
    
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, node):
        self.next = node

    def getNextNode(self):
        return self.next