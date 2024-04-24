Linked-List Construction-

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
        
def LinkedList(head):
    cur = head 
    while cur != None:
        print(cur.data,end = " ",)
        cur = cur.next
    print()
    
    
def insertAtEndOfTail(head,ele):
    newblock = Node(ele)
    if head == None:
        return newblock
    cur = head 
    while cur.next != None:
        cur = cur.next
    cur.next = newblock
    return head

n = int(input())
listt = map(int,input().split())
head = None 
for ele in listt:
    head = insertAtEndOfTail(head,ele)
LinkedList(head)

````````````````````````````````````````````````````````````````````````````
Insert a Node at the Tail of a Linked List-

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if not head:
        return SinglyLinkedListNode(data)
    current = head
    while current.next:
        current = current.next
    current.next = SinglyLinkedListNode(data)
    return head
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`````
Insert a node at the head of a linked list-

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    new_node.next = llist
    return new_node
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')
    
    fptr.close()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Insert a node at a specific position in a linked list-

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = llist
        return new_node
    
    current = llist 
    for _ in range(position - 1):
        current = current.next
        
    new_node.next = current.next
    current.next = new_node
    
    return llist
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Delete a node at specific position in Singly-linked list-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addToTail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def printForward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def deleteAtPosition(self, position):
        if position <= 0 or not self.head:
            print( )
            return

        if position == 1:
            self.head = self.head.next
            return

        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            print()
            return

        current.next = current.next.next

n = int(input())
elements = list(map(int, input().split()))
position = int(input())

curr = SinglyLinkedList()
for element in elements:
    curr.addToTail(element)

curr.printForward()
curr.deleteAtPosition(position)
curr.printForward()
print()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Delete tail node in Singly-linked list-

class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data,end = " ",)
        curr = curr.next
    print()


def insertAtEndOfTail(head,ele):
    newBlock =  Node(ele)
    if head == None:
        return newBlock
    curr = head
    while curr.next!= None:
        curr = curr.next
    curr.next = newBlock
    return head



def deleteTailNode(head):
    curr = head
    previous = None
    while curr.next != None:
        previous =curr
        curr = curr.next 
    previous.next = None
    return head
    
    

n= int(input())
l = map(int,input().split())
head = None
for ele in l:
    head = insertAtEndOfTail(head,ele)
printLinkedList(head)
head = deleteTailNode(head)
printLinkedList(head)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Delete head node in Singly-linked list-

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
 
def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head
 
def printlist(head):
    curr=head
 
    while curr!=None:
 
        print(curr.data,end=" ")
        curr=curr.next
    print()
 
 

 
def deleteHeadNodeInLinkedList(head):
  
    if head == None:
        return None 
 
    secondNode = head.next 
    head.next = None 
    return secondNode
 
  
 
 

 

 
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printlist(head)
head = deleteHeadNodeInLinkedList(head)
printlist(head)

