class Node:
        def __init__(self,data=None):
                self.data = data
                self.next = None



class LinkedList:
        def __init__(self, head=None):
                self.head = head

        def insert(self, newNode ):
                temp = newNode
                temp.next = self.head
                self.head = temp
                

        def delete(self,data):
                if self.head is None:
                        print("Nothing to delete")
                        return
                current  = self.head
                previous = self.head
                while True:
                        if current is None:
                                break
                        if current.data == data:
                            previous.next = current.next

                        previous = current
                        current = current.next

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

            # Returns data at given index in linked list 
        def getNth(self, index): 
            current = self.head # Initialise temp 
            count = 0 # Index of current node 

            # Loop while end of linked list is not reached 
            while (current): 
                if (count == index): 
                    return current.data 
                count += 1
                current = current.next

            # if we get to this line, the caller was asking 
            # for a non-existent element so we assert fail 
            assert(false) 
            return 0; 

n1 = Node(10)
ll = LinkedList()
ll.delete(90)
ll.insert(n1)
n2 = Node(20)
ll.insert(n2)
n2 = Node(30)
ll.insert(n2)
n2 = Node(30)
ll.insert(n2)
n2 = Node(50)
ll.insert(n2)
print("Before delete")
ll.printList()
ll.delete(90)
print("after delete")
ll.printList()
