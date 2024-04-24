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
