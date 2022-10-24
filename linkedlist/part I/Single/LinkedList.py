from node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
            item = self.head
            while(item):
                print(item.data , "  ",end= " ")
                item = item.next

    def size_list(self) :
        item = self.head
        i = 0
        while(item) :
            item = item.next
            i = i + 1
        return i

    def add_in_bigining(self, data):
        data = Node(data)
        data.next = self.head
        self.head = data

    def add_at_end(self, data):
        if(self == None):
            self.add_in_bigining(self, data)
        else:
            help = self.head
            data = Node(data)
            while help.next :
                help = help.next
            help.next = data
    def add_at_given_index(self,position,data):
        if(position == self.size_list()+1):
            self.add_at_end(data)
        else:
            if(position == 1):
                self.add_in_bigining(data)
            else:
                help = self.head
                prev = None
                data = Node(data)
                i = 0
                while i < position :
                    prev = help
                    help = help.next
                    i = i + 1
                prev.next = data
                data.next = help
        

    

liste = LinkedList() 
liste.head = Node(1)
# print(liste.size_list())
liste.add_in_bigining(3)
liste.add_in_bigining(7)
# liste.printList()
liste.add_at_end(6)
liste.add_at_given_index(3,5)
liste.print_list()


