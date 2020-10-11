class CircularLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        # if the nodes list is provided, then create the linked list
        if nodes is not None:
            # assign the head node
            node = Node(nodes.pop(0))
            self.head = node
            # loop through the rest of the nodes and link them
            for element in nodes:
                node.next = Node(data=element)
                node = node.next
            # link the last node to the head
            node.next = self.head

    def __iter__(self):
        node = self.head
        while node is not None and (node.next != self.head):
            yield node
            node = node.next

    def find_node(self, data):
        for node in self:
            # print(node, node.next)
            if node.data == data:
                return node

    def traverse(self, starting_point=None):
        # if the starting point is not provided, then start from head node
        if starting_point is None:
            starting_point = self.head
        else:
            starting_point = self.find_node(starting_point)
        # set the current node as the starting point node and loop through
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point=starting_point):
            nodes.append(str(node))
        print(' -> '.join(nodes))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


circular_llist = CircularLinkedList(list('abcde'))
circular_llist.print_list()
circular_llist.print_list('d')

