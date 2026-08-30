class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(12)
n2=Node(2)
n3=Node(42)
n1.next=n2
n2.next=n3

def printLinkedList(n:Node):
    currentNode=n
    while(currentNode):
        print(currentNode.data,end="->")
        currentNode=currentNode.next
    print("None")
printLinkedList(n1)

