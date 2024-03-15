import bst
import matplotlib.pyplot as plt
import numpy as np

def is_full(t):
    # Base case(s)
    # Available recursive calls
    #if tree is empty return true
    #if tree.left of tree.right are null return false
    #return is_full(t.right) + is_full(t.left)
    # Solution
    #
    if t.is_empty:
        return True

    
    if (t.left.is_empty & (not t.right.is_empty)) | ((not t.left.is_empty) & t.right.is_empty):
        return False

    return is_full(t.left) and is_full(t.right)


def equal_trees(t1, t2):
    # Base case(s)
    # Available recursive calls
    #if t1 and t2 are empty return true
    #if t1 is empty and t2 is not empty, or t1 is not empty and t2 is empty return false
    #return (t1.key==t2.key) + qual_trees(t1.left, t2.left) + qual_trees(t1.right, t2.right)
    # Solution
    #
    if t1.is_empty & t2.is_empty:
        return True
    if (t1.is_empty & (not t2.is_empty)) | ((not t1.is_empty) & t2.is_empty):
        return False
    return equal_trees(t1.left, t2.left) and equal_trees(t1.right, t2.right)

def in_leaf(t,k):
    # Base case(s)
    # Available recursive calls
    #if t is empty return false
    #if t = k and t.left is empty and t.right is emoty return true
    #return in_leaf(t.left,k) + in_leaf(t.right,k)
    # Solution
    #
    if t.is_empty:
        return False
    if (t.key == k) & (t.left.is_empty & t.right.is_empty):
        return True
    elif t.key>k:
        return in_leaf(t.left,k)
    else:
        return in_leaf(t.right,k)

def path_string(t,k):
    # Base case(s)
    #if t is empty return ''
    #if t.key is equal to k return 'T'
    #else if t.key is grater than k return path_string(t.left,k) + 'L'
    #else if t.key is less than k return path_string(t.right,k) + 'R'
    # Available recursive calls
    #
    # Solution
    #
    if t.is_empty:
        return 'F'

    if t.key == k:
        return 'T'

    elif k < t.key:
        return 'L' + path_string(t.left, k)

    else:
        return 'R' + path_string(t.right, k)
    
def keys_by_level(t):
    # Solution
    # Initialize empty queue Q and empty list K; K will contain the elements stored by depth
    # Add t to Q
    # While Q is not empty
    #    dequeue node x for Q
    #    if x is not empty, append key in x to K, add left child of x to Q, add right child of x to Q
    # return K
    k = []
    q = []
    q.append(t)
    
    while len(q) != 0:
        x = q.pop(0)
        if not x.is_empty:
            k.append(x.key)
            q.append(x.left)
            q.append(x.right)
    return k
    
def test_is_full():
    assert(is_full(t0)==True)
    assert(is_full(t1)==False)
    assert(is_full(t2)==True)
    assert(is_full(t3)==False)
    print('is_full() passed all tests')


def test_equal_trees():
    assert(equal_trees(t0, t4)==True)
    assert(equal_trees(t1, t5)==True)
    assert(equal_trees(t2, t6)==True)
    assert(equal_trees(t3, t7)==True)
    assert(equal_trees(t0, t1)==False)
    assert(equal_trees(t1, t2)==False)
    assert(equal_trees(t2, t3)==False)
    assert(equal_trees(t3, t0)==False)
    print('equal_trees() passed all tests')

def test_in_leaf():
    assert(in_leaf(t0,1)== False)
    assert(in_leaf(t1,1)==False)
    assert(in_leaf(t1,2)==True)
    assert(in_leaf(t3,1)==True)
    assert(in_leaf(t3,2)==False)
    assert(in_leaf(t3,3)==False)
    print('test_is_in_bst() passed all tests')

def test_path_string():
    assert(path_string(t0,1)=='F')
    assert(path_string(t1,1)=='T')
    assert(path_string(t1,2)=='RT')
    assert(path_string(t2,2)=='LLRF')
    assert(path_string(t3,1)=='LLRLT')
    assert(path_string(t3,9)=='LRT')
    assert(path_string(t3,20)=='RRF')
    print('path_string() passed all tests')

def test_keys_by_level():
    assert(keys_by_level(t0)==[])
    assert(keys_by_level(t1)==[1,2])
    assert(keys_by_level(t2)==[11,3,14,1,7,13,17,5,9])
    assert(keys_by_level(t3)==[11,4,18,0,9,15,3,5,10,1])
    print('keys_by_level() passed all tests')

if __name__ == "__main__":

    draw_trees = True
   #draw_trees = False

    t0 = bst.from_list([])
    t1 = bst.from_list([1,2])
    t2 = bst.from_list([11, 14, 17, 3, 1, 7, 5, 9, 13])
    t3 = bst.from_list([11, 4, 18, 0, 9, 5, 3, 10, 1, 15])
    t4 = bst.from_list([]) # Equal to t0
    t5 = bst.from_list([1,2]) # Equal to t1
    t6 = bst.from_list([11, 14, 17, 3, 1, 7, 5, 9, 13]) # Equal to t2
    t7 = bst.from_list([11, 4, 18, 0, 9, 5, 3, 10, 1, 15]) # Equal to t3

    if draw_trees:
        t0.draw('t0')
        t1.draw('t1')
        t2.draw('t2')
        t3.draw('t3')

    print('\nQuestion 1')
    test_is_full()

    print('\nQuestion 2')
    test_equal_trees()

    print('\nQuestion 3')
    test_in_leaf()

    print('\nQuestion 4')
    test_path_string()

    print('\nQuestion 5')
    test_keys_by_level()
#
