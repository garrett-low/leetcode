# binary search tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, head = None):
        self.head = head
    
    def __str__(self):
        if self.head == None:
            return "BST:\t\t\tEmpty!"
        retval = "BST Pre Order:\t\t"
        preTraversalList = []
        self.preTraversal(self.head, preTraversalList)
        for item in preTraversalList:
            retval += f"[{item}]"
            
        retval += "\nBST In Order:\t\t"
        inOrderList = []
        self.inOrderTraversal(self.head, inOrderList)
        for item in inOrderList:
            retval += f"[{item}]"
            
        retval += "\nBST Post Order:\t\t"
        postOrderList = []
        self.inOrderTraversal(self.head, postOrderList)
        for item in postOrderList:
            retval += f"[{item}]"
        return retval
    
    def preTraversal(self, curr, printlist):
        if curr == None:
            return
        printlist.append(curr.val)
        if curr.left != None:
            self.preTraversal(curr.left, printlist)
        if curr.right != None:
            self.preTraversal(curr.right, printlist)
        
    def inOrderTraversal(self, curr, printlist):
        if curr == None:
            return
        if curr.left != None:
            self.inOrderTraversal(curr.left, printlist)
        printlist.append(curr.val)
        if curr.right != None:
            self.inOrderTraversal(curr.right, printlist)
    
    def postOrderTraversal(self, curr, printlist):
        if curr == None:
            return
        if curr.left != None:
            self.postOrderTraversal(curr.left, printlist)
        if curr.right != None:
            self.postOrderTraversal(curr.right, printlist)
        printlist.append(curr.val)
    
    def prettyPrint(self):
        if self.head == None:
            print("BST PRETTY PRINT: \t\t EMPTY!")
            return
        
        self.pp(self.head, 0)
    
    def pp(self, curr, indent):
        if curr == None:
            return
        if curr.left != None:
            self.pp(curr.left, indent + 1)
            
        if indent > 0:
            print("\t" * indent)
        print("\t" * indent, f"[{curr.val}]")
        
        if curr.right != None:
            print()
            self.pp(curr.right, indent + 1)
    
    def add(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        
        self.addInner(self.head, new_node)
        
    def addInner(self, curr, new_node):
        if curr.val < new_node.val:
            if curr.left == None:
                curr.left = new_node
            else:
                self.addInner(curr.left, new_node)
        else:
            if curr.right == None:
                curr.right = new_node
            else:
                self.addInner(curr.right, new_node)

def main():
    tree1 = BinaryTree()
    print(tree1)
    tree1.add(5)
    print(tree1)
    tree1.add(69)
    print(tree1)
    tree1.add(1)
    print(tree1)
    tree1.add(2)
    print(tree1)
    tree1.add(4)
    print(tree1)
    tree1.add(3)
    print(tree1)
    tree1.add(420)
    print(tree1)
    tree1.prettyPrint()
    
if __name__ == "__main__":
    main()