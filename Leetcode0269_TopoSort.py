class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 1:
            # we can sort the words in any order
            return words[0]
        graph = {}
        inDegree = {}
        prev = words[0]
        # build the graph
        for i in range(1, len(words)):
            curr = words[i]
            # we now compare each letter of the current word with the prev word
            minLen = min(len(prev), len(curr))
            for vertex in set(prev+curr):
                if vertex not in graph:
                    graph[vertex] = set()
                    inDegree[vertex] = 0
            if prev[:minLen] == curr[:minLen] and len(prev)>len(curr):
                return ""
            for j in range(minLen):
                u = prev[j]
                v = curr[j]
                if u == v:
                    # we need to check the next letter
                    continue
                if v not in graph[u]:
                    graph[u].add(v)
                    inDegree[v] += 1
                break
            prev = curr
                        
        # after we built the graph, we use topological sorting to traverse it
        order = ""
        queue = collections.deque()
        # initialize the queue
        for u in graph.keys():
            if inDegree[u] == 0:
                queue.appendleft(u)
        while(queue):
            u = queue.pop()
            order += u
            inDegree[u] = -1
            for v in graph[u]:
                if inDegree[v] == -1:
                    return ""
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    queue.appendleft(v)
                    
        for u in inDegree.keys():
            if inDegree[u] != -1:
                return ""
        return order
