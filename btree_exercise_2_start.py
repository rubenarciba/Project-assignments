import btree
import matplotlib.pyplot as plt
import numpy as np

def full_nodes(t):
    count = 0
    if len(t.child)==0:
        if len(t.data)== t.max_items:
            return 1
        return 0
    if len(t.data) == t.max_items:
        count+=1
    for c in t.child:
        count+= full_nodes(c)
    return count
    
    

def equal_trees(t1, t2):
   if t1.data != t2.data:
       return False
   if len(t1.child) != len(t2.child):
       return False
   for i in range(len(t1.child)):
       if equal_trees(t1.child[i], t2.child[i])==False:
           return False
   return True
    

def in_leaf(t,k):
    if len(t.child)==0:
        if k in t.data:
            return True
        return False
    i = 0 
    while i < len(t.data) and k>t.data[i]:
        i+=1
    
    return in_leaf(t.child[i], k)

def follow_path(t,p):
    
    if not t.child:
        if len(p) > 1:
            return None
        if len(p) > 0 and t.data is not None:
            if p[0] < len(t.data):
                return t.data[p[0]]
            else: 
                return None
        
    if len(p)>0:   
        index = p[0]

        if index < 0 or index >= len(t.child):
            return None

        next_node = t.child[index]
    
        return follow_path(next_node, p[1:])
    else: 
        return None
    
        


def find_path(t,k):
    
    if k in t.data:
        return [t.data.index(k)]
    
    if not t.child:
        return []
    
    for i, c in enumerate(t.child):
        
        if c is not None:
            path_in_child = find_path(c, k)
            
            if path_in_child:
                return [i] + path_in_child
            
def btree_to_list(t):
    result = []
    if len(t.child)==0:
        return t.data
    for i, child in enumerate(t.child):
        result.extend(btree_to_list(child))
        if i<len(t.data):
            result.append(t.data[i])
    return result

def test_full_nodes():
    assert(full_nodes(t0)==1)
    assert(full_nodes(t1)==2)
    assert(full_nodes(t2)==1)
    assert(full_nodes(t3)==3)
    print('full_nodes() passed all tests')

def test_equal_trees():
    assert(equal_trees(t0, t4)==True)
    assert(equal_trees(t1, t5)==True)
    assert(equal_trees(t2, t6)==True)
    assert(equal_trees(t0, t1)==False)
    assert(equal_trees(t2, t3)==False)
    print('equal_trees() passed all tests')

def test_in_leaf():
    assert(in_leaf(t0,10)==True)
    assert(in_leaf(t1,10)==False)
    assert(in_leaf(t2,10)==False)
    assert(in_leaf(t2,30)==True)
    print('in_leaf() passed all tests')

def test_follow_path():
    assert(follow_path(t0,[2])==21)
    assert(follow_path(t0,[2,2])==None)
    assert(follow_path(t2,[2,2])==None)
    assert(follow_path(t2,[1,1])==None)
    assert(follow_path(t2,[0,3,2])==25)
    print('follow_path() passed all tests')

def test_find_path():
    assert(find_path(t0,21)==[2])
    assert(find_path(t1,11)==[1,0])
    assert(find_path(t2,3)==[0,0,2])
    assert(find_path(t2,32)==[1,0])
    print('find_path() passed all tests')

def test_btree_to_list():
    # Correct outputs already provided below
    assert(btree_to_list(t0)==[10, 16, 21, 29, 32])
    print(btree_to_list(t1))
    assert(btree_to_list(t2)==[1,2,3,6,7,8,9,12,13,14,16,18,19,20,21,22,24,25,26,27,29,30,31,32,33,37,39,41,42,43,44,45,46,47,48,49,53,54,55,56,57,58,59])
    print('btree_to_list() passed all tests')

if __name__ == "__main__":

    draw_trees = True
    draw_trees = False
    np.random.seed(0)
    L0 = list(np.random.permutation(10)[:5])
    L0 = [10,16,21,29,32]
    L1 = list(np.random.permutation(40)[:24])
    L2 = list(np.random.permutation(60)[:43])

    t0 = btree.from_list(L0)
    t1 = btree.from_list(L1)
    t2 = btree.from_list(L2)
    t3 = btree.from_list(L2 + [11,28])

    t4 = btree.from_list(L0)
    t5 = btree.from_list(L1)
    t6 = btree.from_list(L2)

    trees = {'t'+str(i):t for i,t in enumerate([t0,t1,t2,t3,t4,t5,t6])}

    if draw_trees:
        for name in trees:
            trees[name].draw(name)

    print('\nQuestion 1')
    test_full_nodes()

    print('\nQuestion 2')
    test_equal_trees()

    print('\nQuestion 3')
    test_in_leaf()

    print('\nQuestion 4')
    test_follow_path()

    print('\nQuestion 5')
    test_find_path()

    print('\nQuestion 6')
    test_btree_to_list()

