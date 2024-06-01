class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

class Queue:
    def __init__(self):
        self.queue = []


    def get_prior(self, item):
        return item[1]
    def push(self, item, priority):
        self.queue.append((item, priority))
 
        self.queue.sort(key = self.get_prior)

    def pop(self):
        return self.queue.pop(0)[0]


class Dijkstra:
    def __init__(self):
        self.vertexes = []


    def computePath(self, sourceId):
        root = None

        vertexes_dict = {}
        for v in self.vertexes:
            vertexes_dict[v.id] = v

        queue = Queue()
        
        for v in self.vertexes:
            if v.id == sourceId:
                v.minDistance = 0
                root = v
            queue.push(v, v.minDistance)
        
        while len(queue.queue) != 0:
            current = queue.pop()
            for edge in current.edges:
                new_dist = current.minDistance + edge.weight
                target = vertexes_dict[edge.target]

                if new_dist < target.minDistance:
                    target.minDistance = new_dist
                    target.previousVertex = current
                    queue.push(target, target.minDistance)


        # dist = {}
        # for vertex in self.vertexes:
        #     dist[vertex.id] = float('inf')

        # prev = {}
        # for vertex in self.vertexes:
        #     prev[vertex.id] = None

        # unvist = []
        # for vertex in self.vertexes:    
        #     unvist.append(vertex.id)

            # r vertex in self.vertexes:
        #     source_vert = None
        #     if vertex.id == sourceId:
        #         vertex.minDistance = 0
        #         vertex.previous = None
        #         source_vert = vertex
        # for ver in self.vertexes.remove(source_vert):

                        
    

    def getShortestPathTo(self, targetId):
        path = []
        vertexes_dict = {}
        for v in self.vertexes:
            vertexes_dict[v.id] = v
        current = vertexes_dict[targetId]
        while current is not None:
            path.insert(0, current)
            current = current.previousVertex
        return path

    def createGraph(self, vertexes, edgesToVertexes):
        for vertex in vertexes:
            for edge in edgesToVertexes:
                if edge.source == vertex.id:
                    vertex.edges.append(edge)
            self.vertexes.append(vertex)
            

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None

    def getVertexes(self):
        return self.vertexes

#Test graph
# vertexes = [
#   Vertex(0, 'Redville'),
#   Vertex(1, 'Blueville'),
#   Vertex(2, 'Greenville'),
#   Vertex(3, 'Orangeville'),
#   Vertex(4, 'Purpleville')
# ]
# edges = [
#   Edge(0, 1, 5),
#   Edge(0, 2, 10),
#   Edge(0, 3, 8),
#   Edge(1, 0, 5),
#   Edge(1, 2, 3),
#   Edge(1, 4, 7),
#   Edge(2, 0, 10),
#   Edge(2, 1, 3),
#   Edge(3, 0, 8),
#   Edge(3, 4, 2),
#   Edge(4, 1, 7),
#   Edge(4, 3, 2)
# ]