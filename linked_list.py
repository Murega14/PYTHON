# demonstrating how to create a linked_list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        """
        inserts a node at the beginning of the list
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head()
            self.head = new_node

    def insert_at_index(self, value, index):
        """
        inserts  a node at a specific position
        """
        new_node = Node(value)
        current_node = self.head
        position = 0

        if position == index:
            self.insert_at_beginning(value)
        else:
            # iterating through the linked list until it reaches the node
            # just before the desired index
            while(current_node != None and position+1 != index):
                position = position+1 #keeps tracks of the current position in the list
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("index is not present")

    def insert_at_end(self, value):
        """
        inserts a node at the end of the list
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def update_node(self, val, index):
        """
        updates a node at a specific position
        """
        current_node = self.head
        position = 0
        
        if position == index:
            current_node.value = val
        else:
            while (current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                current_node.value = val
            else:
                print("index is not present")

    def remove_first_node(self):
        """
        removes the first node from the list
        """
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        """
        removes the last node from the list
        """
        if self.head is None:
            return
        current_node = self.head
        while (current_node.next.next):
            current_node = current_node.next
        current_node.next = None

    def remove_node_at_index(self, index):
        """
        removes a node at a specific position
        """
        if self.head is None:
            return
        current_node = self.head
        position = 0

        if position == index:
            self.remove_first_node()
            return
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node
            else:
                print("index is not present")

    def remove_node(self, value):
        """
        removes a node
        """
        current_node = self.head
        
        if current_node.value == value:
            self.remove_first_node()
            return

        while(current_node != None and current_node.next.value != value):
            current_node = current_node.next
            
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    def linked_list_size(self):
        """
        prints the size of the linked list
        """
        size = 0

        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    def print_linked_list(self):
        current_node = self.head

        while current_node:
            print(current_node.value)
            current_node = current_node.next

ted = LinkedList()
ted.insert_at_beginning(25)
ted.insert_at_end(50)
ted.remove_node(50)
ted.print_linked_list()
