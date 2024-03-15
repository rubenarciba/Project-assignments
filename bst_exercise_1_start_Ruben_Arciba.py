import bst
import numpy as np
import matplotlib.pyplot as plt


def is_in_bst(t,k):
    # Write your solution definition here - handle base case(s) correctly, assume recursive calls work, do not use any additional variables
    if t.is_empty :
        return False
    if t.key == k:
        return True
    elif k<t.key:
        return is_in_bst(t.left,k)
    elif k>t.key:
        return is_in_bst(t.right,k)

def count_nodes(t):
    # Write your solution definition here - handle base case(s) correctly, assume recursive calls work, do not use any additional variables
    
    if t.is_empty:
        return 0
    return 1+count_nodes(t.left) +  count_nodes(t.right)

def largest(t):
    # Write your solution definition here - handle base case(s) correctly, assume recursive calls work, do not use any additional variables
  
    if t.is_empty:
        return -np.inf
    elif t.right.is_empty == False:
       return largest(t.right)
    else:
       return t.key
    
def bst_to_list(t):
    # Write your solution definition here - handle base case(s) correctly, assume recursive calls work, do not use any additional variables
    L = []
    if t.is_empty:
        return L
    
    L.extend(bst_to_list(t.left))
    L.append(t.key)
    L.extend(bst_to_list(t.right))
    return L

def height(t):
    # Write your solution definition here - handle base case(s) correctly, assume recursive calls work, do not use any additional variables
    if t.is_empty:
        return -1
    hight_left = height(t.left)
    hight_right = height(t.right)
    
    return max(hight_left, hight_right) + 1

def leaves(t):
    # Write your solution definition here - handle base case(s) correctly, assume recursive calls work, do not use any additional variables
    L = []
    if t.is_empty:
        return L
    
    L.extend(leaves(t.left))
    
    if t.left.is_empty & t.right.is_empty:
        L.append(t.key)
        
    L.extend(leaves(t.right))
    
    return L

if __name__ == "__main__":

    t0 = bst.BST()
    t1 = bst.from_list([16,2,1,6,3,14,4,9,22,18,24,23])
    t2 = t1.left
    t3 = t1.right

    t0.draw('t0')
    t1.draw('t1')
    t2.draw('t2')
    t3.draw('t3')

    print('\nQuestion 1')
    for i,t in  enumerate([t0,t1,t2,t3]):
        for k in [2,19,23]:
            print(f'is_in_bst(t{str(i)},{k}) = {is_in_bst(t,k)}')

    print('\nQuestion 2')
    for i,t in  enumerate([t0,t1,t2,t3]):
        print(f'count_nodes(t{str(i)}) = {count_nodes(t)}')

    print('\nQuestion 3')
    for i,t in  enumerate([t0,t1,t2,t3]):
        print(f'largest(t{str(i)}) = {largest(t)}')

    print('\nQuestion 4')
    for i,t in  enumerate([t0,t1,t2,t3]):
        print(f'bst_to_list(t{str(i)}) = {bst_to_list(t)}')

    print('\nQuestion 5')
    for i,t in  enumerate([t0,t1,t2,t3]):
        print(f'height(t{str(i)}) = {height(t)}')

    print('\nQuestion 6')
    for i,t in  enumerate([t0,t1,t2,t3]):
        print(f'leaves(t{str(i)}) = {leaves(t)}')

'''
Edit this part to submit your expected answers

Question 1
is_in_bst(t0,2) = False
is_in_bst(t0,19) = False
is_in_bst(t0,23) = False
is_in_bst(t1,2) = True
is_in_bst(t1,19) = False
is_in_bst(t1,23) = True
is_in_bst(t2,2) = True
is_in_bst(t2,19) = False
is_in_bst(t2,23) = False
is_in_bst(t3,2) = False
is_in_bst(t3,19) = False
is_in_bst(t3,23) = True

Question 2
count_nodes(t0) = 0
count_nodes(t1) = 12
count_nodes(t2) = 7
count_nodes(t3) = 4

Question 3
largest(t0) = -inf
largest(t1) = 24
largest(t2) = 14
largest(t3) = 24

Question 4
bst_to_list(t0) = []
bst_to_list(t1) = [1, 2, 3, 4, 6, 9, 14, 16, 18, 22, 23, 24]
bst_to_list(t2) = [1, 2, 3, 4, 6, 9, 14]
bst_to_list(t3) = [18, 22, 23, 24]

Question 5
height(t0) = -1
height(t1) = 4
height(t2) = 3
height(t3) = 2

Question 6
leaves(t0) = []
leaves(t1) = [1, 4, 9, 18, 23]
leaves(t2) = [1, 4, 9]
leaves(t3) = [18, 23]

'''