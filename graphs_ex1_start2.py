import graph
import numpy as np

def num_vertices(G):
    return len(G.V)

def num_edges(G):
    count = 0 
    for i in G.E:
        count+= len(G.E.get(i))
    return count

def out_degree(G,v):
     
    return len(G.E.get(v))

def in_degree(G,v):
    count = 0
    for i in G.E:
        if v in G.E.get(i):
            count+=1
    return count

def is_isolated(G,v):
    count = 0
    for i in G.E:
        if (v not in G.E.get(i)):
            count+=1
    if (count == len(G.E)) and (len(G.E.get(v))==0):
        return True
    return False

if __name__ == "__main__":

    draw_graphs = True
    draw_graphs = False

    q = 1
    print('Question',q)
    for directed in [False, True]:
        np.random.seed(q+directed)
        v = np.random.randint(4,9)
        g = graph.Graph.random_graph(v, v+2, directed=directed,seed=3*q+directed)
        g.display()
        if draw_graphs: g.draw('Question 1')
        print(f'{num_vertices(g) = }')

    q = 2
    print('Question',q)
    for directed in [False, True]:
        np.random.seed(q+directed)
        v = np.random.randint(5,9)
        g = graph.Graph.random_graph(v, v+2, directed=directed,seed=3*q+directed)
        g.display()
        if draw_graphs: g.draw('Question 2')
        print(f'{num_edges(g) = }')

    q = 3
    print('Question',q)
    np.random.seed(q)
    v = np.random.randint(4,9)
    g = graph.Graph.random_graph(v, v+2, directed=True,seed=3*q)
    g.display()
    if draw_graphs: g.draw('Question 3')
    for i in range(v):
        print(f'out_degree(g,{i}) = {out_degree(g,i)}')

    q = 4
    print('Question',q)
    np.random.seed(q+1)
    v = np.random.randint(4,9)
    g = graph.Graph.random_graph(v, v+2, directed=True,seed=3*q)
    g.display()
    if draw_graphs: g.draw('Question 4')
    for i in range(v):
        print(f'in_degree(g,{i}) = {in_degree(g,i)}')

    q = 5
    print('Question',q)
    np.random.seed(q)
    v = np.random.randint(4,9)
    g = graph.Graph.random_graph(v, v-2, directed=True,seed=3*q)
    g.display()
    if draw_graphs: g.draw('Question 5')
    for i in range(v):
        print(f'is_isolated(g,{i}) = {is_isolated(g,i)}')

