from linked_list import LinkedList, Node

# using the above class create a linked list
llist = LinkedList()
print(llist)
# add the first node
first_node = Node('a')
llist.head = first_node
print(llist)
# add subsequent nodes
second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
print(llist)

# create the linked list by passing in the nodes list
llist = LinkedList(list('abcde'))
print(llist)

# traversing through the linked list
for e in llist:
    print(e)

# inserting an element to the first of the linked list
llist.add_first(Node('x'))
llist.add_first(Node('y'))
print(llist)

# inserting an element to the last of the linked list
llist.add_last(Node('f'))
llist.add_last(Node('g'))
print(llist)

# inserting a node in between
# adding to an empty linked list
llist = LinkedList()
# llist.add_after('a', Node('b')) # exception
print(llist)
# adding an element after a target node
llist = LinkedList(list('abcde'))
llist.add_after('c', Node('cc'))
print(llist)
# attempt to add after a non-existent target node
# llist.add_after('f', Node('g')) # exception
print(llist)

# inserting a node before a target node
llist.add_before('c', Node('bb'))
print(llist)
llist.add_before('a', Node('zz'))
print(llist)

# removing a node
llist.remove_node('zz')
print(llist)
llist.remove_node('cc')
llist.remove_node('bb')
print(llist)

# get the node at position i
print(llist.get(3))
# print(llist.get(7)) # exception

# get the node at position i using subscript
print(llist[3])
# print(llist[7]) # exception

# get the reversed linked list
print(llist.reverse())

# get the length of the linked list
print(len(llist))
print(llist.__len__())
