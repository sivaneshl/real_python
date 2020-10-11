# class LinkedList will only have the pointer to the start of the linked list
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        # if the nodes list is provided, create the linked list
        if nodes is not None:
            # assign the head node
            node = Node(data=nodes.pop(0))
            self.head = node
            # loop through the rest of the nodes and assign the next nodes
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    # add a __repr__ to have a more helpful representation of the objects
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # traversing through the linked list
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # inserting an element to the first linked list
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # inserting an element to the last of the linked list
    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        node.next = None

    # inserting a new node after a target node
    def add_after(self, target_node_data, new_node):
        # if the list is empty then throw an exception
        if not self.head:
            raise Exception('List is empty')
        # loop through the nodes and find the target node and insert the new node after the target node
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        # raise an exception if we reach here -- the target node is not found
        raise Exception('Node with data {} is not found'.format(target_node_data))

    # add a new node before a target node
    def add_before(self, target_node_data, new_node):
        # throw an exception if the linked list is empty
        if not self.head:
            raise Exception('List is empty')
        # if the target node is the head then add the new node before the head and make it the head
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        # find the target node and insert the new node before the target node
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        # if we reach here that means we are not able to find the target node
        raise Exception('Node with data {} not found'.format(target_node_data))

    # removing a node
    def remove_node(self, target_node_data):
        # throw an exception if the list is empty
        if not self.head:
            raise Exception('List is empty')
        # if the target node is head...
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        # else find the target node and rearrange its next
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        # if we are here, it means we cannot find the target node
        raise Exception('Node with data {} not found'.format(target_node_data))

    # removes the first node
    def remove_first(self):
        # throw an exception if the linked list is empty
        if not self.head:
            raise Exception('List is empty')
        self.head = self.head.next

    # removes the last node
    def remove_last(self):
        # throw an exception if the linked list is empty
        if not self.head:
            raise Exception('List is empty')
        self[len(self)-2].next = None


    # get a node given the position
    def get(self, pos):
        # raise an exception if the list is empty
        if not self.head:
            raise Exception('List is empty')
        # retrieve the element for the given position
        for i, node in enumerate(self):
            if i == pos:
                return node
        # raise exception when the target position is not found
        raise Exception('List has no node at position {}'.format(pos))

    # get the node value using subscript
    def __getitem__(self, pos):
        return self.get(pos)

    # convert to list
    def to_list(self):
        return [node.data for node in self]

    # reverse the linked list
    def reverse(self):
        # rev_list = LinkedList()
        # for item in self.to_list():
        #     rev_list.add_first(item)
        # return rev_list

        # alternate method
        return LinkedList(list(reversed(self.to_list())))

    # get the length of the linked list
    def __len__(self):
        print('in __len__')
        return len(self.to_list())

# for each node in the linked list we will create a class Node which has 2 parameters -
# the data and the pointer to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # add a __repr__ to have a more helpful representation of the objects
    def __repr__(self):
        return self.data
