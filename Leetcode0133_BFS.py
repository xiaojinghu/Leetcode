"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # THIS IS A BFS IMPLEMENTATION
        # copied is a map to return the copied node given the original node
        copied = {}   
        # use a queue to traverse the graph
        # All nodes in the queue are copied but their neighbors are not copied
        # queue's used to store nodes that are not processed, we consider a node to be processed if it is copied and its neighbors has been copied
        # so we only store nodes that are copied and hasn't been fully processed, which is "grey" into the queue.
        queue = deque([node])
        newNode = Node(node.val,[])
        copied[node] = newNode
        # a 3 color illustration:
        # White: all nodes not in copied are white
        # Grey: all nodes in queue are grey， all nodes in copied are black or grey
        # Black: all nodes poped out of queue are black
        while(queue):
            currOriginNode = queue.pop()
            # we've copied this node, we need to copy its neighbors and add them into the queue
            # check if its neighbors are copied
            # if not copied, copy them
            for neighbor in currOriginNode.neighbors:
                # check if the node is white
                if neighbor not in copied:
                    # if the neighbor is white
                    newNeighbor = Node(neighbor.val,[])
                    # mark it as grey
                    copied[neighbor] = newNeighbor
                    # add the newNeighbor as the neighbor of the newCurrNode
                    copied[currOriginNode].neighbors.append(newNeighbor)
                    # add this neighbor into the queue
                    queue.appendleft(neighbor)
                else:
                    copied[currOriginNode].neighbors.append(copied[neighbor])
            
                
        return newNode
              
                    
            
        
              
