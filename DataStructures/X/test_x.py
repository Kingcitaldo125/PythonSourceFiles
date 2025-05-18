import pytest

from x import Tree, lca, lca_help

def test_one():
	t = Tree(2)

	t.left = Tree(1)
	t.right = Tree(3)
	t.right.right = Tree(4)
	t.right.right.right = Tree(5)
	t.right.right.right.right = Tree(6)

	assert lca(t, 4, 6).info == 3

def test_two():
	t = Tree(4)

	t.left = Tree(2)
	t.left.left = Tree(1)

	t.right = Tree(7)
	t.right.left = Tree(6)

	assert lca(t, 1, 7).info # 4

def test_three():
	t = Tree(8)

	t.left = Tree(4)
	t.left.right = Tree(6)
	t.left.right.left = Tree(5)
	t.left.left = Tree(1)
	t.left.left.right = Tree(2)
	t.left.left.right.right = Tree(3)

	t.right = Tree(9)

	assert lca(t, 1, 2).info == 1

def test_four():
	t = Tree(9)

	t.left = Tree(7)
	t.left.right = Tree(8)
	t.left.left = Tree(5)
	t.left.left.right = Tree(6)
	t.left.left.left = Tree(4)
	t.left.left.left.left = Tree(3)
	t.left.left.left.left.left = Tree(1)

	assert lca(t, 1, 6).info == 5
