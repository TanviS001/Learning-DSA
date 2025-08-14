class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        
class Queue:
    def __init__(self, value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
        
    def print_queue(self):
        temp=self.first
        while temp:
            print(temp.value)
            temp=temp.next
        
    def enqueue(self, value):
        new_node=Node(value)
        self.last.next=new_node
        self.last=new_node
        self.length+=1
    
    def dequeue(self):
        if self.length==0:
            return None
          
        temp=self.first
        self.first=temp.next
        temp.next=None
        self.length-=1
        
        if self.length==0:
            self.last=None
            
        return temp

    ###############################

my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)
# (0) Items - Returns None
print(my_queue.dequeue())


"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""
