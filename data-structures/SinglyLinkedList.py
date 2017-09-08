class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def addNodeFront(self,data):
    newNode      = Node(data)
    newNode.next = self.head
    self.head    = newNode

  def printList(self):
    print("The Singly Linked List data : ")
    node = self.head
    while(node != None):
      print(node.data,end=" ")
      node = node.next
    print()


def main():
  llist = SinglyLinkedList()
  flag = True
  while(flag == True):
    print('''
      1. add node at front
      2. add node at last
      3. add node after a node
      4. delete a node
      5. print linked list
    ''')
    choice = int(input())
    if choice == 1:
      #add node at front
      print("enter the node data :")
      data = int(input())
      llist.addNodeFront(data)      
    elif choice == 2:
      #add node at last
      print("enter the node data :")
      data = int(input())
    elif choice == 3:
      print("enter the node data :")
      data = int(input())
    elif choice == 4:
      print("enter the node data :")
      data = int(input())
    elif choice == 5:
      llist.printList()
    elif choice == 6:
      pass
    elif choice == 7:
      pass
    elif choice == 8:
      pass
    elif choice == 9:
      pass
    elif choice == 10:
      pass
    elif choice == 11:
      pass
    elif choice == 12:
      pass
    elif choice == 13:
      pass
    elif choice == 14:
      pass
    elif choice == 15:
      pass
    elif choice == 16:
      pass
    elif choice == 17:
      pass
    elif choice == 18:
      pass
    elif choice == 19:
      pass
    elif choice == 20:
      pass
    elif choice == 21:
      pass
    elif choice == 22:
      pass
    elif choice == 0:
      flag = False
    



if __name__ == '__main__':
    main()
