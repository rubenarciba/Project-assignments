import matplotlib.pyplot as plt
import btree
import numpy as np

def height(t):
    # if t have one node return 0
    # otherwise 1 + height of first subtree
    if len(t.child)==0:
        return 0
    return 1 + height(t.child[0])

def smallest(t):
    if len(t.child)==0:
        return t.data[0]
    return smallest(t.child[0])

def largest(t):
    if len(t.child)==0:
        return t.data[len(t.child)-1]
    return largest(t.child[len(t.child)-1])

def count_nodes(t):
    
    x = 1
    for c in t.child:
        x += count_nodes(c)
    return x

def count_leaves(t):
    if len(t.child)==0:
        return 1
    x = 0
    for c in t.child:
        x += count_leaves(c)
    return x

def is_in_btree(t,k):
    if k in t.data:
        return True

    i=0
    while i<len(t.data) and k>t.data[i]:
        i+=1
    if i<len(t.child):
        return is_in_btree(t.child[i], k)
    elif t.child:
        return is_in_btree(t.child[-1], k)
    else:
        return False
      

def test_height():
    assert(height(t0)==0)
    assert(height(t1)==1)
    assert(height(t2)==2)
    print('height() passed all tests')

def test_smallest():
    assert(smallest(t0)==1)
    assert(smallest(t1)==0)
    assert(smallest(t2)==2)
    print('smallest() passed all tests')


def test_largest():
    assert(largest(t0)==9)
    assert(largest(t1)==37)
    assert(largest(t2)==59)
    print('largest() passed all tests')

def test_count_nodes():
    assert(count_nodes(t0)==1)
    assert(count_nodes(t1)==6)
    assert(count_nodes(t2)==14)
    print('count_nodes() passed all tests')

def test_count_leaves():
    assert(count_leaves(t0)==1)
    assert(count_leaves(t1)==5)
    assert(count_leaves(t2)==10)
    print('count_leaves() passed all tests')

def test_is_in_btree():
    assert(is_in_btree(t0,4)==True)
    assert(is_in_btree(t0,5)==False)
    assert(is_in_btree(t1,29)==True)
    assert(is_in_btree(t1,0)==True)
    assert(is_in_btree(t1,30)==True)
    assert(is_in_btree(t1,5)==False)
    assert(is_in_btree(t1,12)==False)
    assert(is_in_btree(t1,42)==False)
    assert(is_in_btree(t2,26)==True)
    assert(is_in_btree(t2,16)==True)
    assert(is_in_btree(t2,58)==True)
    assert(is_in_btree(t2,1)==False)
    assert(is_in_btree(t2,31)==False)
    assert(is_in_btree(t2,60)==False)

    print('is_in_btree() passed all tests')

if __name__ == "__main__":

    draw_trees = True
    #draw_trees = False

    np.random.seed(0)

    t0 = btree.from_list(np.random.permutation(10)[:5])
    t1 = btree.from_list(np.random.permutation(40)[:20])
    t2 = btree.from_list(np.random.permutation(60)[:40])

    if draw_trees:
        t0.draw('t0')
        t1.draw('t1')
        t2.draw('t2')

    print('Question 1')
    test_height()

    print('Question 2')
    test_smallest()

    print('Question 3')
    test_largest()

    print('Question 4')
    test_count_nodes()

    print('Question 5')
    test_count_leaves()

    print('Question 6')
    test_is_in_btree()

