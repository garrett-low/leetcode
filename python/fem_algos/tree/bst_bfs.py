from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return f"[{self.val}]"

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, val):
        new_node = Node(val)
        
        if self.root == None:
            self.root = new_node
            return
        
        self.addInner(new_node, self.root)
        
    def addInner(self, new_node, curr_node):
        if new_node.val < curr_node.val:
            if curr_node.left == None:
                curr_node.left = new_node
            else:
                self.addInner(new_node, curr_node.left)
        else:
            if curr_node.right == None:
                curr_node.right = new_node
            else:
                self.addInner(new_node, curr_node.right)
    
    def remove(self, val):
        self.removeInner(val, self.root)
    
    def removeInner(self, val, curr_node):
        if curr_node == None:
            return None
        if val < curr_node.val:
            curr_node.left = self.removeInner(val, curr_node.left)
            return curr_node
        elif val > curr_node.val:
            curr_node.right = self.removeInner(val, curr_node.right)
            return curr_node
        else: # node found
            if curr_node.left == None and curr_node.right == None: # leaf
                return None
            elif curr_node.left == None and curr_node.right != None:
                return curr_node.right
            elif curr_node.left != None and curr_node.right == None:
                return curr_node.left
            else: # two children - remove inorder successor (next highest is min in right subtree)
                inorder_succ = curr_node.right
                while inorder_succ.left != None:
                    inorder_succ = inorder_succ.left
                curr_node.val = inorder_succ.val # replace deleted node with inorder successor
                curr_node.right = self.removeInner(inorder_succ.val, curr_node.right) # delete inorder succ that was swapped up
                return curr_node
    
    def prettyPrint(self):
        if self.root == None:
            print("BST PRETTY PRINT: \t\t EMPTY!")
            return
        
        print("=" * 30 + "BST PRETTY PRINT:" + "=" * 30)
        self.pp(self.root, 0)
    
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
    
    # Print in tree-level/BFS order
    def bst_print(self):
        print("BST tree-level/BFS order: ", end='')
        if self.root == None:
            print("Empty!", end='')
        
        queue = deque([self.root])
        while len(queue) != 0:
            next_node = queue.popleft()
            print(next_node, end='')
            if next_node.left != None:
                queue.append(next_node.left)
            if next_node.right != None:
                queue.append(next_node.right)
        print()
    
    def bfs(self, val):
        queue = deque([self.root])
        
        while len(queue) != 0:
            next_node = queue.popleft()
            
            if next_node == None:
                continue
            if next_node.val == val:
                return True
            if next_node.left != None:
                queue.append(next_node.left)
            if next_node.right != None:
                queue.append(next_node.right)
        return False
    
def main():
    tree1 = BST()
    tree1.add(69)
    tree1.add(32)
    tree1.add(5)
    tree1.add(1)
    tree1.add(2)
    tree1.add(27)
    tree1.add(35)
    tree1.add(420)
    tree1.add(690)
    tree1.prettyPrint()
    tree1.remove(69)
    tree1.prettyPrint()
    tree1.add(34)
    tree1.add(80)
    tree1.prettyPrint()
    tree1.remove(35)
    tree1.prettyPrint()
    tree1.add(81)
    tree1.prettyPrint()
    tree1.remove(32)
    tree1.prettyPrint()
    tree1.bst_print()
    print(tree1.bfs(35))
    print(tree1.bfs(2))
    
if __name__ == "__main__":
    main()