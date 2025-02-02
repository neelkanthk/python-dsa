class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.item = data
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        self.start = None
    
    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.start
        new_node.prev = self.start
        self.start = new_node
        return new_node
    
    def insert_at_last(self, data):
        new_node = Node(data)
        if not self.is_empty():
            cursor = self.start
            while cursor is not None:
                if cursor.next is None:
                    new_node.prev = cursor
                    new_node.next = None
                    cursor.next = new_node
                    break
                cursor = cursor.next

    def print(self):
        if self.start is None:
            pass
        else:
            cursor = self.start
            while cursor is not None:
                print(cursor.item, end=' ')
                cursor = cursor.next

mylist = DLL()
mylist.insert_at_start(1)
mylist.insert_at_start(2)
mylist.insert_at_start(3)

mylist.print()

mylist.insert_at_last(4)
mylist.insert_at_last(5)
mylist.print()