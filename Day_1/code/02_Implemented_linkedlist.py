# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Index cannot be negative.")
            return

        if index == 0:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if not current:
            print("Index out of bounds.")
            return

        new_node.next = current.next
        current.next = new_node

    def remove_at_index(self, index):
        if index < 0:
            print("Index cannot be negative.")
            return

        if not self.head:
            print("List is empty.")
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0

        while current.next and count < index - 1:
            current = current.next
            count += 1

        if not current.next:
            print("Index out of bounds.")
            return

        current.next = current.next.next

    def get(self, index):
        if index < 0:
            print("Index cannot be negative.")
            return None

        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1

        print("Index out of bounds.")
        return None

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_start(5)
    ll.insert_at_index(1, 7)
    ll.print_list()         # Output: 5 -> 7 -> 10 -> 20

    ll.remove_at_index(2)
    ll.print_list()         # Output: 5 -> 7 -> 20

    print(ll.get(1))        # Output: 7
    print(ll.get(10))       # Output: Index out of bounds.
