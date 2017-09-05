class node():
  def __init__(self,data):
      self.data  = data
      self.left  = None
      self.right = None

class binaryTree():
  def __init__(self):
    self.head = None

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
      menuDict = [
          ('add node',addNode),
          'print pre-order tree':printPreorder,
          'print in-order tree':printInorder,
          'print post-order tree':printPostorder
          }
      i = 1
      for x in menuList:
        print(str(i) + " " +x)
        i += 1

def main():
  bt = binaryTree()
  bt.printMenu()

if __name__ == '__main__':
  main()
