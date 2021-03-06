Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?
O(1) - push method uses the index to find start of array and add before the prev start of the array.

2. What is the runtime complexity of `push` using a linked list?
O(1) - Add to head just needs a new head node and a pointer pointing it to the prev head.

3. What is the runtime complexity of `pop` using a list?
O(1) - pop method uses the last index of list to add to the end

4. What is the runtime complexity of `pop` using a linked list?
O(1) - you just need to change the prev head to the new head 

5. What is the runtime complexity of `len` using a list?
O(1)- the array doesn't need to be iterated over 

6. What is the runtime complexity of `len` using a linked list?
O(n) - The linked list neads to be interated over

## Queue

1. What is the runtime complexity of `enqueue` using a list?
O(1) - push method uses the index to find start of array and add before the prev start of the array.

2. What is the runtime complexity of `enqueue` using a linked list?
O(1) - you just need to change the prev tail to point to the new tail, new tail point to none

3. What is the runtime complexity of `dequeue` using a list?
O(1) - pop method uses the last index of list to add to the end

4. What is the runtime complexity of `dequeue` using a linked list?
O(1) - you just need to change the prev head to the new head 

5. What is the runtime complexity of `len` using a list?
O(1)- the array needs to be iterated over

6. What is the runtime complexity of `len` using a linked list?
O(n) - The linked list neads to be interated over

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

DLL = O(1)  Array.splice = O(n) because it has to potentially copy over all the elements.

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

4. What is the runtime complexity of `for_each`?
    
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
