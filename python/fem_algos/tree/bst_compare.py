from bst_bfs import BST
#from bst_bfs import Node

def compare(node1, node2):
    if node1 == None and node2 == None:
        return True
    elif node1 == None or node2 == None: # one is None
        return False
    elif node1.val != node2.val:
        return False
    
    return compare(node1.left, node1.left) and compare(node2.right, node2.right)

def main():
    tree1 = BST()
    tree1.add(20)
    tree1.add(32)
    tree1.add(5)
    tree1.prettyPrint()
    tree2 = BST()
    tree2.add(20)
    tree2.add(32)
    tree2.add(5)
    tree2.prettyPrint()
    print(compare(tree1.root, tree2.root))
    tree3 = BST()
    tree3.add(5)
    tree3.add(32)
    tree3.add(20)
    tree3.prettyPrint()
    print(compare(tree2.root, tree3.root))
    
if __name__ == "__main__":
    main()