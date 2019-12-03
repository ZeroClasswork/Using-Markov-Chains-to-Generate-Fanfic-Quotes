#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.current = None
        self.tail = None  # Last node
        self.list_length = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        """Identifies LinkedList as an iterable type"""
        self.current = self.head
        return self
    
    def __next__(self):
        """Identifies LinkedList as an iterable type"""
        current = self.current
        if self.current is None:
            raise StopIteration
        self.current = self.current.next
        return current

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(1) since simply calling a variable"""
        # current_node = self.head
        # count = 0
        # while current_node != None:
        #     count += 1
        #     current_node = current_node.next
        # return count
        return self.list_length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) since does same execution every time"""
        self.list_length += 1
        new_node = Node(item)
        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) since does same execution every time"""
        self.list_length += 1
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        if self.head.next == None:
            self.tail = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if first item
        Worst case running time: O(n) if last item because must traverse whole list"""
        current_node = self.head
        while current_node != None:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if list empty, if item is first node
        Worst case running time: O(n) if last item or not in list because it 
            must traverse the whole list"""
        if self.head is None:
            raise ValueError('Item not found: {}'.format(item))
        if item == self.head.data:
            old_head = self.head
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            self.list_length -= 1
            return
        previous_node = self.head
        current_node = self.head.next
        while current_node != None:
            if item == current_node.data:
                if current_node == self.tail:
                    self.tail = previous_node
                previous_node.next = current_node.next
                self.list_length -= 1
                return
            previous_node = current_node
            current_node = current_node.next
        raise ValueError('Item not found: {}'.format(item))

    def replace(self, item, replacement):
        """Replaces the given item from this linked list with replacement, or raise ValueError.
        Best case running time: O(1) if item is first node
        Worst case running time: O(n) if last item or not in list because it 
            must traverse the whole list"""
        self.delete(item)
        self.append(replacement)


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

    # Test iterable
    for item in ['A', 'B', 'C', 'D']:
        ll.append(item)
    for index, node in enumerate(ll):
        print(index, node.data)

if __name__ == '__main__':
    test_linked_list()
