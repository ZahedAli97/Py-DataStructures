class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, " -> ", end="")
            if temp.next == None:
                pretemp = temp
                # print(pretemp.data)
            temp = temp.next

        print("")

        while pretemp:
            print(pretemp.data, " -> ", end="")
            pretemp = pretemp.prev

        print("")

    def addatfront(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        temp.prev = self.head

    def addattail(self, data):
        temp = self.head
        while temp.next:
            temp = temp.next
        prev = temp
        temp.next = Node(data)
        temp.next.prev = prev

    def addafter(self, prev, data):
        temp = self.head
        new = Node(data)
        while temp.data != prev:
            temp = temp.next
        new.next = temp.next
        new.prev = temp
        # Assinging prev pointer of variable after new to point to new
        afternew = temp.next
        afternew.prev = new
        temp.next = new

    def addbefore(self, nexti, data):
        temp = self.head
        new = Node(data)
        while temp.next.data != nexti:
            temp = temp.next
        afternew = temp.next
        afternew.prev = new
        temp.next = new
        new.prev = temp
        new.next = afternew

    def deleteNode(self, data):
        temp = self.head
        while temp.next.data != data:
            temp = temp.next
        pre = temp
        actual = temp.next
        post = actual.next
        pre.next = actual.next
        post.prev = actual.prev

    def reverseList(self):
        temp = self.head
        pre = None
        current = self.head

        while current:
            post = current.next
            # Since we are changing current.next
            current.next = pre
            current.prev = post
            pre = current
            current = post

        self.head = pre


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.head = Node(1)
    second = Node(2)
    third = Node(3)
    dll.head.next = second
    second.prev = dll.head
    second.next = third
    third.prev = second
    dll.traverse()
    dll.addatfront(0)
    dll.traverse()
    dll.addattail(4)
    dll.traverse()
    dll.addafter(2, 5)
    dll.traverse()
    dll.addbefore(5, 6)
    dll.traverse()
    dll.deleteNode(6)
    dll.traverse()
    print("--Reverse--")
    dll.reverseList()
    dll.traverse()
