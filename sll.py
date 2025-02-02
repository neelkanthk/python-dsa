class Iterator:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            data = self.current.item
            self.current = self.current.next
            return data

class Node:
    def __init__(self, data = None, next = None):
        self.item = data
        self.next = next

class SLL:
    def __init__(self):
        self.start = None

    def __iter__(self):
        return Iterator(self.start)

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            new_node.next = self.start
            self.start = new_node
        return new_node
    
    def insert_at_last(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            cursor = self.start
            while cursor is not None:
                if cursor.next is None:
                    cursor.next = new_node
                    break
                cursor = cursor.next

    def print_list(self):
        cursor = self.start
        while cursor is not None:
            print(cursor.item, end=' ')
            cursor = cursor.next
        print('\n')

    def insert_after(self, data, after):
        new_node = Node(data)
        if self.start is None:
            pass
        else:
            cursor = self.start
            while cursor is not None:
                if cursor.item == after:
                    new_node.next = cursor.next
                    cursor.next = new_node
                    break
                cursor = cursor.next

    def search(self, data):
        if self.start is None:
            pass
        else:
            cursor = self.start
            while cursor is not None:
                if cursor.item == data:
                    return True
                cursor = cursor.next
            return False
        
    def delete_first(self):
        if self.start is None:
            pass
        else:
            first_node = self.start
            self.start = first_node.next

    def delete_last(self):
        if self.start is None:
            pass
        else:
            cursor = self.start
            while cursor.next is not None:
                if cursor.next.next is None:
                    cursor.next = None
                    break
                cursor = cursor.next

    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            cursor = self.start
            while cursor.next is not None:
                if cursor.next.item == data:
                    cursor.next = cursor.next.next
                    break
                cursor = cursor.next




mylist = SLL()

mylist.insert_at_start(1)
mylist.insert_at_start(2)
mylist.insert_at_start(3)
mylist.insert_at_last(5)
mylist.insert_at_last(6)
mylist.insert_after(4, 1)
for item in mylist:
    print(item)
print('\n')
mylist.delete_first()
for item in mylist:
    print(item)
print('\n')
mylist.delete_last()
for item in mylist:
    print(item)
print('\n')
mylist.delete_item(5)
for item in mylist:
    print(item)
print('\n')
print(mylist.search(0))
print(mylist.search(2))