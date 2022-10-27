from node import Node
class LinkedList :
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end="   ")
            temp = temp.next

    def size_list(self):
        temp = self.head
        i = 0
        while temp :
            i = i+1
            temp = temp.next
        return i
    
    def add_in_biginin(self,data):
        node = Node(data)
        node.next = self.head
        node.prev = None
        if(self.head != None):
            self.head.prev = node
        
        self.head = node
    def add_at_end(self, data):
        temp = self.head
        if(temp == None):
            self.add_in_biginin(data)
        else:
            node = Node(data)
            node.next = None
            while temp.next:
                temp = temp.next
            temp.next = node
            node.prev = temp
    def add_at_given_index(self, data, pos):
        if pos == 1:
            self.add_in_biginin(data)
        else :
            if pos == self.size_list()+1:
                self.add_at_end(data)
            else:
                i = 1
                temp = self.head
                node = Node(data)
                while i<pos:
                    temp = temp.next
                    i = i+1
                node.prev = temp.prev
                node.next = temp
                temp.prev.next = node
    
    
                
                
                


liste = LinkedList()
liste.add_in_biginin(1)
liste.add_at_end(3)
liste.add_at_given_index(2, 2)
liste.print_list()


    