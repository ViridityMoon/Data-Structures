"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.

Encapsulation of the ListNode class. Takes in a value, previous
node (full ListNode Object), and a next node (full ListNode Object).
The ListNode will be used to occupy our Doubly Linked Lists down the line.
"""
class ListNode:
    # initialization method
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    # method to insert after on any invoked node: takes in a value
    def insert_after(self, value):
        # capture the full ListNode Object in self.next into:
        # 'current_next'
        current_next = self.next
        # creates a new ListNode(value, prev, next), entering in
        # the specific ListNode that had the method invoked as
        # the prev node, and the one after it prior to it's next
        new_node = ListNode(value, self, self.next)
        # reassigns the self's next to the node we just made
        self.next = new_node
        # if the aforementioned 'self.next' was not pointing to None
        # this would happen if we inserted into the end of the ListNodes
        if current_next:
            # then we want to set the current next to point back to the
            # new node, previously reassigned as self.next
            current_next.prev = self.next
    
    # method to insert before on any invoked node: takes in a value
    def insert_before(self, value):
        # capture the full ListNode Object in self.prev into:
        # 'current_prev'
        current_prev = self.prev
        # creates a new ListNode(value, prev, next), entering in
        # the specific ListNode that had the method invoked as
        # the next node, and the one prev ListNode as it's prev
        new_node = ListNode(value, self.prev, self)
        # reassigns the self's prev to the node we just made
        self.prev = new_node
        # if the aforementioned 'self.prev' was not pointing to None;
        # this would happen if we inserted into the beginning of the ListNodes
        if current_prev:
            # then we want to set the current prev to point forward to the
            # new node, previously reassigned as self.prev
            current_prev.next = self.prev

    # method to delete any invoked node
    def delete(self):
        # if the previous exists (not at the beginning); set it's next to
        # the invoked ListNode's (self) next
        if self.prev:
            self.prev.next = self.next
            # self.prev = None
        # if the next exists (not at the end); set it's prev to the
        # invoked ListNode's (self) prev
        if self.next:
            self.next.prev = self.prev   
            # self.next = None   
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.

The DoublyLinkedList will hold our nodes in order. We will
have the option to add/remove the head, the tail, or any given
value. There will also be functionality to move specific nodes
to the head or tail and get the MaxValue.
"""
class DoublyLinkedList:
    # initialization of a DoublyLinkedList, takes in a node,
    # defaults to None if nothing given
    def __init__(self, node=None):
        # holds the value of the head (full ListNode Object)
        self.head = node
        # holds the value of the tail (full ListNode Object)
        self.tail = node
        # if it has a passed in node, then it's 1, otherwise
        # it must be empty
        self.length = 1 if node is not None else 0

    # getter for length
    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # creates a new ListNode, choosing the default
        new_node = ListNode(value, None, None)
        # when adding to the list, we will increment the
        # length by 1
        self.length += 1

        # if the self's head or tail do not exist (None)
        if not self.head and not self.tail:
            # make the head and tail the new ListNode we made
            self.head = new_node
            self.tail = new_node
        # otherwise
        else:
            # have the new node's next value become the current head
            new_node.next = self.head
            # reassign the current head's previous from None to the
            # new node
            self.head.prev = new_node
            # give the status of head to the new node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # captures the value from the head
        value = self.head.value
        # invokes the ListNode's delete method ln.53
        self.delete(self.head)
        # return the deleted node's value
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # creates a new ListNode, choosing the default
        new_node = ListNode(value, None, None)
        # when adding to the list, we will decrement the
        # length by 1
        self.length += 1

        # if the self's head or tail do not exist (None)
        if not self.tail and not self.head:
            # make the tail and head the new ListNode we made
            self.tail = new_node
            self.head = new_node
        # otherwise
        else:
            # have the new node's prev value become the current tail
            new_node.prev = self.tail
            # reassign the current tails's next from None to the
            # new node
            self.tail.next = new_node
            # give the status of tail to the new node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # captures the value from the tail
        value = self.tail.value
        # invokes the ListNode's delete method ln.53
        self.delete(self.tail)
        # returns the deleted node's value
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # check to see if the given node is the head
        if node is self.head: 
            # if it is do nothing
            return None

        # capture the value of the node
        value = node.value

        # check to see if the given node was the tail
        if node is self.tail:
            # we need to invoke the DoublyLinkedList's 
            # remove_from_tail method ln. 161
            self.remove_from_tail()
        # otherwise
        else:
            # invokes the node's delete method ln.53
            node.delete()
            # since we are deleting we want to decrement the length by 1
            self.length -= 1
        
        # at the end, we'll invoke the DoublyLinkedList's 
        # add_to_head method ln.94; passing in the value
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check to see if the node is the tail
        if node is self.tail:
            # if it is do nothing
            return None

        # capture the value of the node
        value = node.value

        # check to see if the given node was the head
        if node is self.head:
            # invoke the DoublyLinkedList's
            # remove_from_head method ln.121
            self.remove_from_head()
        
        # otherwise
        else:
            # invoke the particular node's delete method ln.53
            node.delete()
            # since we are deleting we want to decrement the length by 1
            self.length -= 1

        # at the end, we'll invoke the DoublyLinkedList's 
        # add_to_tail method ln.134; passing in the value
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if not self.head and not self.tail:
        #     return None

        # since we are deleting we want to decrement the length by 1
        self.length -= 1

        # check to see if the head and tail are the same, implying
        # that the list has one Node (we're deleting one thing)
        if self.head == self.tail:
            # set the head and tail of the DoublyLinkedList to none
            self.head = None
            self.tail = None
        
        # check to see if the node is the head
        # (if it passes, we're attempting to delete the head)
        elif self.head == node:
            # make the next node the new head
            self.head = node.next
            # set the next node's previous node to None, as it
            # will be the new head (heads point back to None)
            node.next.prev = None
            # invoke the particular node's delete method ln.53
            node.delete()

        # check to see if the node is the tail
        # (if it passes, we're attempting to delete the tail)
        elif self.tail == node:
            # make the next node the new tail
            self.tail = node.prev
            # set the next node's next node to None, as it
            # will be the new tail (tails point forward to None)
            node.prev.next = None
            # invoke the particular node's delete method ln.53
            node.delete()

        # otherwise
        else:
            # invoke the particular node's delete method ln.53
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # checking if head exists (if it didn't, the list would be empty)
        if not self.head:
            # If the list is empty there is no max to collect, return None
            return None
        # capture the value of the head into a variable: max_val
        max_val = self.head.value
        # capture the full Node Object into a variable: current_node
        current_node = self.head
        # while current_node is not None (at the end, the last node points to None)
        while current_node:
            # check if the previously made 'max-val' is bigger or smaller than the
            # next node's value
            if current_node.value > max_val:
                # if the check passes, then take that new value, as it's larger and
                # closer to the max
                max_val = current_node.value

            # after finding if the next value is bigger or smaller, move onto the next
            # node to repeat until the end, when current_node.next (at the end of the loop)
            # will point to None, therefore 'while current_node' would no longer be valid
            current_node = current_node.next
        
        # return the true 'max_val'
        return max_val