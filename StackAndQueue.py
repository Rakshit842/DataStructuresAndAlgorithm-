st = []

st.append(8)
st.append(1)
st.append(3)
st.append(4)

print(st)

st.pop()
print(st)

# Stack all functions
class stack:
    def __init__(self):
        self.st = []

    def push(self,x):
        self.st.append(x)

    def pop(self):
        if len(self.st) == 0:
            return -1
        x = self.st[-1]
        self.st.pop()
        return x
    
    def top(self):
        if len(self.st) == 0:
            return -1
        return self.st[-1]
    
    def size(self):
        return len(self.st)  

stack = stack()

stack.push(5)
stack.push(4)
stack.push(3)
stack.push(9)

print(stack.pop())
print(stack.top())
print(stack.size())



# Making stack using node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, x):
        self.length += 1
        if self.top is None:
            self.top = Node(x)
            return
        else:
            newNode = Node(x)
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        self.length -= 1
        x = self.top.data
        self.top = self.top.next
        return x
    
    def getTop(self):
        if self.top == None:
            return -1
        return self.top.data
    
    def size(self):
        return self.length


# Queue Operations using List in Python
class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, value):
        self.queue.append(value)
        print(value, "inserted into queue")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue.pop(0), "removed from queue")

    # Front element
    def front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front element is:", self.queue[0])

    # Rear element
    def rear(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Rear element is:", self.queue[-1])

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Size of queue
    def size(self):
        print("Size of queue:", len(self.queue))

    # Display queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue)


# Driver Code
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.front()

q.rear()

q.dequeue()

q.display()

q.size()

print("Is queue empty?", q.is_empty())