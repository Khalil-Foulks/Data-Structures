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
        if self.head == self.tail:
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
        if not self.head:
            # there is nothing to remove so return None
            return None

        # if 1 node in LinkedList
        if self.head == self.tail:
            # store current head
            current_head = self.head
            # set head and tail to None
            self.head == None
            self.tail == None
            # remove 1 from length
            self.length -= 1
            # return removed head 
            return current_head.value

        # if > 1 node in LinkedList
        else:
            # store current head
            current_head = self.head
            # store the value of current head's pointer to next
            new_head = current_head.next
            # set current head next pointer to None
            current_head.next = None
            # set head to new head
            self.head = new_head
            # change new head prev pointer to None
            new_head.prev = None
            # remove 1 from length
            self.length -= 1
            # return removed head 
            return current_head.value

            
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
        if not self.tail:
            # there is nothing to remove so return None
            return None
        # if 1 node exists in DLL
        if self.head == self.tail
        # if > 1 node exists in DLL
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass