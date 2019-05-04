
class Node:
   def __init__(self,key):
      self.key    = key
      self.parent = None
      self.right  = None
      self.left   = None

class Tree:
   def __init__(self):
      self.root = None
      self.node = Node(self.root)
      self.find_node = None

   def add(self,key):
      if (self.root == None):
         self.root = Node(key)
      else:
         self._add(key,self.root)

   def _add(self,key,node ):
      if key> node.key:
         if node.left != None:
            self._add(key,node.left)
         else:
            node.left = Node(key)
            node.left.parent = node
         
      else:   
         if node.right != None:
            self._add(key,node.right)
         else:
            node.right = Node(key)
            node.right.parent = node

   def search (self,key):
      if self.root == None:
         print ("This tree is empty, so there is any " + str(key)+ " !")
         return
      else:
         self._search(key,self.root)
         
   def _search(self,key,node):
      if node == None:
         print ("There is no " + str(key))
         return
      elif key> node.key:
         self._search(key,node.left)
         
      elif key< node.key:
         self._search(key,node.right)
         
      else:
         print ( "Here its --->" + str(node))
         self.find_node = node
         return node

   def del_node(self,key):
      self.search(key)
      node = self.find_node
      if ( node.right == None and node.left == None):
         print (str (node.key) )
         print (node.parent.key)
         if (node.parent.key > node.key):
            node.parent.right = None
         else:
            node.parent.left = None
         
         
         
      elif ( node.right != None and node.left == None):
         x=node.right
         y=node.parent
         print (str (node.key) )
         if (node.parent.key > node.key):
            node.parent.right = None
         else:
            node.parent.left = None
         if y.key > x.key:
            y.right = x
         else:
            y.left = x
      elif (node.right == None and node.left != None):
         x = node.left
         y = node.parent
         print (str (node.key) )
         if (node.parent.key > node.key):
            node.parent.right = None
         else:
            node.parent.left = None
         if y.key > x.key:
            y.right = x
         else:
            y.left = x
      else:
         x = node.left
         while x.right != None:
            print (x.key)
            x = x.right
         y=node.parent
         print (str (node.key))
         if (node.parent.key > node.key):
            node.parent.right = None
         else:
            node.parent.left = None
         if y.key > x.key:
            y.right = x
         else:
            y.left = x
         
   def print_tree(self):
      if(self.root != None):
         self._print_tree(self.root)
         
   def _print_tree(self,node):
      if(node != None):
         self._print_tree(node.left)
         print (node.key)
         self._print_tree(node.right)
               
   def get_parent(self,key):
      self.search(key)
      x = self.find_node.parent
      if x is not None:
         x = x.key
      return x
   def get_child(self,key):
      self.search(key)
      x,y = self.find_node.right,self.find_node.left
      if x is not None:
         x = x.key
      if y is not None:
         y = y.key
      return x,y

def main():
   Binary_tree = Tree()
   Binary_tree.add(5)
   Binary_tree.add(4)
   Binary_tree.add(8)
   Binary_tree.add(9)
   Binary_tree.add(3)
   Binary_tree.add(0)
   Binary_tree.add(7)
   Binary_tree.add(6)
   Binary_tree.add(2)
   Binary_tree.add(1)
   Binary_tree.print_tree()
   Binary_tree.search(2)
   Binary_tree.print_tree()
   Binary_tree.del_node(8)
   Binary_tree.print_tree()
   Binary_tree.search(8)
   Binary_tree.print_tree()

if __name__ == "__main__":
   main()

         
