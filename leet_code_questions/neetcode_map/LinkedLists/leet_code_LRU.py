"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
	int get(int key) Return the value of the key if the key exists, otherwise return -1.
	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from 
	this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""

class LRUCache:

	def __init__(self, capacity: int):
		self.capacity = capacity

		#initilaize the hashmap
		self.recentCache = {}

		
	def get(self, key: int) -> int:

		self.key = key
		#the return value 
		if self.key in self.recentCache:
			print(self.key)
			return self.recentCache[self.key]
		else:
			return -1
		

	def put(self, key: int, value: int) -> None:
		
		self.key = key
		self.value = value 
		length = len(self.recentCache) - 1
		#check the length and evict the recent one 

		if self.key in self.recentCache:
			self.recentCache[self.key] = self.value 

		if len(self.recentCache) >= self.capacity:
			
			#evict from the bottom 
			self.recentCache.pop(self.recentCache[length])

			#add the value 
			self.recentCache[self.key] = self.value 


		else:
			#put in the right place, just append 
			self.recentCache[self.key] = self.value


if __name__ == "__main__":
	LruCache = LRUCache(2)
	LruCache.put(1,1)
	LruCache.put(2,2)
	LruCache.put(3,4)
	print(LruCache.get(8))