from node import Node
class LinkedList :
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end="   ")
            temp = temp.next
    
    def print_list_reversly(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data)
            temp = temp.prev

    def size_list(self):
        temp = self.head
        i = 0
        while temp :
            i = i+1
            temp = temp.next
        return i
    
    def add_in_bigining(self,data):
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
                node.next = temp
                node.prev = temp.prev
                temp.prev.next = node
                temp.prev = node
    def delete_first(self):
        self.head = self.head.next
        self.head.prev = None
    
    def delete_last(self):
        if self.size_list() == 1:
            self.delete_first()
        else:
            temp = self.head          
            while temp.next:
                temp = temp.next
            temp.prev.next = None
        
    def delete_by_index(self, pos):
        if(pos == 1):
            self.delete_first()
        else:
            if(pos == self.size_list()):
                self.delete_last()
            else:
                item = self.head
                i = 1
                while i<pos:
                    item = item.next
                    i = i+1
                item.prev.next = item.next
                item.next.prev = item.prev 

    def search_value(self,data):
        item = self.head
        i = 1
        while item:
            if(item.data == data):
                return i
            i = i+1
            item = item.next
        return False
    
    def delete_by_value(self, data):
        help = self.search_value(data)
        if(help != False):
            self.delete_by_index(help)
        else:
            print("item : ",data," not exist")
    
    def reverse_list(self):
        temp1 = self.head
        temp2 = self.head
        while temp1.next:
            temp1 = temp1.next
        for i in range(int(self.size_list()/2)):
            perm = temp1.data 
            temp1.data = temp2.data
            temp2.data = perm
            temp1 = temp1.prev
            temp2 = temp2.next

    def sort_liste(self):
        item = self.head
        while item.next:
            node = item.next
            while node:
                if item.data > node.data:
                    perm = item.data
                    item.data = node.data
                    node.data = perm
                node = node.next
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
            liste.add_at_given_index(data,pos)

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
                liste.delete_by_index(pos)
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
            index = liste.search_value(val)
            if(index!=False):
                print("the ",val," at index : ",index)
            else:
                print("the value: ",val," not found !")

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




    