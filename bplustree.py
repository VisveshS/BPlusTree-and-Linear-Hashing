import sys
import bisect
MAX_NODE_SIZE = 3#maximum of 3 keys

class Node:
	def __init__(self,keys,children,nextr,leaf):
		self.keys = keys
		self.children = children
		self.next = nextr
		self.leaf = leaf

	def split(self):
		mid = int(len(self.keys)/2)
		new_key = self.keys[mid]
		if self.leaf:
			temp_node = Node(self.keys[mid:],self.children[mid:],self.next,self.leaf)
			self.keys = self.keys[:mid]
			self.children = self.children[:mid]
			self.next = temp_node
		else:
			temp_node = Node(self.keys[mid+1:],self.children[mid+1:],None,self.leaf)
			self.keys = self.keys[:mid]
			self.children = self.children[:mid+1]

		return new_key, temp_node


class BPlusTree:
	def __init__(self):
		self.root = Node([],[],None,True)
	
	def insert(self, value, node):
		if node.leaf:
			new_key, new_node = [value, value]
		else:
			new_key, new_node = self.insert(value, node.children[bisect.bisect(node.keys, value)])
		if new_key is None:
			return None,None
		idx = bisect.bisect(node.keys, new_key)
		node.keys.insert(idx, new_key)
		node.children.insert(idx+(not node.leaf), new_node)
		if len(node.keys) <= MAX_NODE_SIZE:
			return None, None
		new_key, new_node = node.split()
		if node is self.root:
			new_root = Node([new_key],[self.root, new_node],None,False)
			self.root = new_root
		return new_key, new_node

	def count(self,value):
		node = self.first_leaf(value,self.root)
		instances = 0
		while node is not None:
			instances = instances+node.children.count(value)
			node = node.next
		return(instances)

	def find(self,value):
		instances = self.count(value)
		return "YES" if instances else "NO"

	def range(self,low,high):
		node = self.first_leaf(low,self.root)
		instances = 0
		while node is not None:
			for values in node.children:
				instances = instances+(values>=low and values<=high)
			node = node.next
		return instances
			
	def first_leaf(self,value, node):
		return node if node.leaf else self.first_leaf(value, node.children[bisect.bisect(node.keys, value)])

if len(sys.argv) != 2:
	exit('Error: correct syntax is "python3 bplustree.py </path/to/input/file>"')
tree = BPlusTree()
with open(sys.argv[1], 'r') as f:
	for line in f:
		line = line.strip().split(' ')
		if(line[0] == "INSERT"):
			tree.insert(int(line[1]),tree.root)
		elif(line[0] == "RANGE"):
			print(tree.range(int(line[1]),int(line[2])))
		elif(line[0] == "COUNT"):
			print(tree.count(int(line[1])))
		elif(line[0] == "FIND"):
			print(tree.find(int(line[1])))
			