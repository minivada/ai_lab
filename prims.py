import sys
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[[0 for column in range(vertices)]  for row in range(vertices)]
    def printMSt(self,parent):
        print("Edge\t weight")
        for i in range(1,self.v):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
    def minKey(self,key,mstset):
        min_val=sys.maxsize
        for v in range(self.v):
            if key[v]<min_val and not mstset[v]:
                min_val=key[v]
                min_index=v
        return min_index
    def primMst(self):
        key=[sys.maxsize]*self.v
        parent=[None]*self.v
        mstset=[False]*self.v
        key[0]=0
        parent[0]=-1
        for _ in range(self.v):
            u=self.minKey(key,mstset)
            mstset[u]=True
            for v in range(self.v):
                if self.graph[u][v]>0 and not mstset[v] and key[v]>self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u
        self.printMSt(parent)
if __name__ == '__main__':
    g = Graph(5)
    g.graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    g.primMst()
