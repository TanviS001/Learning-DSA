class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        
class Stack:
    def __init__(self, value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
        
    def print_stack(self):
        temp=self.top
        while temp:
            print(temp.value)
            temp=temp.next
    
    def push(self, value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        self.height+=1
    
    def pop(self):
        pre=self.top
        self.top=pre.next
        pre.next=None
        self.height-=1
        
my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)
print(my_stack.print_stack())
