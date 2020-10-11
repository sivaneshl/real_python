from linked_list import LinkedList, Node

class Queue(LinkedList):
    def enqueue(self, data):
        self.add_last(Node(data))

    def dequeue(self):
        self.remove_first()

# new queue
q = Queue(list('abcde'))
print(q)

# new blank queue
q = Queue()

# enqueue - add to last
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(q)

# dequeue - pop first
q.dequeue()
q.dequeue()
print(q)

