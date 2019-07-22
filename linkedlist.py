class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def taverse(self):
        temp = self.head
        while temp:
            print(temp.data, end="")
            print("->", end="")
            temp = temp.next
        print("")

    def addathead(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def addattail(self, data):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def addafter(self, prev, data):
        temp = self.head
        while temp.data != prev:
            temp = temp.next
        nexti = temp.next
        temp.next = Node(data)
        temp.next.next = nexti

    def addbefore(self, data, next):
        temp = self.head
        while temp.next.data != next:
            temp = temp.next
        nexti = temp.next
        temp.next = Node(data)
        temp.next.next = nexti

    def deletenode(self, data):
        temp = self.head
        while temp.next.data != data:
            temp = temp.next
        prevtemp = temp
        deltemp = temp.next
        prevtemp.next = deltemp.next

    def reverselist(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.taverse()
    llist.addathead(0)
    llist.taverse()
    llist.addattail(4)
    llist.addattail(5)
    llist.taverse()
    llist.addafter(3, 6)
    llist.taverse()
    llist.addbefore(7, 6)
    llist.taverse()
    llist.deletenode(4)
    llist.taverse()
    llist.reverselist()
    llist.taverse()
    llist.reverselist()
    llist.taverse()
