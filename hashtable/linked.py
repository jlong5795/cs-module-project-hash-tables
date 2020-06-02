# notes from lecture 6/2/2020

class Node:
   def __init__(self, value) :
       self.value = value
       self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self,node):
        node.next = self.head
        self.head = node

    def find(self, value):
        current = self.head
        # look until the end
        while current is not None:
            # is the current value the one we want? If yes, return the current node
            if current.value == value:
                return current
            current = current.next
        
        return None

    def delete(self, value):
        current = self.head

        # special case of deleting the head of the list
        if current.value == value:
            self.head = self.head.next
            return current
        
        # general case
        previous = current
        current = current.next

        while current is not None:
            if current.value == value:
                previous.next = current.next # cuts old node out of sll
                return current
            else:
                previous = previous.next
                current = current.next

        return None



if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_at_head(Node(11))