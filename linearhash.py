import sys
import math
MAX_OCCUPANCY = 0.85
BUCKET_SIZE = 2

class LinearHash:

	def __init__(self):
		self.buckets=[[],[]]
		self.hash_i = 1
		self.no_of_buckets = 2
		self.no_of_records = 0

	def hashvalue(self,number):
		h_v = int(number%math.pow(2,self.hash_i))
		return int(h_v if h_v < self.no_of_buckets else h_v-math.pow(2,self.hash_i-1))

	def insert(self,value):
		if float(self.no_of_records)/(self.no_of_buckets*BUCKET_SIZE) > MAX_OCCUPANCY:
			self.buckets.append([])
			self.no_of_buckets = self.no_of_buckets+1
			if math.pow(2,self.hash_i) < self.no_of_buckets:
				self.hash_i = self.hash_i+1
			split_index = int(bin(self.no_of_buckets-1)[3:],2)
			self.buckets[self.no_of_buckets-1] = [record for record in self.buckets[split_index] if self.hashvalue(record) == self.no_of_buckets-1]
			self.buckets[split_index] = [record for record in self.buckets[split_index] if self.hashvalue(record) == split_index]
		self.buckets[self.hashvalue(value)].append(value)
		self.no_of_records = self.no_of_records+1

	def present(self,value):
		return value in self.buckets[self.hashvalue(value)]

	def show(self):
		for i in range(self.no_of_buckets):
			print(i,self.buckets[i])

if len(sys.argv) != 2:
	sys.exit("Usage: python file.py input_file")
LIN_HASH = LinearHash()
with open(sys.argv[1], 'r') as f:
	for line in f:
		new_record = int(line.strip())
		if not LIN_HASH.present(new_record):
			print(new_record)
		LIN_HASH.insert(new_record)
# LIN_HASH.show()
