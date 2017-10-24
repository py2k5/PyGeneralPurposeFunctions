class Node:
        def __init__(self,data=None):
                self.data = data
                self.next = None



class LinkedList:
        def __init__(self):
                self.head = None

        def insert(self, newNode ):
                temp = self.head
                self.head = newNode
                self.head.next = temp
                del temp

        def delete(self):
                pass
        def printList(self):
                if self.head is None:
                        print("List is empty")
                        return
                current = self.head
                while True:
                        if current is None:
                                break
                        print(current.data)
                        current = current.next


n1 = Node(10)
ll = LinkedList()
ll.insert(n1)
n2 = Node(20)
ll.insert(n2)
ll.printList()
