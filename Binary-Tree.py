Pre-Order Traversal along with Binary-Tree construction:-

class TreeNode:
    def __init__(self , value):
        self.value = value
        self.left = None 
        self.right = None
        
def preorder_traversal(node):
    if node:
        print(node.value ,end =" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

node11 = TreeNode(11)
node7 = TreeNode(7)
node5 = TreeNode(5)
node3 = TreeNode(3)
node9 = TreeNode(9)
node8 = TreeNode(8)
node10 = TreeNode(10)
node15 = TreeNode(15)
node13 = TreeNode(13)
node12 = TreeNode(12)
node14 = TreeNode(14)
node20 = TreeNode(20)
node18 = TreeNode(18)
node25 = TreeNode(25)

node11.left = node7
node11.right = node15
node7.left = node5
node7.right = node9
node5.left = node3
node9.left = node8
node9.right = node10
node15.left = node13
node15.right = node20
node13.right = node12
node12.left = node14
node20.right = node18
node18.right = node25

preorder_traversal(node11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
In-Order Traversal along with Binary-Tree construction:-

class TreeNode:
    def __init__(self , value):
        self.value = value 
        self.left = None
        self.right = None
        
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value,end=" ")
        inorder_traversal(node.right)
    
    
node3 = TreeNode(3)
node5 = TreeNode(5)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node11 = TreeNode(11)
node12 = TreeNode(12)
node13 = TreeNode(13)
node14 = TreeNode(14)
node15 = TreeNode(15)
node18 = TreeNode(18)
node20 = TreeNode(20)
node25 = TreeNode(25)


node11.left = node7 
node11.right = node15
node7.left = node5
node7.right = node9
node5.left = node3
node9.left = node8
node9.right = node10
node15.left = node13
node15.right = node20
node13.left = node12
node13.right = node14
node20.left = node18
node20.right = node25


inorder_traversal(node11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Post-Order Traversal along with Binary-Tree construction:-

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")

node3 = TreeNode(3)
node5 = TreeNode(5)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node11 = TreeNode(11)
node12 = TreeNode(12)
node13 = TreeNode(13)
node14 = TreeNode(14)
node15 = TreeNode(15)
node18 = TreeNode(18)
node20 = TreeNode(20)
node25 = TreeNode(25)

node11.left = node7
node11.right = node15
node7.left = node5
node7.right = node9
node5.left = node3
node9.left = node8
node9.right = node10
node15.left = node13
node15.right = node20
node13.left = node12
node13.right = node14
node20.left = node18
node20.right = node25



postorder_traversal(node11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Level-Order Traversal along with Binary-Tree construction:-

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def print_level_order(root):
    if root is None:
        return

    queue = [root]

    while queue:
        print(' '.join(str(node.val) for node in queue))
        queue = [child for node in queue for child in (node.left, node.right) if child]

root = Node(11)
root.left = Node(7)
root.right = Node(15)
root.left.left = Node(5)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(20)
root.left.left.left = Node(3)
root.left.right.left = Node(8)
root.left.right.right = Node(10)
root.right.left.left = Node(12)
root.right.left.right = Node(14)
root.right.right.left = Node(18)
root.right.right.right = Node(25)


print_level_order(root)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Zig-Zag level-Order Traversal along with Binary-Tree construction:-


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def zigzag_level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_values = []
        level_size = len(queue)

        for _ in range(level_size):
            if left_to_right:
                node = queue.popleft()
                level_values.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                node = queue.pop()
                level_values.append(node.value)
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)

        result.append(level_values)
        left_to_right = not left_to_right

    return result

root = TreeNode(11)
root.left = TreeNode(7)
root.right = TreeNode(15)
root.left.left = TreeNode(5)
root.left.right = TreeNode(9)
root.right.left = TreeNode(13)
root.right.right = TreeNode(20)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(8)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(12)
root.right.left.left = TreeNode(14)
root.right.right.left = TreeNode(18)
root.right.right.right = TreeNode(25)

result = zigzag_level_order_traversal(root)
for level in result:
    print(*level)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Left view of a Binary-tree along with its construction:-


class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def leftViewOfBinaryTree(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
 
    # print("Left view is:")
    print(*result)   
    
    
root = TreeNode(11)
obj2 = TreeNode(7)
obj3 = TreeNode(15)
obj4 = TreeNode(5)
obj5 = TreeNode(9)
obj6 = TreeNode(13)
obj7 = TreeNode(20)
obj8 = TreeNode(3)
obj9 = TreeNode(8)
obj10 = TreeNode(10)
obj11 = TreeNode(12)
obj12 = TreeNode(14)
obj13 = TreeNode(18)
obj14 = TreeNode(25)



root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj3.left = obj6
obj3.right = obj7

obj4.left = obj8

obj5.left = obj9
obj5.right = obj10 

obj6.left = obj11
obj6.right = obj12

obj7.left = obj13 
obj7.right = obj14 
leftViewOfBinaryTree(root)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Right view of a Binary-tree along with its construction:-

class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def rightViewOfBinaryTree(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            if i == n - 1:
                result.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
 
    # print("Right view is:")
    print(*result)  
    
    
root = TreeNode(11)
obj2 = TreeNode(7)
obj3 = TreeNode(15)
obj4 = TreeNode(5)
obj5 = TreeNode(9)
obj6 = TreeNode(13)
obj7 = TreeNode(20)
obj8 = TreeNode(3)
obj9 = TreeNode(8)
obj10 = TreeNode(10)
obj11 = TreeNode(12)
obj12 = TreeNode(14)
obj13 = TreeNode(18)
obj14 = TreeNode(25)



root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj3.left = obj6
obj3.right = obj7

obj4.left = obj8

obj5.left = obj9
obj5.right = obj10 

obj6.left = obj11
obj6.right = obj12

obj7.left = obj13 
obj7.right = obj14 
rightViewOfBinaryTree(root)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Top view of a Binary-tree along with its construction:-

class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def printTopViewOfBinaryTree(root):
    result = []
 
    Q = [[root, 0]]
    store = dict()
    while len(Q) > 0:
        currPair = Q.pop(0)
        node = currPair[0]
        hd = currPair[1]
 
        if hd not in store:
            store[hd] = node.data 
 
        if node.left != None:
            Q.append([node.left, hd - 1])
 
        if node.right != None:
            Q.append([node.right, hd + 1])
 
    
    allKeys = sorted(store.keys())
    for eachKey in allKeys:
        result.append(store[eachKey])
 

    print(*result)
 
    
root = TreeNode(11)
obj2 = TreeNode(7)
obj3 = TreeNode(15)
obj4 = TreeNode(5)
obj5 = TreeNode(9)
obj6 = TreeNode(13)
obj7 = TreeNode(20)
obj8 = TreeNode(3)
obj9 = TreeNode(8)
obj10 = TreeNode(10)
obj11 = TreeNode(12)
obj12 = TreeNode(14)
obj13 = TreeNode(18)
obj14 = TreeNode(25)



root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj3.left = obj6
obj3.right = obj7

obj4.left = obj8

obj5.left = obj9
obj5.right = obj10 

obj6.left = obj11
obj6.right = obj12

obj7.left = obj13 
obj7.right = obj14 
printTopViewOfBinaryTree(root)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bottom view of a Binary-tree along with its construction:-

class TreeNode:

    def __init__(self, data):

        self.data = data 

        self.left = None 

        self.right = None 

def printBottomViewOfBinaryTree(root):

    result = []

 

    Q = [[root, 0]]

    store = dict()

    while len(Q) > 0:

        currPair = Q.pop(0)


        node = currPair[0]

        hd = currPair[1]

 

        

        store[hd] = node.data 

 

        if node.left != None:

            Q.append([node.left, hd - 1])

 

        if node.right != None:

            Q.append([node.right, hd + 1])

 

    

    allKeys = sorted(store.keys())

    for eachKey in allKeys:

        result.append(store[eachKey])

 


    print(*result)

 

    

root = TreeNode(11)

obj2 = TreeNode(7)

obj3 = TreeNode(15)

obj4 = TreeNode(5)

obj5 = TreeNode(9)

obj6 = TreeNode(13)

obj7 = TreeNode(20)

obj8 = TreeNode(3)

obj9 = TreeNode(8)

obj10 = TreeNode(10)

obj11 = TreeNode(12)

obj12 = TreeNode(14)

obj13 = TreeNode(18)

obj14 = TreeNode(25)

root.left = obj2 

root.right = obj3 

 

obj2.left = obj4 

obj2.right = obj5 

 

obj3.left = obj6

obj3.right = obj7

obj4.left = obj8

obj5.left = obj9

obj5.right = obj10 

obj6.left = obj11

obj6.right = obj12

obj7.left = obj13 

obj7.right = obj14 

printBottomViewOfBinaryTree(root)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
