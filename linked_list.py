class Node:
    def __init__(self,data):
        self.data=data
        self.next=None;

n1=Node(12)
n2=Node(2)
n3=Node(42)
n4=Node(400)
n5=Node(32)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

def printLinkedList(n:Node):
    currentNode=n
    while(currentNode):
        print(currentNode.data,end="->")
        currentNode=currentNode.next
    print("None");
# printLinkedList(n1)

def insert(starting:Node,where:int,newNode:Node)->Node:
    if where==0:
        newNode.next=starting
        return newNode
    prev=starting
    index=0
    while prev and index<where-1:
        prev=prev.next
        index+=1
    newNode.next=prev.next
    prev.next=newNode
    return starting

      
newNode=Node(9)
printLinkedList(insert(n1,3,newNode));





  


def deleteNode(starting:Node,deleteNode:Node):
      currentNode=starting
      while(currentNode):
          if currentNode.next==deleteNode:
              currentNode.next=deleteNode.next
          currentNode=currentNode.next
      return starting

printLinkedList(deleteNode(n1,n3))

    
