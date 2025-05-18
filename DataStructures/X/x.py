from Tree import Tree, add, print_tree

t = Tree(2)

t.right = Tree(3)
t.right.left = t

t.right.right = Tree(4)
t.right.right.left = t.right

t = add(t, 1)

print_tree(t)
