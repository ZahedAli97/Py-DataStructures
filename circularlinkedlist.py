

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def taverse(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data, end="")
                print("->", end="")
                temp = temp.next
                if temp == self.head:
                    break
            print("")

    def addNode(self, data):
        new = Node(data)
        temp = self.head
        new.next = temp

        if self.head:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new
        else:
            new.next = new
            self.head = new

    def deleteNode(self, data):
        temp = self.head
        prev = self.head
        while temp.next.data != data:
            prev = temp.next
            temp = temp.next
        temp = temp.next
        prev.next = temp.next

    def reverseList(self):
        prev = None
        current = self.head
        # post = current.next
        # current.next = prev
        # current = post
        back = current
        while current.next != self.head:
            post = current.next
            current.next = prev
            prev = current
            current = post
        current.next = prev
        self.head = current
        back.next = self.head


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.addNode(1)
    cll.addNode(2)
    cll.addNode(3)
    cll.taverse()
    cll.deleteNode(2)
    cll.taverse()
    cll.addNode(7)
    cll.addNode(10)
    cll.addNode(29)
    cll.addNode(32)
    cll.taverse()
    cll.deleteNode(10)
    cll.taverse()
    cll.reverseList()
    cll.taverse()
    cll.reverseList()
    cll.taverse()
