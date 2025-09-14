from database.DAO import DAO
import networkx as nx
import copy

from model.piloti import PilotaGara


class Model:
    def __init__(self):
        self.DAO = DAO()
        self.G = None
        self.pilot = None
        self.sol_best = []

    def get_anni(self):
        return self.DAO.get_anni()

    def get_grafo(self, data):
        self.G = nx.DiGraph()
        self.pilot = self.DAO.get_piloti(data)
        for i in self.pilot:
            self.G.add_node(i)
        for i in self.pilot:
            for j in self.pilot:
                if i.raceId == j.raceId and i.driverId != j.driverId:
                    if i.position > j.position:
                        c = self.peso(j.driverId, i.driverId, data)
                        if c != 0:
                            self.G.add_edge(j, i, weight=c)
                    else:
                        c = self.peso(i.driverId, j.driverId, data)
                        if c != 0:
                            self.G.add_edge(i, j, weight=c)
        print(sorted(list(self.G.edges(data="weight")), key=lambda x: x[2], reverse=True))
        return self.G.number_of_nodes()

    def get_archi(self):
        return self.G.number_of_edges()

    def peso(self, id1, id2, data):
        pil = []
        c = 0
        for i in self.pilot:
            for j in self.pilot:
                if i.driverId == id1 and j.driverId == id2 and i.raceId == j.raceId and i.raceId not in pil:
                    pil.append(i.raceId)
                    if i.position < j.position:
                        c = c + 1
        return c

    def miglior_pilota(self):
        pilota = []
        n = 0
        for i in self.G.nodes():
            c = self.G.out_degree(i, weight="weight") - self.G.in_degree(i, weight="weight")
            if c > n:
                n = c
                pilota.append(i)
        return pilota[-1], n

    def dream_team(self, k):
        piloti = []
        minn = float("inf")
        self.ricorsione(k, piloti, c, minn)
            piloti.pop()



    def ricorsione(self, k, piloti, c, minn):
        if c < minn:
            minn = c
            self.sol_best = copy.deepcopy(piloti)
            if len(piloti) == k:
                c = 0
                for i in piloti:
                    b = 0
                    for j in self.G.in_edges(i):
                        if self.G.in_edges(i)[j][0] in piloti:
                            b = b + self.G[self.G.in_edges(i)[j][0]][i]["weight"]
                    c = c + (self.G.in_degree(i, weight="weight") - b)
                    self.ricorsione(k, piloti, c, minn)






if __name__ == '__main__':
    Model = Model()
    print(Model.get_grafo(1963))
    print(Model.miglior_pilota())
    print(Model.get_archi())