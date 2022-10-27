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
        self.head = help.head

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
        if(self.head == None):
            self.add_in_bigining(data)
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
    def delete_by_position(self, pos):

        if pos == 1:
            self.delete_first()
        else:
            if pos == self.size_list():
                self.delete_last()
            else:
                help = self.head
                prev = None
                i = 1
                while i < pos :
                    prev = help
                    help = help.next
                    i = i + 1
                prev.next = help.next

    def search_by_value(self,value):
        head = self.head
        i = 1
        while(head):
            if(head.data == value):
                return i
            head = head.next
            i = i + 1
        return False

    def delete_by_value(self,value):
        help = self.search_by_value(value)
        if help != False :
            self.delete_by_position(help)

    def sort_liste(self):
        item = self.head
        while item.next :
            help = item.next
            while help:
                if(item.data > help.data):
                    perm = item.data
                    item.data = help.data
                    help.data = perm
                help = help.next
            item = item.next


       

    def get_the_minimum(self):
        item = self.head
        min = item.data
        while item.next :
            if min > item.next.data :
                min = item.next.data 
            item = item.next
        return min

    def get_the_maximun(self):
        item = self.head
        max = item.data
        while item.next :
            if max < item.next.data :
                max = item.next.data      
            item = item.next
        return max
    
    def delete_duplicated_item(self):
        self.sort_liste()
        item = self.head
        while item.next:
            if(item.data == item.next.data):
                self.delete_by_value(item.data)
            item = item.next
        


ask = True
liste = LinkedList() 
while ask :
    print("\t\t\t Linked List implementation ")
    print("\t\t\t Size list : ",liste.size_list()," items")
    print("\n\n\t\t 1/ Read liste           \t\t 2/ Read liste reversly")
    print("\t\t 3/ Insert in beginig        \t\t 4/ Insert at given position")
    print("\t\t 5/ Insert at the end        \t\t 6/ Delete the first")
    print("\t\t 7/ Delete by key            \t\t 8/ Delete the last")
    print("\t\t 9/ Delete by value          \t\t 10/ Reverse List ")
    print("\t\t 11/ Sort List               \t\t 12/ Search by value")
    print("\t\t 13/ Delete duplicated items \t\t 14/ The minimun ")
    print("\t\t 15/ The maximun ")
   
    choise = int(input("Enter your choise : "))
    if choise == 1 :
        liste.print_list()
    if choise == 2 :
         liste.print_list_reversly()
    if choise == 3 : 
            data = int(input("Enter value : "))
            liste.add_in_bigining(data)  
   
    if choise == 4 :
            data = int(input("Enter data    : "))
            pos = int(input("Enter position : "))
            liste.add_at_given_index(pos,data)

    if choise == 5 :
            data = int(input("Enter data : "))
            liste.add_at_end(data)

    if choise == 6 :
        if(liste.head != None) :
            liste.delete_first()

    if choise == 7 : 
        if liste.head != None :
            pos = int(input("Enter position : ")) 
            if( pos <= liste.size_list() and pos > 0) : 
                liste.delete_by_position(pos)
        else :
            print("liste empty !!")
        

    if choise == 8 :
        if(liste.head != None) :
            liste.delete_last()
    if choise == 9 :
        if(liste.head != None) :
            val = int(input("Enter data    : "))
            liste.delete_by_value(val)
   
    if choise == 10 :
        if(liste.head != None) :
            liste.reverse_list()

    if choise == 11 :
        if(liste.head != None and liste.size_list() > 1):
            liste.sort_liste()


    if choise == 12 :
        if(liste.head != None) :
            val = int(input("Enter data    : "))
            index = liste.search_by_value(val)
            if(index!=False):
                print("the ",val," at index : ",index)
            else:
                print("the value not found !")

    if choise == 13 :
        if(liste.head != None and liste.size_list() > 1) :
            liste.delete_duplicated_item()
        
    if choise == 14 :
        if(liste.head != None) :
            print("the minimun is : ",liste.get_the_minimum())
        
    if choise == 15 :
        if(liste.head != None) :
            print("the maximun is : ",liste.get_the_maximun())
            
         
    print("\n")
    x = input("Return to the menu principal [y/n] : ")
    if(x != 'y' and x != 'Y'):
        ask = False



