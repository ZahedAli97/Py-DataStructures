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

    def addattail(self, data):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)


class HashTable:
    def __init__(self):
        self.hastable = []
        print(self.hastable)

    def insertElement(self, data):


ht = HashTable()
