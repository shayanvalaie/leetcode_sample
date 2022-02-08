

''''

743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
'''


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Create an edges variable that will store the edges their weight and value
        edges = collections.defaultdict(list)

        for u, v, w in times:  # Loop through all vars in times and add it to our default dic
            edges[u].append((v, w))  # Node 2 -> 1 has a weight of 1

        minHeap = [(0, k)]  # Init minheap with 0 cost and source node given
        visit = set()  # Are visited nodes will be tracked in a set
        t = 0  # Our min total for each node to be reached

        while minHeap:  # Continue this algorithm while our minHeap is not null
            # pop from the minheap and store it as weight 1 and node 1
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:  # If node has been visited we want to continue
                continue

            visit.add(n1)  # Else we want to add node into our visited set
            # our total is equal to the max between what t currently is and the weight from our current node
            t = max(t, w1)

            for n2, w2 in edges[n1]:  # Now we check neighboring edges of the node we are on
                if n2 not in visit:  # If neighbor node is not in visit
                    # We add the node into our minHeap and add its weight AND the weight of the previous node that we used to get here
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
        '''At the end of our loop we want to return t which stores our shortest path
        if the length of visit is equal to n which stores our total nodes.  If it is 
        equal we have completed our algorithim and we have visited each node.  If it 
        is not equal it means one or more nodes were not reached and we return -1
        '''
