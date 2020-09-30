class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node #next node in list

    def get_value(self):
        return self.get_value

    def get_next_node(self):
        return self.get_next_node

    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None #points to first node
        self.tail = None #points to last node
        self.length = 0 #length of array


    def add_to_tail(self, value):
        if not self.tail:
            # create new node
            new_tail = Node(value, None)
            # set head and tail to new node
            self.head = new_tail
            self.tail = new_tail
            # if there is a tail
        else:
            # create new node
            new_tail = Node(value, None)
            # set current tail.next (pointer) to new node
            old_tail = self.tail
            old_tail.next = new_tail
            # set tail to new tail
            self.tail = new_tail
            # new length
            self.length += 1

    def remove_head(self):
        # if no element in  list (empty list)
        if not self.head:
            return None
        elif  self.head == self.tail:
            # set head to current_head
            current_head = self.head
            # set head and tail to None, basically deleting 
            self.head = None
            self.tail = None
            # remove the 1 item from length
            self.length -= 1
            # return the new array value
            return current_head.value
        else:
            #set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            # return current_head.value
            self.length -= 1
            return current_head.value


    def remove_tail(self):
        # if no values in tail
        if self.tail is None:
            return None
        else:
            ret_value = self.tail.get_value
            # 1 element
            if self.tail is self.head:
                # set values to None, delete
                self.head = None
                self.tail = None
                # if more than 1 element
            else:
                self.tail = self.tail.get_next_node()
                return ret_value
