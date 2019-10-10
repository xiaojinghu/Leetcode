# this is a bfs implementation
class Solution(object):
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        # if a node can be infected by different node from different path, then delete one single infected node cannot prevent it from been affected
        # Goal: for each infected node, find the number of uninfected nodes that can only be infected by it.
        
        infectedList = collections.defaultdict(list)
        initialSet = set(initial)
        for infected in initial: 
            queue = collections.deque([infected])
            visited = set()
            while(queue):
                infectedNode = queue.pop()
                if infectedNode in visited:
                    continue
                visited.add(infectedNode)
                for v in range(len(graph[infectedNode])):
                    if graph[infectedNode][v]!=1 or v in visited:
                        continue
                    # make sure that we get to nodes in diffent ways
                    if v in initialSet:
                        visited.add(v)
                        continue
                    queue.appendleft(v)
                    infectedList[v].append(infected)
        count = {}
        maxNum = 0
        index = -1
        for node in infectedList:
            if len(infectedList[node])>1:
                continue
            infected = infectedList[node][0]
            if infected not in count:
                count[infected] = 0
            count[infected] += 1
            if count[infected]>maxNum:
                maxNum = count[infected]
                index = infected
            if count[infected]==maxNum:
                index = min(infected, index)
        if index == -1:
            return min(initial)
        return index
                
                    
                    
                        
            
            
        