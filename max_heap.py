"""HEAPS, HEAP-SORT"""

from collections.abc import MutableSequence


class Heap(MutableSequence):
	"""docstring for MaxHeap"""
	def __init__(self, *args):
		self.list = list()
		self.extend(list(args))
		self.len = len(self.list)

	def __len__(self):
		return len(self.list)

	def __getitem__(self, i):
		try:
			if i > self.len-1:
				return False
			return self.list[i]
		except IndexError as error:
			return False

	def __delitem__(self, i):
		del self.list[i]

	def __setitem__(self, i, v):
		self.list[i] = v

	def __eq__(self, other):
	    if isinstance(other, Heap):
	        return self.list == other.list
	    return False

	def __iter__(self):
		for elem in self.list:
			if not elem:
				break
			yield elem

	def insert(self, i, v):
		self.list.insert(i, v)

	def __str__(self):
		return str(self.list)

	def __repr__(self):
		return str(self.list)


def get_parent(index):
	"""parent: (i - 2)/2"""
	return (index - 1)//2

def left_child(heap, parent):
	"""left child: 2*p + 1"""
	return 2*parent + 1

def right_child(heap, parent):
	""" right child: 2*p + 2"""
	return 2*parent + 2

def max_heapify(heap, p):
	"""max heapify function"""
	left = left_child(heap, p)
	right = right_child(heap, p)
	if heap[left] > heap[right]:
		if heap[left] > heap[p]:
			temp = heap[p]
			heap[p] = heap[left]
			heap[left] = temp
			max_heapify(heap, left)
	else:
		if heap[right] > heap[p]:
			temp = heap[p]
			heap[p] = heap[right]
			heap[right] = temp
			max_heapify(heap, right)

def extract_max(heap):
	popped = heap.pop(0)
	build_max_heap(heap)
	return popped

def build_max_heap(heap):
	"""convert A[1...n] into a max-heap"""
	for j in range(heap.len//2, -1, -1):
		max_heapify(heap, j)

def heap_sort(heap):
	"""sort maxheap"""
	while heap.len >= 1:
		swap_min_max(heap)
		# restore max heap!
		max_heapify(heap, 0)

def swap_min_max(heap):
	"""swap min and max, and reduce length of heap"""
	temp = heap[0]
	heap[0] = heap[heap.len-1]
	heap[heap.len-1] = temp
	heap.len -= 1
	return

def main():
	build_max_heap(swe)
	heap_sort(swe)
	print("swe: ->", end='')
	print(swe)
	assert swe == proper_swe, "first example no longer works"
	build_max_heap(mit)
	heap_sort(mit)
	print("mit: ->", end='')
	print(mit)
	assert mit == proper_mit, "second example no longer works"


mit = Heap(16, 14, 10, 8, 7, 9, 3, 2, 4, 1)
swe = Heap(10, 6, 7, 5, 15, 17, 12)
proper_swe = Heap(5, 6, 7, 10, 12, 15, 17)
proper_mit = Heap(1, 2, 3, 4, 7, 8, 9, 10, 14, 16)

if __name__ == '__main__':
	main()
