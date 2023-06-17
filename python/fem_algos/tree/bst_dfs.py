from bst_bfs import BST

def dfs_iter_print(tree):
    stack = [tree.root]
    
    while len(stack) != 0:
        curr_node = stack.pop()
        print(curr_node, end='')
        if curr_node.left != None:
            stack.append(curr_node.left)
        if curr_node.right != None:
            stack.append(curr_node.right)
    print()

def dfs_recurse(tree, val):
    return dfs_inner(tree.root, val)

def dfs_inner(curr_node, val):
    if curr_node == None:
        return False
    if curr_node.val == val:
        return True
    if curr_node.val < val:
        return dfs_inner(curr_node.right, val)
    return dfs_inner(curr_node.left,val)

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
    print(dfs_recurse(tree1, 123))
    print(dfs_recurse(tree1, 690))
    print(dfs_recurse(tree1, 2))
    dfs_iter_print(tree1)
    
    
if __name__ == "__main__":
    main()
