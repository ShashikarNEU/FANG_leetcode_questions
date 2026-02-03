# Good Question
# Here, root is missing
# So, we start from p and q, go till root then, p_pointer starts from q and q_pointer starts from p
# they will meet at LCA(exit while loop)
# Logic behind doing this:- 
# distance from p to LCA -> p_dis
# distance from q to LCA -> q_dis
# distance from LCA to root -> x

# Total distance travelled if we reverse the pointers will be the same
# p_dis + x + q_dis == q_dis + x + p_dis
# They will meet at LCA
# Do a dry run using this logic and see

# Reference Video -> https://www.youtube.com/watch?v=iaOceNnKIQQ

# Definition for a Node.
from collections import defaultdict


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p, q):
        t1 = p
        t2 = q
        while t1 != t2:
            t1 = t1.parent 
            t2 = t2.parent 

            if not t1:
                t1 = q
            if not t2:
                t2 = p

            if t1 == t2:
                return t1

# Meta asks two variants
# Variant 1-> if val is a char, string instead of int
# Ans -> Nothing changes

# Variant 2 -> Parent pointer is removed, instead we are given a list of nodes in a unordered order
# we are given p and q, find LCA
# Ans -> Iterate through the list, take a dict, find of the node if they exist then, key -> child and value -> node(parent)
# Then, we can use the old algo to find the LCA. if we reach the root then, root will have no key in dict so, we cahnge the pointers.

class Solution:
    def lowestCommonAncestor(self, p, q, Nodelist):
        hashTable = defaultdict(Node)

        for node in Nodelist:
            if node.left:
                hashTable[node.left] = node
            if node.right:
                hashTable[node.right] = node
            
        t1 = p
        t2 = q
        while t1 != t2:
            t1 = hashTable[t1] if hashTable[t1] else q
            t2 = hashTable[t2] if hashTable[t2] else p

            if t1 == t2:
                return t1