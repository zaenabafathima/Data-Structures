# binary search tree - here we go!

class Node:
	def __init__(self, name, val):
		self.name = name
		self.val = val
		self.left = None
		self.right = None


class Tree:
	def __init__(self):
		self.root = None


	def insert_iteratively(self, node):
		if not self.root:
			self.root = node
			print("Inserted at root", self.root.name, self.root.val)
		else:
			start = self.root
			while start:
				if node.val > start.val:
					if start.right:
						start = start.right
					else:
						# we found the spot, going to insert
						print("Inserting", node.name, node.val, " to the right of ", start.name, start.val)
						start.right = node
						break
				else:
					if start.left:
						start = start.left
					else:
						print("Inserting", node.name, node.val, " to the left of ", start.name, start.val)
						start.left = node
						break


	def insert_recursively(self, node, root=None):
		if not self.root:
			self.root = node
			return
		if not root:
			root = self.root
		
		if node.val > root.val:
			if not root.right:
				root.right = node
				return
			else:
				self.insert_recursively(node, root.right)
		else:
			if not root.left:
				root.left = node
				return
			else:
				self.insert_recursively(node, root.left)


	def flip(self, parent_node):
		if not parent_node:
			return

		temp = parent_node.left
		parent_node.left = parent_node.right
		parent_node.right = temp
		self.flip(parent_node.left)
		self.flip(parent_node.right)

	
	def reverse(self):
		new_tree = Tree()
		if not self.root:
			return;
		start = self.root
		new_tree.root = self.root
		self.flip(new_tree.root)
		print("The reversed tree is ----")
		self.traverse(new_tree.root)


	def neater_reverse(self, root):
		if root is not None:
			root.left, root.right = self.neater_reverse(root.right), \
									self.neater_reverse(root.left)
		return root


	def traverse(self, root):
		# inorder traversal
		if not root:
			return
		self.traverse(root.left)
		print(root.name, root.val)
		self.traverse(root.right)




my_tree = Tree()
my_root = Node('Alice', 100)
my_tree.insert_recursively(my_root)
my_tree.insert_recursively(Node('Jim', 90))
my_tree.insert_recursively(Node('Major', 120))
my_tree.insert_recursively(Node('Roadie', 80))
my_tree.insert_recursively(Node('Rando', 95))
my_tree.insert_recursively(Node('Junior', 70))
my_tree.insert_recursively(Node('Roadie Right', 85))

my_tree.traverse(my_root)

reversed_root = my_tree.neater_reverse(my_root)
print("After cooler inversion tree is------")
my_tree.traverse(reversed_root)
