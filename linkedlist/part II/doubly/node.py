class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def setPrevious(self, previous):
        self.previous = previous