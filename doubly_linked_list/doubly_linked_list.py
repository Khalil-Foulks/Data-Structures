"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # if head doesn't exist
        if not self.head:
            # use value to create new head node
            new_head = ListNode(value)
            # new head's prev and next == None (done by default in ListNode)
            # set head and tail to new node
            self.head = new_head
            self.tail = new_head
            # add 1 to length
            self.length += 1
        
        # if any node in LinkedList
        else:
            # store old head
            old_head = self.head        
            # use value to create new head node 
                # new head prev == None
                # new head next == old head
            new_head = ListNode(value,None,old_head)
            # old head prev == new head
            old_head.prev = new_head
            # old head next == None (done by default in ListNode)
            # set head to new node
            self.head = new_head
            # add 1 to length
            self.length += 1

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """  
    def remove_from_head(self):
        # if head doesn't exist
        if self.head is None:
            return None
        # if 1 node in LinkedList
        if self.head.next is None:
            head_val = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return head_val
        # if > 1 node in LinkedList
        else:
            # store current head value
            head_val = self.head.value
            # set head to old head's pointer to next node
            self.head = self.head.next
            # remove 1 from length
            self.length -= 1
            # return removed head
            return head_val    

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # if tail doesn't exist
        if not self.tail:
            # use value to create new head node
            new_tail = ListNode(value)
            # new head's prev and next == None (done by default in ListNode)
            # set head and tail to new node
            self.head = new_tail
            self.tail = new_tail
            # add 1 to length
            self.length += 1
        # if any node exists in DLL
        else:
            # store old tail
            old_tail = self.tail        
            # use value to create new head node 
                # new head prev == None
                # new head next == old head
            new_tail = ListNode(value,old_tail,None)
            # old tail next == new tail
            old_tail.next = new_tail
            # old tail prev doesn't change
            # set tail to new node
            self.tail = new_tail
            # add 1 to length
            self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if tail doesn't exist
        if self.tail is None:
            # there is nothing to remove so return None
            return None
        # if 1 node exists in DLL
        if self.tail.prev is None:
            # store current tail value
            tail_val = self.tail.value
            # set head and tail to None
            self.head = None
            self.tail = None
            # remove 1 from length
            self.length = 0
            # return removed tail 
            return tail_val
        # if > 1 node exists in DLL
        else:
            # store current tail value
            tail_val = self.tail.value
            # set tail to old tail's prev
            self.tail = self.tail.prev
            # remove 1 from length
            self.length -= 1
            # return removed old tail value
            return tail_val
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if DLL length is 0 it's already at front return None
        if self.length == 0:
            return
        # if node is the head it's already at front return None
        if node is self.head:
            return
        # if > 1 node in DLL
        # store old value
        old_head_val = node.value
        # removes node from DLL
        self.delete(node)
        # adds to head of DLL
        self.add_to_head(old_head_val)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # if DLL length is 0 it's already at end return None
        if self.length == 0:
            return
        # if node is the tail it's already at end return None
        if node is self.tail:
            return
        # if > 1 node in DLL
        # store old value
        old_value = node.value
        # removes node from DLL
        self.delete(node)
        # adds to head of DLL
        self.add_to_tail(old_value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Check for no items in list
        if self.head is None:
            print("Empty list")
            return None
        # Check if list has only 1 node
        if self.length == 1:
            # if node is not the head
            if self.head != node:
                print("Only one element, but it's not inputed node")
                return None
            # if node is the head, remove the node, head/tail are none list is empty
            else:
                print("Node removed")
                self.head = None
                self.tail = None
                self.length -= 1
                return node
        # If head matches node remove from head
        elif self.head == node and self.tail != node:
            print("removing the head")
            self.remove_from_head()
            return self.head.value
        # If tail matches node remove from tail
        elif self.tail == node and self.head != node:
            print("removing tail")
            self.remove_from_tail()
            return self.tail.value
        # If more then one element in list, and node != to head or tail the node is somewhere in the middle
        else:
            print("somewhere in the middle")
            # store node's prev
            prev_node = node.prev
            # prev node's next becomes node's next
            prev_node.next = node.next
            # store next node
            next_node = node.next
            # next node prev becomes node's prev
            next_node.prev = prev_node
            # decrement by 1
            self.length -= 1
            # node's prev and next no longer point to anything
            node.prev = None
            node.next = None
            # return deleted node
            return node            

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # check if head exist, 
        if not self.head:
        # if it doesn't list is empty return none
            return None
        # store current head's value as the max value for 1st go
        max_value = self.head.value
        # store current head as current node for 1st go
        current_node = self.head
        # while loop runs until 
        while current_node:
            # if current node is higher than the max, it becomes the new max
            if current_node.value > max_value:
                max_value = current_node.value
            # if not move to current_node's next and that become the new current node
            else:
                current_node = current_node.next
        return max_value