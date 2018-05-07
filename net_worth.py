'''
Creates a treee and finds the sum of subtrees ("net worth")
'''
import sys
import os



class Node:
    def __init__(self, val=None, name="John Doe"):
        self.val = val
        self.name = name
        self.children = []
        self.net = 0


class Tree:
    def __init__(self):
        self.root = None


    def getRoot(self):
        return self.root


    def getDaddy(self, dad_name, parent=None):
        # returns the parent node, given name
        if not self.root:
            return None;
        if self.root.name == dad_name:
            return self.root
        if not parent:
            parent = self.root

        for child in parent.children:
            if child.name == dad_name:
                return child
            if len(child.children):
                getDaddy(dad_name, child)


    def add(self, val, name="John Doe", parent=None):
        #create a new node
        new_child = Node(val, name)
        if not self.root:
            self.root = new_child
        else:
            if parent:
                # fetching the parent node
                daddy = self.getDaddy(parent)
                daddy.children.append(new_child)
        return new_child


    def find_net_worth(self, parent=None):
        # Net worth(node) = (value of children) + (value of node)
        if not parent:
            parent = self.root

        if not len(parent.children):
            parent.net = parent.val
            print(parent.name, " has net ", parent.net)
            return

        for kid in parent.children:
                self.find_net_worth(kid)
    
        sum = 0
        for kid in parent.children:
            sum += kid.net
        parent.net = sum + parent.val
        print(parent.name, " has net ", parent.net)


    def display(self, parent=None):
        if not parent:
            parent = self.root

        print("Node:", parent.name, "(", parent.val, ")")
        print("Children:")
        for item in parent.children:
            print(item.name, "(", item.val, ")" " -- Kids:", len(item.children))
            if(len(item.children)):
                self.display(item)
        print("----------")




my_tree = Tree()
tree_root = my_tree.add(100, 'Grandpa')
my_tree.add(50, 'Daddy 1', tree_root.name)
my_tree.add(40, 'Daddy 2', tree_root.name)
my_tree.add(30, 'Daddy 3', tree_root.name)
my_tree.display()

my_tree.add(15, 'Kid 1', 'Daddy 2')
my_tree.display()


# now that the tree is created, we find the net worth!!
my_tree.find_net_worth()




    

    


    



