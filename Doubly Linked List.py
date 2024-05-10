# Programmer: Rizon Takabe
# Class: CS 240
# Date: 4/15/23
# Assignment: Insertion Sort
# This code creates a doubly linked list with the numbers in the numbers-2.txt file and performs various operations on it.
# It can read, insert, and delete, elements at the beginning, end, or position you choose. It does this by adjusting the next and previous pointers.
# It also can sort the list using a selection sort algorithm which traverses the unsorted part of the list until it finds the smallest value, then swaps with the current unsorted value.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    # Inserts a new node at beggining by creating a new node at the heads previous, new node becomes head
    def insert_beginning(self, value):
        new_node = Node(value)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert_at_position(self, value, position):
        if position == 0:
            self.insert_beginning(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        if current is None:
            raise IndexError("Position out of range")
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    # if there is more than 1 element in the list it deletes 2nd elements previous
    def delete_beginning(self):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.next:
            self.head.next.prev = None
        self.head = self.head.next

    # traverses to last node, then goes to previous node to delete last node
    def delete_end(self):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.next is None:  # If there's only one node in the list
            self.head = None
            return
        current = self.head
        while current.next:  # Traverse until the last node is reached
            current = current.next
        current.prev.next = None  # use the previous method to delete the last node

    def delete_at_position(self, position):
        if position == 0:
            self.delete_beginning()
            return
        current = self.head
        for _ in range(position):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        if current is None:
            raise IndexError("Position out of range")
        if current.next:
            current.next.prev = current.prev
        current.prev.next = current.next

    # iterates through list until it finds the value, returns the position
    def linear_search(self, value):
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    # iterates to index then prints value
    def read(self, position):
        current = self.head
        index = 0
        while index < position:
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
            index += 1
        if current is None:
            raise IndexError("Position out of range")
        print(current.value)
    
    # prints head of list
    def read_beginning(self):
        if self.head is None:
            raise Exception("List is empty")
        print(self.head.value)

    # traverses through list to print final node
    def read_end(self):
        if self.head is None:
            raise Exception("List is empty")
        current = self.head
        while current.next:
            current = current.next
        print(current.value)

    # iterates through unsorted part of list until it finds the min value then swaps with the current unsorted value
    def selection_sort(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head
        while current:
            min_node = current
            temp = current.next
            while temp:
                if temp.value < min_node.value:
                    min_node = temp
                temp = temp.next

            if min_node != current:
                current.value, min_node.value = min_node.value, current.value

            current = current.next


def main():
    linked_list = DoublyLinkedList()
    numbers = read_file("numbers-2.txt")
    for num in numbers:
        linked_list.insert_end(num)
    # User menu
    while True:
        answer = input("(RP) Read Position (RB) Read Beginning, (RE) Read End\n(IP) Insert Position, (IB) Insert Beginning, (IE) Insert End\n(DP) Delete Position, (DB) Delete Beginning, (DE) Delete End\n(S)earch\n(Sort)\n(E)xit\n").lower()
        if answer == "rp":
            position = int(input("Enter position to read: "))
            linked_list.read(position)
        elif answer == "rb":
            linked_list.read_beginning()
        elif answer == "re":
            linked_list.read_end()
        elif answer == "ip":
            value = int(input("Enter value to insert: "))
            position = int(input("Enter position to insert: "))
            linked_list.insert_at_position(value, position)
        elif answer == "ib":
            value = int(input("Enter value to insert at the beginning: "))
            linked_list.insert_beginning(value)
        elif answer == "ie":
            value = int(input("Enter value to insert at the end: "))
            linked_list.insert_end(value)
        elif answer == "dp":
            position = int(input("Enter position to delete: "))
            linked_list.delete_at_position(position)
        elif answer == "db":
            linked_list.delete_beginning()
        elif answer == "de":
            linked_list.delete_end()
        elif answer == "s":
            value = int(input("Enter value to search: "))
            index = linked_list.linear_search(value)
            if index != -1:
                print(f"Value {value} found at position {index}")
            else:
                print(f"Value {value} not found in the list")
        elif answer == "sort":
            linked_list.selection_sort()
            print("List sorted")

        elif answer == "e":
            break

# copy file to array
def read_file(file_name):
    arr = []
    with open(file_name) as file:
        for line in file:
            arr.append(int(line.strip()))
    return arr

main()