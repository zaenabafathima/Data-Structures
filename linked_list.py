# starting out with the simple stuff, linked lists!
# this is the bare minimum, insert at rear, delete from front

class Node:
	def __init__(self, name):
		self.name = name
		self.next = None

class List:
	def __init__(self):
		self.head = None

	def insert(self, node):
		if not self.head:
			self.head = node
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = node
		print("Just inserted:", node.name)

	def delete(self):
		if not self.head:
			print("List Empty!")
			return
		print("Deleting...", self.head.name)
		self.head = self.head.next


	def traverse(self):
		curr = self.head
		if not curr:
			print("List Empty!")
			return

		print("---- THE LIST ----------")
		while curr:
			print(curr.name)
			curr = curr.next
		print("------------------------")



def init():
	my_list = List()
	
	my_list.traverse()
	my_list.insert(Node('Jim'))
	my_list.traverse()
	my_list.insert(Node('Alice'))
	my_list.traverse()
	my_list.insert(Node('Sam'))
	my_list.traverse()
	my_list.insert(Node('Vicky'))
	my_list.traverse()


	my_list.delete()
	my_list.traverse()
	my_list.delete()
	my_list.traverse()
	my_list.delete()
	my_list.traverse()
	my_list.delete()
	my_list.traverse()


init()