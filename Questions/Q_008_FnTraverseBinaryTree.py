"""""""""
Question 8 - Python function to traverse a binary tree path

Question: For a given binary tree, write a function to return all root-to-leaf paths.
We'll use the tree below to walk through how your code should work. 
"A" is the root, and "E" would be considered the leaf in the path A-> B -> E.

The expectation for your function is to return all root to leaf combinations.
The output of your code, given the tree below, would be: ["A -> B -> E", "A -> B -> D", "A-> C"]
        
           A                  
         /   \        
        B     C       
      /   \           
     E     D               
"""


class BinaryTree:
    def __init__(self, key):
        self.left_child = None
        self.right_child = None
        self.value = key

    def insert_left(self, newNode):
        if self.left_child is None:
            self.left_child = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)          # Created a new Tree
            tree.left_child = self.left_child   # Add the existing left child as left child to the new node
            self.left_child = tree              # Added the new tree as left child of current tree

    def insert_right(self, newNode):
        if self.right_child is None:
            self.left_child = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right_child = self.right_child
            self.right_child = tree


def print_tree(tree):
    if tree is not None:
        print_tree(tree.left_child)
        print(tree.value)
        print_tree(tree.right_child)


bt = BinaryTree('a')
bt.insert_left('b')
bt.insert_left('e')
bt.insert_right('c')
bt.insert_right('d')

print_tree(bt)