from Node import Node

class Pilha:
    def __init__(self):
        self.top = None

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.top is not None:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value

    def is_empty(self):
        return self.top is None
