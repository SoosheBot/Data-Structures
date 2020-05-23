"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
​
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
​
    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
​
    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
​
my_node = ListNode(12)
my_node.insert_after(25)
my_node.insert_after(100)
my_node.next.insert_after(99)
​
def iterate_list(node):
    while node is not None:
        print(node.value)
        node = node.next
​
# iterate_list(my_node)
# my_node = ListNode(12)
# ||
# my_node.next = ListNode(100)
# ||
# ListNode(99)
# ||
# ListNode(25)
​
# not so efficient: finding a value
​
# efficient: removing/adding from beginning and end
​
# delete
# update
​
"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
​
    def __len__(self):
        return self.length
​
    def find_middle(self):
        middle = self.head
        end = self.head
​
        while end.next != None and end.next.next != None:
            end = end.next.next
            middle = middle.next
​
        return middle
        
    # head should now be tail
    # tail should now be head
    # no recursion, no other data structures
    def reverse_list(self):
        pass
​
    def iterate_nodes(self):
        total = 0
        node = self.head
        while node is not None:
            total += 1
            node = node.next
​
        return total
​
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # wrap the given value in a ListNode
        new_node = ListNode(value, None, None)
        self.length += 1
        # handle if list has a head
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # handle if list has no head
        else:
            self.head = new_node
            self.tail = new_node
​
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
​
        return value
​
​
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
​
        # there is a tail
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        # there is no tail
        else:
            self.head = new_node
​
        self.tail = new_node
​
​
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
​
        # self.delete(self.tail)
        # if 0 nodes
        if not self.tail:
            return
​
        # if head and tail are the same (1 node)
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        # if more than 1 node
        else:
            self.tail = self.tail.prev
            self.tail.next = None
​
        self.length -= 1
​
        return value
​
​
    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)
​
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
​
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
​
​
    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
​
        # if list is empty
        if not self.head:
            print("you got nothing on me!")
            return
​
        self.length -= 1
​
        # if list has just one item
        if self.head == self.tail:
            self.head = None
            self.tail = None
​
        # we have at least two nodes, and the node we want to delete is the head
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        
        # we have at least two nodes, and the node we want to delete is the tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
​
        else:
            node.delete()
​
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # walk through the entire list
        # keep track of the biggest value we've found
​
        highest_value = self.head.value
        current_node = self.head
​
        while current_node is not None:
            if current_node.value > highest_value:
                highest_value = current_node.value
​
            current_node = current_node.next
​
        return highest_value
​
​
# dll = DoublyLinkedList()
# dll.add_to_tail(1)
# dll.add_to_tail(2)
# dll.add_to_tail(3)
# dll.add_to_tail(4)
# dll.add_to_tail(5)
​
# middle = dll.find_middle()
# print(middle.value)


---------

# file I/O - for another day
​
# add to the back of a text buffer
# add to the front of a text buffer
# delete from the back of a text buffer
# delete from the front of a text buffer
​
# join text buffers together
​
# add to the middle
​
# array vs DLL
# array: add to back. O(1)
# array: add to front: O(n)
# array: delete from back: O(1)
# array: delete from front: O(n)
# array: join text buffers together: O(n)
​
# DLL: add to back: O(1)
# DLL: add to front: O(1)
# DLL: delete from front: O(1)
# DLL: delete from front: O(1)
# DLL: join text buffers together: O(1)
​
# __str__, to print out what's inside
# array, O(n)
# DLL, O(n)
​
import sys
​
sys.path.append('./doubly_linked_list')
​
from doubly_linked_list import DoublyLinkedList
​
class TextBuffer:
    def __init__(self):
        self.storage = DoublyLinkedList()
​
    def __str__(self):
        string_to_return = ""
​
        node = self.storage.head
        while node is not None:
            string_to_return += node.value
            node = node.next
​
        return string_to_return
​
    def join(self, other_buffer):
        # link tail of this buffer to the head of the other_buffer
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
​
        # point our tail to the new tail
        self.storage.tail = other_buffer.storage.tail
​
​
    def append(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_tail(char)
​
    def prepend(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_head(char)
​
    def delete_from_front(self, number_of_chars_to_remove):
        for _ in range(number_of_chars_to_remove):
            self.storage.remove_from_head()
​
    def delete_from_back(self, number_of_chars_to_remove):
        for _ in range(number_of_chars_to_remove):
            self.storage.remove_from_tail()
​
    def find_text(self, text_to_find):
        pass
​
text = TextBuffer()
text.append('hello')
​
other_buffer = TextBuffer()
other_buffer.append(' how are you')
​
text.join(other_buffer)
​
print(text)