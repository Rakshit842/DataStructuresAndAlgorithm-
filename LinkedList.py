# linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(5)
b = Node(6)
c = Node(7)

a.next = b
b.next = c

head = a

print(head.data)
print(head.next.data)
print(head.next.next.data)

# Traverse Linked List
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end =" ")
        curr = curr.next

printLinkedList(head)

# insertion at the beginning
newNode = Node(4)
newNode.next = head
head = newNode
printLinkedList(head)

# insertion at the end
newNode = Node(8)
curr = head 
while curr.next != None:
    curr = curr.next

curr.next = newNode
printLinkedList(head)


# insertion at Kth index
k=2
newNode = Node(1)
curr = head 
for i in range(k-1):
    curr = curr.next 

curr.next = curr.next.next
curr.next = newNode

# Delete first Node
head = head.next
printLinkedList(head)

# delete last node
curr = head 
while curr.next.next != None:
    curr = curr.next

curr.next = None 
printLinkedList(head)

# Delete at Kth index
k = 2
curr = head
for i in range(k-1):
    curr = curr.next

curr.next = curr.next.next 

# DOUBLY LINKEDLIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(5)
b = Node(6)
c = Node(7)

a.next = b
b.next = c

head = a

print(head.data)
print(head.next.data)
print(head.next.next.data)

curr = head

while True:
    print(curr.data, end=" ")
    curr = curr.next
    if curr==head:
        break
 
# Middle node
def MiddleNode():
    curr = head

    l=0
    while curr != None:
        curr = curr.next
        l+=1

    curr = head
    for i in range(l//2):
        curr = curr.next

    return curr


# Slow and fast pointer middle pointer 
def FastSlowPointer():
    slow = head 
    fast = head 

    while fast!=None and fast.next!=None:
        fast = fast.next.next
        slow = slow.next

    return slow