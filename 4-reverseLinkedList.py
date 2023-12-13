class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def reverse(self, head):
        prev = None
        curr = head
        next_node = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head = prev
        return head

# Creating a linked list: 1 -> 2 -> 3 -> 4
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

# Testing the reverse method
print("Original linked list:")
current_node = node1
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")

# Reversing the linked list
node1 = node1.reverse(node1)

# Testing the reversed linked list
print("Reversed linked list:")
current_node = node1
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")
