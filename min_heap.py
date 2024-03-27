# Code to implement basic min heap operations
# Programmed by Olac Fuentes
# Last modified March 3, 2024

import matplotlib.pyplot as plt
import numpy as np

class HeapRecord:
    def __init__(self,key, data=None):
        self.key = key
        self.data = data

class MinHeap:

    def __init__(self):
        # heap is a list of heap_record objects
        # heap records are ordered by key (the record with the smallest key is the heap's root)
        # actual data are stored in the data attribute of heap_record object
        # The constructor creates an empty heap
        self.heap = []

    def insert(self,rec):
        # Add record to heap. If rec is an int, it creates a heap_record containing that int as key and None as data
        if type(rec) != HeapRecord:
            rec = HeapRecord(rec)
        self.heap.append(rec) # Add new item to end of heap
        self.bubble_up(len(self.heap)-1)

    def bubble_up(self,i):
      if i>0 and self.heap[i].key < self.heap[self.parent(i)].key:
          self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
          self.bubble_up(self.parent(i))

    def extract_min(self):
        assert len(self.heap)>0 # Raise error if trying to extractMin from empty heap
        if len(self.heap) == 1:
            return self.heap.pop() # Return and remove root; heap is now empty
        root = self.heap[0]
        self.heap[0] = self.heap.pop() # Move last element from heap to root, reduce heap size
        self.percolate_down(0)
        return root

    def percolate_down(self,i):
        smallest = i
        for k in self.children(i):
            if self.heap[k].key < self.heap[smallest].key:
                smallest = k
        if smallest != i: # Parent is not smaller than either of its  children
            self.heap[i],self.heap[smallest] = self.heap[smallest],self.heap[i] # Swap parent with smaller
            self.percolate_down(smallest)

    def print_keys(self):
        print('keys in heap: ',end=' ')
        for h in self.heap:
            print(h.key,end=' ')
        print()

    def parent(self,i):
        return (i-1)//2

    def children(self,i):
        return [k for k in [self.left(i),self.right(i)] if k<len(self.heap)]

    def left(self,i):
        return 2*i + 1

    def right(self,i):
        return 2*i + 2

    def draw(self,title='',indices=False):
        if len(self.heap)>0:
            fig, ax = plt.subplots()
            self._dh_(0, 0, 0, 100, 50, ax,indices)
            ax.axis('off')
            fig.suptitle(title, fontsize=14)
            plt.show()

    def _dh_(self, i, x, y, dx, dy, ax,indices):
        if self.left(i) < len(self.heap):
            p=np.array([[x,y], [x-dx,y-dy]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            self._dh_(self.left (i), x-dx, y-dy, dx/2, dy, ax, indices)
        if self.right(i) < len(self.heap):
            p=np.array([[x,y], [x+dx,y-dy]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            self._dh_(self.right(i), x+dx, y-dy, dx/2, dy, ax, indices)
        ax.text(x,y, str(self.heap[i].key), size=20,
            ha="center", va="center",
            bbox=dict(facecolor='w',boxstyle="circle"))
        if indices:
            ax.text(x-4,y-24, str(i), size=12,color='r')
