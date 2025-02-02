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
    
    def print(self):
        if self.start is None:
            return
        else:
            cursor = self.start
            while cursor is not None:
                print(cursor.item, end=' ')
                cursor = cursor.next
            return

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

    def insert_after(self, data, item):
        new_node = Node(data)
        if self.start is None:
            new_node.prev = self.start
            new_node.next = None
            self.start = new_node
        else:
            cursor = self.start
            while cursor is not None:
                if cursor.item == item:
                    new_node.prev = cursor
                    new_node.next = cursor.next
                    cursor.next = new_node
                    cursor.next.prev = new_node
                    break
                cursor = cursor.next
    
    def delete_first(self):
        if self.start is None:
            return
        else:
            delete_node = self.start
            self.start = delete_node.next
            delete_node.next.prev = self.start
            return delete_node
        
    def delete_last(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
            return
        else:
            cursor = self.start
            while cursor.next.next is not None:  # Stop at second-last node
                cursor = cursor.next
            cursor.next = None
            return
            

mylist = DLL()
mylist.insert_at_start(1)
mylist.insert_at_start(2)
mylist.insert_at_start(3)

#mylist.print()

mylist.insert_at_last(4)
mylist.insert_at_last(5)
#mylist.print()

mylist.insert_after(0, 1)
mylist.delete_first()
print("\n")
mylist.print()
print("\n")