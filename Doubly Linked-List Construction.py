Doubly Linked-List Construction-

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_left_to_right(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def print_right_to_left(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev


if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))

    curr = DoublyLinkedList()

    for value in values:
        curr.insert(value)

    curr.print_left_to_right()
    print()
    curr.print_right_to_left()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
Delete a node at specific position in Doubly-linked list-

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

    def delete_at_position(self, position):
        if position < 1:
            print("Invalid position")
            return
        elif position == 1:
            if self.head:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            else:
                print("List is empty")
            return

        current = self.head
        count = 1
        while current and count != position:
            current = current.next
            count += 1

        if not current:
            print("Position out of range")
            return

        if current == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

n = int(input())
elements = list(map(int,input().split()))

position = int(input())


cur = DoublyLinkedList()
for element in elements:
    cur.add_to_tail(element)


cur.print_forward()
cur.print_backward()
cur.delete_at_position(position)

cur.print_forward()
cur.print_backward()
print()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Insert at tail in Doubly-linked list-

class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

  def print_forward(self):
    current = self.head
    while current:
      print(current.data, end=" ")
      current = current.next
    print()

  def print_backward(self):
    current = self.tail
    while current:
      print(current.data, end=" ")
      current = current.prev
    print()

n = int(input())
elements = list(map(int, input().split()))
new_number = int(input())


curr = DoublyLinkedList()
for element in elements:
    curr.add_to_tail(element)



curr.print_forward()
curr.print_backward()

curr.add_to_tail(new_number)

curr.print_forward()
curr.print_backward()
print()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Delete tail node in Doubly-linked list-

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

    def delete_last_node(self):
        if not self.tail:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

n = int(input())
elements = list(map(int, input().split()))

curr = DoublyLinkedList()
for element in elements:
    curr.add_to_tail(element)

curr.print_forward()
curr.print_backward()

curr.delete_last_node()

curr.print_forward()
curr.print_backward()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Delete head node in Doubly-linked list-

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node

    def delete_first(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()


n = int(input())
elements = list(map(int, input().split()))


curr = DoublyLinkedList()
for element in elements:
    curr.insert_end(element)



curr.display_forward()
curr.display_backward()


curr.delete_first()

curr.display_forward()
curr.display_backward()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Insert at head in Doubly-linked list-

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node

    def insertStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def displayForward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def displayBackward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()


n = int(input())
elements = list(map(int, input().split()))
new_element = int(input())

curr = DoublyLinkedList()
for element in elements:
    curr.insertEnd(element)

curr.displayForward()
curr.displayBackward()

curr.insertStart(new_element)
curr.displayForward()
curr.displayBackward()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Insert at specific position in Doubly-linked list-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    
    curr = head 
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    
    tail = head 
    while tail.next != None:
        tail = tail.next 
        curr = tail
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.prev 
    print()
 
def addNodeAtTailOfLinkedList(head, ele):
    newBlock = Node(ele)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock 
    newBlock.prev = tail 
    return head


def insertAtSpecificPosition(head, position,val):
    newBlock = Node(val)
    if head == None:
        return newBlock
 
    index = 1 
    curr = head 
 
    while index != position-1:
        index += 1 
        curr = curr.next 
    nextNode = curr.next 
    newBlock.next = nextNode 
    nextNode.prev = newBlock 
    curr.next = newBlock 
    newBlock.prev = curr 
    return head


n=int(input()) 
l = map(int,input().split())
pos,val = list(map(int,input().split()))
head = None 
for ele in l:
    head =  addNodeAtTailOfLinkedList(head, ele)
    
printLeftToRightManner(head)
printRightToLeftManner(head)   


head = insertAtSpecificPosition(head, pos,val)
printLeftToRightManner(head)
printRightToLeftManner(head)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

