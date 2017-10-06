class Stack(object):
    """Implementation of Stack ADT"""

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue(object):
    """Implementation of Queue ADT."""

    def __init__(self, items=[]):
        self.items = items
        self.items.reverse()

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)


class Deque(object):
    """Implementation of Deque ADT."""

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class Node(object):
    """Implementation of a Node."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class OrderedList(object):
    """Implementation of ordered Linked list."""

    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        previous = None
        current = self.head
        found = False

        while current and not found:
            if current.get_data() < item:
                found = True
            else:
                previous, current = current, current.get_next()

        node = Node(item)
        node.set_next(current)
        self.length += 1

        if previous is None:
            self.head = node
        else:
            previous.set_next(node)

    def size(self):
        current = self.head
        counter = 0

        while current is not None:
            current = current.get_next()
            counter += 1

        return counter

    def search(self, item):
        current = self.head
        found = False

        while current and current.get_data() >= item and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        previous = None
        current = self.head
        found = False

        while current and current.get_data() >= item and not found:
            if current.get_data() == item:
                found = True
            else:
                previous, current = current, current.get_next()

        if previous is None:
            if found and current is not None:
                self.head = current.get_next()
                self.length -= 1
        else:
            if found and current is not None:
                previous.set_next(current.get_next())
                self.length -= 1

    def retrieve(self, position):
        current = self.head
        found_pos = False
        counter = self.length - 1

        while current and not found_pos:
            if counter == position:
                found_pos = True
            else:
                current = current.get_next()
                counter -= 1

        if found_pos:
            return current.get_data()

        raise ValueError('Index %s is out of bound.' % position)

    def index(self, item):
        current = self.head
        found = False
        counter = self.length - 1

        while current and current.get_data >= item and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                counter -= 1

        if found:
            return counter

        raise ValueError('%s is not in the list' % item)

    def pop(self, position=None):
        previous = None
        current = self.head
        found_pos = True

        if position is not None:
            found_pos = False
            counter = self.length - 1

        while current and not found_pos:
            if counter == position:
                found_pos = True
            else:
                previous, current = current, current.get_next()
                counter -= 1

        if previous is None:
            if current is not None:
                popped_data = current.get_data()
                self.head = current.get_next()
        else:
            if current is not None:
                popped_data = current.get_data()
                previous.set_next(current.get_next())

        if current:
            self.length -= 1
            return popped_data

        raise ValueError('Index %s is out of bound.' % position if position else 'List is empty.')

    def __getitem__(self, position):
        return self.retrieve(position)

    def __str__(self):
        items = ''

        current = self.head
        counter = 0

        while current:
            if not items:
                items = ']'

            items = str(current.get_data()) + items
            current = current.get_next()

            if current:
                items = ', ' + items

            counter += 1

        if items:
            items = '[' + items
        else:
            items = '[]'

        return items


class UnorderedList(OrderedList):
    """Implementation of unordered Linked list ADT."""

    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node
        self.length += 1

    def append(self, item):
        self.add(item)

    def search(self, item):
        current = self.head
        found = False

        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        previous = None
        current = self.head
        found = False

        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                previous, current = current, current.get_next()

        if previous is None:
            if current is not None:
                self.head = current.get_next()
                self.length -= 1
        else:
            if current is not None:
                previous.set_next(current.get_next())
                self.length -= 1

    def insert(self, position, item):
        previous = None
        current = self.head
        found_pos = False
        counter = self.length - 1

        while current and not found_pos:
            if counter == position:
                found_pos = True
            else:
                previous, current = current, current.get_next()
                counter -= 1

        if previous is None:
            self.add(item)
        else:
            node = Node(item)
            node.set_next(current)
            previous.set_next(node)
            self.length += 1

    def index(self, item):
        current = self.head
        found = False
        counter = self.length - 1

        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                counter -= 1

        if found:
            return counter

        raise ValueError('%s is not in the list' % item)

    def __setitem__(self, position, item):
        self.insert(position, item)


class Map(object):
    """Implementation of Map ADT."""

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    @staticmethod
    def hash_function(key, table_size):
        total = 0

        for pos in range(len(key)):
            total += ord(key[pos]) * (pos + 1)

        return total % table_size

    @staticmethod
    def rehash_function(old_hash, table_size):
        return (old_hash + 1) % table_size

    def put(self, key, data):
        hash_value = self.hash_function(key, self.size)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        elif self.slots[hash_value] == key:
            self.data[hash_value] = data
        else:
            hash_value = self.rehash_function(hash_value, self.size)
            while self.slots[hash_value] is not None and self.slots[hash_value] != key:
                hash_value = self.rehash_function(hash_value, self.size)

            if self.slots[hash_value] is None:
                self.slots[hash_value] = key
                self.data[hash_value] = data
            else:
                self.data[hash_value] = data

    def get(self, key):
        hash_value = self.hash_function(key, self.size)
        found = stop = False
        start_hash_value = hash_value

        while self.slots[hash_value] is not None and not (found or stop):
            if self.slots[hash_value] == key:
                found = True
            else:
                hash_value = self.rehash_function(hash_value, self.size)
                if hash_value == start_hash_value:
                    stop = True

        return self.data[hash_value]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


class BinaryTree(object):
    """Implementation of BinaryTree ADT."""

    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def insert_left(self, data):
        if self.left_child == None:
            self.left_child = BinaryTree(data)
        else:
            node_tree = BinaryTree(data)
            node_tree.left_child, self.left_child = self.left_child, node_tree

    def insert_right(self, data):
        if self.right_child == None:
            self.right_child = BinaryTree(data)
        else:
            node_tree = BinaryTree(data)
            node_tree.right_child, self.right_child = self.right_child, node_tree

    def set_node_value(self, data):
        self.key = data

    def get_node_value(self):
        return self.key


class MinBinaryHeap(object):
    """Implementation of Heap ADT."""

    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up()

    def percolate_up(self):
        current_index = self.size
        parent_index = self.size // 2

        while parent_index > 0:
            if self.heap_list[current_index] < self.heap_list[parent_index]:
                tmp = self.heap_list[parent_index]
                self.heap_list[parent_index] = self.heap_list[current_index]
                self.heap_list[current_index] = tmp
                current_index, parent_index = parent_index, parent_index // 2
            else:
                parent_index = 0

    def remove_min(self):
        if self.size >= 1:
            min_value = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.size]
            self.heap_list.pop()
            self.size -= 1
            self.percolate_down(1)

            return min_value

    def percolate_down(self, index):
        current_index = index
        left_child_index = index * 2

        while left_child_index <= self.size:
            min_child = self.min_child(current_index)
            if self.heap_list[min_child] < self.heap_list[current_index]:
                tmp = self.heap_list[current_index]
                self.heap_list[current_index] = self.heap_list[min_child]
                self.heap_list[min_child] = tmp
                current_index, left_child_index = min_child, min_child * 2
            else:
                left_child_index = self.size + 1


    def min_child(self, current_index):
        if current_index * 2 + 1 > self.size and current_index * 2 <= self.size:
            return current_index * 2
        else:
            if self.heap_list[current_index * 2] < self.heap_list[current_index * 2 + 1]:
                return current_index * 2
            else:
                return current_index * 2 + 1

    def build_heap(self, arr_list):
        index = len(arr_list) // 2
        self.heap_list = [0] + arr_list
        self.size = len(arr_list)

        while index > 0:
            self.percolate_down(index)
            index -= 1


class Vertex(object):
    """Implementation of Graph Vertex."""

    def __init__(self, key):
        self.id = key
        self.neighbors = {}

    def add_neighbor(self, vertex, weight):
        self.neighbors[vertex] = weight

    def get_neighbors(self):
        return [x for x in self.neighbors.keys()]

    def get_weight(self, neighbor):
        if neighbor in self.get_neighbors():
            return self.neighbors[neighbor]

    def __repr__(self):
        return self.id

    def __str__(self):
        return '{} is connected to: {}'.format(self.id, [x.id for x in self.neighbors])


class Graph(object):
    """Implementation of Graph ADT."""

    def __init__(self):
        self.vertices = {}
        self.vertices_count = 0

    def __contains__(self, key):
        return key in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, key):
        new_vertex = Vertex(key)

        if key not in self.vertices:
            self.vertices_count += 1

        self.vertices[key] = new_vertex

        return new_vertex

    def add_edge(self, left_vertex, right_vertex, weight=0):
        if left_vertex not in self.vertices:
            self.add_vertex(left_vertex)

        if right_vertex not in self.vertices:
            self.add_vertex(right_vertex)

        self.vertices[left_vertex].add_neighbor(self.vertices[right_vertex], weight)

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]

    def get_vertices(self):
        return [x for x in self.vertices.values()]
