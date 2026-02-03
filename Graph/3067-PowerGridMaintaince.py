from collections import defaultdict
from sortedcontainers import SortedList # type: ignore

# Apply DSU to find parent array and path decompression
# Now have a hashMap where parent -> nodes
# form this hashMap after DSU
# if action=2, find hashMap[root] and do remove
# if action=1, if node in hashMap[root] return node else return min of the hashMap[root]

# To do this, we have sortedList from python(we can do remove, add, find min in logn)
class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        parent = [i for i in range(c+1)]
        rank = [1]*(c+1)
        hashMap = defaultdict(SortedList)

        def find(n):
            res = n
            while parent[res] != res:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parent[p1] = p2
                rank[p2]+=rank[p1]
            
            return 1
        
        for u,v in connections:
            union(u,v)
        
        for node in range(1,c+1):
            root = find(node)
            hashMap[root].add(node)
        
        res = []
        for s, node in queries:
            if s == 2:
                root = find(node)
                if node in hashMap[root]:
                    hashMap[root].remove(node)
            elif s == 1:
                root = find(node)
                nodes = hashMap[root]
                if node in nodes:
                    res.append(node)
                elif len(nodes) == 0:
                    res.append(-1)
                else:
                    res.append(nodes[0])
                
        return res


# Algo
# // --- 1. DSU Setup ---
#     // (We assume DSU.find() and DSU.union() are implemented)
#     Initialize DSU for 'c' stations.
    
#     // --- 2. Build Components (Phase 1) ---
#     // Run DSU on all connections to find the final components.
#     For each [u, v] in connections:
#         DSU.union(u, v)

#     // --- 3. Populate Component Sets (Phase 2) ---
#     // Now that components are fixed, add all stations to their
#     // component's SortedList.
#     Initialize component_sets as an empty Map.
    
#     For i from 1 to c:
#         // Find the final root for station i
#         root = DSU.find(i) 
        
#         // Add station i to its component's set.
#         // If the set doesn't exist, create it.
#         component_sets[root].add(i)

#     // --- 4. Process Queries ---
#     Initialize results as an empty list.
    
#     For each [query_type, node] in queries:
    
#         // Find the root of the node's component
#         root = DSU.find(node)
        
#         // Get the specific SortedList for this component
#         stations_in_component = component_sets[root]

#         // --- Query Type 2: Station goes offline ---
#         If query_type == 2:
#             // Check if the node is in the set before removing.
#             // This prevents an error if it's already offline.
#             If node in stations_in_component:
#                 stations_in_component.remove(node)
        
#         // --- Query Type 1: Maintenance check ---
#         Else (query_type == 1):
            
#             // Case 1: The node itself is online.
#             If node in stations_in_component:
#                 results.append(node)
            
#             // Case 2: Node is offline AND its component has NO online stations.
#             Else if stations_in_component is empty:
#                 results.append(-1)
                
#             // Case 3: Node is offline, but its component has other online stations.
#             Else:
#                 // Get the smallest station from the sorted set
#                 // (e.g., set.first() or set[0])
#                 smallest_station = stations_in_component.get_minimum() 
#                 results.append(smallest_station)

#     // --- 5. Return ---
#     Return results



        
