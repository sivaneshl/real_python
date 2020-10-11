# https://realpython.com/linked-lists-python/

from collections import deque

# create an empty linked list using deque
llist = deque()
print(llist)

# populate the linked list at its creation
llist = deque('abc')
print(llist)
llist = deque(['a', 'b', 'c'])
print(llist)
llist = deque([{'data': 'a'},
               {'data': 'b'}])
print(llist)

###
# adding an element to the linked list
llist = deque('abcde')
llist.append('f')
print(llist)

# removing an element from the linked list
llist.pop()
print(llist)

###
# adding an element to the front (left)
llist.appendleft('x')
print(llist)

# removing an element from the front (left)
llist.popleft()
print(llist)

###
# implementing a queue (fifo) using deque
queue = deque()
# adding elements to the end of the queue
queue.append('john')
queue.append('mary')
queue.append('adam')
print(queue)
# removing elements from the front of th queue
queue.popleft()
queue.popleft()
print(queue)

###
# implementing a stack (lifo) using deque
stack = deque()
# adding elements to the top of the stack
stack.appendleft('john')
stack.appendleft('mary')
stack.appendleft('adam')
print(stack)
# removing elements from the top of the stack
stack.popleft()
stack.popleft()
print(stack)
