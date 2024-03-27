# Implementation of graphs using sets and dictionaries
# Programmed by Olac Fuentes
# Last modified March 18, 2024

import numpy as np
import matplotlib.pyplot as plt

class Graph:
    # Constructor, builds graph with v vertices and no edges
    def __init__(self, v, weighted=False, directed = False):
        self.V = set(range(v))  # Vertex set
        self.E = {v:set() for v in self.V} # Edge dictionary. E[v] is the set of destinations of edges with source v
        self.weighted = weighted  # Boolean indicator - its True is graph is weighted
        self.directed = directed  # Boolean indicator - its True is graph is directed
        if weighted:              # Weight dictionary, used only for weighted graphs
            self.W = {}           # W[(u,v)] is the weight of the edge with source u and destination v

    def insert_edge(self,source,dest,weight=1):
        # T(V,E) = O(1)
        for v in [source, dest]:
            if v not in self.V:
                print('Error, vertex',v,'does not exist in graph')
                return
        if source == dest:
            print('Error, self-edges are not allowed!')
            return
        else:
            self.insert_edge_directed_(source,dest,weight)
            if not self.directed:
                self.insert_edge_directed_(dest,source,weight)

    def insert_edge_directed_(self,source,dest,weight):
        # T(V,E) = O(1)
        self.E[source].add(dest)
        if self.weighted:
            self.W[(source,dest)] = weight

    def delete_edge(self,source,dest):
        # T(V,E) = O(1)
        for v in [source, dest]:
            if v not in self.V:
                print('Error, vertex',v,'does not exist in graph')
                return
        if dest not in self.E[source]:
            print('Error, edge to delete not found')
            return
        self.delete_edge_directed_(source,dest)
        if not self.directed:
            self.delete_edge_directed_(dest,source)

    def delete_edge_directed_(self,source,dest):
        # T(V,E) = O(1)
        self.E[source].remove(dest)
        if self.weighted:
            del self.W[(source,dest)]

    def edge_set(self):
        # T(V,E) = O(|V| + |E|)
        S = {(u,v) for u in self.V for v in self.E[u]}
        if not self.directed:
          S =  {(u,v) for (u,v) in S if u<v}
        if self.weighted:
          S =  {(u,v,self.W[(u,v)]) for (u,v) in S}
        return S

    def display(self,name ='Graph'):
        # T(V,E) = O(|V| + |E|)
        print(name+' representation')
        print('directed: {}, weighted: {}'.format(self.directed,self.weighted))
        print('Vertex set:')
        print(self.V)
        print('Edge dictionary:')
        print(self.E)
        if self.weighted:
            print('Weight dictionary:')
            print(self.W)

    def draw(self,title='',tries=1,reset_xy=True,vertex_names=None):
        # T(V,E) = O(|V| + |E|)
        if not 'x' in dir(self) or reset_xy:
            self._set_xy(tries)
        fig, ax = plt.subplots()
        self._draw_edges_(ax)
        self._draw_vertices_(ax,vertex_names)
        ax.axis('off')
        fig.suptitle(title, fontsize=14)
        ax.set_aspect(1.0)
        plt.show()

    def _draw_r(self,title=''):
        # Draws graph trying to minimize the sum of the lengths in the drawing by randomly swapping vertex locations
        # T(V,E) = O(|V| + |E|)
        self.draw(title,tries=200,reset_xy=True)

    def _draw_edges_(self,ax):
        x,y = self.x, self.y
        ax.plot(x,y,linewidth=1,color='w')
        wu = 0.55
        wv = 1-wu
        for u in self.V:
            for v in self.E[u]:
                if self.directed or (u<v):
                    ax.plot([x[u],x[v]],[y[u],y[v]],linewidth=1,color='k')
                    if self.directed:
                        ax.arrow(x[u],y[u],0.89*(x[v]-x[u]),0.89*(y[v]-y[u]), head_width=0.05, overhang=1,
                             head_length=0.05, length_includes_head=True, fc='k', ec='k')
                    if self.weighted:
                        if (not self.directed) and (v-u == len(self.V)-1): u,v = v,u
                        dx, dy = x[v]-x[u], y[v]-y[u]
                        m = np.sqrt((dx*dx+dy*dy))
                        dx, dy = dx/m/15,dy/m/15
                        theta_text = -np.arctan2(x[v]-x[u], y[v]-y[u])*180/np.pi+90
                        if np.abs(theta_text)>90:
                            theta_text -= 180*np.sign(theta_text)
                        if np.abs(theta_text)>89 and self.W[(u,v)] in [6,9]:
                            theta_text -= 10*np.sign(theta_text)
                            #theta_text = 0
                        ax.text((wu*x[u]+wv*x[v])+dy,(wu*y[u]+wv*y[v])-dx, str(self.W[(u,v)]), size=10,ha="center", va="center",rotation=theta_text)

    def _draw_vertices_(self,ax,vertex_names=None):
        if vertex_names is None:
            vertex_names = list(self.V)
        for u, name in enumerate(vertex_names):
            ax.text(self.x[u],self.y[u], str(name), size=12,ha="center", va="center",
                bbox=dict(facecolor='w',boxstyle="circle"))

    def _compute_lengths(self,x,y,edge_set):
        # Internal function used for drawing
        dist = 0
        for u,v in edge_set:
            dist += np.sqrt((x[u]-x[v])**2 + (y[u]-y[v])**2)
        return dist

    def _set_xy(self,tries=200):
        # Internal function used for drawing
        theta = np.linspace(-np.pi,np.pi,len(self.E)+1)
        x = np.cos(theta)
        y = np.sin(theta)
        max_dist = np.inf
        ind = np.arange(len(self.V))
        edge_set = {(v[0],v[1]) for v in self.edge_set()}
        np.random.seed(0)
        for i in range(tries):
            if i>0:
                ind[1:] = np.random.permutation(len(self.V)-1)+1
            dist = self._compute_lengths(x[ind],y[ind],edge_set)
            if dist<max_dist:
                max_dist = dist
                best_ind = np.copy(ind)
        self.x,self.y = x[best_ind],y[best_ind]
        np.random.seed(None)

def random_graph(vn, edges, directed=False,weighted=False,seed=None):
    if seed!=None:
        np.random.seed(seed)
    edges = min(edges, vn*(vn-1)//2)
    g = Graph(vn,directed=directed,weighted=weighted)
    n = 0
    w = sorted(set(range(1,edges+3)).difference(set([6,9])))
    w = [w[i] for i in np.random.permutation(edges)]
    while n<edges:
        u,v = np.random.choice(vn,size=2)
        if u!=v and u not in g.E[v] and v not in g.E[u]:
            g.insert_edge(u,v,w[n])
            n+=1
    return g

