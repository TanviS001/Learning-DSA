def partition_list(self, x):
        less_head=Node(0)
        more_head=Node(0)
        
        less=less_head
        more=more_head
        
        current=self.head
        while current:
            next_node=current.next
            current.next=None
            current.prev=None
            
            if current.value<x:
                less.next=current
                current.prev=less
                less=current
            else:
                more.next=current
                current.prev=more
                more=current
                
            current=next_node
        
        if less_head.next:
            less.next=more_head.next
            if more_head.next:
                more_head.next.prev=less
            new_head=less_head.next
            new_head.prev=None
        else:
            new_head=more_head.next
            if new_head:
                new_head.prev=None
            
        return new_head


