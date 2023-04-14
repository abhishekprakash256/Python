"""
implemnet a Lru cache for the machine

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
	int get(int key) Return the value of the key if the key exists, otherwise return -1.
	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
	If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

"""
class Node:
	def __init__(self,val):
		self.next = None
		self.prev = None
		self.val = val




class LRUCache:

	def __init__(self, capacity: int):
		"""
		The function to initilaize the capacity of the cache
		"""
		self.capacity = capacity
		self.mapper = {}

	def get(self, key: int) -> int:
		pass
		

	def put(self, key: int, value: int) -> None:
		pass


if __name__ == "__main__":
	cache = LRUCache(6)
	#cache.get()