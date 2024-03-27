import matplotlib.pyplot as plt
import numpy as np
import min_heap

def change_key(H,k,m):
    # If putting m at position k breaks heap property, return -1
    # else put m at position k in the heap and return 1
    if k>len(H.heap):
        return -1
    
    C = H.children(k)
    if  H.heap[H.parent(k)].key > m or (len(C) > 0 and (H.heap[C[0]].key < m or H.heap[C[-1]].key < m)):
        return -1
    else:
        H.heap[k].key = m
        return 1

def max_diff(H):
    if len(H.heap)<=1:
        return 0
    
    max_diff = 0
    for i in range(len(H.heap)):
        
        parent_key = H.heap[i].key
        left_child_i = H.left(i)
        right_child_i = H.right(i)
        
        if left_child_i < len(H.heap):
            left_child_key = H.heap[left_child_i].key
            max_diff = max(max_diff, abs(parent_key - left_child_key))
        
        if right_child_i < len(H.heap):
            right_child_key = H.heap[right_child_i].key
            max_diff = max(max_diff , abs(parent_key - right_child_key))
        
    return max_diff

def less_than_k(H,k):
    L = []
    for i in H.heap:
        if i.key < k:
            L.append(i.key)
    L.sort()
    return L

def extract_from_2_heaps(H1,H2,k) :
    L = []
    combined_heaps = H1.heap + H2.heap
    combined_heaps.sort(key=lambda x: x.key)
    
    for i in combined_heaps[:k]:
        L.append(i.key)
    return L

if __name__=="__main__":

    L1 = [ 5,  2, 11, 10,  3,  1,  8, 13,  0, 14,  7,  4,  9, 12,  6]
    L2 = [13,17,18]
    L3 = [1,2,4,8,14,5,6,7,6]
    L4 = [5,0,3,7,8,9,1,5,6,7,6,13]

    H =  min_heap.MinHeap()
    for i in L1:
        H.insert(i)
    H.draw('Original heap',indices=True)

    print('Question 1')
    key_changes = [(0,3), (8,2), (5,10), (7,8), (5,2),(6,7),(4,7),(3,9)]
    for index, new_key in key_changes:
        H.print_keys()
        ch = change_key(H,index, new_key)
        print('change_key(H,{},{}) = {}'.format(index, new_key, ch))
        if ch ==1:
            print('Heap was modified')
            H.print_keys()
            H.draw('New heap'+str(index)+str(new_key),indices=True)
        else:
            print('Could not place {} in position {} without violating heap property'.format(new_key,index))
        print()

    print('Question 2')
    for L in [L1,L2,L3,L4]:
        H = min_heap.MinHeap()
        for i in L:
            H.insert(i)
        H.draw('Heap for questions 2 and 3')
        print('max_diff(H) =',max_diff(H))

    print('Question 3')
    for L in [L1,L2,L3,L4]:
        H = min_heap.MinHeap()
        for i in L:
            H.insert(i)
        for k in [8,12]:
            print('less_than_k(H,{}) = {}'.format(k,less_than_k(H,k)))

    print('Question 4')
    L1 = [20,1,7,2,8,9,15]
    L2 = [18, 25, 11,6,10,12,13]
    H1 = min_heap.MinHeap()
    for L in [L1,L2]:
        H = min_heap.MinHeap()
        for i in L:
            H.insert(i)
        H.draw('Heap for question 4')
    for k in [1,2,4,8,16,32]:
        H1 = min_heap.MinHeap()
        for i in L1:
            H1.insert(i)
        H2 = min_heap.MinHeap()
        for i in L2:
            H2.insert(i)
        print('k=',k)
        print(extract_from_2_heaps(H1,H2,k))

'''
Question 1
keys in heap:  0 1 2 3 5 4 6 13 10 14 7 11 9 12 8
change_key(H,0,3) = -1
Could not place 3 in position 0 without violating heap property

keys in heap:  0 1 2 3 5 4 6 13 10 14 7 11 9 12 8
change_key(H,8,2) = -1
Could not place 2 in position 8 without violating heap property

keys in heap:  0 1 2 3 5 4 6 13 10 14 7 11 9 12 8
change_key(H,5,10) = -1
Could not place 10 in position 5 without violating heap property

keys in heap:  0 1 2 3 5 4 6 13 10 14 7 11 9 12 8
change_key(H,7,8) = 1
Heap was modified
keys in heap:  0 1 2 3 5 4 6 8 10 14 7 11 9 12 8

keys in heap:  0 1 2 3 5 4 6 8 10 14 7 11 9 12 8
change_key(H,5,2) = 1
Heap was modified
keys in heap:  0 1 2 3 5 2 6 8 10 14 7 11 9 12 8

keys in heap:  0 1 2 3 5 2 6 8 10 14 7 11 9 12 8
change_key(H,6,7) = 1
Heap was modified
keys in heap:  0 1 2 3 5 2 7 8 10 14 7 11 9 12 8

keys in heap:  0 1 2 3 5 2 7 8 10 14 7 11 9 12 8
change_key(H,4,7) = 1
Heap was modified
keys in heap:  0 1 2 3 7 2 7 8 10 14 7 11 9 12 8

keys in heap:  0 1 2 3 7 2 7 8 10 14 7 11 9 12 8
change_key(H,3,9) = -1
Could not place 9 in position 3 without violating heap property

Question 2
max_diff(H) = 10
max_diff(H) = 5
max_diff(H) = 12
max_diff(H) = 8
Question 3
less_than_k(H,8) = [0, 1, 2, 3, 4, 5, 6, 7]
less_than_k(H,12) = [8, 9, 10, 11]
less_than_k(H,8) = []
less_than_k(H,12) = []
less_than_k(H,8) = [1, 2, 4, 5, 6, 6, 7]
less_than_k(H,12) = [8]
less_than_k(H,8) = [0, 1, 3, 5, 5, 6, 6, 7, 7]
less_than_k(H,12) = [8, 9]
Question 4
k= 1
[1]
k= 2
[1, 2]
k= 4
[1, 2, 6, 7]
k= 8
[1, 2, 6, 7, 8, 9, 10, 11]
k= 16
[1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 20, 25]
k= 32
[1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 20, 25]
'''

