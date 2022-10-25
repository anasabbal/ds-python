from ast import Delete
from node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
            item = self.head
            while(item):
                print(item.data , "  ",end= " ")
                item = item.next
    def print_list_reversly(self):
            item = self.head
            help = LinkedList()
            while(item) :
                help.add_in_bigining(item.data)
                item = item.next
            help.print_list()

    def reverse_list(self):
        item = self.head
        help = LinkedList()
        while(item) :
            help.add_in_bigining(item.data)
            item = item.next
        self.head = help

    def size_list(self) :
        item = self.head
        i = 0
        while(item) :
            item = item.next
            i = i+1
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
        if(position == self.size_list()):
            self.add_at_end(data)
        else:
            if(position == 1):
                self.add_in_bigining(data)
            else:
                help = self.head
                prev = None
                data = Node(data)
                i = 1
                while i < position :
                    prev = help
                    help = help.next
                    i = i + 1
                prev.next = data
                data.next = help
    def delete_first(self):
        self.head = self.head.next

    def delete_last(self):
        item = self.head
        for i in range(self.size_list()-2):
            item = item.next
        item.next = None
        # using while
        # while  item.next.next :
        #     item = item.next
        # item.next = None
    
ask = True
liste = LinkedList() 
while True :
    print("\t\t\t Linked List implementation ")
    print("\t\t\t Size list : ",liste.size_list()," items")
    print("\n\n\t\t 1/ Read liste     \t\t 2/ Read liste reversly")
    print("\t\t 3/ Insert in beginig  \t\t 4/ Insert at given position")
    print("\t\t 5/ Insert at the end  \t\t 6/ Delete the first")
    print("\t\t 7/ Delete by position \t\t 8/ Delete the last")
    print("\t\t 9/Delete by key       \t\t 10/ Reverse List \n\t\t 11/ Sort List")
   
    choise = int(input("Enter your choise : "))
    if choise == 1 :
        liste.print_list()
    if choise == 2 :
         liste.print_list_reversly()
    if choise == 3 : 
            data = int(input("Enter value : "))
            liste.add_in_bigining(data)  
    if choise == 5 :
            data = int(input("Enter data : "))
            liste.add_at_end(data)
    if choise == 4 :
            data = int(input("Enter data    : "))
            pos = int(input("Enter position : "))
            liste.add_at_given_index(pos,data)
    if choise == 6 :
        if(liste.head != None) :
            liste.delete_first()

    if choise == 7 :
         if(liste.head != None) :
            pos = int(input("Enter position : "))
            liste.delete_last()

    if choise == 8 :
        if(liste.head != None) :
            liste.delete_last()

            
    print("\n")
    x = input("Return to the menu principal [y/n] : ")
    if(x != 'y' and x != 'Y'):
        ask = False



