class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
  
# enqueue at the back
# dequeue at the front

class Queue:
    def __init__(self, value):
        new_node=Node(value)
        self.front=new_node
        self.back=new_node
        self.length=1
        
    def print_queue(self):
        temp=self.front
        while temp:
            print(temp.value)
            temp=temp.next
        
    def enqueue(self, value):
        new_node=Node(value)
        self.back.next=new_node
        self.back=new_node
        self.length+=1
    
    def dequeue(self):
        if self.length==0:
            return None
        temp=self.front
        self.front=temp.next
        temp.next=None
        self.length-=1
        return temp
        
        
        
my_queue = Queue(4)

print('front:', my_queue.front.value)
print('back:', my_queue.back.value)
print('Height:', my_queue.length)

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print(my_queue.print_queue())

my_queue.dequeue()

print(my_queue.print_queue())
