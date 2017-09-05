class node():
  def __init__(self,data):
      self.data  = data
      self.left  = None
      self.right = None

class binaryTree():
  def __init__(self):
    self.head = None
 
  def insertNode(self, data):

    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = node(data)
        else:
          self.left.insertNode(data)
      elif data > self.data:
          if self.right is None:
            self.right = node(data)
          else:
            self.right.insertNode(data)
    else:
      self.data = data    

  def printPreorder(self,node):
    if node == None:
      return
    print(node.data)
    printPreorder(node.left)
    printPreorder(node.right)
    
  def printInorder(self,node):
    if node == None:
      return
    printInorder(node.left)
    print(node.data)    
    printInorder(node.right)
    
  def printPostorder(self,node):
    if node == None:
      return
    printPostorder(node.left)
    printPostorder(node.right)
    print(node.data)    
    
  def printMenu(self):
      menuList = [
          ['add node','insertNode'],
          ['print pre-order tree','printPreorder'],
          ['print in-order tree','printInorder'],
          ['print post-order tree 2','printPostorder']
          ]

      for x in enumerate(menuList):
         print (str(x[0]) + ". "  + str(x[1]))
      print("before choice")
      choice = 0
      #choice = int(input())
      print("choice : " + str(choice))
      if menuList[choice][1] == 'insertNode':
        print("enter the node data : ")
        data = int(input())
        insertNode(data)
      elif menuList[choice][1] == 'printPreorder':
        printPreorder()
      elif menuList[choice][1] == 'printPostorder':
        printPostorder()
      elif menuList[choice][1] == 'printInorder':
        printInorder()


def main():
  bt = binaryTree()
  bt.printMenu()

if __name__ == '__main__':
  main()
